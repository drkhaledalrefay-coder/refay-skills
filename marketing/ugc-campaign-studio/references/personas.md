# Phase 2 — Personas & scripts

The examples here come from real campaigns (see the intake for this market's specifics). For another market or category, keep the *structure* and swap the specifics from the intake: gender/age of the buyers, local faces and the drift to negate, dress rules (or none), climate, income level, and the product's natural use-moment (applying, eating, cooking, cleaning, using the device…).

## Why these rules exist
Each rule below came from a real rejection by the brand manager on a first campaign:
| Rejection | Rule |
|---|---|
| "Same 4 faces in 8 videos — they're not bloggers" | One different ordinary person per video |
| "AI makes the faces look like the wrong country" | Name the local features + negative clause |
| "Skin problems are overdone" | Mild, realistic concern; face reads healthy & pretty first |
| "Rooms look poor/old/messy; our buyers are middle-class to affluent" | Modern, clean, tasteful settings; "raw" = phone look, not mess |
| "Winter clothes in a hot city?" | Climate-correct fabrics within the market's modesty rules |
| "Expressions grim/dead-eyed" | Warm genuine half-smile, bright eyes |
| Hair visible despite the modesty rule | Under-cap wording + negative |
| Second phone in hand, dusty old car, crumpled sunshade | Explicit "no second phone", new clean car, nothing on dashboard |
| Old "style DNA" allowed a slipped hairline | Market modesty rule overrides any style text — ask the user when they conflict |

## Persona object (content.json → personas[])
`video, name, age, city, occupation, life_detail, concern (mild), face_descriptor, hijab_or_hair, outfit (climate-correct), setting, expression, voice (accent, pace), anchor_phrase, still_prompt, still_filename (V0N_NAME_still.png)`

Casting spread: vary age bands, jobs (student, nurse, teacher, new mom, cashier, office admin, pharmacy assistant, shop clerk…), cities within the dialect region, skin tones realistic for the region, and outfit/head-covering colours. Match concern to product (the persona's life should *explain* the problem — e.g. outdoors all day → sun spots).

Dialect consistency: all personas must plausibly speak the script's dialect (a <REGION> script → cities of that region only…).

## Still-image prompt template
```
Raw front-camera phone selfie, NOT a portrait photo, 9:16 vertical. Ordinary <nationality> woman/man, <age>, <occupation>, naturally beautiful <regional> face, not a model and not an influencer: <face shape>, <undertone>, <eyes>, <brows>, <nose>, <lips>, <skin tone> skin that reads healthy and pretty first, <very subtle concern>, barely noticeable at first glance, natural skin texture, no makeup, no beauty filter. <Regional> features, not <drift ethnicity 1>, not <drift ethnicity 2> features. <Modesty/hair line, e.g. "<colour> <fabric> head covering wrapped snugly over the forehead with an under-cap (bonnet), hairline completely hidden, no hair visible anywhere, neck covered" — or delete this clause entirely if the market has no such rule>. Wardrobe: <climate-correct fabric + cut + sleeves + neckline>. Front-camera arm's-length selfie, not a mirror selfie, chest-up framing, phone slightly below eye level, one arm out of frame holding the camera phone, other hand empty, no second phone visible. Soft genuine half-smile, bright eyes, warm and approachable, as if about to tell a friend something. <Light, slightly uneven, auto-exposure look>. No ring light, no studio lighting. Ungraded, slightly desaturated, warm-neutral phone-camera color, mild grain. Background: <clean modern tasteful local home/car/place matching the audience's means>, a real phone photo, not a styled shoot and not a hotel. Avoid: exaggerated skin problems, messy or old rooms, dirty surfaces, sad or blank expression, visible hair, second phone, heavy makeup, beauty-filter skin.
```
Adapt the modesty, ethnicity and setting lines to the market from the intake — the structure stays.

Cars: "recent-model <SUV/sedan>, clean <colour> leather interior, parked in shade, clean dashboard with nothing on it". Outdoors: name a real local place (e.g. a well-known waterfront promenade in the target city).

## Scripts
- 2–3 clips, ~8 s each; line per clip. Hook (problem, relatable, first 2 s) → product moment (what she does with it) → result (felt experience, no numbers) + CTA-free natural close.
- Table columns: clip/timing · native dialogue · transliteration · English meaning · on-screen text (CapCut) · reviewer notes.
- Caption + hashtags (brand + range + category in native language) + disclosure line.
- Don't reword approved native copy; strip invisible bidi controls (U+2066–U+2069) that render as boxes.
- New lines written by an agent → `needs_native_review: true` and shown as "DRAFT — native review" in the deck.
