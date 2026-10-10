# Running the work with an agent fleet

## Detect
```
cursor-agent --version && cursor-agent models      # pick names from the live list
codex --version
agy help                                           # may need full path on Windows
```
Plus Claude subagents (Agent tool) with model overrides (opus / sonnet / haiku).

## Routing
| Job | Preferred | Fallback |
|---|---|---|
| Intake, gates, user comms, verification | You (director) | — |
| Brand/product analysis, personas, scripts, prompts | strongest reasoning agent (Cursor Grok xhigh / Codex high / Opus subagent) | you |
| Deck build + QA, file ops, image selection | implementation agent (Cursor Grok high / Codex / Sonnet subagent) | you |
| Second opinion on personas or claims | different vendor, read-only | skip |
No CLIs → Opus director + Codex (if any) as deputy reviewer + Sonnet subagents as builders. Nothing at all → do it yourself.

Use the user's delegate skills if installed (cursor-delegate, codex-delegate, agy-delegate): brief on stdin, background run, `result.json` report. On Windows dispatch from PowerShell (Git Bash breaks PowerShell-syntax hooks).

## Brief rules
- Agents see only the brief: include paths, the exact output files, what NOT to touch, rules, validation script to write/run, and a short report contract. Tell them not to commit.
- One output file set per agent. Parallel agents get disjoint files; merge later (e.g. `persona_prompts_v3.json` with `replacements[]` merged into `content.json` by the builder).
- Ask for incremental work: write small files immediately, get a first artifact out, then QA. Give long runs a watchdog (e.g. 2 h) and a file-change monitor; if nothing is written for ~30 min, restart with a smaller-step brief.
- Resume the same agent session for fixes (delta brief) so it keeps context.

## Verification (every time)
- Re-run the agent's checks yourself; open outputs; render slides and look.
- For decks: slide count, text/Arabic integrity diff, overlaps, font floors actually used (agents report shrinking to 7–8 pt as "PASS" — that's a fail for readability).
- For prompts: lint for banned words; read 2–3 prompts fully.
- Report to the user in their language: done / running / needs your decision.
