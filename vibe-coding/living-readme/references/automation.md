# Automation: warn when the README drifts

Both examples below only **warn**. Neither one edits the README, commits
anything, or fails a build by default. The reason is simple: a machine that
rewrites prose on its own is how a README starts lying, and the whole point of
this skill is that a README never lies. A human or an agent reads the warning
and runs Mode B.

---

## 1. GitHub Actions workflow

Save as `.github/workflows/readme-drift.yml`.

```yaml
name: README drift check

on:
  pull_request:
  push:
    branches: [main, master]

permissions:
  contents: read
  pull-requests: write   # only needed for the optional PR comment below

jobs:
  readme-drift:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout (full history so the last-sync SHA is reachable)
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Detect README-relevant changes since the last sync
        id: drift
        run: |
          python living-readme/scripts/detect_changes.py \
            --since-marker README.md \
            --fail-on-relevant=false \
            --json > /tmp/readme-drift.json
          python living-readme/scripts/detect_changes.py \
            --since-marker README.md \
            --fail-on-relevant=false \
            --quiet > /tmp/readme-drift.txt
          {
            echo "### README drift check"
            echo ""
            echo '```'
            cat /tmp/readme-drift.txt
            echo '```'
          } >> "$GITHUB_STEP_SUMMARY"
          cat /tmp/readme-drift.txt

      - name: Warn when relevant changes exist
        if: always()
        run: |
          python - <<'PY'
          import json, os, pathlib
          path = pathlib.Path("/tmp/readme-drift.json")
          if not path.exists():
              print("::warning::README drift check produced no JSON report")
              raise SystemExit(0)
          report = json.loads(path.read_text())
          if report.get("relevant_count"):
              cats = ", ".join(b["category"] for b in report["relevant"])
              print(f"::warning title=README may be stale::"
                    f"{report['relevant_count']} README-relevant change category(ies) since "
                    f"{(report.get('since') or {}).get('sha')}: {cats}. Run living-readme Mode B.")
          else:
              print("::notice::README still accurate - nothing README-relevant changed.")
          PY

      # Optional: say it on the pull request itself.
      # - name: Comment on the PR
      #   if: github.event_name == 'pull_request'
      #   env:
      #     GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      #   run: |
      #     gh pr comment "${{ github.event.number }}" \
      #       --body-file /tmp/readme-drift.txt

      # Optional: make it blocking once the team trusts it.
      # - name: Fail when the README is stale
      #   run: |
      #     python living-readme/scripts/detect_changes.py \
      #       --since-marker README.md --fail-on-relevant=true --quiet
```

**What it does, in plain English.** On every pull request and on every push to
the main branch, a fresh machine clones the repository *with its full history*
(needed because the check compares against an older commit). It runs
`detect_changes.py` in marker mode: the script reads the `last-sync` SHA out of
`README.md`, looks at everything changed since that commit, and sorts the
changes into "a README reader would care" (new routes, dependency bumps, changed
setup commands, CI changes, new docs) versus "nobody outside the diff cares"
(typos, tests, lockfiles, formatting). The result lands in the run's summary page
and, when something relevant changed, as a yellow warning annotation on the
commit or pull request. `--fail-on-relevant=false` keeps the job green, so the
warning informs instead of blocking. When the team trusts the check, flip that to
`--fail-on-relevant=true` and the job turns red until someone re-syncs the README.

Two notes: `fetch-depth: 0` matters — a shallow clone cannot resolve the marker's
old SHA, and the script will say so instead of guessing. And the workflow assumes
the skill lives at `living-readme/` in the repository; if it lives elsewhere
(installed globally, or `tools/living-readme/`), change the two script paths.

---

## 2. Git `pre-push` hook

Save as `.git/hooks/pre-push` and make it executable
(`chmod +x .git/hooks/pre-push` on Linux/macOS; on Windows, Git for Windows runs
it through its bundled shell).

```sh
#!/bin/sh
# living-readme: warn (never block) when the README is behind the code.
# Install: cp this file to .git/hooks/pre-push && chmod +x .git/hooks/pre-push
# Bypass once:  git push --no-verify

set -u

README="README.md"
SCRIPT="living-readme/scripts/detect_changes.py"

[ -f "$README" ] || exit 0
[ -f "$SCRIPT" ] || { echo "living-readme: $SCRIPT not found, skipping drift check"; exit 0; }

PY=$(command -v python3 || command -v python)
[ -n "${PY:-}" ] || { echo "living-readme: python not found, skipping drift check"; exit 0; }

echo "living-readme: checking whether $README is still accurate..."
"$PY" "$SCRIPT" --since-marker "$README" --fail-on-relevant=false || true

exit 0   # always allow the push; the warning is the point
```

**What it does, in plain English.** Right before Git sends your commits to the
remote, this small script runs the same drift check locally and prints the same
report to your terminal — so you see "3 README-relevant changes: new
UserController, express bumped, CI triggers changed" *before* anyone reviews the
branch. It exits `0` no matter what, so it can never block a push; `git push
--no-verify` skips it entirely. Note that Git does not version or copy hooks: each
clone has its own `.git/hooks/` directory, so to share this with the team either
commit the hook somewhere in the repo (for example `living-readme/hooks/pre-push`)
and tell people to copy it, or set a shared hooks directory once:

```sh
git config core.hooksPath living-readme/hooks   # then commit living-readme/hooks/pre-push
```

---

## Which one should you use?

| | CI workflow | pre-push hook |
|---|---|---|
| Sees everyone's changes | Yes | Only yours, on your machine |
| Needs Python on the runner | Yes (`setup-python`) | Yes, locally |
| Can block by accident | No (default) | No |
| Best for | Teams, shared repos, PR review | Solo repos, catching it before you push |

Use both if you like: the hook catches it early, CI makes it visible to the team.
In either case the follow-up is the same — run **Mode B UPDATE**, or record
"README still accurate" and move on.
