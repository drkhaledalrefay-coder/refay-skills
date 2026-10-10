---
name: painterly-world-building-engine
description: "Design coherent painterly cinematic worlds — visual bible, characters, environments, props and keyframes — built from locked identity, world logic, visual language, shot design and continuity layers for AI image/video pipelines. Use for 'world building', 'visual bible', 'keyframes', or extending a film's look across scenes."
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Painterly World-Building Engine

## Purpose
A reusable agent skill for designing coherent painterly cinematic worlds, characters, environments, props, and keyframes for AI image/video pipelines.

Use this skill when an agent must:
- establish or extend a visual world;
- turn story material into a consistent visual bible;
- generate character/environment/prop prompt systems;
- create high-quality cinematic keyframes before animation;
- preserve continuity across multiple scenes or tools.

This skill is project-agnostic. Never assume a franchise, geography, ethnicity, costume, religion, era, or political setting unless the project source material explicitly requires it.

---

## Core Principle

Do not begin by asking an image model to "make it cinematic."

Build the image from five locked layers:

1. **Identity** — who/what must remain unchanged.
2. **World logic** — architecture, materials, culture, technology, weather, era.
3. **Visual language** — shape design, texture, edge behavior, palette, lighting.
4. **Shot design** — lens, camera height, composition, depth and focal hierarchy.
5. **Continuity** — references, negative rules, recurring props, color accents.

A strong production frame should already look like the final film before animation begins.

---

## Source-First Rule

Before generating anything, inspect all available project sources in this order:

1. project README / handoff;
2. story or script;
3. character bible;
4. visual bible / negative visual rules;
5. approved character references;
6. environment references;
7. prior approved frames;
8. continuity tracker;
9. current scene brief.

If sources conflict:
- do not invent a reconciliation;
- prefer the newest explicitly approved source;
- flag unresolved contradictions;
- never silently overwrite identity rules.

---

## Visual Bible Extraction

Convert project material into these blocks.

### A. Rendering Language
Define:
- 2D / 2.5D / 3D hybrid balance;
- surface finish;
- brush or line texture;
- clean vs broken edges;
- matte vs glossy materials;
- degree of stylization;
- facial-plane treatment;
- background detail density.

### B. Shape Language
Define:
- angular vs rounded;
- thin vs heavy silhouettes;
- architectural geometry;
- costume geometry;
- prop geometry;
- repeating motifs.

### C. Palette Logic
Define:
- base neutral family;
- shadow family;
- key-light family;
- one or two permitted accent colors;
- colors forbidden unless narratively motivated.

### D. Lighting Logic
Define:
- hard vs soft key;
- warm/cool relationship;
- rim-light behavior;
- atmospheric haze;
- practical sources;
- silhouette separation.

### E. Detail Distribution
Use the hierarchy:

**face / focal object > hands / costume cues > immediate environment > background**

Never render every surface at equal detail.

---

## Character Lock Protocol

For each character, extract and preserve:

- age;
- apparent height;
- build;
- face shape;
- eye shape/color;
- nose;
- mouth;
- hair;
- facial hair;
- scars or marks;
- skin tone;
- costume layers;
- footwear;
- accessories;
- recurring props;
- posture;
- habitual expression;
- silhouette;
- character-specific accent color.

### Character Sheet Standard
Prefer:
- front;
- back;
- 3/4;
- profile if identity requires it;
- face close-up;
- expression row when useful.

Keep:
- neutral background;
- consistent lens;
- consistent light;
- consistent proportions;
- no costume mutation.

### Identity Lock Language
For later prompts, explicitly state:

> Preserve exact face identity, body proportions, age, hairstyle, costume construction, accessories, height relationships, and recurring props from the approved references. Do not redesign the character.

---

## Environment Design Protocol

Every location must answer:

### Function
What happens here?

### Spatial Logic
- size;
- entrances/exits;
- vertical levels;
- usable surfaces;
- obstacles;
- sight lines;
- background landmarks.

### Material Logic
- stone;
- plaster;
- concrete;
- timber;
- metal;
- glass;
- fabric;
- vegetation;
- dust;
- water.

### Culture / Era Logic
Use only project-supported details.

### Light Logic
Identify:
- time of day;
- natural source;
- practical lights;
- dominant shadow color;
- accent light.

### Motion Potential
Identify objects later useful for animation:
- hanging fabric;
- smoke;
- dust;
- rain;
- wires;
- foliage;
- signs;
- loose paper;
- curtains;
- reflective surfaces;
- moving vehicles;
- practical lights.

