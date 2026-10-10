---
name: painterly-multishot-animation-engine
description: 'Turn a story idea plus reference images into a SET of self-contained, timecoded multi-shot animation prompts — one per "generation" — in a painterly, Arcane-inspired cinematic style, with continuity across separate generations. Use when the user wants a painterly or stylised animation prompt, a multi-shot animation scene, an Arcane-style shot sequence, a fight or action beat as animation, or a story broken into multiple AI video generations from character/location reference images. Trigger on: "animation prompt", "painterly prompt", "Arcane style", "multi-shot animation", "animate this scene", "break this story into generations", "shot sequence for animation", or when the user uploads character/creature/location references for a stylised animated sequence. Also trigger when the user names AI video tools (Seedance, Kling, Sora, Veo, Runway, Luma, Hailuo, Wan, Higgsfield) in an animation or painterly context, or says "generation 1/2/3", "multi-generation", or wants a story spanning more than one 15-second clip.'
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Painterly Multi-Shot Animation Prompt Engine

This skill turns a story idea and a set of reference images into **a sequence of self-contained animation prompts**, each one ready to paste into an AI video generator. It is built for painterly, semi-realistic, Arcane-style animation with strong held hero poses and a hand-painted look.

The core idea that makes this different from a single-shot prompt: a story is broken into **generations**. Each generation is one ~15-second video generation, produced *independently*, fed its own matching reference images. The generator producing Generation 2 cannot see Generation 1's output. So the craft is in writing each generation to stand alone *while* the whole set reads as one continuous story. That continuity is engineered in the prompt, not assumed.

**Hard rule: each generation is 2,000 characters or fewer** (counting the shot text plus the metadata block). This is non-negotiable — it fits the prompt-length limits of tools like Seedance, Kling, Veo and Higgsfield. Every generation is counted and trimmed to fit.

---

## Workflow

### Step 1 — Break the story into generations

Take the user's idea and split it into story beats, where each beat is one ~15-second generation. A typical three-part structure is **Arrival → Conflict → Resolution**, but let the story dictate the count (two generations for a simple beat, four or five for a longer sequence).

Name each generation by its function (e.g. *Arrival*, *The Fight*, *The Finish*). Before writing any shots, know:

