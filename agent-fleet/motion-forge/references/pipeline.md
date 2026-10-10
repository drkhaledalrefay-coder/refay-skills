# Pipeline — phases, briefs, gates

Every brief: `<task>` · `<context>` (files to read) · `<director_decisions>` · `<steps>` ·
`<outputs>` (the ONLY files it may write) · `<gates>` (numbers) · `<report>` (final message only).
Tell it: do not commit, do not touch source clips, write only inside the work folder.

## 0. Intake (before any dispatch)
Ask/record: work folder, deadline, duration cap, delivery specs (size, fps, aspect), source folders,
paid/free tool boundaries, language, script owner, approval owner. Default what the director skips
and write the defaults into PLAN.md.

## 1. Story lock → PLAN.md
Beats with seconds, total under the cap with headroom, worlds (cinematic / app / infographic),
match-cuts between worlds, what text is on screen (code-rendered), VO lines draft, ownership.
Ask the director only what changes the plan (≤4 questions, recommended option first). Write the
director's answers into PLAN.md "Decisions" with the date.
The story idea governs every edit choice — write it in one sentence at the top of every later brief
(e.g. "the past scholar alone → the young man alone → they meet and shake hands at the very end").

## 2. Plates
Reuse existing plates first. New plates: free built-in image gen only (e.g. Codex), same style refs
in the folder, max 3 attempts per plate, no-text fallback. Gate: the fleet crops any readable text and
reads it letter by letter against the exact string; INDEX.md one line per plate.
Before sending prompts, the conductor or a reviewer checks each prompt against its plate (light side,
what is already on the page) and fixes mismatches.

## 3. Video prompts (Flow/Veo/Seedance) — CINEFLOW format
Per shot: REFERENCES (first frame file, last frame optional, consistency ref) · clip length ·
**edit uses 0:0a–0:0b → timeline t1–t2** · SCENE CONTEXT · FIRST FRAME · CHARACTER/ENVIRONMENT LOCK ·
CAMERA (FOV° 107/84/63/47/29/18/8) · ACTION TIMING per second · PERFORMANCE · PHYSICS · LIGHTING
(source + direction) · SOUND (ends "No music.") · NEGATIVE CONSTRAINTS (shot-specific).
Paste every block inline in chat — directors often cannot reach repo paths.
Ask for 2–3 takes per shot named `shotN_takeK.mp4`; accept any folder layout they actually use.

## 4. Take intake + QA (fleet; vision-capable preferred, ffmpeg fallback required)
No vision-capable agent → generate the contact sheets anyway and ask the director to pick takes;
continue with ffprobe/audio/text gates only.
Steps: ffprobe all → 1 fps contact sheet per clip → map each clip to a shot by matching plates →
score: heading/text exactness, hands/faces/eyes, flicker/morph, continuity, emergent pseudo-text,
audio present → suggested in/out → one pick per shot or REGENERATE + reason.
Outputs: TAKES.md, MANIFEST.json, qa_takes/. Gates: row count = clip count, sheets exist, JSON parses.
Report to the director: coverage table + fails in plain words. Then: "use what's available" is a
valid director call — cover weak beats from other takes instead of regenerating.

## 5. Describe + EDL + silent draft
TAKES-DESCRIBED.md (2–4 lines per clip, usable spans, which beat it can serve) → EDL.md (row | timeline
in–out | source span | beat | transition | reason, sums exactly) → draft_vN.mp4.
Defaults: 1920×1080, 30 fps CFR, H.264 yuv420p, 0.3 s dissolves inside a world, matched grade +
uniform grain, no audio stream, no letterbox. qa contact sheet: first + middle frame of every row.
Gates: ffprobe line, EDL sum, last-N-seconds freeze = frame diff ≈ 0, text crops exact, eyes check
frames listed.

## 6. Independent review (other vendor, read-only)
Checklist table Check | PASS/FAIL | evidence: faces/eyes · exact text · pseudo-text duration ·
screens look natural + real RTL text · continuity/drift (extra people!) · anachronisms (electric
lights, pencils, logos) · story order. Max 3 fixes, most important first. Apply fixes as a delta brief.

## 7. Revisions
Delta brief = only the changes + "everything else identical to vN". Keep all versions. If a revision
is already running and a new note arrives, stop it and restart with the combined brief (cheaper than
two passes on the same files). Re-verify the specific notes with a frame scan (e.g. "handshake frames
exist only at 110–114 s").

## 9–10. Motion body + final assembly
Motion section: reuse an existing render (HTML animatic / scenes) — map paragraph → picture span with
whisper on its original narration, then fit each span to the new narration (hold last frame or slow
≤10 %, trim idle tails; never cut mid text-reveal). Drop all foreign audio.
Timeline: opening → dissolve from the bridge frame → body → closing shot under the last line → hold →
fade to black. HARD cap (e.g. ≤119.5 s): reduce gaps → trim holds/idle picture → narration atempo (max 1.05×
faster / 0.95× slower) only as a last micro-fit.
Final gates: ffprobe (1 video + 1 audio, duration ≤ cap), I = −16 ±0.5 LUFS, TP ≤ −1 dBTP, SRT cue count
= paragraphs and non-overlapping, whisper on the last 10 s ends with the last words, duplicate-shot scan.