### Depth Layers
Build at least:
- foreground occluder;
- midground action plane;
- background world plane.

Use parallax-ready composition whenever the frame may later become video.

---

## Prop and Symbol Protocol

Recurring props must have:
- exact dimensions or relative scale;
- material;
- wear pattern;
- color;
- placement;
- hand relationship;
- narrative meaning;
- allowed variants;
- forbidden mutations.

Never let a key prop randomly:
- change scale;
- change material;
- disappear;
- swap hands without reason;
- change color;
- gain decorative details.

---

## Cinematic Keyframe Construction

Build every important frame in this order:

### 1. Narrative Beat
What single instant are we freezing?

### 2. Emotional Verb
Choose one:
- waits;
- hunts;
- realizes;
- resists;
- hides;
- breaks;
- confronts;
- protects;
- escapes;
- mourns.

### 3. Camera
Specify:
- framing;
- camera height;
- lens feeling;
- angle;
- distance;
- tilt if needed.

### 4. Blocking
Place:
- subject;
- secondary subject;
- focal object;
- foreground;
- background.

### 5. Light
Describe what is lit and what is deliberately lost.

### 6. Texture
State surface behavior and brush/edge behavior.

### 7. Negative Rules
Remove:
- photorealism if unwanted;
- glossy skin;
- generic anime;
- generic clean CGI;
- over-detailed backgrounds;
- random costume additions;
- text artifacts;
- extra people.

---

## Prompt Architecture

Use this order:

### SUBJECT / IDENTITY
Who is visible and what must remain exact.

### LOCATION
Where the scene occurs and the spatial/material logic.

### NARRATIVE MOMENT
The exact frozen beat.

### COMPOSITION
Framing, perspective, silhouette and depth.

### LIGHT
Key, shadow, rim, atmosphere and practical sources.

### RENDERING
Surface texture, edge behavior, shape language, stylization.

### CONTINUITY LOCK
Approved-reference preservation instructions.

### NEGATIVE RULES
What must not appear.

Avoid bloated synonym chains. Each phrase should control a visible feature.

---

## Background Discipline

A common failure is equal-detail rendering.

Correct it by specifying:
- focal face sharpest;
- foreground selectively sharp;
- immediate set readable;
- distant background simplified;
- atmospheric separation;
- abstract or painterly suggestion where appropriate.

---

## Variation Rule

When asked for a "different scene" do not only change props.

Change at least four of:
- location topology;
- camera grammar;
- palette relationship;
- lighting source;
- environmental motion;
- blocking;
- focal length;
- action axis;
- silhouette design;
- dominant material.

Preserve character identity while changing cinematic language.

---

## Image-to-Video Preparation

Before animating, verify the still frame has:
- correct identity;
- physically usable poses;
- visible hands where required;
- stable prop geometry;
- no impossible overlaps;
- clear foreground/midground/background;
- room for intended camera motion;
- clothing/hair elements that can react naturally;
- no unintended background characters.

If the still is weak, regenerate the still. Do not ask motion generation to fix broken production design.

---

---

## Hero Character Sheet Gold Standard

When the user asks to build a hero or recurring principal character, treat the character sheet as a production asset, not an illustration.

### Mandatory Full-Body Rule
If a turnaround is requested:
- explicitly say **FULL-BODY**;
- explicitly say **head to feet**;
- explicitly prohibit cropped legs or feet;
- allocate the majority of the sheet to full-body views;
- keep close-ups secondary.

Recommended layout:
1. full-body front;
2. full-body 3/4 front;
3. full-body side;
4. full-body back;
5. full-body action or personality pose;
6. small expression close-ups.

For important hero sheets, use a target such as:
> At least 70% of the sheet must be full-body views. Feet fully visible.

### Character Definition Order

Write identity information in this order:

1. **Role / age / cultural context**
2. **Body build and height relationship**
3. **Skin**
4. **Face**
5. **Hair**
6. **Wardrobe**
7. **Props**
8. **Expression/personality**
9. **Sheet layout**
10. **Lighting**
11. **Background**
12. **Consistency lock**
13. **Negative rules**
14. **Aspect ratio / output class**

This order reduces identity drift.

### Skin-Tone Precision

If complexion is visually critical, do not use one vague adjective.

Define:
- relative brightness;
- undertone;
- surface quality;
- consistency across views;
- explicit exclusions when the model frequently drifts.

