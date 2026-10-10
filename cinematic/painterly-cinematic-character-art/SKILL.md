---
name: painterly-cinematic-character-art
description: Art-direction and Midjourney prompt-writing for a specific painterly-cinematic character-design style (Arcane / Alberto Mielgo / game-cinematic lineage) with graphic dust-and-smoke motion trails and streetwear-driven wardrobe. Use this skill whenever the user wants a still image, character design, outfit concept, creature design, or location/environment prompt in this house style — including phrases like "write me a prompt for," "design a character," "give me an outfit," "concept art," a scene idea to expand, or a style critique of an existing image. Applies to Midjourney v8.1 image generation specifically. Use it even when the user doesn't name the style explicitly but is clearly working within this established look, and use it to critique and steer designs, not only to generate prompts.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Painterly-Cinematic Character Art

Art-direction skill for a distinctive painterly look used in AI filmmaking. It does two jobs: (1) write ready-to-paste Midjourney v8.1 prompts in the house style, and (2) steer design decisions — critiquing, correcting, and pushing concepts away from generic toward striking. This covers **still images only**. Motion/video (Seedance) is a separate skill.

## The style in one line

Painterly, textured, hand-painted concept art in the Arcane / Alberto Mielgo / game-cinematic tradition — the collision of a *slow, crafted, gallery* render with *fast, graphic, kinetic* effects. Most work commits to one register; holding both is the signature.

## The STYLE CORE (keep constant across a project)

This block is fixed. It goes after the subject + wardrobe description. Do not paraphrase it loosely between generations — consistency of wording is consistency of look.

```
painterly cinematic concept art, stylised character in the vein of Arcane and
Alberto Mielgo, thick visible hand-painted brushstrokes, rough oil-painting texture,
matte brush-textured skin not glossy, lost-and-found edges, expressive slightly
enlarged eyes, strong jawline, angular sculptural facial planes, pushed stylised
proportions, graphic face markings, baggy oversized clothing, desaturated earthy
palette with one saturated accent pop. Detail concentrated on the face and focal
point; background thrown into a shallow, painterly depth of field — loose, abstract,
thick brushstrokes suggesting the setting rather than detailing it, like a comic-book
background, not smooth photographic blur. Moody cinematic lighting, strong
chiaroscuro, aggressive rim light separating the figure, cool shadows against a warm
key, atmospheric haze. Painterly and hand-crafted, not smooth or clean.
--stylize 600 --style raw --v 8.1
--no smooth gradient shading, glossy skin, clean lineart, anime cel shading, even flat lighting, sharp detailed background
```

Prompt structure is always: `[SUBJECT] + [WARDROBE] + [STYLE CORE] + [params]`.

### Why this wording (the Arcane gap)
The default failure mode is a render that reads **high-end anime / webtoon** instead of Arcane: smooth gradient shading, glossy airbrushed skin, clean line, and — most of all — a background rendered at the *same sharp fidelity* as the subject. Arcane is the opposite: retained visible brushwork, matte painted skin, and detail held ONLY on the focal point while everything else collapses into loose abstract paint. The load-bearing fixes, most to least impactful: (1) **texture** — visible brushstrokes, not smooth; (2) **detail distribution** — sharp face, painterly-blurred background; (3) **proportions** — push the bone structure more angular/sculptural; (4) **lighting** — harder chiaroscuro, cooler shadows. The `--no` block matters as much as the positives, because the usual problem is the *presence* of smoothness, not the absence of paint.

### Painterly depth of field (key device)
Backgrounds should fall into shallow DoF rendered as **thick loose brushstrokes** — a painter's blur, not a lens blur. A few confident strokes suggest a window/tree/wall without resolving them. Always phrase it as a painter's effect ("loose abstract brushwork, thick strokes suggesting the setting, not smooth photographic blur") or the model gives smooth gaussian bokeh and undoes the painterly aim. This is the comic-book/BD convention of holding rendering on the hero and letting the background go gestural.

### Dialing the render
- `--stylize 600` is now the default — high stylize is the cheap win for painterliness and abstraction away from a literal clean read. Drop toward **250** only when a shot needs tighter control and is coming out too abstract.
- `--ar` changes by shot: `16:9` cinematic/action/establishing, `2:3` or `4:5` for character portraits and full-body turnarounds.

