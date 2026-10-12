---
name: living-readme
description: Create or update a truthful, professional README for any repository. Use when the user says "write a README", "update the README", "refresh the README", "make this repo professional", "the README is stale", "does the README still match the code", "document this project", "explain this repo on GitHub", or when handing a repository to someone new. Mode A creates a README from evidence in the repository (git history, manifests, CI, tests, docs, screenshots). Mode B re-checks an existing README after real changes and edits only the sections the changes touched. The README never claims anything the repository cannot prove.
---

# living-readme

A README is a promise about a project. This skill keeps that promise true:
every sentence traceable to a file, a command or a commit — and refreshed only
when something real changed.

Two modes:

| Mode | When | Outcome |
|---|---|---|
| **A — CREATE** | No README, or the existing one is a placeholder | A new README drafted from facts, verified, shown to the owner |
| **B — UPDATE** | A README exists and carries the last-sync marker | Only the affected sections change, or an explicit "still accurate" |

Everything is plain Markdown plus two Python scripts. No tool-specific features
are required: it works the same in Claude Code, Codex, Cursor, ChatGPT or any
agent that can read a folder and run a command.

**Locating the scripts.** The commands below assume the skill folder sits inside
the repository at `living-readme/`. If it is installed globally (for example
`~/.claude/skills/living-readme/`), resolve the script and reference paths
relative to this `SKILL.md` file instead, and always pass `--repo <repo root>`
so the scripts measure the right project, not the skill folder.

## Principles

1. **Truth over polish.** Every claim must be backed by evidence you actually
   saw: a file path, a command output, a git record. If you cannot point at the
   evidence, cut the sentence. A shorter true README beats a beautiful untrue one.
2. **Humans first, developers second.** The first screen answers "what is this,
   who is it for, is it alive?" in plain language for a business or first-time
   reader. Architecture, stack and commands come after. Never open with jargon.
3. **Detailed but scannable.** Headings, short tables, short sentences. Deep
   detail belongs in `docs/`; the README links to it. Target ~800–2500 words.
4. **Honest limits, dated.** Real constraints (single-process server, no queue
   worker, unmeasured performance, unfinished modules) are stated as
   "as of YYYY-MM-DD". An undated status line is a lie waiting to happen.
5. **The owner's story comes from the owner.** Effort numbers, motivations,
   credit to people and AI tools, and anything about the team are only written
   when the owner said them. Never invent a founder story, a timeline or a
   collaborator.
6. **Ask for what the code cannot tell you.** Purpose, audience, scale,
   credentials, what must stay private, which screenshots are allowed — ask,
   don't guess. See `references/owner-questions.md`.
7. **Never auto-publish.** Show the owner the draft. Pushing, committing or
   publishing happens only after explicit approval.

## Mode A — CREATE

Work from the repository root. Keep the user informed between steps: this is a
short pipeline, not a silent rewrite.

**Step 1 — Collect facts.**

```bash
python3 living-readme/scripts/collect_facts.py --repo . -o facts.json
```

Read `facts.json`. It is the only source for counts, dates, authors, languages,
dependencies, CI jobs, test counts and media candidates. Do not use numbers from
memory, and do not round "296 commits" into "hundreds of commits".
If the owner keeps it out of the repository, write it outside the repo or delete
it afterwards; it is a working file, not a deliverable.

**Step 2 — Identify audience and product identity.** From the facts plus the
code, answer for yourself: what is this, what is it *not*, who uses it, what
does it replace, is it a library / web app / CLI / data or research project, is
it public or private?

Then **ask the owner** the short question list in
`references/owner-questions.md` for anything the code cannot answer — purpose,
origin, real numbers, credit, status, privacy, screenshots. One message, the
questions only, no essay. If the owner is unavailable, write only what the
repository proves and mark nothing as invented; leave the story sections out
rather than filling them with plausible fiction.

**Step 3 — Draft with `references/readme-template.md`.** Follow its section
order. Mark which sections are optional for this project type, and delete the
ones that do not apply. Open the file with the marker and keep the auto facts
block machine-generated:

```markdown
<!-- living-readme: last-sync <commit-sha> <YYYY-MM-DD> -->
...
<!-- living-readme:facts:start -->
...numbers copied from facts.json...
<!-- living-readme:facts:end -->
```

Use the latest commit SHA and today's date for the marker
(`git rev-parse --short HEAD`). Badges are only real ones: a CI badge whose
workflow file exists, a license badge whose license file exists, a live-link
badge only if the URL is confirmed.

