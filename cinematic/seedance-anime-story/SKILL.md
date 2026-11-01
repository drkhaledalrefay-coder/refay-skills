---
name: seedance-anime-story
description: >
  Production method for a 60-second kids anime short on Higgsfield Seedance 2.0 or Seedance 2.0 Mini, with Seedream stills. Works for any story and any lead character (a girl, a boy, an old man, an animal companion or none). Use when the user asks for a Seedance kids story, a moral or hadith animation on Higgsfield, Seedream sheets then Seedance blocks, @image references with a start image, or a side-by-side with Google Flow. If the user has no story, suggest three and build from the one they pick. Confirms model, tier and cost before any generation.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Seedance anime story (kids, 60 seconds)

Same film pipeline as the Flow skill: lock the story, make free stills, then animate. The prompt format is Seedance's block format, not Flow's @ paragraph.

The assistant plans and writes the prompts. The user confirms the model and spend, and generates in Higgsfield.

## 1. Before any generation: confirm model, tier and cost

Ask and wait for a clear answer:
- Which model: Seedance 2.0 Mini or full 2.0.
- Which resolution and length.
- The cost shown on the Higgsfield page for that choice.

Never switch to a bigger model or a longer clip without a fresh yes. Measured costs on one project, for reference only: Seedance 2.0 Mini, 8 credits per 8 s at 720p; full 2.0, 67.5 credits for a 15 s 720p clip. Prices change, so confirm on the page.

## 2. Story (or suggest one)

If the user has a story, use it. If not, suggest three short options in one table: a moral or hadith line (to verify), one lead character, an optional companion, one place, and a 60-second beat sheet of seven or eight shots. The user picks one. Never invent a quote. A religious line is used only if the user supplies it or it is checked on a reliable source.

## 3. Language limit (important)

Seedance prompts are written in English. In testing, Arabic speech did not come out of Seedance 2.0 Mini. Plan the dialogue for the edit (recorded voice in Arabic, laid over the picture), or keep the shots silent with ambience only.

## 4. Locks

- **CHARACTER LOCK.** Age as a wholesome phrase, hair, outfit, palette, one signature prop. Kid-safe: no body proportions for children.
- **COMPANION LOCK (optional).** Type, colour, markings, eyes, size, mood in this shot.
- **STYLE LOCK.** One sentence placed in the STYLE block, identical in every prompt.
- **LOCATION LOCK.** Place, time of day, light, palette. Put the location as a suffix on every keyframe.
- **AUDIO.** Ambience named. End with: "No music. No text or subtitles."

## 5. Sheets and keyframes (Seedream, free on the plan used)

1. Seedream character sheet for each lead character (front, side, back, close-up), plain warm background, no text. Generate two, pick one.
2. Companion sheet, if there is one.
3. Seedream keyframe per shot. Attach the character sheet, and the companion sheet only when that companion is in frame. Add the location suffix.
4. Approve every sheet before any video.

## 6. Seedance blocks

For each shot, write only the blocks the shot needs, in this order. The prompt opens on SCENE CONTEXT. Style is not a prefix.

1. SCENE CONTEXT: one or two sentences, what happens and where.
2. ACTIVE REFERENCES: `start_image` = that shot's keyframe. `image_references`: `@image1` = character sheet, `@image2` = companion sheet only if it is in frame. Never tag a reference that is not in the shot.
3. LOCATION MAP: foreground, midground, background, where the camera is, where the light comes from.
4. FIRST FRAME / BLOCKING: who is where at the first frame.
5. OPTICS: shot size and FOV in degrees (use the steps 107, 84, 63, 47, 29, 18, 12, 8).
6. CAMERA: one move, motivated, with speed in km/h or % of the frame. Put the CAMERA block third.
7. ACTION: a timeline (0–2 s, 2–5 s, 5–8 s), with the camera motion and the subject motion stated separately.
8. PERFORMANCE: the emotion as muscle movement, not a label ("her shoulders drop, she swallows once").
9. LIGHTING and COLOUR (as material and light, not a list).
10. AUDIO: ambience only, or the edit voice.
11. STYLE and OUTPUT SETTINGS: the STYLE LOCK sentence and the resolution, placed just before the locks.
12. POSITIVE LOCKS: the continuity fixers, in positive form ("same outfit, prop stays in the named hand").

Write everything positively. "Still, not moving" is written as "stays still in frame".

## 7. Shot list (example shape)

Seven shots of 8 s each, one change per shot: setup, problem, a choice, a turn, a resolution, a payoff. Show the shot names and the camera for each in a table before writing blocks.

## 8. Edit

- The end card (moral or hadith with its source) is built in the edit. Verify the exact wording first.
- Letterbox bars are an edit fix, not a prompt fix.
- Captions optional. Loudness about −16 LUFS for a kids film.
- A side-by-side with Flow: same story, same locks, same sheets when possible, so the comparison is fair.

## 9. Checklist

- [ ] Model, tier and cost confirmed by the user
- [ ] Story and moral chosen; any quote verified
- [ ] Locks written; character and companion are kid-safe
- [ ] Sheets and keyframes approved before video
- [ ] start_image is this shot's keyframe; only tagged references are in the shot
- [ ] Prompt has all the blocks it needs, in order, in positive form
- [ ] Arabic dialogue planned for the edit (not spoken by Seedance Mini)
- [ ] End card built outside the generator, wording verified
- [ ] Review: face, outfit, companion, extra limbs, stray text

## Example

A complete example film (seven shots, prompts and locks) is in the repository at `examples/roqa-kids-anime/`. It is one story, shown for reference only.
