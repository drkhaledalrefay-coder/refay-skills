# living-readme

An agent skill that **writes** a professional README for any repository — and
**keeps it true** afterwards, updating it only when something that a README
reader would care about actually changed.

No vendor lock-in: it is Markdown instructions plus two small Python 3 scripts
(standard library only), so it runs the same in Claude Code, Codex, Cursor,
ChatGPT or any agent that can read a folder and execute a command.

## Why it exists

Most READMEs fail in one of two ways. They are written once and then quietly go
stale — install commands that no longer work, module tables that list deleted
folders, "coming soon" features that shipped. Or they are polished fiction:
impressive claims with nothing behind them, an invented founder story, a
"production-ready" badge on a prototype.

This skill takes the opposite position: **every sentence must be traceable to
evidence** — a file path, a command output, a git record — and the parts the
code cannot prove (purpose, credits, roadmap, privacy) are asked of the owner,
never guessed.

## Install

Copy the whole folder into your agent's skills directory, for example:

```bash
# Claude Code / Codex-style skills directory
cp -r living-readme ~/.claude/skills/living-readme

# or keep it in the repository and reference it from the project's agent file
cp -r living-readme ./tools/living-readme
```

Nothing else to install: the scripts use only the Python 3 standard library.
Run an agent and mention one of the trigger phrases — *write a README*, *update
the README*, *the README is stale*, *make this repo professional*, *document this
project* — or point the agent straight at `SKILL.md`.

## Use it: Mode A — create

```bash
python3 living-readme/scripts/collect_facts.py --repo . -o facts.json
```

Then ask the agent to draft the README from `facts.json` using
`references/readme-template.md`, answer `references/owner-questions.md` for the
things only you know (purpose, credits, status, what must stay private), and let
it run `references/verify-checklist.md` before showing you anything. Nothing is
committed or pushed without your approval.

The created README starts with a marker the agent will use later:

```markdown
<!-- living-readme: last-sync <commit-sha> <YYYY-MM-DD> -->
```

## Use it: Mode B — update

```bash
python3 living-readme/scripts/detect_changes.py --since-marker README.md
```

The script reads the marker, diffs everything since that commit, and sorts the
changes into README-relevant categories (new/removed modules or routes,
dependencies/stack, setup commands, env/config, CI and quality gates, docs
added, very large diffs) versus noise (typos, tests only, lockfiles,
formatting, assets).

- **Nothing relevant changed** → the honest answer is "README still accurate",
  and the agent stops. Only the marker date is bumped, if anything.
- **Something relevant changed** → the agent edits only the affected sections
  plus the auto-generated block between `<!-- living-readme:facts:start -->` and
  `<!-- living-readme:facts:end -->`, then bumps the marker:

  ```bash
  python3 living-readme/scripts/detect_changes.py --since-marker README.md \
    --write-marker README.md --quiet
  ```

Exit codes: `0` report produced (relevant or not), `1` relevant changes and you
asked for `--fail-on-relevant=true`, `2` the repository or arguments could not
be read. `--json` prints the full report for scripting.

Want a nudge instead of a habit? `references/automation.md` has a GitHub Actions
workflow and a git `pre-push` hook that warn when the README drifts. Both only
warn — neither edits prose on its own.

## What's in the folder

| File | Purpose |
|---|---|
| `SKILL.md` | The instructions the agent follows: principles, Mode A, Mode B, delegation, safety |
| `references/readme-template.md` | Section-by-section skeleton, with what is optional per project type |
| `references/owner-questions.md` | Ten short questions to ask the owner; never invent answers |
| `references/verify-checklist.md` | The pre-publication gate: numbers, commands, links, honesty, secrets |
| `references/automation.md` | Sample CI workflow and pre-push hook, explained in plain English |
| `scripts/collect_facts.py` | Gathers checkable facts (git, languages, stack, CI, tests, docs, media) as JSON |
| `scripts/detect_changes.py` | Classifies changes since the last sync into relevant vs noise |

## Testing it on any repository

No configuration, no state, safe to run anywhere read-only:

```bash
# 1. Facts about a repo (works even without git: degrades to a file walk)
python3 living-readme/scripts/collect_facts.py --repo /path/to/repo | head -40

# 2. What changed since a commit (use any real SHA)
python3 living-readme/scripts/detect_changes.py --repo /path/to/repo --since HEAD~5

# 3. The full loop: sync a marker, then re-check
python3 living-readme/scripts/detect_changes.py --repo /path/to/repo \
  --since-marker README.md --write-marker README.md
python3 living-readme/scripts/detect_changes.py --repo /path/to/repo --since-marker README.md
#    -> "README still accurate - nothing README-relevant changed."
```

Outside a git repository both scripts exit `0` with an `errors` list explaining
what was unavailable, so they are safe in CI and in sandboxes without git.

## License

Use it, fork it, adapt the rules at the top of `detect_changes.py` to your
project's conventions. Keep the honesty rules: they are the point.
