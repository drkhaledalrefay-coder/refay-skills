# Worked example — Ruqayya and the kitten (Flow)

Seven clips exist (S01–S07), Omni 1.1 Flash, 8 seconds, 12 credits each, 0 retakes. S08 is the hadith card in the edit.

Only prompts saved verbatim in the project notes are copied below. Where the log records the line and the inputs but not the full prompt, the gap is marked. Do not fill it with a guessed prompt.

## Sheets

Girl sheet that won: style phrase + braids, yellow T-shirt, denim overalls, satchel. Two versions. **v1 (tidy / closed smile) is the lock.** v2 is a big grin.

Kitten sheet: orange tabby, white paws, thirsty close-up and drinking close-up.

Rejected earlier: hijab and mint dress with the cel-shading phrase; a long child-body prompt (policy block); a short pink-polo school uniform (outfit ok, style still flat).

## S02 keyframe (verbatim, free image)

```
Generate 2 versions. Use the FIRST Ruqayya character sheet and the FIRST kitten sheet as exact character references (same face, braids, yellow T-shirt, denim overalls, satchel; same orange tabby kitten). SCENE 02 keyframe, widescreen 16:9, premium hand-painted Japanese animated feature-film aesthetic. A hot summer noon in a Egyptian countryside village: dusty stone path beside a low mud-brick wall, a few palm trees, green fields and mountains in the distance, fluffy clouds, strong sunlight with soft shade. Ruqayya kneels down in the shade of the wall, concerned, looking at the tiny thin kitten lying tired in the shade with its mouth open. Medium shot, eye level with the girl. No text.
```

Result: character consistent in both versions. This still also became the location reference.

## S01 video

Mode: **first-frame** (image → video), S01 keyframe only. 8 seconds. Generated. The full prompt text was not saved. Lesson: one image only, so the sheet cannot lock the face.

## S02 video (verbatim, R2V)

Inputs: girl sheet, kitten sheet, S02 keyframe.

```
Use Reference-to-Video. @Character design sheet of girl is Ruqayya. @Kitten character design sheet is the kitten. @Girl looking at tired kitten is the scene and composition. SCENE 02 — THE KITTEN. An exactly 8-second continuous animated shot. Widescreen 16:9. Premium hand-painted Japanese animated feature-film aesthetic. Ruqayya kneels in the shade of the mud-brick wall, looking at the tiny thin orange tabby kitten lying tired with its mouth open, panting. The kitten lifts its head weakly and gives a tiny faint meow. Ruqayya's face fills with concern; she leans closer and whispers in sweet, natural Egyptian Arabic: "يا حبيبتي... إنتي عطشانة؟". The camera slowly moves down to eye level with the kitten. Audio: cicadas, faint weak meow, her soft whisper. No music. No text or subtitles.
```

The keyframe was a medium kneel. The clip came out closer. R2V treats the keyframe as composition guidance, not a literal first frame.

## S03 and S04

Keyframes: free images, text telling the model to use the first sheets. The kitten on the S03 still looked a bit like it was hissing. The video prompt corrected the read to sad and weak.

| Shot | Mode | Inputs | Line saved in the log |
|---|---|---|---|
| S03 so thirsty | R2V | girl sheet + kitten sheet + S03 keyframe | مسكينة... مفيش ميه خالص |
| S04 the choice | R2V | girl sheet + kitten sheet + S04 keyframe | وأنا كمان عطشانة... |

Full prompt text for these two videos was not saved. Whisper later confirmed the lines; S04 had low confidence. Review S04 by ear.

## S05–S07 keyframes (verbatim, one message, free)

```
Generate 3 images (one per scene). @roqa_sheet_v1 is Ruqayya, @kitten_sheet_v1 is the kitten, @location_wall is the village location: keep all three exactly. Premium hand-painted Japanese animated feature-film aesthetic, widescreen 16:9, hot summer noon, no text.
IMAGE A — SCENE 05 keyframe: Ruqayya kneels by the wall, the small lid of her lunchbox on the ground in front of the kitten; she carefully pours water from her blue bottle into the lid, a clear sparkling stream of water; the weak kitten lifts its head toward the water.
IMAGE B — SCENE 06 keyframe: low eye-level close shot: the orange tabby kitten drinks happily from the lunchbox lid, little tongue lapping; Ruqayya beside it, smiling with relief, gently stroking its back.
IMAGE C — SCENE 07 keyframe: wide shot on the dusty village path, softer late-afternoon light, a gentle breeze moving the palm leaves; Ruqayya walks home with her satchel, looking back over her shoulder and laughing, as the happy kitten trots after her.
```

On the second account the same three stills were made in one message using the uploaded v1 girl sheet, the kitten sheet, and the S02 location still. All three stayed consistent.

## S05 video (verbatim)

```
Use Reference-to-Video. @roqa_sheet_v1 is Ruqayya. @kitten_sheet_v1 is the kitten. @S05 keyframe is the scene and composition. SCENE 05 — SHARING. An exactly 8-second continuous animated shot. Widescreen 16:9. Premium hand-painted Japanese animated feature-film aesthetic. Ruqayya takes the small lid off her lunchbox, places it gently in front of the weak kitten, opens her blue bottle and slowly pours the water into the lid; the water sparkles in the sun. She whispers in sweet, natural Egyptian Arabic: "خدي... اشربي". The kitten lifts its head toward the water. Close, warm camera, slight push-in on the water. Audio: cicadas, water pouring, her soft whisper. No music. No text or subtitles.
```

## S06 video (verbatim)

```
Use Reference-to-Video. @roqa_sheet_v1 is Ruqayya. @kitten_sheet_v1 is the kitten. @S06 keyframe is the scene and composition. SCENE 06 — SHE DRINKS. An exactly 8-second continuous animated shot. Widescreen 16:9. Premium hand-painted Japanese animated feature-film aesthetic. The orange tabby kitten drinks eagerly from the lunchbox lid, little tongue lapping, ears perking up, getting its strength back. Ruqayya watches with a huge relieved smile, gently strokes its back and says softly in sweet, natural Egyptian Arabic: "الحمد لله". The kitten looks up and gives a happy little meow. Eye-level camera, gentle slow drift. Audio: soft lapping, a happy meow, cicadas. No music. No text or subtitles.
```

## S07 video (verbatim)

```
Use Reference-to-Video. @roqa_sheet_v1 is Ruqayya. @kitten_sheet_v1 is the kitten. @S07 keyframe is the scene and composition. SCENE 07 — WALKING HOME. An exactly 8-second continuous animated shot. Widescreen 16:9. Premium hand-painted Japanese animated feature-film aesthetic. The light softens into warm late afternoon, a gentle breeze moves the palm leaves and cools the air. Ruqayya walks home along the dusty village path, looks back over her shoulder and laughs as the happy kitten trots after her. The camera slowly rises and widens to reveal the peaceful village, green fields and palm trees. Audio: soft breeze, light footsteps, a playful meow. No music, no speech. No text or subtitles.
```

## S08

Not a Flow prompt. End card in the edit: the hadith in calligraphy and the source line, after the wording is checked.
