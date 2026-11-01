---
name: flow-anime-story
description: >
  Production method for a 60-second kids anime short in Google Flow (Omni 1.1 Flash video, Nano Banana images, Reference-to-Video). Use when the user asks for an anime short in Google Flow, a kids story film, a hadith/moral animation, Flow Omni R2V, character sheets then keyframes, or a hand-painted Japanese-style kids short. Covers story lock, paste-ready locks, free stills, R2V prompts, credit split, policy rewrites, browser driving, and the edit.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Flow anime story (kids, 60 seconds)

Make a short moral film in Google Flow by locking the story, then the pictures, then the motion. Images are free. Video spends credits. Approve stills before any video.

The assistant plans and judges. The user generates inside Flow.

Verified on one example film (7 shots, Omni 1.1 Flash, first try on every shot). The example prompts are not part of this method: see `examples/roqa-kids-anime/` in the repo only if you want a reference. Paste blocks: `references/locks.md`. Blank template: `references/shot-prompt.md`.

## No story yet? Suggest one first

If the user has no story, do not stop. Propose three short story options in one table, each with: a moral or hadith line (to verify), one child character, one animal or friend, one place, and a 60-second beat sheet. Ask the user to pick one, or to change one detail. Then write the locks and shots from the chosen story. Never invent a quote or hadith: if the moral is religious, use a line the user supplies or one checked against a reliable source.

## 1. Story lock

Lock these before any image:

1. **Moral or hadith.** Keep the exact wording that will appear on screen. Do not paraphrase it inside Flow, and do not put it on a Flow frame. Confirm the exact line and its source with the user, and check the citation on a reliable hadith database before publish. Flag that check; do not invent a citation.
2. **One sentence.** A child does one clear kind act. Picture tells the story. No narrator. Only the child speaks, and only if the shot needs it.
3. **Kid-safe.** No prophets or Companions on screen. Modest clothing. No music in the Flow shots. A nasheed, if any, is a separate project.
4. **Length.** About 60 seconds. **7 or 8 shots × 8 seconds** inside Flow, then a short end card made outside Flow. 7 × 8s is already longer than 60s, so the edit trims.

Beat sheet used here (picture times from the script; each Flow clip is 8s and gets trimmed):

| Shot | Picture | Speech | Sound |
|---|---|---|---|
| S01 | Hot noon. She walks home and wipes her forehead | none | cicadas, footsteps |
| S02 | She kneels by a mud-brick wall. A tiny kitten pants in the shade | Egyptian Arabic whisper | faint meow |
| S03 | Close on the weak kitten. She is worried | Egyptian Arabic whisper | soft pant |
| S04 | She holds her own bottle. She is thirsty too. She hesitates | Egyptian Arabic whisper | cicadas, a pause |
| S05 | She pours water into the lunchbox lid | Egyptian Arabic whisper | water pour |
| S06 | The kitten drinks. She smiles and strokes it | Egyptian Arabic | lapping, happy meow |
| S07 | Softer light. She walks home. The kitten follows | none | breeze, footsteps |
| S08 | Hadith end card. **Not Flow** | none | silence or soft ambient |

Lines are optional. Arabic from the video model is a risk (pronunciation, lip-sync). This project tested it and Whisper later confirmed the five spoken lines; S04 had low Whisper confidence, so check that line by ear. If a new film's first speaking shot is weak, generate the rest silent and record the line in the edit.

## 2. Locks

Copy a lock into every prompt that needs it. Full text is in `references/locks.md`.

**CHARACTER LOCK (per character).** Age as a short wholesome phrase that already passed ("a 7-year-old Egyptian girl", "a cheerful little schoolgirl, about 6 years old"). Hair, outfit, palette, silhouette. Reuse the same face, braids, clothes, and bag in every shot. **No body descriptions of children** (no proportions, no missing teeth, no body-part inventory). Clothes and hair carry identity.

**KITTEN / ANIMAL LOCK.** Species, coat, markings, eyes, size, and the mood of this shot (thin and tired, or lively with the tail up). If a still looks angry, say the face is sad and weak in the video prompt.

**STYLE LOCK (the phrase that worked).** Premium hand-painted Japanese animated feature-film aesthetic. Widescreen 16:9. Daylight, warm sun, painted backgrounds. The earlier lock ("2D hand-drawn anime, soft cel shading…") was rejected as a flat Western kids'-book look. Do not go back to it.

**LOCATION LOCK.** One village, reused: dusty stone path, low mud-brick wall, palms, green fields, distant mountains. State time of day per shot (harsh noon, or softer late afternoon).

**AUDIO LOCK.** Dialect if she speaks: sweet, natural Egyptian Arabic, one short line. Ambience named (cicadas, pour, lap, breeze, footsteps, meow). End every shot with: no music, no text, no subtitles.

**CAMERA LANGUAGE (per shot).** Shot size, angle, move, and how fast or how gentle. One move. Examples that shipped: eye-level medium, camera lowers to the kitten; close warm push-in on the water; gentle drift; camera rises and widens. In R2V the keyframe guides composition and is not a guaranteed first frame (S02 was asked as a kneel and arrived closer).

## 3. Sheets first (images are free)

Order:

1. Character sheet (front, and the expression you will keep). Generate 2. Pick one. On this film, v1 (tidy closed smile) was the lock; v2 was a big grin. Name them so you can tell them apart in the @ picker.
2. Animal sheet: thirsty close-up and drinking close-up.
3. Location still (the wall / path). The S02 keyframe doubled as the location reference.
4. Then **1–2 keyframes per shot**, in the same chat, telling the model to use the **first** sheet of each character as the exact reference (same face, braids, yellow T-shirt, denim overalls, satchel; same kitten).

