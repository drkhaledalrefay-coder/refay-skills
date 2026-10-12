#!/usr/bin/env python3
"""detect_changes.py - decide whether a README still tells the truth.

Compares the current branch against the commit recorded in the README's
last-sync marker (or a --since SHA) and classifies every changed path into
README-relevant categories vs. noise.

Python 3 standard library only.

Usage:
    python3 living-readme/scripts/detect_changes.py --since-marker README.md
    python3 living-readme/scripts/detect_changes.py --since abc1234 --json
    python3 living-readme/scripts/detect_changes.py --since-marker README.md --fail-on-relevant=true
    python3 living-readme/scripts/detect_changes.py --since-marker README.md --write-marker README.md

Exit codes:
    0  report produced (relevant changes found or not) - the normal case
    1  --fail-on-relevant=true AND relevant changes exist
    2  bad arguments, or the repository/sha could not be read at all

The script never edits the README body. --write-marker only rewrites the single
marker line. It WARNS; a human or agent decides what to change.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import OrderedDict

# --------------------------------------------------------------------------
# Configuration: the classification rules. Edit these, not the code below.
# Each rule: id, human label, regexes matched against the changed path,
# "why" (the sentence shown to the owner), and "keywords" used to spot
# matching commit subjects.
# --------------------------------------------------------------------------

RELEVANT_RULES = [
    {
        "id": "modules_routes",
        "label": "Modules, routes and entry points",
        "patterns": [
            r"(^|/)(routes?|routers?|controllers?|handlers?|endpoints?|api|views?|pages?|screens?|components?|services?|models?|middleware)(/|\.|$)",
            r"(^|/)(main|app|index|server|cli|manage|wsgi|asgi)\.(py|js|ts|php|rb|go|rs|java)$",
            r"(^|/)(urls|web|console)\.(py|php)$",
        ],
        "why": "modules, routes or entry points were added, removed or renamed",
        "keywords": ["add", "remove", "route", "module", "controller", "endpoint", "page", "feature"],
    },
    {
        "id": "dependencies_stack",
        "label": "Dependencies and stack",
        "patterns": [
            r"(^|/)(package\.json|composer\.json|pyproject\.toml|requirements[^/]*\.txt|setup\.py|setup\.cfg|"
            r"Pipfile|go\.mod|go\.sum|Cargo\.toml|Gemfile|pom\.xml|build\.gradle[^/]*|\.csproj|Package\.swift)$",
            r"(^|/)(Dockerfile|docker-compose[^/]*\.ya?ml|\.nvmrc|\.python-version|\.tool-versions|"
            r"\.ruby-version|rust-toolchain[^/]*)$",
        ],
        "why": "a manifest or runtime file changed: install steps, versions or badges may be stale",
        "keywords": ["bump", "upgrade", "dependency", "dependencies", "php", "node", "python", "version", "package"],
    },
    {
        "id": "setup_commands",
        "label": "Setup, build and run commands",
        "patterns": [
            r"(^|/)(Makefile|makefile|justfile|Taskfile[^/]*\.ya?ml|build\.sh|install\.sh|setup\.sh|deploy\.sh|"
            r"run\.sh|bootstrap\.sh|start\.sh|Procfile|railway\.json|vercel\.json|netlify\.toml|render\.ya?ml|"
            r"fly\.toml|heroku\.ya?ml)$",
            r"(^|/)(package\.json|composer\.json|pyproject\.toml)$",  # scripts section lives here too
        ],
        "why": "a build/run/deploy entry point changed: the README's commands may no longer work",
        "keywords": ["script", "make", "build", "deploy", "install", "setup", "run", "command"],
    },
    {
        "id": "env_config",
        "label": "Environment and configuration",
        "patterns": [
            r"(^|/)\.env(\.[^/]*)?$", r"(^|/)\.env\.example$", r"(^|/)env\.example$",
            r"(^|/)(config|configs|settings)(/|\.|$)",
            r"(^|/)(nginx|apache|php|caddy|supervisor|systemd)[^/]*\.(conf|ini|ya?ml|service)$",
            r"(^|/)(migrations?|schema\.(sql|rb|prisma))(/|\.|$)",
        ],
        "why": "configuration, environment variables or schema changed: setup and 'honest limits' may be wrong",
        "keywords": ["config", "env", "variable", "migration", "schema", "database", "setting", "secret"],
    },
    {
        "id": "ci_quality",
        "label": "CI and quality gates",
        "patterns": [
            r"^\.github/workflows/", r"^\.gitlab-ci\.yml$", r"^\.circleci/", r"^azure-pipelines\.yml$",
            r"^\.woodpecker\.yml$", r"^\.drone\.yml$", r"(^|/)Jenkinsfile$", r"^bitbucket-pipelines\.yml$",
            r"(^|/)(\.eslintrc[^/]*|eslint\.config\.[^/]+|\.php-cs-fixer[^/]*|pint\.json|phpstan[^/]*\.neon|"
            r"psalm[^/]*\.xml|\.golangci[^/]*\.ya?ml|ruff\.toml|\.flake8|mypy\.ini|\.pre-commit-config\.ya?ml|"
            r"codecov\.ya?ml|sonar-project\.properties|\.snyk)$",
        ],
        "why": "CI or quality-gate configuration changed: badges and the 'quality gates' section may be wrong",
        "keywords": ["ci", "workflow", "lint", "static analysis", "test pipeline", "badge", "actions"],
    },
    {
        "id": "docs",
        "label": "Documentation",
        "patterns": [
            r"^docs?/", r"^documentation/", r"(^|/)(README|CONTRIBUTING|CHANGELOG|SECURITY|ARCHITECTURE|"
            r"CODE_OF_CONDUCT|GOVERNANCE|ROADMAP|LICENSE|LICENCE|ATTRIBUTION|AGENTS|CLAUDE)[^/]*$",
        ],
        "why": "documentation was added or removed: the README's 'documents & where to verify' table is affected",
        "keywords": ["doc", "readme", "changelog", "license", "guide"],
    },
    {
        "id": "structure",
        "label": "Repository structure",
        "patterns": [
            r"^[^/]+/$", r"^\.github/", r"^\.devcontainer/", r"^scripts?/", r"^tools?/",
        ],
        "why": "top-level layout changed: the repository map is affected",
        "keywords": ["move", "restructure", "rename", "layout", "structure", "directory"],
    },
]

NOISE_RULES = [
    {
        "id": "readme_itself",
        "label": "The README being synced",
        "patterns": [r"^README(\.[a-z]+)?$"],
    },
    {
        "id": "lockfile_only",
        "label": "Lockfiles",
        "patterns": [
            r"(^|/)(package-lock\.json|npm-shrinkwrap\.json|yarn\.lock|pnpm-lock\.yaml|bun\.lockb?|"
            r"composer\.lock|poetry\.lock|Pipfile\.lock|Gemfile\.lock|Cargo\.lock|go\.sum|"
            r"packages\.lock\.json|mix\.lock|pubspec\.lock)$",
        ],
    },
    {
        "id": "tests_only",
        "label": "Tests only",
        "patterns": [
            r"(^|/)(tests?|spec|specs|__tests__|testing|fixtures|testdata|snapshots?)(/|$)",
            r"(^|/)(test_[^/]+|[^/]+_test|test\.[a-z]+|[^/]+\.(test|spec)\.[a-z]+|[^/]+Test\.(php|java|kt|cs))$",
        ],
    },
    {
        "id": "style_only",
        "label": "Formatting and metadata",
        "patterns": [
            r"(^|/)(\.editorconfig|\.prettierrc[^/]*|\.prettierignore|\.gitignore|\.gitattributes|"
            r"\.npmignore|\.dockerignore|\.stylelintrc[^/]*|\.vscode/|\.idea/|\.DS_Store|"
            r"\.mailmap|tsconfig\.json|jsconfig\.json)$",
        ],
    },
    {
        "id": "assets_only",
        "label": "Static assets",
        "patterns": [
            r"\.(png|jpe?g|gif|svg|webp|avif|ico|woff2?|ttf|eot|mp4|webm|mov|mp3|wav|pdf)$",
            r"\.(min\.js|min\.css|map)$",
        ],
    },
]

# Commit subjects that are noise no matter which file changed.
SUBJECT_NOISE_RE = re.compile(
    r"^\s*(typo|fix\s+typo|format(ting)?|prettier|eslint|lint|whitespace|style|comment|"
    r"revert|wip|chore|merge|bump\s+version)\b",
    re.IGNORECASE,
)

BIG_CHANGE_LINES = 1500   # added + removed lines
BIG_CHANGE_FILES = 60     # changed files

MARKER_RE = re.compile(
    r"<!--\s*living-readme:\s*last-sync\s+(?P<sha>[0-9a-fA-F]{4,40})"
    r"(?:\s+(?P<date>\d{4}-\d{2}-\d{2}))?\s*-->")

MARKER_TEMPLATE = "<!-- living-readme: last-sync {sha} {date} -->"


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def run_git(args, repo, errors, timeout=120):
    try:
        proc = subprocess.run(
            ["git"] + args, cwd=repo, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=timeout,
        )
    except FileNotFoundError:
        errors.append("git is not installed or not on PATH")
        return None
    except subprocess.TimeoutExpired:
        errors.append("git command timed out: git %s" % " ".join(args))
        return None
    except OSError as exc:
        errors.append("could not run git: %s" % exc)
        return None
    if proc.returncode != 0:
        message = (proc.stderr or proc.stdout or "").strip().splitlines()
        errors.append("git %s failed: %s" % (" ".join(args[:2]), message[0] if message else "unknown error"))
        return None
    return proc.stdout


def read_marker(path, errors):
    """Return {"path", "found", "sha", "date", "line_index"} for a README file."""
    result = {"path": path, "found": False, "sha": None, "date": None, "line_index": None}
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            lines = handle.read().splitlines()
    except OSError as exc:
        errors.append("could not read marker file %s: %s" % (path, exc))
        return result
    for index, line in enumerate(lines):
        match = MARKER_RE.search(line)
        if match:
            result.update({"found": True, "sha": match.group("sha"),
                           "date": match.group("date"), "line_index": index})
            return result
    errors.append("no '<!-- living-readme: last-sync <sha> <date> -->' marker found in %s" % path)
    return result


def classify(path, status):
    """Return (relevant_rule_or_None, noise_rule_or_None) for one changed path."""
    clean = path.replace("\\", "/")
    while clean.startswith("./"):
        clean = clean[2:]
    noise = None
    for rule in NOISE_RULES:
        if any(re.search(pattern, clean, re.IGNORECASE) for pattern in rule["patterns"]):
            noise = rule
            break
    if noise and noise["id"] in ("lockfile_only", "readme_itself"):
        return None, noise  # a lockfile alone is never README-relevant
    for rule in RELEVANT_RULES:
        if any(re.search(pattern, clean, re.IGNORECASE) for pattern in rule["patterns"]):
            return rule, noise
    return None, noise


def parse_name_status(output):
    """Parse `git diff --name-status` into [{status, path, old_path}]."""
    entries = []
    for line in (output or "").splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0].strip()
        if status[:1] in ("R", "C") and len(parts) >= 3:
            entries.append({"status": status, "path": parts[2].strip(), "old_path": parts[1].strip()})
        else:
            entries.append({"status": status, "path": parts[1].strip(), "old_path": None})
    return entries


def parse_numstat(output):
    added = removed = 0
    files = 0
    for line in (output or "").splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        files += 1
        try:
            added += int(parts[0])
        except ValueError:
            pass  # binary file: "-"
        try:
            removed += int(parts[1])
        except ValueError:
            pass
    return added, removed, files


def subjects_for(rule, subjects, limit=5):
    hits = []
    for subject in subjects:
        low = subject.lower()
        if SUBJECT_NOISE_RE.match(subject):
            continue
        if any(keyword in low for keyword in rule["keywords"]):
            hits.append(subject)
        if len(hits) >= limit:
            break
    return hits


def build_report(repo, since, marker, errors, verbose):
    report = OrderedDict()
    report["repository"] = repo
    report["marker"] = marker
    report["since"] = {"sha": since}
    report["errors"] = errors

    head_sha = run_git(["rev-parse", "HEAD"], repo, errors)
    head_date = run_git(["show", "-s", "--format=%cI", "HEAD"], repo, errors)
    head_branch = run_git(["rev-parse", "--abbrev-ref", "HEAD"], repo, errors)
    report["head"] = {
        "sha": head_sha.strip() if head_sha else None,
        "date": (head_date or "").strip()[:10] or None,
        "branch": head_branch.strip() if head_branch else None,
    }

    if not since:
        report["verdict"] = "unknown"
        if not errors:
            errors.append("no --since or --since-marker given, and no usable marker was found")
        report["relevant"] = []
        report["noise"] = []
        report["relevant_count"] = 0
        report["commits"] = {"count": 0, "subjects": []}
        report["files_changed"] = 0
        report["lines"] = {"added": 0, "removed": 0}
        report["big_change"] = {"is_big": False, "reason": None}
        return report

    # Resolve the since commit to a full SHA.
    resolved = run_git(["rev-parse", "--verify", "--quiet", "%s^{commit}" % since], repo, errors)
    if resolved is None:
        errors.append("cannot resolve commit '%s' (shallow clone, rebase or wrong SHA?); "
                      "re-run a full CREATE pass or re-sync the marker" % since)
        report["verdict"] = "unknown"
        report["relevant"] = []
        report["noise"] = []
        report["relevant_count"] = 0
        report["commits"] = {"count": 0, "subjects": []}
        report["files_changed"] = 0
        report["lines"] = {"added": 0, "removed": 0}
        report["big_change"] = {"is_big": False, "reason": None}
        return report
    report["since"]["resolved_sha"] = resolved.strip()
    since_date = run_git(["show", "-s", "--format=%cI", resolved.strip()], repo, errors)
    report["since"]["date"] = (since_date or "").strip()[:10] or None

    if head_sha and resolved.strip() == head_sha.strip():
        report["commits"] = {"count": 0, "subjects": []}
        report["files_changed"] = 0
        report["lines"] = {"added": 0, "removed": 0}
        report["relevant"] = []
        report["noise"] = []
        report["relevant_count"] = 0
        report["big_change"] = {"is_big": False, "reason": None}
        report["verdict"] = "accurate"
        return report

    diff = run_git(["diff", "--name-status", "-M", "%s..HEAD" % resolved.strip()], repo, errors)
    numstat = run_git(["diff", "--numstat", "-M", "%s..HEAD" % resolved.strip()], repo, errors)
    log = run_git(["log", "--format=%s", "%s..HEAD" % resolved.strip()], repo, errors)
    subjects = [line.strip() for line in (log or "").splitlines() if line.strip()]
    entries = parse_name_status(diff)
    added, removed, counted_files = parse_numstat(numstat)

    relevant = OrderedDict()
    noise = OrderedDict()
    uncategorized = []

    for entry in entries:
        relevant_rule, noise_rule = classify(entry["path"], entry["status"])
        record = {"status": entry["status"], "path": entry["path"]}
        if entry["old_path"]:
            record["old_path"] = entry["old_path"]
        if relevant_rule:
            bucket = relevant.setdefault(relevant_rule["id"], {
                "category": relevant_rule["id"], "label": relevant_rule["label"],
                "why": relevant_rule["why"], "files": [], "commit_subjects": [],
            })
            if len(bucket["files"]) < 40:
                bucket["files"].append(record)
        elif noise_rule:
            bucket = noise.setdefault(noise_rule["id"], {
                "category": noise_rule["id"], "label": noise_rule["label"], "files": [],
            })
            if len(bucket["files"]) < 40:
                bucket["files"].append(record)
        else:
            uncategorized.append(record)

    for bucket in relevant.values():
        bucket["commit_subjects"] = subjects_for(
            next(rule for rule in RELEVANT_RULES if rule["id"] == bucket["category"]), subjects)
        bucket["file_count"] = len(bucket["files"])

    if uncategorized:
        bucket = noise.setdefault("uncategorized", {
            "category": "uncategorized", "label": "Other files (judge by hand)", "files": [],
        })
        bucket["files"] = uncategorized[:40]
        bucket["file_count"] = len(uncategorized)

    big_reasons = []
    if added + removed > BIG_CHANGE_LINES:
        big_reasons.append("%d lines changed (threshold %d)" % (added + removed, BIG_CHANGE_LINES))
    if len(entries) > BIG_CHANGE_FILES:
        big_reasons.append("%d files changed (threshold %d)" % (len(entries), BIG_CHANGE_FILES))
    big = {"is_big": bool(big_reasons), "reason": "; ".join(big_reasons) or None}
    if big["is_big"]:
        relevant["size"] = {
            "category": "size", "label": "Big change", "why": "very large diff: re-read the README end to end",
            "files": [], "commit_subjects": [], "file_count": 0, "detail": big["reason"],
        }

    noise_subjects = [s for s in subjects if SUBJECT_NOISE_RE.match(s)]
    report["commits"] = {"count": len(subjects), "subjects": subjects[:30],
                         "noise_subjects": noise_subjects[:10]}
    report["files_changed"] = len(entries) or counted_files
    report["lines"] = {"added": added, "removed": removed}
    report["relevant"] = list(relevant.values())
    report["noise"] = list(noise.values())
    report["relevant_count"] = len(relevant)
    report["big_change"] = big
    if relevant:
        report["verdict"] = "update_needed"
    elif entries or subjects:
        report["verdict"] = "accurate"
    else:
        report["verdict"] = "accurate"

    if verbose and not entries and not subjects:
        report["note"] = "no commits and no file changes since %s" % resolved.strip()[:12]
    return report


def print_human(report, stream=sys.stdout):
    def out(text=""):
        stream.write(text + "\n")

    out("README change report")
    out("=" * 60)
    marker = report.get("marker") or {}
    if marker.get("path"):
        if marker.get("found"):
            out("Marker:      %s -> %s (%s)" % (marker["path"], marker.get("sha"), marker.get("date") or "no date"))
        else:
            out("Marker:      %s -> NOT FOUND" % marker["path"])
    since = report.get("since") or {}
    head = report.get("head") or {}
    if since.get("resolved_sha"):
        out("Comparing:   %s (%s) -> HEAD %s (%s)" % (
            since["resolved_sha"][:12], since.get("date") or "?",
            (head.get("sha") or "?")[:12], head.get("date") or "?"))
    commits = report.get("commits") or {}
    out("Commits:     %s   Files changed: %s   Lines: +%s / -%s" % (
        commits.get("count", 0), report.get("files_changed", 0),
        (report.get("lines") or {}).get("added", 0), (report.get("lines") or {}).get("removed", 0)))
    out()

    relevant = report.get("relevant") or []
    if relevant:
        out("README-relevant changes: %d category(ies)" % len(relevant))
        for bucket in relevant:
            out("  [%s] %s (%d file(s))" % (bucket["category"], bucket["label"], bucket.get("file_count", 0)))
            out("      why: %s" % bucket.get("why", ""))
            if bucket.get("detail"):
                out("      detail: %s" % bucket["detail"])
            for record in bucket.get("files", [])[:8]:
                suffix = " (was %s)" % record["old_path"] if record.get("old_path") else ""
                out("      %s %s%s" % (record["status"], record["path"], suffix))
            if len(bucket.get("files", [])) > 8:
                out("      ... %d more" % (len(bucket["files"]) - 8))
            for subject in bucket.get("commit_subjects", [])[:3]:
                out("      commit: %s" % subject)
    else:
        out("README-relevant changes: none")

    noise = report.get("noise") or []
    if noise:
        out()
        out("Not README-relevant (noise):")
        for bucket in noise:
            out("  [%s] %s (%d file(s))" % (bucket["category"], bucket.get("label", ""),
                                            bucket.get("file_count", len(bucket.get("files", [])))))
            for record in bucket.get("files", [])[:4]:
                out("      %s %s" % (record["status"], record["path"]))
            if len(bucket.get("files", [])) > 4:
                out("      ... %d more" % (len(bucket["files"]) - 4))

    noise_subjects = (report.get("commits") or {}).get("noise_subjects") or []
    if noise_subjects:
        out()
        out("Commit subjects that look like noise (typos, formatting, WIP):")
        for subject in noise_subjects[:5]:
            out("  - %s" % subject)

    out()
    verdict = report.get("verdict")
    if verdict == "update_needed":
        out("Verdict: README LIKELY NEEDS AN UPDATE (Mode B, steps 4-6).")
    elif verdict == "accurate":
        out("Verdict: README still accurate - nothing README-relevant changed.")
    else:
        out("Verdict: UNKNOWN - fix the errors below, then re-run.")
    errors = report.get("errors") or []
    if errors:
        out()
        out("Errors / warnings:")
        for error in errors:
            out("  - %s" % error)


def str2bool(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("1", "true", "yes", "on")


def write_marker(path, sha, date, errors):
    """Rewrite (or insert) the single last-sync marker line. Returns True on success."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace", newline="") as handle:
            text = handle.read()
    except OSError as exc:
        errors.append("could not read %s to write the marker: %s" % (path, exc))
        return False
    line = MARKER_TEMPLATE.format(sha=sha, date=date)
    newline = "\r\n" if "\r\n" in text else "\n"
    if MARKER_RE.search(text):
        text = MARKER_RE.sub(line, text, count=1)
    else:
        lines = text.splitlines()
        insert_at = 0
        for index, existing in enumerate(lines[:40]):
            if existing.startswith("# ") or existing.strip().startswith("<div align="):
                insert_at = index + 1
                break
        pieces = text.split(newline)
        pieces.insert(insert_at, "")
        pieces.insert(insert_at + 1, line)
        text = newline.join(pieces)
    if not text.endswith(("\n", "\r")):
        text += newline
    try:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    except OSError as exc:
        errors.append("could not write marker to %s: %s" % (path, exc))
        return False
    return True