### The DUST/EFFECTS MODULE (append when motion is wanted)
```
sweeping arc of dust and smoke trailing behind the movement, curling volumetric
plumes that taper like brush swipes, particles catching the rim light, trails
forming leading lines that frame the subject
```
The dust is the strongest device in the whole look. It does three jobs at once: **motion vector** (traces path + speed from a single frame), **composition** (leading lines that curl around and frame the hero), and it is **graphic not simulated** — it curls and tapers like a calligraphic brush swipe, sumi-e ink wash and Hokusai-wave DNA, not physically accurate turbulence. That's why it reads elegant not noisy. Keep this framing when writing effects.

## Design philosophy (this is what keeps it from going generic)

Apply these when generating OR critiquing. They are the load-bearing rules.

1. **Wardrobe carries the character, not a costume.** Nobody wears a "hero outfit" — they wear *fits* (oversized tailoring, technical utility, sportswear) pushed to an extreme silhouette. For superheroes/genre characters specifically: express the power through *fashion and material*, not spandex.
2. **Silhouette first.** Every strong design reads as a black shape before any detail: towering collar, boxy tee over skinny legs, dread-spike up top. Design the outline before the surface.
3. **One material tells the power/identity.** No logo needed — a texture can *be* the concept: chrome, smoke, gold, glass, ash. (E.g. a gold-power character whose jewelry is literally spreading up the forearms as molten veins.)
4. **One saturated accent against a restrained palette.** Desaturated earths/slates/teals, then a single hit of orange, magenta, or acid green. Flat solid-colour backgrounds (hot pink, orange, sage) are on-style for character sheets.
5. **The "cool" accessory vocabulary.** Gold jewelry, glasses/tinted shades/goggles, texture-hair (dreads, undercuts, bleached streaks, static-charged strands), tattoos and graphic face markings, chains, piercings. These recur and do reliable shorthand work.
6. **Wardrobe DNA = three references fused:** oversized streetwear silhouettes + techno-utility hardware (harness straps, buckles, D-rings, collar rings, respirators, goggles) + sportswear (jerseys, compression sleeves, chunky sneakers, taping). Plus caps/headwraps/durags.

## Correction instincts (learned steering moves)

- **"Looks like they work in a coffee shop" / too twee → swap materials, keep palette.** Corduroy, hand-knit scarves, beanies read *barista*. Fix by moving to technical fabrics (nylon windbreakers, colour-block shells), sportswear, structured tailoring, and harder accessories (tinted glasses, gold, chains, utility pouches, bumbag-across-chest). Keep the bright clashing colours — swap the fabric, not the hue.
- **Clashing colours are deliberate.** Teal/burnt-orange/pink/mustard fighting a little sells "dresses by feel." A coordinated palette reads as a designed uniform — usually the wrong note for a scavenger/street character. If it's too busy, neutralize *one* item (plain cream trousers, drop the scarf) to rest the eye — don't coordinate everything.
- **Two-weapon / complex-prop artifacts.** Models merge props or add limbs when a character holds e.g. both a gun and a katana. Generate the clean character sheet with the simpler load (katana on back), then add the second drawn weapon only in action shots.
- **Creature design: keep the attitude, change the parts.** "An odd version of a cat" works best by keeping the *scale and attitude* (aloof, lap-sized, unimpressed) while building the body from stranger parts (extra legs, moss-fuzz, antennae-whiskers, goat pupils, glowing tail bulb) so it reads as its own species, not a cat.
- **Balance the cast.** If reference material or a generated set skews to one race/type, vary it deliberately — but don't overcorrect into a *uniform* set the other way, which is the same lack-of-variation problem inverted. Mix.

## Location / environment prompts

- **Sell scale through contrast.** For an epic establishing shot, make the huge thing absurdly huge and the human-scale thing almost lost in it. If the model centres or oversizes the subject, add explicit smallness ("the metal sphere very small, tree fills the frame") and push it off-centre. Low angle looking up exaggerates height/vertigo.
- **Clutter is characterisation.** Interiors tell you who lives there before anyone moves — crisp packets, glowing TV, salvaged junk. Name the mess.
- **Lighting shift = tonal shift.** A single added light (e.g. a red alert light cutting warm amber) flips cosy → threat in one move. Reach for this for story beats.
- Keep the STYLE CORE's painterly/atmospheric tokens; swap character tokens for environment ones (establishing/interior/wide shot, sense of height, atmospheric haze catching golden light).