S05–S07 keyframes were one message that asked for three images, each with @ tags for the girl, the kitten, and the location.

Style phrase plus sheets in the **same Flow chat** held consistency without a separate upload step. A new account does need the files: upload the chosen sheets (and the location still). A fresh sheet is a different girl. Do not redraw her on the second account if you can upload the winner.

## 4. Video

Model used: **Omni 1.1 Flash**. Each clip is **exactly 8 seconds**, continuous, 16:9.

**First-frame mode takes one image.** The character sheet cannot ride along, and the face can drift. S01 was made this way. Use it only when you accept that limit.

**Reference-to-Video (R2V)** is the method for every later shot. Type `@`, pick each asset, and assign roles in the prompt:

- `@` character sheet is the girl
- `@` kitten sheet is the kitten
- `@` keyframe is the scene and composition

Rule from the session: **every shot = @character sheet + @keyframe** (plus the animal sheet when the animal is in frame).

Prompt shape (template in `templates/shot-prompt.md`):

```
Use Reference-to-Video. @… is the girl. @… is the kitten. @… is the scene and composition.
SCENE 0X — TITLE. An exactly 8-second continuous animated shot. [STYLE LOCK]
[Who is where]. [One action across the 8 seconds]. [Optional line].
The camera [size, angle, move].
Audio: [ambience]. No music. No text or subtitles.
```

Action timeline inside those 8 seconds: one action, then a small change (head lifts, pour finishes, look back). Do not stack a second scene.

Ingredients that worked: girl sheet + kitten sheet + the shot keyframe.

## 5. Credits

From this production, not from a general price list:

| Item | Cost |
|---|---|
| Nano Banana images (sheets, keyframes) | 0 credits |
| Omni 1.1 Flash, 8 seconds, R2V or first-frame | 12 credits each |
| 7 shots | 84 credits |

Each Google account gets free daily credits in Flow (50 per day at the time of this project). One 8 s video costs 12 credits, so one account makes about 4 clips a day. Read the balance on the account you are in, and split the remaining shots across accounts.

Before spending on a second account: upload the **same** winning sheets, rebuild free keyframes there with @ tags, then R2V. Check the balance before a 3-clip batch (36 credits).

## 6. Policy pitfalls and rewrites

Documented block: a prompt that described the child's **body proportions** or a **missing tooth** was rejected. Rewrite to clothes, hair, face as "cute round face" / "wholesome", age in years, and the action. The short wholesome prompt (braids, bows, pink polo) passed the filter and still looked flat until the style phrase and the overalls design replaced it.

Keep child wording on hair, outfit, palette, and silhouette.

These session notes do not record a "prominent people" block or a refund. Do not invent a refund click-path. If a real person's name is pulled into a prompt, the notes' own naming rule is to call the on-camera adult role **"the host"** (or "her mother" for the story) and not a public name. The hadith end card stays outside Flow, so source names are typed in the edit, not generated as a face.

## 7. Browser driving

What actually failed and the fix:

- Wait until Flow finishes its reply before Send. Sending during a reply hits Stop and shows "Response was cancelled".
- After **Add to prompt** in the @ picker, focus leaves the box and typed text disappears. Click at the end of the box and press Ctrl+End, then type.
- A stray attached video turns the request into a paid edit. Confirm nothing extra is attached.
- An uploaded sheet can appear **twice**. Open the preview: v1 = closed smile, v2 = big grin. Pick v1 if that is the lock.
- The page sometimes jumped into a clip's edit view. Do not type there (edits cost credits). Go back to the project.

## 8. Edit

- Three Flow shots had **black letterbox bars**. Fix the bars in the edit. Do not rerun the shot for that.
- Arabic captions for her lines are optional.
- **S08 hadith end card is not a Flow generation.** Build it in the edit (HTML or calligraphy render): exact hadith plus the source line after the sunnah.com check.
- Assembly target is about 60 seconds: trim the 8s clips, add SFX, no music unless a separate nasheed project is finished.
- Review: face, outfit, kitten colors, extra fingers, stray text. This film had **0 retakes**.

## 9. Worked example

For a new film, write the shots from this skill's locks and the shot template. The example film's prompts are in `examples/roqa-kids-anime/worked-shots-flow.md` for reference only; do not copy its characters into a new film.

## 10. Checklist

- [ ] Hadith wording marked "verify on sunnah.com" until the creator confirms the on-screen line
- [ ] 7–8 beats, one action each, kid-safe, no narrator
- [ ] Style lock is the hand-painted feature-film sentence
- [ ] Character lock has age, hair, outfit, silhouette, and no child body description
- [ ] Animal lock and location lock pasted
- [ ] Audio line ends with no music, no text, no subtitles
- [ ] Sheets approved (one girl, one kitten, one location) before keyframes
- [ ] Keyframes approved before video
- [ ] Video is R2V with @sheet + @keyframe, unless you accept first-frame's single image
- [ ] Prompt says exactly 8 seconds, one camera move, one dialogue line or none
- [ ] Balance covers 12 credits × remaining shots; otherwise switch account and upload the same sheets
- [ ] @ picker preview matches v1; no stray video attached; reply finished before Send
- [ ] Bars, captions, and the hadith card are edit tasks, not Flow tasks
