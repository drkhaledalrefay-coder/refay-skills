---
name: flow-anime-story
description: >
  Production method for a 60-second kids anime short in Google Flow (Omni 1.1 Flash video, Nano Banana images, Reference-to-Video). Works for any story and any lead character (a girl, a boy, an old man, an animal companion or none). Use when the user asks for an anime short in Google Flow, a kids story film, a moral or hadith animation, Flow Omni R2V, character sheets then keyframes, or credit planning for a Flow film. If the user has no story, suggest three and build from the one they pick.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Flow anime story (kids, 60 seconds)

Make a short moral film in Google Flow by locking the story, then the pictures, then the motion. Images are free in Flow. Video spends credits. Approve stills before any video.

The assistant plans, writes the prompts and checks. The user generates inside Flow.

## 1. Story (or suggest one)

If the user has a story, use it. If not, suggest three short options in one table. Each option has: a moral or hadith line (to verify), one lead character (age, role, look), an optional companion (animal, friend, parent, or none), one place, and a 60-second beat sheet of seven or eight shots. The user picks one or changes a detail. Never invent a quote or a hadith. If the moral is religious, use a line the user supplies or one checked on a reliable source, and flag it as "verify before publish".

Beat sheet rules:
- 7 story shots of 8 s each, plus an optional end card built outside Flow.
- One clear change per shot: a problem, a choice, a turn, a resolution.
- The moral is shown by action, not by a narrator.

## 2. Locks (paste into every prompt that needs them)

Write these once and reuse them word for word.

- **CHARACTER LOCK (per character).** Age as a short wholesome phrase ("a cheerful 7-year-old", "a young boy about 8", "a kind old man with grey hair"). Hair, outfit, palette, silhouette, one signature prop. Kid-safe: no body proportions and no body-part inventory for children. Clothes, hair and props carry identity.
- **COMPANION LOCK (optional).** Species or type, coat or colour, markings, eyes, size, and the mood in this shot (tired, lively, calm).
- **STYLE LOCK.** One phrase used in every prompt, for example "premium hand-painted Japanese animated feature-film aesthetic, widescreen 16:9". Keep it identical across shots.
- **LOCATION LOCK.** The place, the time of day, the light, the palette.
- **AUDIO LOCK.** Dialect if someone speaks (natural spoken Arabic works in Flow), one short line, and the ambience named (wind, water, birds, footsteps). End every shot with: "No music. No text or subtitles."
- **CAMERA LANGUAGE (per shot).** Shot size, angle, one move, and how gentle it is.

## 3. Sheets first (images are free)

1. Character sheet for each lead character: front, side, back, and one close-up. Generate two, pick one, and name them so you can tell them apart in the @ picker.
2. Companion sheet, if there is one: a calm pose and an action pose.
3. Location sheet: the main place in the same light.
4. Then 1–2 keyframes per shot, in the same chat, telling the model to use the first sheet of each character as the exact reference.
5. Approve every sheet before any keyframe. A new sheet is a different character.

## 4. Video: Reference-to-Video (R2V)

**First-frame mode takes one image.** The sheets cannot ride along, and the face can drift. Use it only when you accept that limit.

Use R2V for every shot after the first:
- `@` character sheet is the lead character.
- `@` companion sheet is the companion (only if it is in frame).
- `@` keyframe is the scene and composition.

Rule: every shot = @character sheet + @keyframe, plus the companion sheet when it is in frame.

Shot template (fill the brackets):

```
Use Reference-to-Video. @[character sheet] is [name]. @[companion sheet] is [companion]. @[keyframe] is the scene and composition. SCENE [0X] — [TITLE]. An exactly 8-second continuous animated shot. Widescreen 16:9. [STYLE LOCK]. [Who is where; clothes and hair only for children]. [Action from 0–8 s: start state, one change, end state]. [Optional line: she/he says "..." in natural spoken Arabic.] [Camera: size, angle, one move]. Audio: [ambience]. No music. No text or subtitles.
```

## 5. Credits and accounts

- Images (sheets, keyframes) cost 0 credits in Flow.
- One 8-second video costs 12 credits (measured on one project). A 7-shot film is about 84 credits.
- Each account gets a daily free allowance and a monthly reset. Read the balance on the account you are using; do not assume a number.
- Before a batch, check the balance covers 12 credits times the remaining shots. If not, split the shots across accounts.
- A second account needs the same winning sheets uploaded again. Rebuild the keyframes there, then R2V. Do not redraw the character.

## 6. Policy and wording

- Kids: describe clothes, hair, props and expression. Never body proportions or missing teeth. A prompt with a body description was rejected in testing; rewrite it to clothes and face.
- Real people: do not name a real person in a prompt. Use "the host" with a reference photo, or use the voice avatar for voice only.
- If a prompt is blocked, simplify the wording and resend. Do not chase the same blocked line.

## 7. Browser driving (if the assistant drives Flow)

- Wait for Flow to finish answering before sending the next message. A send during an answer can cancel it.
- After you pick an asset from the @ picker, the focus leaves the box. Click the end of the text box and press Ctrl+End before typing.
- Check the preview of each sheet before using it as a reference. An uploaded sheet can appear twice.

## 8. Edit

- Keep the film in 16:9. Fix any letterbox bars in the edit, not in the prompt.
- The end card (hadith, moral line, source) is built in the edit, not in Flow. Verify the exact wording before publish.
- Captions are optional. If used, one line at a time, same font as the end card.
- Loudness target about −16 LUFS for a kids film with voice and ambience.

## 9. Checklist

- [ ] Story and moral chosen; any quote verified
- [ ] Lead character and companion locks written
- [ ] Sheets approved (one per character, one location)
- [ ] Keyframes approved before video
- [ ] Each video is R2V with @sheet + @keyframe, or first-frame accepted on purpose
- [ ] Balance covers the remaining shots, or accounts are split
- [ ] Prompts pass the kid-safety and naming rules
- [ ] End card built outside Flow, wording verified
- [ ] Review: face, outfit, companion colour, extra fingers, stray text

## Example

A complete example film (seven shots, prompts and locks) is in the repository at `examples/roqa-kids-anime/`. It is one story, shown for reference only. Build your own locks for your own film.
