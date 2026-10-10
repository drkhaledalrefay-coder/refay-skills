# Phase 3 — Stills, holding references, clip prompts

## 3.1 Selecting generated stills
Users often generate 2–3 candidates per persona and name them `V0N_NAME_still.png_<suffix>.jpg` (e.g. `V01_HERO_still.png_01.jpg`). Check duplicates by hash. View each and rank:
1. Rules (modesty, no visible hair) — a fail disqualifies.
2. Market-correct, attractive face; warm expression.
3. Concern mild.
4. Setting clean/modern; no artifacts (extra fingers, second phone, warped objects); climate-correct clothes.
5. Video-usable: sharp, front-facing, chest-up, 9:16.
Copy winners (don't move) to `selected/V0N_NAME_still.jpg`. Make a labelled contact sheet. Report honestly per persona; set `needs_regeneration` with a reason when nothing passes.

## 3.2 Holding-product reference (before video)
Video models guess product size badly. Generate, per video, an image with two references:
```
Use reference image 1 (the person) and reference image 2 (the product). Same person, same face, same hair or head covering and outfit, same room and light as image 1. They are holding <product> exactly as in image 2 — same shape, colour, cap and label, label facing the camera and legible. SCALE: <hand-relative sentence, e.g. "a 40 ml tube about 13 cm long — as long as an open palm plus half the fingers; fits in one hand">. Natural grip, five fingers, relaxed hand at chest height, <action pose from the script>. <Modesty line>. Raw front-camera phone selfie, 9:16. Avoid: product too big or too small, distorted or invented label, extra fingers, visible hair, second phone, messy room.
```
Its output becomes reference image 2 for every clip of that video (instead of the bare packshot).

## 3.3 Clip prompt structure (Google Flow / Veo; adapt for Kling etc.)
```
REFERENCES: 1) V0N_NAME_still (or holding image) — the person; 2) <packshot/holding image> — the product
[STYLE DNA]  (one shared block, on its own deck slide; paste in full or reference)
<Name> (<persona descriptor — identical across the video's clips>). Setting: <…>.
0–2s: <opening move> · 2–8s: <action + what they say>
They say in a casual <dialect> accent: "<native line>"
Camera: front selfie, arm's length, small handheld drift, auto-exposure hunting.
Light: <…>. Audio: her voice close-mic, room tone.
Product handling: <how she holds/uses it>. SCALE LOCK: <product> is <cm> — <hand-relative>; keep this size in every frame.
End of clip: <invisible-cut transition — hand/palm covers lens, whip toward shelf, product passes the lens…>
NEGATIVE: [MASTER NEGATIVE] + product wrong size, label changes, visible hair, second phone.
```
Invisible cuts to reuse: palm over lens · product passes the lens · whip pan to shelf · head turn out of frame · lean into mirror blur · water splash/towel pat · reach down out of frame · lens covered by fabric.

## 3.4 Style DNA & master negative
Write one STYLE DNA block (phone-camera realism: front camera, ungraded, mild grain, uneven exposure, no ring light, natural speech, no presenter energy) and one MASTER NEGATIVE (studio lighting, beauty filter, influencer posing, subtitles burned in, logos other than the product, extra fingers, warped labels, visible hair / immodest clothing per market, messy/dirty settings). If an inherited style text conflicts with the market rules, the market rule wins — tell the user.

## 3.5 Lint
`python scripts/lint_prompts.py content.json --market hot-modest` before the deck. Zero banned hits; every clip has SCALE LOCK; every still prompt has an Avoid line.
