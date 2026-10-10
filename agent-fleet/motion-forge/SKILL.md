---
name: motion-forge
description: >-
  Produce a professional explainer / motion-graphics / hybrid cinematic video (≤ a few minutes) by
  conducting whatever agent fleet is installed — 1 agent or 10 — at zero paid-generation cost. The
  conductor plans, writes briefs and judges; the fleet builds and verifies; the human generates paid
  media (video clips, voice). Covers story lock, first-frame plates, per-second video prompts, take
  intake and QA, EDL and silent cuts, independent review, voice-over prompt and placement, motion
  body fitted to narration, final mix and delivery. Use when the user says "make a motion graphic /
  explainer / cinematic video", "use the fleet to edit this video", "motion-forge", or drops
  generated clips and wants them cut into a finished video. DO NOT USE for a single short animation
  you can render directly (use motion-graphics / hyperframes) or for one prompt only (use
  cineflow-prompt).
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Motion Forge — fleet-built professional video, for free

Proven on a ~2-minute hybrid film (cinematic opening → app motion graphics → cinematic close),
built end-to-end by a fleet of free/included agents while the conductor only planned and judged.

## The three roles (never blur them)

| Role | Who | Does | Never does |
|---|---|---|---|
| **Director** | the human | story calls, generates paid media (Flow/Veo/Higgsfield clips, ElevenLabs voice), approves | — |
| **Conductor** | you | discovers the fleet, writes briefs, dispatches, reads report tails, decides, talks to the director | renders, edits files by hand, watches videos frame by frame, reads big logs |
| **Fleet** | any installed agents | builds (ffmpeg, HTML/JS motion, image gen if free/included), self-verifies with gates, cross-reviews | spends paid credits, commits, publishes, generates video/voice on paid platforms |

Token rule: the conductor's cost should be briefs + report tails only. Verification is numbers
(ffprobe, loudnorm, whisper, frame-diff) produced by the fleet, not your eyes.

## Step 0 — Discover the fleet (every session)

Read [references/fleet.md](references/fleet.md). In one shell call, probe which CLIs exist
(`codex grok cursor-agent cline agy claude opencode …`) and which `*-delegate` relay skills are
installed. Build a roster: **builder(s)**, **reviewer (different vendor from the builder)**,
**fallback chain**. Works with any count:
- 1 agent → it builds; you run its read-only mode (or a second session) as reviewer.
- 2–3 → builder + reviewer + fallback.
- 4+ → parallelize by file ownership (one owner per output file), add a cheap cross-checker.
- No `*-delegate` relay skills → run the strongest available agent CLI directly (non-interactive
  mode, same brief, cwd, timeout, output folder, read-only flag for reviews).
- No agent CLI at all → tell the director Motion Forge cannot fleet-run; offer a single-conductor plan.
Known limits seen in practice: Codex credits run out mid-day (switch automatically); AGY headless
needs a permission flag (ask the director once); Cline free models hit daily caps.

## The pipeline (each phase = one brief → one dispatch → gates → report)

| # | Phase | Output | Director needed? |
|---|---|---|---|
| 1 | Story lock | `PLAN.md`: beats, total ≤ cap, hard rules, ownership | approves |
| 2 | Plates (first frames) | `plates/p01…pNN.png` + `INDEX.md` | only if new art; reuse existing plates first |
| 3 | Video prompts | `FLOW-PROMPTS.md` (CINEFLOW blocks) — **paste them inline in chat too** | generates clips |
| 4 | Intake + take QA | `TAKES.md`, `MANIFEST.json`, `qa_takes/*.jpg` | — |
| 5 | Describe + EDL + silent cut | `TAKES-DESCRIBED.md`, `EDL.md`, `draft_vN.mp4` | watches, gives notes |
| 6 | Independent review | PASS/FAIL table (other vendor, read-only) | — |
| 7 | Revisions | delta briefs → `draft_vN+1.mp4` (never overwrite older versions) | notes |
| 8 | Voice-over prompt | `VO-PROMPT.md` — AFTER picture lock, paste inline | records voice |
| 9 | VO split + placement | `audio/segments/*.wav`, `SEGMENTS.md` | — |
| 10 | Motion body + assembly | `final.mp4`, `final.srt`, `EDL_FULL.md` — stop after director approval or an explicit revision request | final approval |

Before phase 1, run the **intake** in pipeline.md (work folder, deadline, cap, specs, sources,
paid/free boundaries, language, script owner, approver). Do not dispatch until known or defaulted.

Phase details, brief templates and gates: [references/pipeline.md](references/pipeline.md).
Voice specifics: [references/voice.md](references/voice.md).
Failure lessons (read before phase 3 and before every revision): [references/lessons.md](references/lessons.md).

## Conductor loop (per phase)

1. Write a brief file (scratchpad): task, inputs, director decisions, steps, outputs (files it may
   write — nothing else), **gates with numbers**, report contract ("final message only: …").
2. Dispatch with the selected relay (check its `--help` once; flags differ), in the background
   (e.g. Claude Code `run_in_background`), timeout 30–45m; record the exact command in the phase log. Queue dependent jobs with
   `until [ -f prev/result.json ]; do sleep 20; done; <next dispatch>` so nothing waits on you.
3. On notification read only the report tail. Judge by disk (file exists, mtime, size), not status.
4. Important outputs → second agent, other vendor, read-only review → PASS/FAIL table.
5. Send the file to the director (`SendUserFile`, render) + open it in the system player. Short
   message: what changed, what was verified and by whom, weak spots, one decision you need.

## Speed & survival

- Deadline mode: put `HARD DEADLINE: N min — prefer holds/trims over perfect retiming` in the brief;
  start independent parts in parallel (e.g. motion body while the opening VO finishes) and have the
  later agent poll for the earlier file with a fallback after X minutes.
- Auto-fallback: wrap the dispatch — if `result.json` status ≠ completed or the output is missing,
  re-dispatch the same brief to the next agent in the chain.
- Notify even if you die: launch the detached watcher in [scripts/watch.ps1](scripts/watch.ps1) (opens
  the final file and shows a message when it is stable on disk). Tell the director it only means
  "file written", not "reviewed".

## Hard rules (defaults — the director can override per project)

- No music unless asked. Light natural SFX only, ≥18 dB under voice; strip all generated audio (`-an`).
- Never AI-generate sacred/quoted text (e.g. Qur'an) — type it in code with a proper font.
- Readable text inside generated images only if exact; verify letter by letter (fleet crops + reads).
- No identifiable faces unless the director allows; check eyes in sampled frames, crop or trim.
- Real UI on screens = real screenshots corner-pinned, never generated letters.
- Never publish, push, upload, or email without the director's explicit yes.
- One owner per video/session; never edit another session's files — copy read-only.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