def resolve_path(path, repo):
    """Prefer a path relative to the current directory, else relative to the repo."""
    if os.path.isabs(path):
        return path
    if os.path.exists(path):
        return os.path.abspath(path)
    return os.path.join(repo, path)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Classify changes since the README's last-sync commit into "
                    "README-relevant categories vs. noise.")
    parser.add_argument("--since", help="commit SHA/ref the README was last synced to")
    parser.add_argument("--since-marker", metavar="README",
                        help="read the last-sync SHA from this README file")
    parser.add_argument("--repo", default=".", help="repository root (default: current directory)")
    parser.add_argument("--json", action="store_true", help="also print the report as JSON")
    parser.add_argument("--only-json", action="store_true", help="print JSON only")
    parser.add_argument("--fail-on-relevant", type=str2bool, nargs="?", const=True, default=False,
                        help="exit 1 when relevant changes exist (default false)")
    parser.add_argument("--write-marker", metavar="README",
                        help="update the last-sync marker in this README to the current HEAD")
    parser.add_argument("--quiet", action="store_true", help="suppress the human summary")
    args = parser.parse_args(argv)

    repo = os.path.abspath(args.repo)
    errors = []
    marker = {"path": None, "found": False}

    if not os.path.isdir(repo):
        payload = json.dumps({"repository": repo, "verdict": "unknown",
                              "errors": ["not a directory: %s" % repo]}, indent=2)
        print(payload)
        return 2

    since = None
    if args.since_marker:
        marker_path = resolve_path(args.since_marker, repo)
        marker = read_marker(marker_path, errors)
        since = marker.get("sha")
    elif args.since:
        since = args.since
        marker = {"path": None, "found": None, "note": "SHA supplied with --since"}

    report = build_report(repo, since, marker, errors, verbose=True)

    if args.write_marker:
        head = report.get("head") or {}
        marker_target = resolve_path(args.write_marker, repo)
        if head.get("sha"):
            ok = write_marker(marker_target, head["sha"][:12], head.get("date") or "", errors)
            report["marker_written"] = bool(ok)
            report["marker_written_path"] = marker_target if ok else None
        else:
            errors.append("cannot write marker: HEAD sha is unknown")

    if not args.quiet and not args.only_json:
        print_human(report)
    if args.json or args.only_json:
        payload = json.dumps(report, indent=2, ensure_ascii=False)
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass
        print(payload)

    if args.fail_on_relevant and report.get("relevant_count"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