### Backdrop defaults
- **Characters and creatures** default to a **simple flat grey backdrop** (neutral, lets the subject's own colour and lighting carry — especially good for translucent/coloured creatures where a saturated background would compete). Saturated flat backgrounds (hot pink, orange, sage) are also on-style when a punchier character-sheet look is wanted.
- **Locations/environments are the exception — never put them on grey.** The environment *is* the subject: sky, haze, horizon, architecture are the point, and grey flattens or confuses it. Drop the grey-backdrop line entirely for any location prompt.

### Continuity-safe fight locations (important for the video stage)
Image-to-video models don't hold a mental map, so a **distant landmark (a skyline, a mountain) becomes a directional anchor that drifts** when the camera cuts or swings during action — it reappears at wrong angles and breaks continuity conspicuously. Design fight locations to remove the anchor:
- **Enclose the space** (walled garden, forest glade, courtyard/quad) so there's no far horizon to get wrong; distant elements become texture, not tracked objects.
- **Flat even ground + wraparound similar scenery** (tree-ring, repeating cloister arches) reads plausibly from any angle.
- A **large central object** (e.g. a big central tree) actually *helps* — it's a fixed landmark that looks the same from every angle, giving the AI something consistent to orient around.
- Pattern: shoot the landmark-heavy "hero view" (e.g. hilltop over a city) as a **static establishing beat** where continuity doesn't matter, then cut the actual fight into a **contained, anchor-free location**.

## Continuity across a series (critical)

Words alone won't hold a look or a character across shots. Use references:
- **`--sref [job-url]`** — lock the *style/texture* across a whole series. Grab the URL of the first frame you love and feed it to everything after. This holds the painterly render far better than words.
- **`--oref [url]` with `--ow 60–100`** — lock the *character* (face markings, design) between shots (omni-reference).
- **`--cref`** — character reference for turnaround sets (front / profile / action / close-up).
- For a **pet or second character** in the same world, lock the hero frame first, then generate the companion referencing it so they read as the same world.
- For **location interior/exterior pairs**, feed the exterior into the interior generation (and vice versa) so shared features — porthole shape, materials — agree.

## Pipeline reality (Midjourney → GPT-Image2 / Nano Banana Pro)

The workflow is: generate source assets (character sheets, locations) in **Midjourney v8.1**, then **combine references** (e.g. character sheet + location) into each final key image using **GPT-Image2** or **Nano Banana Pro**. This changes how the STYLE CORE is applied:
- **Midjourney params don't carry to the combine step.** `--stylize`, `--no`, `--sref`, `--ar` etc. are Midjourney-only. GPT-Image2 / Nano Banana read **plain language**, so at the combine stage lean on the *descriptive tokens* (visible brushstrokes, painterly DoF, matte skin, chiaroscuro) and drop the params. Worth keeping two tails: one **with params for MJ source gens**, one **prose-only for the combine step**.
- **The combine tools render cleaner/smoother by nature** — they are the step most likely to sand off the brushwork and push it back toward the anime read. So painterly tokens matter *most* here, and even then may fight you.
- **The real fix for smoothness is upstream:** make the input references (MJ character sheet + location) already heavily painterly, so there's brushwork in the source for the combine to preserve. You can't reliably add texture at the combine step that wasn't in the inputs.
- For **face/outfit continuity** use the character sheet as the reference (the `--oref` equivalent in whichever tool); for a scene referencing two sources, the character sheet drives the person and the location drives the setting.

## Output conventions

- Output prompts as clean, copy-pasteable blocks. Full worked prompt = subject + wardrobe + STYLE CORE + params, assembled.
- When the user gives *story context* but says not to put it in the prompt, honour that — use it to inform design choices silently, don't inject narrative into the prompt.
- When generating multiple concepts, give each a short name and a one-line design logic before the prompt, so the user can see the *idea*, not just the words.
- Offer concrete next moves (turnaround set, harder-street variant, action beat, matching location) rather than open-ended "what next?" — but keep to one such offer.
- Default to prose reasoning when critiquing; reserve the fixed template only for the STYLE CORE and modules.

## Reference lineage (for grounding critique and vocabulary)

Arcane (Fortiche); **Alberto Mielgo — *The Witness*, *Jibaro* (the single best reference for painterly-in-motion + fashion-forward stylization)**; Spider-Verse (graphic motion/effects); Love Death & Robots, Secret Level (Blur game-cinematic); Star Wars: Visions esp. Trigger's *The Duel*; AKIRA (cel lineage, graphic energy); samurai/chanbara + Samurai Champloo / Afro Samurai for the dust-as-drama convention. Concept-art tradition: Craig Mullins, Sparth, Feng Zhu, Ben Eblen.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