**Step 4 — Verification pass.** Go through
`references/verify-checklist.md` item by item and fix what fails. Then
double-check the risky parts yourself: run (or read) the setup commands, open
every relative link, re-read every number against `facts.json`.

**Step 5 — Show the owner.** Present the README and a short "what I could not
verify" note. Never commit, push, or publish without explicit approval.

## Mode B — UPDATE

**Step 1 — Read the marker.**

```bash
grep -n "living-readme: last-sync" README.md
# <!-- living-readme: last-sync 4f2a91c 2026-09-30 -->
```

No marker? This is a Mode A job (or the README was written elsewhere): run one
CREATE pass and add the marker so future updates are cheap.

**Step 2 — Detect changes.**

```bash
python3 living-readme/scripts/detect_changes.py --since-marker README.md
```

It runs `git diff --name-status` and `git log` since that commit and sorts every
path into README-relevant categories (new/removed modules or routes,
dependencies/stack, setup/commands, env/config, CI/quality gates, docs added,
big size changes) versus noise (style-only, tests-only, typos, lockfiles,
assets). Read the human summary, not just the exit code. Add `--json` when you
want to script the decision.

**Step 3 — If nothing relevant changed**, report exactly that: "README still
accurate as of <date>; only noise since <sha> (tests, lockfile, formatting)."
Stop. Do not rewrite prose to look busy. If the only outcome is a marker bump,
that is a legitimate result — bump it, and say so.

**Step 4 — If something relevant changed**, update only the affected sections:

| Change category | Sections to touch |
|---|---|
| Modules / routes added or removed | "What's inside" table, "How it works", repo map |
| Dependencies / stack / runtime version | badges, technical stack, getting started |
| Setup, build or run commands | getting started, quality gates |
| Env vars, config, migrations | getting started, honest limits, privacy note |
| CI / quality gates | badges, quality gates |
| Docs added or moved | "Documents & where to verify" |
| Big diff (> ~1500 lines or > ~60 files) | re-read the whole README, not one section |

Also refresh the auto facts block between
`<!-- living-readme:facts:start -->` and `<!-- living-readme:facts:end -->`
from a fresh `collect_facts.py` run. Leave untouched sections byte-identical —
that is what makes the diff reviewable.

**Step 5 — Bump the marker** to the current HEAD and today's date. The script
can do the single-line edit for you:

```bash
python3 living-readme/scripts/detect_changes.py --since-marker README.md \
  --write-marker README.md --quiet
```

**Step 6 — Verify and get approval.** Re-run the checklist for the changed
sections, show the owner the diff summary (what changed, why, what you could not
verify). Approval before commit or push, always.

## Optional automation (warn, never edit)

A CI job or a pre-push hook can run `detect_changes.py` and *warn* when relevant
changes exist since the last sync. It must never rewrite the README: a machine
that edits prose unsupervised is exactly how a README starts lying.

```bash
python3 living-readme/scripts/detect_changes.py --since-marker README.md \
  --fail-on-relevant=false
```

Exit codes: `0` = report produced (relevant or not), `1` = relevant changes and
you passed `--fail-on-relevant=true`, `2` = the repo or arguments could not be
read. Ready-to-paste GitHub Actions workflow and git `pre-push` hook:
`references/automation.md`.

## Delegation

Mechanical, checkable work can go to a cheaper model: running `collect_facts.py`,
running `detect_changes.py`, drafting the first version of a section, and
formatting tables. Keep on the strongest model (or the owner) the parts that
require judgement: deciding what is true, what is private, what the product is
*not*, the final verification pass, and the wording of honest limits. Whatever
the model, the checklist and the owner's approval are the gate.

## Safety

- **Never** put secrets, API keys, tokens, private hostnames, internal IPs,
  admin URLs, customer names, or production weak points ("the DB password is in
  `.env`", "no rate limit on `/login`") into a README of a **public** repository.
- For a **private** repo, such sections are allowed but must be explicitly
  marked, e.g. `> INTERNAL ONLY — do not copy outside the company`, and the
  owner must confirm the repository stays private.
- Prefer describing the *shape* of configuration (`see .env.example`) over
  repeating values.
- Screenshots: only real captures the owner approved; never a mockup presented
  as the running product. Blur or crop real data before it ships.
- If facts and the owner's claims disagree, say so and ask — do not silently
  pick the flattering version.

## Running the scripts

Python 3.8+ standard library only. Use whichever launcher exists: `python3`, `python`, `py -3` (Windows), or `uv run --no-project --python 3.12 <script>`. If no Python is available, do the same steps by hand with `git log`, `git diff --name-status` and `git ls-files`, and say so in the report.
