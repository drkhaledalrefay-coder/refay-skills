---
name: seedance-anime-story
description: >
  Production method for a 60-second kids anime short on Higgsfield Seedance 2.0 or Seedance 2.0 Mini, with Seedream stills. Use when the user asks for a Seedance kids story, a hadith/moral animation on Higgsfield, Seedream sheets then Seedance blocks, @image references with a start image, or a side-by-side with Google Flow. Confirms model, tier, and cost before any generation.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Seedance anime story (kids, 60 seconds)

Same film pipeline as Flow: lock the story, make free stills, then animate. The prompt format is Seedance's, not Flow's @ picker paragraph.

Images: **Seedream** (free on the plan used in the notes; the comparison names Seedream 4.5).
Video: **Seedance 2.0** or **Seedance 2.0 Mini** on Higgsfield.

**Always confirm model, tier, and cost with the user before generating.** The only measured price in these notes is Mini.

Full block rules: `references/prompt-blocks.md`. The example film's seven prompts (reference only): `examples/roqa-kids-anime/worked-shots-seedance.md`.

## No story yet? Suggest one first

If the user has no story, do not stop. Propose three short story options in one table, each with: a moral or hadith line (to verify), one child character, one animal or friend, one place, and a 60-second beat sheet. Ask the user to pick one, or to change one detail. Then write the Seedream sheets, the keyframes and the Seedance blocks from the chosen story. Never invent a quote or hadith: if the moral is religious, use a line the user supplies or one checked against a reliable source.

## Story lock

Same story as the Flow film so the comparison stays fair: same beats, same intention, same style sentence.

- Hadith for the edit card only (not inside the generator): «في كل ذات كبد رطبة أجر». Check the exact on-screen wording and source on sunnah.com before publish. The notes attribute it to al-Bukhari and Muslim and say not to publish unverified wording.
- 7 shots × 8 seconds, 16:9, one continuous shot each. The camera does not cut on its own.
- Kid-safe. No child body description. Hair, outfit, satchel, bottle.
- No music.

## Speech limit (measured)

Seedance prompts are **English**. This Mini batch asked for Egyptian Arabic lines. **Arabic speech did not come out.** Flow is the path that produced Arabic (Whisper confirmed Flow's five lines).

For a new Seedance shot pick one:

- **No speech** (ambience only), and record Arabic in the edit, or
- An **English** line, if English is acceptable for that film.

Do not promise Arabic lip-sync from Seedance. The worked example keeps the Arabic lines that were actually submitted, and those lines are the dialogue gap, not a method to copy for Arabic.

## Pipeline

1. Seedream character sheet, then animal sheet, plain warm cream background, no text.
2. Seedream keyframes. Attach the girl sheet, and the kitten sheet when the kitten is in frame. Add the common location suffix.
3. Seedance: `start_image` = that shot's keyframe. `image_references`: `@image1` = girl sheet, `@image2` = kitten sheet only if the kitten is in frame. Never tag a reference that is not in the shot.
4. Settings used for the comparison: 16:9, 720p, 8 s, native audio on, model `seedance_2_0_mini`.
5. If Higgsfield suggests a preset (this run suggested "IN THE DARK"), decline it and submit the written prompt.
6. Each prompt is a sealed shot. No "as above", no previous scene number the model must remember, no unused character.

The user generates Seedream stills. Confirm cost, then generate video.

## Prompt blocks

Write only the blocks the shot needs, in this order. Style is not a prefix. The prompt opens on SCENE CONTEXT. The look sentence sits in STYLE, near the end. Full rules and the FOV table are in `references/prompt-blocks.md`.

```
SCENE CONTEXT
ACTIVE REFERENCES
LOCATION MAP
FIRST FRAME / BLOCKING
FORMAT MODE
OPTICS
CAMERA
ACTION
PERFORMANCE          (when acting matters)
PHYSICS              (when liquid or contact matters)
LIGHTING
AUDIO
STYLE
POSITIVE LOCKS
```

Rules that this film actually followed:

- `@image1` / `@image2` by load order, plus a short identity line and "100% matches the reference."
- Keep the identity line short so it does not fight the reference image.
- Shot size plus **FOV in degrees** from the anchor steps (47°, 29°, 63° on this film). Not millimetres.
- Camera speed in **km/h** (1 km/h push, 2 km/h dolly or crane). Subject walk speeds were 2 km/h and 3 km/h.
- White balance in kelvin when light is specified (5600K noon, 5200K, 4500K shade bounce, 3800K late afternoon).
- Left and right are from the camera.
- Emotion as muscle: brows lift, she swallows, dry lips, smile at the corners. Not the word "sad" alone.
- Positive locks: same girl, same outfit, prop stays in the named hand, water goes into the lid.
- FORMAT MODE on every shot: one continuous shot, the camera does not cut on its own.

## Camera language used on the seven shots

| Shot | Optics | Camera |
|---|---|---|
| V1 hot noon | WS at 47° | Eye-level, slow dolly-in at 2 km/h |
| V2 the kitten | MS at 47°, easing to MCU at 29° | Eye-level push-in at 1 km/h, then lowers to the kitten |
| V3 so thirsty | CU at 29° | Ground level, tilt-up at 1 km/h to her face |
| V4 the choice | MCU at 29° | Eye-level push-in at 1 km/h |
| V5 sharing | MS at 47°, slight push toward the lid | Low eye-level, push-in at 1 km/h |
| V6 she drinks | MS at 47° | Ground-level drift left to right at 1 km/h |
| V7 walking home | WS at 47°, opening to EWS at 63° | Crane-up and pull-back at 2 km/h |

## Credits (from the notes)

Confirm again on the account before you spend. Prices below are what this comparison measured, not a rate card for every tier.

| Item | Measured cost |
|---|---|
| Seedream sheets and keyframes | Free on the plan used |
| Seedance 2.0 Mini, 8 s, 720p, 16:9, audio on | **8 credits** each |
| 7 Mini shots | **56 credits** |
| Seedance 2.0 (full, not Mini) | **Not priced in these notes.** Ask before generating |

Flow, for the same 7 shots, was 12 credits each (84 total) at 1080p, 24 fps. Mini here was 720p. The notes' verdict: Flow carried Arabic dialogue; Mini was brighter, cleaner, more TV-anime, with smoother motion and stronger consistency (start image + two references). Best combined result in the notes: Seedance picture + Arabic voice added in the edit. Visual retakes on this Mini batch: 0. No visual failures were logged. The gap is speech.

## Child wording

Same boundary as Flow. The sheet prompt used in the example film: cute 7-year-old Egyptian girl, round face, big warm brown eyes, two braids with small red hair ties, yellow T-shirt, blue denim overalls, brown leather crossbody satchel, white sneakers. No body proportions.

## Edit

Letterbox bars were a Flow problem (3 shots), not logged on Mini. Captions optional. Hadith end card is built outside the generator. If Mini is the picture, lay the Arabic lines in the edit.

## Checklist

- [ ] User confirmed model (2.0 or 2.0 Mini), tier, 8 s, 16:9, resolution, audio on/off, and credit cost
- [ ] Speech plan is no speech, or English — not an Arabic promise
- [ ] Seedream sheet and keyframe exist; start_image is this shot's frame
- [ ] @image tags only for subjects in frame, each with "100% matches the reference"
- [ ] Blocks in order, prompt opens on SCENE CONTEXT, STYLE near the end
- [ ] FOV in degrees from the anchor table, speeds in km/h, light in kelvin
- [ ] One continuous shot, positive locks on identity and props
- [ ] Preset suggestion declined if it changes the look
- [ ] Hadith card and any Arabic voice planned for the edit