Example pattern:

```text
SKIN:
[brightness level] [regional/contextual descriptor] skin with a [undertone].
Keep the complexion visually consistent in every view.
Do not shift the character darker, lighter, tanner, redder, or greyer between panels.
```

Use exclusions only when needed for stability. Avoid contradictory complexion language.

### Eye Design

For stylized cinematic characters:
- define eye color;
- relative size;
- shape;
- expressiveness;
- prohibit unintended anime exaggeration when relevant.

Example:
> Large expressive hazel eyes, striking but anatomically grounded, not anime-proportioned.

### Hair Lock

Hair is one of the highest-risk continuity features.

State:
- color;
- texture;
- length;
- exact hairstyle;
- exact number of braids/ponytails/buns;
- accessories and count;
- no hairstyle changes between views.

For critical repeated features, use exact language:
> EXACTLY TWO braids. Each braid ends with ONE bow. No extra braids. No missing bows.

### Wardrobe Lock

Describe:
- category;
- main color;
- sleeve length;
- hem length;
- silhouette;
- base fabric;
- overlay fabric;
- footwear;
- modesty/age suitability if relevant;
- practicality;
- what the wardrobe must NOT become.

Avoid merely saying "beautiful outfit." Give construction logic.

### Prop Lock

For signature props:
- state whether it is held, worn, pocketed, or attached;
- keep scale consistent;
- keep material/color stable;
- do not let it appear/disappear randomly.

### Expression Design

Use expression close-ups to encode personality, not only emotion.

Good recurring expression types:
- suspicious squint;
- warm smile;
- confident deduction;
- worried concentration;
- stubborn refusal;
- quiet amusement.

### Lighting for Character Sheets

Use one controlled studio lighting grammar across all panels.

Example:
- warm key;
- cooler shadow fill;
- subtle rim;
- no dramatic lighting change panel-to-panel.

### Background for Character Sheets

Use a simple textured concept-sheet background that supports silhouette readability.

Avoid:
- detailed environments;
- random props;
- different locations per panel;
- strong background contrast behind one view only.

### Consistency Block

Always include a dedicated consistency paragraph:

```text
CONSISTENCY:
Same skin tone, same eye color, same face, same hairstyle, same accessories,
same costume, same body proportions and same height relationship in every view.
```

### Negative Block

Negative constraints should target known failure modes, not become a random vocabulary dump.

Useful categories:
- wrong complexion;
- eye drift;
- hair drift;
- missing/extra accessories;
- adult anatomy on children;
- cropped feet;
- costume redesign;
- excessive glamorization;
- photorealism when unwanted;
- glossy CGI;
- generic anime / generic cartoon;
- unwanted text.

### Hero Sheet Output Contract

A production-ready hero prompt should contain:
- exact subject lock;
- full-body requirement;
- physical design;
- facial design;
- hair lock;
- wardrobe construction;
- prop lock;
- view list;
- expression list;
- lighting;
- background;
- consistency block;
- negative block;
- aspect ratio/output class.

The sheet should be useful for later image-to-video reference, not merely attractive.


## Agent Output Contract

When this skill is invoked, return:

1. **Source locks**
2. **Visual world block**
3. **Character locks**
4. **Environment block**
5. **Keyframe prompt**
6. **Negative prompt / failure prevention**
7. **References required for generation**
8. **Continuity notes for the next shot**

If the user asks only for the final prompt, provide the prompt without unnecessary explanation.

---

## Quality Gate

Reject a generated design if any of these fail:
- character identity;
- costume continuity;
- prop continuity;
- scale;
- hand anatomy;
- world logic;
- focal hierarchy;
- lighting logic;
- background discipline;
- requested style language.

Do not approve an attractive image that breaks continuity.

---

## Compact Reusable Prompt Skeleton

```text
[CHARACTER / SUBJECT LOCK]

[LOCATION + MATERIAL + ERA LOGIC]

[NARRATIVE MOMENT]

[CAMERA + COMPOSITION + DEPTH]

[LIGHTING + PALETTE]

[RENDERING LANGUAGE + TEXTURE + EDGE BEHAVIOR]

Preserve exact approved identity, proportions, costume, recurring props and scale.
Keep focal detail concentrated on the subject; simplify distant background detail.

Avoid: identity drift, costume mutation, extra characters, glossy CGI surfaces,
generic anime treatment, photorealism when not requested, malformed hands,
floating props, random text, inconsistent scale.
```

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
