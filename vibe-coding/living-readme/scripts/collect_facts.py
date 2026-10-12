#!/usr/bin/env python3
"""collect_facts.py - collect every checkable fact about a repository.

Python 3 standard library only. Runs from any directory (the repository root
by default) and prints a single JSON document to stdout.

Nothing here interprets the project. It only measures it: git history,
languages, manifests, CI jobs, tests, docs, licence, media, top-level layout.
Every number a README claims should come from this file (or from a command the
README shows), never from memory.

Usage:
    python3 living-readme/scripts/collect_facts.py                 # repo = cwd
    python3 living-readme/scripts/collect_facts.py --repo ../app
    python3 living-readme/scripts/collect_facts.py -o facts.json

Exit code is always 0 unless --strict is given and git is unavailable.
Missing git, a broken manifest or an unreadable file never crashes the run;
the problem is appended to the "errors" list instead.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

# --------------------------------------------------------------------------
# Configuration (edit freely)
# --------------------------------------------------------------------------

SKIP_DIR_PARTS = {
    "vendor", "node_modules", "dist", "build", "out", "target", "coverage",
    ".venv", "venv", "env", "__pycache__", ".git", ".next", ".nuxt", ".cache",
    "bower_components", "Pods", ".terraform", ".idea", ".vscode-test",
    "third_party", "thirdparty", "Godeps", "site-packages", ".tox", ".mypy_cache",
    ".pytest_cache", "htmlcov", ".gradle", ".dart_tool",
}

SKIP_PATH_SUBSTRINGS = (
    "/vendor/", "/node_modules/", "/dist/", "/build/", "/public/build/",
    "/storage/framework/", "/.venv/", "/site-packages/", "/coverage/",
)

SKIP_FILE_SUFFIXES = (".min.js", ".min.css", ".map", ".lock")

MAX_FILE_BYTES = 3 * 1024 * 1024      # ignore files larger than this for line counts
MAX_LISTED = 60                        # cap for most lists in the output

LANGUAGES = {
    ".py": "Python", ".pyi": "Python",
    ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript", ".jsx": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".mts": "TypeScript",
    ".php": "PHP", ".phtml": "PHP",
    ".rb": "Ruby", ".erb": "Ruby",
    ".go": "Go", ".rs": "Rust", ".java": "Java", ".kt": "Kotlin", ".kts": "Kotlin",
    ".cs": "C#", ".c": "C", ".h": "C", ".cc": "C++", ".cpp": "C++", ".hpp": "C++",
    ".m": "Objective-C", ".swift": "Swift", ".dart": "Dart", ".scala": "Scala",
    ".sh": "Shell", ".bash": "Shell", ".ps1": "PowerShell", ".bat": "Batch",
    ".sql": "SQL", ".r": "R", ".jl": "Julia", ".lua": "Lua", ".pl": "Perl",
    ".ex": "Elixir", ".exs": "Elixir", ".erl": "Erlang", ".hs": "Haskell",
    ".html": "HTML", ".htm": "HTML", ".css": "CSS", ".scss": "SCSS",
    ".sass": "Sass", ".less": "Less", ".vue": "Vue", ".svelte": "Svelte",
    ".md": "Markdown", ".mdx": "Markdown", ".rst": "reStructuredText",
    ".json": "JSON", ".yml": "YAML", ".yaml": "YAML", ".toml": "TOML",
    ".ini": "INI", ".cfg": "INI", ".xml": "XML", ".tf": "Terraform",
    ".proto": "Protobuf", ".graphql": "GraphQL", ".gql": "GraphQL",
}

LANGUAGE_BY_FILENAME = {
    "Dockerfile": "Docker", "Makefile": "Makefile", "Jenkinsfile": "Groovy",
    "Rakefile": "Ruby", "Gemfile": "Ruby", "Procfile": "Procfile",
}

AI_TOOL_NAMES = [
    "claude", "codex", "cursor", "copilot", "gemini", "deepseek", "aider",
    "windsurf", "cline", "opencode", "grok", "chatgpt", "gpt-4", "gpt-5",
    "opus", "sonnet", "haiku", "qwen", "kimi", "antigravity", "roo",
]

CI_WORKFLOW_GLOBS = (
    ".github/workflows/", ".gitlab-ci.yml", ".circleci/", "azure-pipelines.yml",
    ".woodpecker.yml", ".drone.yml", "Jenkinsfile", "bitbucket-pipelines.yml",
    ".buildkite/", "cloudbuild.yaml", "appveyor.yml", ".travis.yml",
)

TEST_PATH_RE = re.compile(
    r"(^|/)(tests?|spec|specs|__tests__|testing)(/|$)"
    r"|(^|/)(test_[^/]+|[^/]+_test|test\.[a-z]+|[^/]+\.(test|spec)\.[a-z]+"
    r"|[^/]+Test\.(php|java|kt|cs)|[^/]+_spec\.rb)$",
    re.IGNORECASE,
)

DOC_NAMES = re.compile(
    r"^(README|CONTRIBUTING|CHANGELOG|CHANGES|HISTORY|SECURITY|ARCHITECTURE|AGENTS|CLAUDE|"
    r"CODE_OF_CONDUCT|GOVERNANCE|INSTALL|USAGE|ROADMAP|LICENSE|NOTICE|AUTHORS|MAINTAINERS)"
    r"(\.|$)", re.IGNORECASE)

LICENSE_RE = re.compile(r"^(LICEN[CS]E|COPYING|NOTICE|UNLICENSE)(\.|$)", re.IGNORECASE)

IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif", ".avif", ".bmp")
LOGO_HINT_RE = re.compile(r"logo|icon|favicon|brand|mark|avatar", re.IGNORECASE)
SHOT_HINT_RE = re.compile(r"screenshot|screen[-_]?shot|capture|preview|demo|hero|cover|banner|mockup|dashboard", re.IGNORECASE)


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

def log_error(errors, message):
    """Record a non-fatal problem once."""
    if message not in errors:
        errors.append(message)


def run(cmd, cwd, errors, note=None, timeout=120):
    """Run a command, return stdout or None. Never raises."""
    try:
        proc = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=timeout,
        )
    except FileNotFoundError:
        log_error(errors, "command not found: %s" % cmd[0])
        return None
    except subprocess.TimeoutExpired:
        log_error(errors, "command timed out: %s" % " ".join(cmd))
        return None
    except OSError as exc:
        log_error(errors, "could not run %s: %s" % (cmd[0], exc))
        return None
    if proc.returncode != 0:
        if note:
            log_error(errors, note)
        return None
    return proc.stdout


def is_skipped(path):
    """True for paths that must never pollute line counts."""
    lowered = path.replace("\\", "/").lower()
    if lowered.endswith(SKIP_FILE_SUFFIXES):
        return True
    parts = lowered.split("/")
    for part in parts[:-1]:
        if part in SKIP_DIR_PARTS:
            return True
    if parts and parts[-1] in {".gitignore", ".gitattributes"}:
        return False
    return any(seg in lowered for seg in SKIP_PATH_SUBSTRINGS)


def detect_language(path):
    name = os.path.basename(path)
    if name.endswith(".blade.php"):
        return "Blade"
    if name.endswith(".html.twig") or name.endswith(".twig"):
        return "Twig"
    if name in LANGUAGE_BY_FILENAME:
        return LANGUAGE_BY_FILENAME[name]
    ext = os.path.splitext(name)[1].lower()
    return LANGUAGES.get(ext)


def count_lines(abs_path):
    """Count lines in a text file without loading it whole."""
    total = 0
    last_byte_newline = True
    try:
        with open(abs_path, "rb") as handle:
            while True:
                chunk = handle.read(1024 * 1024)
                if not chunk:
                    break
                total += chunk.count(b"\n")
                last_byte_newline = chunk.endswith(b"\n")
    except OSError:
        return None
    return total if last_byte_newline else total + 1


def looks_binary(abs_path):
    try:
        with open(abs_path, "rb") as handle:
            return b"\x00" in handle.read(4096)
    except OSError:
        return True


# --------------------------------------------------------------------------
# File inventory: git first, filesystem walk as fallback
# --------------------------------------------------------------------------

def list_files(root, errors):
    """Return (tracked_files, source) where source is 'git' or 'walk'."""
    out = run(["git", "ls-files", "-z"], root, errors)
    if out is not None:
        files = [f for f in out.split("\0") if f]
        if files:
            return files, "git ls-files"
        log_error(errors, "git ls-files returned no files (empty repository?)")
    walked = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_PARTS and d != ".git"]
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            walked.append(rel.replace("\\", "/"))
    return walked, "filesystem walk"


# --------------------------------------------------------------------------
# Git history
# --------------------------------------------------------------------------

def collect_git(root, errors):
    data = {
        "is_git_repo": False, "branch": None, "remote_url": None, "remote_slug": None,
        "first_commit_date": None, "last_commit_date": None, "commit_count": 0,
        "top_authors": [], "ai_co_author_trailers": {}, "ai_tool_mentions": {},
        "commit_subject_sample": [],
    }

    inside = run(["git", "rev-parse", "--is-inside-work-tree"], root, errors)
    if inside is None or inside.strip() != "true":
        log_error(errors, "not a git repository: git history facts are unavailable")
        return data
    data["is_git_repo"] = True

    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], root, errors)
    if branch:
        data["branch"] = branch.strip()

    remote = run(["git", "config", "--get", "remote.origin.url"], root, errors)
    if remote:
        url = remote.strip()
        data["remote_url"] = url
        slug = re.sub(r"\.git$", "", url)
        slug = re.sub(r"^[a-z+]+://", "", slug)
        slug = re.sub(r"^[^@/]+@", "", slug)
        slug = re.sub(r"^[^/]+[:/]", "", slug)
        data["remote_slug"] = slug or None

    log = run(["git", "log", "--format=%H%x1f%an%x1f%aI%x1f%s%x1f%x1e"], root, errors,
              note="no commit history found (repository has no commits yet)")
    if log is None:
        return data

    authors = Counter()
    ai_trailers = Counter()
    tool_mentions = Counter()
    subjects = []
    dates = []

    for entry in log.split("\x1e"):
        entry = entry.strip("\n")
        if not entry:
            continue
        parts = entry.split("\x1f")
        if len(parts) < 4:
            continue
        _sha, author, iso_date, subject = parts[0], parts[1], parts[2], parts[3]
        body = parts[4] if len(parts) > 4 else ""
        authors[author.strip()] += 1
        if iso_date:
            dates.append(iso_date.strip())
        if subject:
            subjects.append(subject.strip())
        for line in (subject + "\n" + body).splitlines():
            low = line.lower()
            if low.startswith("co-authored-by:"):
                who = line.split(":", 1)[1].strip()
                who = re.sub(r"<[^>]*>", "", who).strip() or line.split(":", 1)[1].strip()
                if who:
                    ai_trailers[who] += 1
            for tool in AI_TOOL_NAMES:
                if re.search(r"\b%s\b" % re.escape(tool), low):
                    tool_mentions[tool] += 1

    data["commit_count"] = len(subjects)
    data["commit_subject_sample"] = subjects[:20]
    if dates:
        dates_sorted = sorted(dates)
        data["first_commit_date"] = dates_sorted[0][:10]
        data["last_commit_date"] = dates_sorted[-1][:10]
    data["top_authors"] = [
        {"name": name, "commits": count} for name, count in authors.most_common(15)
    ]
    data["ai_co_author_trailers"] = dict(ai_trailers.most_common(20))
    data["ai_tool_mentions"] = dict(tool_mentions.most_common(20))
    return data


# --------------------------------------------------------------------------
# Manifest parsing (stack + main dependencies)
# --------------------------------------------------------------------------

def parse_package_json(path, abs_path, errors):
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
            pkg = json.load(handle)
    except Exception as exc:  # noqa: BLE001 - a broken manifest must not stop the run
        log_error(errors, "could not parse %s: %s" % (path, exc))
        return None
    deps = []
    for section in ("dependencies", "devDependencies", "peerDependencies"):
        for name, version in (pkg.get(section) or {}).items():
            if len(deps) < 400:
                deps.append({"name": name, "version": str(version), "section": section})
    scripts = pkg.get("scripts") or {}
    return {
        "path": path, "type": "node", "name": pkg.get("name"), "version": pkg.get("version"),
        "license": pkg.get("license") if isinstance(pkg.get("license"), str) else None,
        "engines": pkg.get("engines") or {},
        "dependencies": deps,
        "scripts": {k: str(v) for k, v in list(scripts.items())[:40]},
    }


def parse_composer_json(path, abs_path, errors):
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
            data = json.load(handle)
    except Exception as exc:  # noqa: BLE001
        log_error(errors, "could not parse %s: %s" % (path, exc))
        return None
    deps = []
    for section in ("require", "require-dev"):
        for name, version in (data.get(section) or {}).items():
            deps.append({"name": name, "version": str(version), "section": section})
    return {
        "path": path, "type": "php", "name": data.get("name"), "version": data.get("version"),
        "license": data.get("license") if isinstance(data.get("license"), str) else None,
        "dependencies": deps,
        "scripts": {k: str(v) for k, v in list((data.get("scripts") or {}).items())[:40]},
        "php_requirement": (data.get("require") or {}).get("php"),
    }


def parse_pyproject(path, abs_path, errors):
    text = ""
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as exc:
        log_error(errors, "could not read %s: %s" % (path, exc))
        return None

    deps, name, version, requires_python, declared_license = [], None, None, None, None
    parsed = False
    try:
        import tomllib  # Python 3.11+
        try:
            data = tomllib.loads(text)
            parsed = True
            project = data.get("project") or {}
            name = project.get("name")
            version = project.get("version")
            requires_python = project.get("requires-python")
            lic = project.get("license")
            if isinstance(lic, str):
                declared_license = lic
            elif isinstance(lic, dict):
                declared_license = lic.get("text") or lic.get("file")
            for item in project.get("dependencies") or []:
                match = re.match(r"^\s*([A-Za-z0-9_.\-\[\]]+)\s*(.*)$", str(item))
                if match:
                    deps.append({"name": match.group(1), "version": match.group(2).strip(), "section": "dependencies"})
            poetry = ((data.get("tool") or {}).get("poetry") or {})
            if poetry:
                name = name or poetry.get("name")
                version = version or poetry.get("version")
                for group in ("dependencies", "dev-dependencies"):
                    for dep_name, spec in (poetry.get(group) or {}).items():
                        if dep_name.lower() == "python":
                            requires_python = requires_python or str(spec)
                            continue
                        deps.append({"name": dep_name, "version": str(spec), "section": "poetry." + group})
                for group_name, group in (poetry.get("group") or {}).items():
                    for dep_name, spec in (group.get("dependencies") or {}).items():
                        if dep_name.lower() == "python":
                            requires_python = requires_python or str(spec)
                            continue
                        deps.append({"name": dep_name, "version": str(spec),
                                     "section": "poetry.group.%s" % group_name})
        except Exception as exc:  # noqa: BLE001
            log_error(errors, "could not parse %s with tomllib: %s" % (path, exc))
    except ImportError:
        pass

    if not parsed:
        block = re.search(r"(?ms)^\[project\].*?(?=^\[|\Z)", text)
        if block:
            for match in re.finditer(r'"([A-Za-z0-9_.\-]+)\s*([<>=!~^][^"]*)"', block.group(0)):
                deps.append({"name": match.group(1), "version": match.group(2).strip(), "section": "dependencies"})
        for match in re.finditer(r'(?m)^\s*([A-Za-z0-9_.\-]+)\s*=\s*"([^"]*)"', text):
            if match.group(1) in ("python", "name", "version", "requires-python", "license"):
                if match.group(1) == "name" and not name:
                    name = match.group(2)
                elif match.group(1) == "version" and not version and re.match(r"^\d", match.group(2)):
                    version = match.group(2)
                elif match.group(1) == "requires-python" and not requires_python:
                    requires_python = match.group(2)

    return {
        "path": path, "type": "python", "name": name, "version": version,
        "license": declared_license, "requires_python": requires_python,
        "dependencies": deps[:400], "parsed_with_tomllib": parsed,
    }


def parse_requirements(path, abs_path, errors):
    deps = []
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
            for raw in handle:
                line = raw.strip()
                if not line or line.startswith("#") or line.startswith("-"):
                    continue
                match = re.match(r"^([A-Za-z0-9_.\-\[\]]+)\s*(.*)$", line)
                if match:
                    deps.append({"name": match.group(1), "version": match.group(2).strip() or None,
                                 "section": "requirements"})
    except OSError as exc:
        log_error(errors, "could not read %s: %s" % (path, exc))
        return None
    return {"path": path, "type": "python-requirements", "dependencies": deps[:400]}


def parse_go_mod(path, abs_path, errors):
    deps = []
    module = None
    go_version = None
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as exc:
        log_error(errors, "could not read %s: %s" % (path, exc))
        return None
    module_match = re.search(r"(?m)^module\s+(\S+)", text)
    if module_match:
        module = module_match.group(1)
    go_match = re.search(r"(?m)^go\s+(\S+)", text)
    if go_match:
        go_version = go_match.group(1)
    for match in re.finditer(r"(?m)^\s*(?:require\s+)?([\w.\-]+\.[\w.\-/]+)\s+(v[\w.\-+]+)", text):
        deps.append({"name": match.group(1), "version": match.group(2), "section": "require"})
    return {"path": path, "type": "go", "name": module, "go_version": go_version,
            "dependencies": deps[:400]}


def parse_cargo_toml(path, abs_path, errors):
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as exc:
        log_error(errors, "could not read %s: %s" % (path, exc))
        return None
    deps, name, version, declared_license = [], None, None, None
    try:
        import tomllib
        data = tomllib.loads(text)
        package = data.get("package") or {}
        name, version = package.get("name"), package.get("version")
        declared_license = package.get("license")
        for group in ("dependencies", "dev-dependencies", "build-dependencies"):
            for dep_name, spec in (data.get(group) or {}).items():
                deps.append({"name": dep_name,
                             "version": spec if isinstance(spec, str) else json.dumps(spec),
                             "section": group})
    except Exception:  # noqa: BLE001 - fall back to regex
        for group in ("dependencies", "dev-dependencies"):
            block = re.search(r"(?ms)^\[%s\](.*?)(?=^\[|\Z)" % re.escape(group), text)
            if not block:
                continue
            for match in re.finditer(r'(?m)^\s*([A-Za-z0-9_\-]+)\s*=\s*"?([^"\n]+)"?', block.group(1)):
                deps.append({"name": match.group(1), "version": match.group(2).strip().rstrip(","),
                             "section": group})
        name_match = re.search(r'(?m)^\s*name\s*=\s*"([^"]+)"', text)
        version_match = re.search(r'(?m)^\s*version\s*=\s*"([^"]+)"', text)
        license_match = re.search(r'(?m)^\s*license\s*=\s*"([^"]+)"', text)
        name = name_match.group(1) if name_match else None
        version = version_match.group(1) if version_match else None
        declared_license = license_match.group(1) if license_match else None
    return {"path": path, "type": "rust", "name": name, "version": version,
            "license": declared_license, "dependencies": deps[:400]}


def parse_gemfile(path, abs_path, errors):
    deps = []
    ruby_version = None
    try:
        with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as exc:
        log_error(errors, "could not read %s: %s" % (path, exc))
        return None
    ruby_match = re.search(r'^\s*ruby\s+["\']([^"\']+)["\']', text, re.MULTILINE)
    if ruby_match:
        ruby_version = ruby_match.group(1)
    for match in re.finditer(r'^\s*gem\s+["\']([^"\']+)["\']\s*(?:,\s*["\']([^"\']+)["\'])?', text, re.MULTILINE):
        deps.append({"name": match.group(1), "version": match.group(2), "section": "gem"})
    return {"path": path, "type": "ruby", "ruby_version": ruby_version, "dependencies": deps[:400]}


def parse_pom_xml(path, abs_path, errors):
    import xml.etree.ElementTree as ET
    deps, artifact, version, java_version = [], None, None, None
    try:
        tree = ET.parse(abs_path)
    except Exception as exc:  # noqa: BLE001
        log_error(errors, "could not parse %s: %s" % (path, exc))
        return None
    root = tree.getroot()
    tag = lambda el: el.tag.split("}")[-1]  # noqa: E731
    for child in root:
        if tag(child) == "artifactId" and artifact is None:
            artifact = child.text
        elif tag(child) == "version" and version is None:
            version = child.text
        elif tag(child) == "properties":
            for prop in child:
                if tag(prop) in ("java.version", "maven.compiler.source"):
                    java_version = prop.text
    deps_node = None
    for child in root:
        if tag(child) == "dependencies":
            deps_node = child
            break
    if deps_node is not None:
        for dep in deps_node:
            group = art = ver = None
            for field in dep:
                if tag(field) == "groupId":
                    group = field.text
                elif tag(field) == "artifactId":
                    art = field.text
                elif tag(field) == "version":
                    ver = field.text
            if art:
                deps.append({"name": ("%s:%s" % (group, art)) if group else art, "version": ver,
                             "section": "dependencies"})
    return {"path": path, "type": "java-maven", "name": artifact, "version": version,
            "java_version": java_version, "dependencies": deps[:400]}


MANIFEST_PARSERS = [
    ("package.json", parse_package_json),
    ("composer.json", parse_composer_json),
    ("pyproject.toml", parse_pyproject),
    ("requirements.txt", parse_requirements),
    ("go.mod", parse_go_mod),
    ("Cargo.toml", parse_cargo_toml),
    ("Gemfile", parse_gemfile),
    ("pom.xml", parse_pom_xml),
]


def collect_stack(files, root, errors):
    present = set(files)
    manifests = []
    for name, parser in MANIFEST_PARSERS:
        candidates = [name] + [f for f in files if f.endswith("/" + name)]
        for rel in sorted(candidates, key=len)[:4]:
            if rel not in present:
                continue
            parsed = parser(rel, os.path.join(root, rel.replace("/", os.sep)), errors)
            if parsed:
                manifests.append(parsed)
    return {
        "manifests_found": [m["path"] for m in manifests],
        "manifests": manifests,
    }


# --------------------------------------------------------------------------
# CI, tests, docs, licence, media, layout
# --------------------------------------------------------------------------

def parse_yaml_keys(text, section):
    """Tiny indentation-aware reader: returns the child keys of a top-level section."""
    keys = []
    lines = text.splitlines()
    in_section = False
    section_indent = None
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        if not in_section:
            if stripped.split(":")[0].strip() == section and stripped.endswith(":"):
                in_section = True
                section_indent = indent
            continue
        if indent <= section_indent and not stripped.startswith("-"):
            break
        if indent == (section_indent or 0) + 2 and ":" in stripped:
            keys.append(stripped.split(":", 1)[0].strip().strip("'\""))
    return keys


def collect_ci(files, root, errors):
    workflows = []
    for rel in files:
        lowered = rel.lower()
        if not lowered.endswith((".yml", ".yaml")) and not lowered.endswith("jenkinsfile"):
            continue
        if not any(rel.startswith(prefix) or rel == prefix or prefix in lowered
                   for prefix in CI_WORKFLOW_GLOBS):
            continue
        abs_path = os.path.join(root, rel.replace("/", os.sep))
        try:
            with open(abs_path, "r", encoding="utf-8", errors="replace") as handle:
                text = handle.read()
        except OSError as exc:
            log_error(errors, "could not read CI file %s: %s" % (rel, exc))
            continue
        jobs = parse_yaml_keys(text, "jobs")
        triggers = []
        on_block = re.search(r"(?m)^on:[ \t]*(\S.*)$", text)
        if on_block:
            triggers = [part.strip(" '\"[]") for part in re.split(r"[,\[\]]", on_block.group(1)) if part.strip()]
        else:
            triggers = parse_yaml_keys(text, "on")
        if not jobs:
            jobs = re.findall(r"(?m)^\s{2}([A-Za-z0-9_.\-]+):\s*$", text)[:20] if "stage" in text else []
        workflows.append({"path": rel, "jobs": jobs, "triggers": triggers})
    return {"workflows": workflows, "workflow_count": len(workflows)}


def collect_tests(files):
    test_files = [f for f in files if TEST_PATH_RE.search(f)]
    return {
        "test_file_count": len(test_files),
        "test_files_sample": sorted(test_files)[:MAX_LISTED],
    }


def collect_docs(files):
    docs = []
    for rel in sorted(files):
        base = os.path.basename(rel)
        if rel.startswith(("docs/", "doc/", "documentation/", "wiki/")) and \
                rel.lower().endswith((".md", ".rst", ".adoc", ".txt")):
            docs.append(rel)
        elif "/" not in rel and DOC_NAMES.match(base) and \
                rel.lower().endswith((".md", ".rst", ".txt", "")):
            docs.append(rel)
    return {"count": len(docs), "files": docs[:MAX_LISTED * 2], "truncated": len(docs) > MAX_LISTED * 2}


def collect_license(files, stack):
    files_found = [f for f in files if "/" not in f and LICENSE_RE.match(os.path.basename(f))]
    declared = None
    for manifest in stack["manifests"]:
        if manifest.get("license"):
            declared = manifest["license"]
            break
    return {"files": sorted(files_found), "present": bool(files_found or declared), "declared": declared}


def collect_media(files):
    logos, shots, others = [], [], []
    for rel in sorted(files):
        if not rel.lower().endswith(IMAGE_SUFFIXES):
            continue
        if is_skipped(rel):
            continue
        if LOGO_HINT_RE.search(rel):
            if len(logos) < MAX_LISTED:
                logos.append(rel)
        elif SHOT_HINT_RE.search(rel):
            if len(shots) < MAX_LISTED:
                shots.append(rel)
        elif len(others) < MAX_LISTED:
            others.append(rel)
    return {"logo_candidates": logos, "screenshot_candidates": shots,
            "other_images_sample": others}


def collect_layout(files):
    counts = Counter()
    for rel in files:
        top = rel.split("/")[0]
        if "/" in rel:
            counts[top + "/"] += 1
        else:
            counts["(root files)"] += 1
    return [{"path": path, "files": count} for path, count in counts.most_common(MAX_LISTED)]


def collect_languages(files, root, errors):
    stats = defaultdict(lambda: {"files": 0, "lines": 0, "extensions": Counter()})
    for rel in files:
        if is_skipped(rel):
            continue
        language = detect_language(rel)
        if not language:
            continue
        abs_path = os.path.join(root, rel.replace("/", os.sep))
        try:
            if os.path.getsize(abs_path) > MAX_FILE_BYTES:
                continue
        except OSError:
            continue
        lines = count_lines(abs_path)
        if lines is None:
            log_error(errors, "could not read %s" % rel)
            continue
        if lines == 0 and looks_binary(abs_path):
            continue
        entry = stats[language]
        entry["files"] += 1
        entry["lines"] += lines
        entry["extensions"][os.path.splitext(rel)[1].lower() or os.path.basename(rel)] += 1
    result = []
    for language, entry in sorted(stats.items(), key=lambda kv: -kv[1]["lines"]):
        result.append({
            "language": language,
            "files": entry["files"],
            "lines": entry["lines"],
            "extensions": [ext for ext, _ in entry["extensions"].most_common(6)],
        })
    return result


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def build_facts(root, errors):
    files, source = list_files(root, errors)
    git = collect_git(root, errors)
    stack = collect_stack(files, root, errors)

    facts = {
        "schema": "living-readme/facts/1",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "repo": {
            "name": os.path.basename(os.path.abspath(root)),
            "root": os.path.abspath(root).replace("\\", "/"),
            "file_source": source,
            "tracked_file_count": len(files),
            "remote_url": git.get("remote_url"),
            "remote_slug": git.get("remote_slug"),
            "branch": git.get("branch"),
            "is_git_repo": git.get("is_git_repo"),
        },
        "git": {k: v for k, v in git.items() if k not in ("remote_url", "remote_slug", "branch", "is_git_repo")},
        "languages": collect_languages(files, root, errors),
        "stack": stack,
        "ci": collect_ci(files, root, errors),
        "tests": collect_tests(files,),
        "docs": collect_docs(files),
        "license": collect_license(files, stack),
        "media": collect_media(files),
        "top_level": collect_layout(files),
        "errors": errors,
    }
    if not files:
        log_error(errors, "no files found: is this the right directory?")
    return facts


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Collect verifiable facts about a repository as JSON (stdlib only).")
    parser.add_argument("--repo", default=".", help="repository root (default: current directory)")
    parser.add_argument("-o", "--output", help="write JSON to this file instead of stdout")
    parser.add_argument("--compact", action="store_true", help="print compact JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 when git is unavailable (facts are still printed)")
    args = parser.parse_args(argv)

    root = os.path.abspath(args.repo)
    if not os.path.isdir(root):
        print(json.dumps({"errors": ["not a directory: %s" % root]}, indent=2))
        return 2

    errors = []
    try:
        facts = build_facts(root, errors)
    except Exception as exc:  # noqa: BLE001 - never crash, always emit usable JSON
        facts = {"schema": "living-readme/facts/1", "errors": errors + ["unexpected failure: %r" % exc]}

    payload = json.dumps(facts, indent=None if args.compact else 2, ensure_ascii=False, default=str)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")
        sys.stderr.write("wrote %s\n" % args.output)
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8")  # keep non-ASCII author names readable
        except Exception:  # noqa: BLE001 - older/odd stdio wrappers
            pass
        print(payload)

    if args.strict and not facts.get("repo", {}).get("is_git_repo"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