- **What changes** in this generation (the beat's job in the story)
- **What must carry** into the next generation (characters, objects, environment state)
- **Which reference images** feed this generation (which characters/creatures/locations appear)

If the user hasn't said how long the story is or how many beats, propose a structure and confirm it before writing.

### Step 2 — Lock the continuity anchors (do this before any shots)

Because each generation is produced blind to the others, continuity has to be *designed in advance* and re-stated in every generation that needs it. Decide these up front:

1. **Identity anchors.** Give each character/creature one unmistakable signature motif that survives across generations — Monster B's gold-seamed white ceramic armour, Hero A's gold gauntlets. Re-describe the motif every time the character appears, in every generation. This is what makes separate generations read as the *same* character.
2. **Persistent objects.** List any object that must survive the whole story (e.g. the coffee cup). Track its status explicitly in *every* generation it appears in — established, protected/set aside, then paid off. Never let a persistent object sit unaccounted for.
3. **Environment integrity.** If a generation introduces something dramatic to the location (a portal, an explosion), resolve or close it *within its own shot* so the location returns to a state the next generation's reference image can match. The courtyard must still be the courtyard in Gen 3.
4. **Disposable in-shot assets.** For weapons, effects, or props conjured mid-shot, use the forge → use → destroy rule: create it, use it, and destroy or dissolve it *inside the same shot*, and explicitly clear the character's hands/arms before the cut. Nothing conjured should ever have to carry between shots or generations, because the next generation can't see it.

Write these anchors down before drafting shots. They are the glue.

### Step 3 — Analyse the reference images (per generation)

For each generation, study its matching reference images and extract a compact description of every character, creature, and the location — enough that a model seeing only this generation could recreate them. Cover:

- **Characters** — hair, face, build, clothing, colours, held objects, and the identity anchor motif from Step 2
- **Creatures/monsters** — silhouette, material, colour, the signature motif (e.g. gold seams)
- **Location** — architecture, materials, palette, light, and current environment state

Keep it tight — this counts against the 2,000-char budget. Weave the details into the shots (clothing in a wide shot, face in a close-up) rather than dumping a description block. If a needed reference hasn't been uploaded, ask for it: the reference image is the visual anchor for the whole generation.

### Step 4 — Design each generation's shot sequence

Each generation totals **exactly 15 seconds**. Within that:

- Each shot is **2–5 seconds**; use **3 shots** (slow, held beats) up to **7 shots** (fast action)
- **Vary the shot count between generations** so the set doesn't feel mechanical
- Each shot opens with a timecode stamp `[MM:SS - MM:SS]` (e.g. `[00:07 - 00:11]`), and the stamps must add up cleanly to 15 seconds

For **every shot**, specify all four technical parameters, and vary them shot to shot (never repeat the same one in consecutive shots):

1. **Shot size** — wide, medium, close-up, macro
2. **Lens** — 24mm, 35mm, 50mm, 65mm, 85mm (wide for scale and environment, long for intimacy and impact)
3. **Camera angle** — low angle sells scale and heroism, eye-level for grounding, high angle for vulnerability, Dutch for chaos
4. **Camera movement** — one clear verb: static (held), slow push in, pull out, tilt up/down, whip pan, track, orbit

**Camera language for this style:** this is painterly hero-pose animation, not handheld live-action. Favour **strong held frames** and deliberate moves — static holds, slow pushes, single decisive whip pans on impacts — that let the hold-snap-settle cadence and the hero poses land. Do **not** default to gritty handheld shake here; that fights the style. (If the user explicitly wants a rougher, handheld animated feel, you can dial it in — but held/stepped is the default for this look.)

Low angles and held hero poses are the backbone of the style — use them on transformations, power moments, and the monster's scale.

### Step 5 — Write each generation

Output each generation as **separate paragraphs inside a single fenced code block** — one paragraph per shot, blank line between, each starting with its timecode stamp. No lists, no headers, no numbered shots inside the block. Each shot reads as continuous cinematic direction.

**Always close each generation with this fixed metadata block**, after a blank line following the final shot. These lines are non-negotiable and count against the 2,000-char budget:

1. **Location:** — the setting and its current environment state for this generation (e.g. `Location: university courtyard under a single dark storm cloud, wind-blown grass, gold light flaring.`)
2. **Style:** — always the fixed painterly line:
   `Style: Painterly cinematic animation, hand-painted brushwork, semi-realistic stylised characters, stepped hold-snap-settle cadence, strong held hero poses, weight and follow-through, drawn gestural dust and debris trails carrying the motion, warm key against cool shadow.`
   *(You may swap the trail descriptor to match the beat — "gold-shard trails", "gold trails" — but keep the rest of the line intact.)*
3. **Constraints:** — always fixed:
   `Constraints: no text, logos, or readable writing anywhere in frame.`
4. **Audio:** — diegetic only, no music/score. Two accepted forms:
   - **Compact (default for dense action beats):** a scene-specific diegetic sound list, e.g. `Audio: Diegetic only — wind, gold ring and shatter, heavy footfalls, Monster B's taunt.`
   - **Full footer (use when there's character headroom):** `Audio: Diegetic sound only — realistic, high-fidelity foley and natural ambience. Grounded, physical sound effects with real weight and texture — impacts, footsteps, cloth, breath — recorded-quality environmental sound. No music, no score, no soundtrack.`
   Either way: **diegetic only, never music or score.** Dense fight generations usually only have room for the compact form once the shots are written — that's expected.

### Step 6 — Count, trim, and deliver

**Count each generation.** If it exceeds 2,000 characters, trim in this order:

1. **Compress adjectives/adverbs** — cut atmospheric padding first
2. **Merge shared elements** — if consecutive shots share a location or lighting note, state it once
3. **Shorten repeat references** — after a character is established in shot one, later shots can use a short identifier ("she", "the Monster B")
4. **Switch the audio line to the compact form** if you were using the full footer
5. **Never cut:** the timecode stamps, the shot size/lens/angle/movement specs, or the Location/Style/Constraints/Audio block

Deliver **each generation in its own fenced code block** so the user can copy them one at a time. After each block, add a short continuity note (1–3 sentences) explaining what that generation sets up or pays off — which anchors it plants, which objects it protects, how it hands off to the next. This is where you make the continuity logic visible to the user.

---

## The continuity rules (worked through)

These are the rules that make separate generations feel like one film. Apply them every time.

- **Identity anchoring.** Two generations that can't see each other only read as the same character if the signature motif is restated in both. Monster B is "the huge white ceramic figure, gold-seamed" in Gen 1 *and* Gen 2 *and* Gen 3. Never assume the reference image alone will hold identity — say it.
- **Object persistence.** An object that pays off later must be tracked in every generation between setup and payoff. The coffee is established beside Hero A in Gen 1, *explicitly set safely aside on a book* before she transforms, and picked up cold in Gen 3. If it had gone unmentioned in between, the payoff breaks.
- **Environment integrity.** Dramatic events resolve inside their own shot so the location can persist. The portal in Gen 1 is gold-seamed (carrying Monster B's identity) and *closes on impact* — so the courtyard is never permanently altered and Gen 3 can end in the same courtyard.
- **Disposable assets.** Every weapon Hero A forges is created, used, and destroyed within a single shot, with hands/arm explicitly cleared before the cut. Nothing carries. This is what lets a fight span multiple blind generations without state leaking or contradicting.
- **Payoff logic.** The finish should pay off a rule the story established. Monster B's armour is "unbreakable", so the win comes *through* his one exposed patch (the eye), sealing him from within with his own armour — the logic the earlier generations set up.

---

## Worked example — "Hero A vs Monster B" (3 generations)

Reference images: Hero A in civilian and hero form, Monster B, and the university courtyard — each generation fed the ones it needs.

### Generation 1 — Arrival

```
[00:00 - 00:03] Wide, 28mm, eye-level, slow push in — a sunlit university courtyard, honey stone walls and gothic windows. Civilian Hero A, brown curly hair and clear glasses in a cream-and-blue track jacket, lies prone on the grass, legs kicked up behind her, deep in plain unbranded books; a flat white in a plain takeaway cup sits beside her. Students lounge, chat, eat lunch, scroll phones. Warm, relaxed summer. Held still.

[00:03 - 00:05] Medium, 50mm, eye-level, static — a deep rumble builds; Hero A slowly lifts her head from her book, eyes widening. Coffee and books still beside her.

[00:05 - 00:07] Wide, 24mm, low angle, tilt up — a single dark storm cloud blooms in the centre of the clear blue sky; wind kicks up, whipping the grass and her hair.

[00:07 - 00:11] Wide, 24mm, eye-level, static — a swirling portal rimmed with molten-gold cracks tears open above the courtyard; the huge white ceramic armoured Monster B, gold-seamed, drops through and slams down at the centre, a burst of dust and torn turf blooming outward. Students scatter.

[00:11 - 00:15] Medium, 35mm, low angle, slow push in — Hero A sets her coffee safely aside on a book, rises to her feet with a determined glare, and transforms: gold igniting up her arms into dripping golden gauntlets, streetwear becoming her gold-wrapped hero form. Hero pose, held.

Location: Sunlit university courtyard, honey stone walls, green lawn, a single storm cloud overhead.
Style: Painterly cinematic animation, hand-painted brushwork, semi-realistic stylised characters, stepped hold-snap-settle cadence, strong held hero poses, weight and follow-through, drawn gestural dust and debris trails carrying the motion, warm key against cool shadow.
Constraints: no text, logos, or readable writing anywhere in frame.
Audio: Diegetic only — birdsong, chatter, rising rumble, wind, portal boom, impact.
```

*Continuity:* Plants both identity anchors (Monster B's gold seams, Hero A's gold gauntlets). The coffee is established, then explicitly set safely aside on a book before the transformation, so it survives to the Gen 3 payoff. The portal is gold-seamed and closes on impact, so the courtyard is never altered.

### Generation 2 — The Fight

```
[00:00 - 00:03] Medium wide, 35mm, low angle, static — Hero A in hero form, gold gauntlets blazing, materialises a giant crystallised-gold sword in both hands and swings it at Monster B; it strikes his white ceramic armour and shatters into a burst of gold fragments. Hands now empty.

[00:03 - 00:06] Wide, 24mm, low angle, whip pan — Monster B slams a ginormous fist down at Hero A; she rolls clear and the fist craters the grass, dust blooming outward. Her hands stay empty.

[00:06 - 00:09] Medium, 40mm, eye-level, static — Hero A forges a huge rail gun of jagged gold shards locked onto her arm and fires; sharp gold slugs streak out and shatter against Monster B's armour one after another.

[00:09 - 00:12] Wide, 35mm, low angle, slow push in — Monster B strides through the barrage unharmed, shrugging off the shattering gold; the rail gun spends its charge and dissolves from her arm, arm now clear. Shards tinkle down into brief quiet.

[00:12 - 00:15] Close-up, 50mm, low angle, static — Monster B grins wide and speaks into the silence: "Do you like my new armour, Hero A? I forged it just for you." Hero A stands firm, gauntlets glowing.

Location: university courtyard under a single dark storm cloud, wind-blown grass, gold light flaring.
Style: Painterly cinematic animation, hand-painted brushwork, semi-realistic stylised characters, stepped hold-snap-settle cadence, strong held hero poses, weight and follow-through, drawn gestural dust and gold-shard trails carrying the motion, warm gold key against cool storm shadow.
Constraints: no text, logos, or readable writing anywhere in frame.
Audio: Diegetic only — wind, gold ring and shatter, heavy footfalls, Monster B's taunt.
```

*Continuity:* Every weapon is a disposable asset — forged, used, destroyed inside its own shot, hands/arm cleared before each cut, so nothing carries. The rail gun spends into a beat of quiet, and Monster B delivers his "unbreakable armour" taunt into that silence — planting the finish logic.

### Generation 3 — The Finish

```
[00:00 - 00:03] Medium wide, 35mm, low angle, static — Monster B's ginormous fist closes around Hero A in hero form, pinning her; only her arms are free. She squirms, panicked, gold gauntlets flexing.

[00:03 - 00:06] Medium, 50mm, low angle, slow push in — Monster B raises Hero A up to its face, a huge evil grin splitting its cracked ceramic features. She hangs in its grip.

[00:06 - 00:09] Close-up, 65mm, eye-level, static — Hero A, suddenly deadpan, raises a single finger and pokes Monster B directly in its exposed eye, its one patch of bare flesh.

[00:09 - 00:12] Wide, 28mm, low angle, static — gold floods from the eye through Monster B; he slowly seizes and turns to a solid golden statue sealed in his white ceramic armour, fist opening as he freezes. Hero A drops free to the grass.

[00:12 - 00:15] Medium, 35mm, eye-level, slow push in — the storm cloud clears and sun returns; Hero A dusts herself off, picks up her plain coffee cup, takes a sip, and grimaces. In an annoyed British accent: "Ugh, now my coffee's cold."

Location: university courtyard, storm clearing to warm sun, a golden Monster B statue frozen mid-lunge.
Style: Painterly cinematic animation, hand-painted brushwork, semi-realistic stylised characters, stepped hold-snap-settle cadence, strong held hero poses, weight and follow-through, drawn gestural dust and gold trails carrying the motion, warm key against cool shadow.
Constraints: no text, logos, or readable writing anywhere in frame.
Audio: Diegetic only — gold groan and chime, wind settling, birdsong returning, Hero A's line.
```

*Continuity:* Pays off the "unbreakable armour" logic — the poke drives gold *through* the one exposed eye and seals him from within, his own armour trapping it. The fist opens as he freezes so Hero A is released cleanly, the storm lifts back to the Gen 1 sun, and the cold-coffee button pays off the cup planted in Gen 1.

---

## Handling variations

**Number of generations.** Two for a simple setup-and-payoff; three for Arrival/Conflict/Resolution; four or five for a longer arc. More generations means more continuity discipline — restate every anchor in every generation.

**Single vs. multiple characters.** For ensembles, distribute character introductions across shots rather than cramming everyone into shot one, and give each their own identity anchor to restate.

**Creature companions.** A creature companion gets the same treatment as a hero — a signature motif restated each generation, and its own held poses. Don't let it become set-dressing.

**Monster/scale beats.** Sell scale with low angles, wide lenses (24mm), and held frames — let the monster loom. Reaction shots on the hero (medium/close, eye-level) cut the scale down to human stakes.

**Quiet / atmospheric generations.** Lean to 3–4 longer shots (4–5s), static or slow-push moves, wider lenses, more negative space. Save the fast cutting for the action generations so the set has rhythm.

**Dialogue beats.** Put spoken lines in a held close-up or medium (50–65mm) so the line lands. Keep dialogue short — it eats the character budget fast.

**Budget pressure.** Dense action generations will crowd the 2,000-char limit. Trim adjectives and use the compact diegetic audio line before you ever touch the timecodes, camera specs, or the fixed Style/Constraints lines.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
