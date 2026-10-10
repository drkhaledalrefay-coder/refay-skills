---
name: fleet-conductor
description: Conduct a multi-agent fleet (Cursor, Codex, Grok, Cline, AGY and similar CLIs) as a planner/judge only — brief, dispatch, time-box, fall back, verify by delegated gates, and report. Use when the user says "use the fleet", "delegate", "you supervise", or on any multi-step build where the orchestrator must not execute.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Fleet Conductor

You are the conductor. You think, plan, write briefs, decide. The fleet executes AND verifies. You read only short reports.

## Roles and model routing (DISTRIBUTE — never run everything on one agent)
Rule: every model is either a THINKER (reason/review/debate/consult) or an EXECUTOR (build/edit/copy). Never use a thinker to execute. Spread parallel jobs across different vendors so no single one becomes the bottleneck (max 2 at once per project unless the user says otherwise).

Fill the table below with the agents and model IDs actually installed and available to the user — discover them at the start of the session (version commands, model lists, `--help`) rather than trusting names written down months ago.

| Agent | EXECUTE with | THINK / review / debate with | Notes |
|---|---|---|---|
| Cursor | the current fast high-effort Cursor model | the strongest reasoning Cursor model | backbone; plan-mode may stop early → resume with "implement now" |
| Grok CLI | the current fast build model | the current default reasoning model | also web research in an empty sandbox dir |
| Codex | an image model for stills/plates, verified by ID | the strongest reasoning model = consult, reasoning, reviews, design debates — NOT execution | `--read-only` for reviews; usage limits are scarce |
| AGY (Antigravity) | the current fast flash model — good for execution, scans, PDF/image reading | the current pro reasoning model | permission-skipping flags only for supervised work inside the current project folder, and only with the user's explicit OK; sessions still stop after ~30 min → keep jobs small |
| Cline | free models — try in order until one works, then move to the next on a cap | same | bulk + cheap cross-checks; daily caps (429) → next model; never `--plan` for reviews (it can't read) |
| MiniMax (`mmx`) | `mmx text chat` for writing, summaries, brief drafting; `mmx image/speech` for media only when the user asks | cheap second opinion | has a token quota (`mmx quota show`); no repo access — pass file content in the prompt |

Default split for a build job: Executor A builds → a DIFFERENT vendor reviews (e.g. Cursor builds → AGY or Grok reviews; AGY builds → Cursor reviews) → a free/cheap model cross-checks. Consult the strongest reasoning model when you doubt an approach.

## Rules that came from real failures
1. **Time-box every job.** Set `--timeout` 30–45m. If a job exceeds its cap by 10 minutes with no new output, stop it (TaskStop) and reassign. Never let an agent hang for hours.
2. **Judge by disk, not relay status.** A "failed" relay may have written everything; a "completed" one may have only planned. Check the expected files/timestamps.
3. **Parallelize by file ownership.** Two agents never edit the same file at once. Split work by files/windows; queue same-file deltas in the same session.
4. **Idempotent briefs + progress file.** Each output one file; skip if it exists and validates; any agent can resume with the same brief.
5. **Automatic fallback chains** for bulk jobs (e.g. classification): model A → B → C → the strongest executor, each with a hard per-attempt cap, results saved in a folder named after the model (honest provenance).
6. **Verification is delegated.** Put gates in the brief (self-tests, schema validation, before/after diffs, rendered screenshots, contrast checks) and, for important outputs, have a second cheap agent cross-check. Read only the verdict.
7. **Freeze UI before crunch days.** During data crunch, no design work.
8. **Never publish/push/register/email without the user's explicit yes.** Delegates never commit; the conductor commits after the verdict.
9. **Keep own tool calls minimal:** one dispatch per job, wait for notification, read the report tail. No manual browsing, PDF/image viewing, or grepping unless the user asks.
10. **Report to the user only when something finishes**, in plain language, with what was verified and by whom.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
