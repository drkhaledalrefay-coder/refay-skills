---
name: painterly-action-choreography-engine
description: "Write fast, physically legible, continuity-safe AI-video action prompts — fights, chases, escapes, impacts, stunts, multi-shot action and image-to-video action. Use for 'action prompt', 'fight scene', 'chase sequence', 'choreograph this action', or any action shot in a painterly or cinematic AI film."
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Painterly Action Choreography Engine

## Purpose
A reusable agent skill for writing AI-video action prompts that are fast, cinematic, physically legible, and continuity-safe.

Use this skill for:
- fights;
- chases;
- escapes;
- physical comedy;
- impacts;
- stunt-like movement;
- multi-shot action sequences;
- image-to-video action prompting.

This skill is not tied to any specific franchise or project.

---

## Core Principle

AI action fails when the prompt asks for too many simultaneous actions without spatial logic.

Design action as:

**setup → attack → reaction → counter → environmental consequence → reset → decisive beat**

Even in a 10–15 second clip, movement must remain readable.

---

## Source-First Rule

Before writing action, inspect:

1. approved character references;
2. character physical limits;
3. costume and props;
4. location geometry;
5. visual style;
6. previous shot / next shot;
7. target video model;
8. requested runtime.

Do not redesign characters inside an action prompt.

---

## Character Lock Block

At the beginning of the prompt, lock:
- face;
- build;
- age;
- clothing;
- height difference;
- hairstyle;
- accessories;
- props.

Repeat only the critical identity rules later.

For children, braids, hijab, hats, glasses, scars, uniforms, and distinctive props, state exact continuity requirements explicitly when those features are prone to mutation.

---

## Fight Geography

Before choreography, establish:
- where each person starts;
- where walls/doors/tables/vehicles/obstacles are;
- escape direction;
- camera side;
- usable environmental objects;
- safe landing zones;
- final positions.

A viewer should understand who is where.

Avoid teleporting characters between cuts.

---

## Action Grammar

### One Primary Action Per Beat
Examples:
- punch;
- duck;
- block;
- shove;
- grab;
- pivot;
- throw;
- slide;
- vault;
- collide.

Secondary reactions can happen simultaneously:
- cloth snap;
- bag inertia;
- dust;
- head recoil;
- shoe scrape.

Do not stack five major actions into one sentence unless they form one continuous mechanical chain.

---

## Physical Causality

Every hit must show:

**wind-up → contact → recoil → consequence**

Add:
- foot pressure;
- hip rotation;
- shoulder rotation;
- balance shift;
- cloth lag;
- hair lag;
- prop inertia;
- surface response;
- dust/debris only where contact justifies it.

Never allow:
- floating bodies;
- weightless falls;
- weapons/props passing through bodies;
- impossible instant recovery;
- direction changes without planted feet or momentum transfer.

---

## Speed Without Confusion

"Fast" should come from editing and pose cadence, not from describing everything at once.

Use:
- whip cut;
- smash cut;
- snap zoom;
- fast lateral tracking;
- hard angle change;
- pose-to-pose acceleration;
- brief impact hold;
- smear transition;
- immediate counter.

Avoid slow motion unless explicitly requested.

For models that become confused by timestamps, write the sequence continuously without timecodes.

---

## Impact Design

A strong impact can combine:

### Body
- torso recoil;
- head snap;
- shoulder compression;
- knees buckling;
- grip failure.

### Costume
- sleeve tension;
- coat whip;
- scarf lag;
- bag swing.

### Environment
- plaster chip;
- dust burst;
- table collapse;
- water vibration;
- loose objects jumping.

### Camera
- micro jolt;
- abrupt stop;
- fast reframing.

### Graphic Frame
When appropriate:
- one-frame silhouette flash;
- negative-space flash;
- radial line burst;
- chromatic offset;
- ink slash;
- posterized contrast.

Use graphic impact frames sparingly so they remain meaningful.

---

## Camera Design

Choose a camera grammar appropriate to the action.

### Chase
- ground-skimming wide;
- retreating camera;
- overhead tracking;
- compressed telephoto pursuit.

### Hand-to-Hand
- side wide for readability;
- low medium for force;
- tight insert for hands/feet;
- occasional Dutch angle for instability.

### Decisive Hit
- snap zoom;
- locked side profile;
- impact insert;
- immediate cut to consequence.

### Comedy Button
After high kinetic density:
- stabilize the camera;
- reduce score;
- hold a clean medium shot;
- deliver the reaction.

Contrast creates comedy.

---

## Editing Rhythm

Use a repeating pattern:

**wide geography → medium exchange → insert detail → wide consequence**

Do not remain in extreme close-up for the whole fight.

Action readability beats visual chaos.

---

## Environment as Choreography

Use location-specific objects so each fight feels unique.

Examples:
- laundry lines;
- stair rails;
- doors;
- tables;
- cables;
- water tanks;
- market awnings;
- parked vehicles;
- sand;
- rain;
- scaffolding;
- curtains;
- chairs;
- rolling shutters.

The environment should alter movement rather than merely decorate the background.

---

## Differentiation Rule

When asked to make a fight "completely different," change at least five:

- location;
- terrain;
- verticality;
- camera grammar;
- dominant color;
- animation finish;
- weapon/prop logic;
- environmental interaction;
- chase direction;
- final gag;
- music language;
- shot scale pattern.

Do not recycle the same wall slam / same angle / same final hit unless requested.

---

## Child Action / Comedy Handling

When a child participates:
- keep body scale and reach believable;
- use an age-appropriate lightweight object if any;
- show two-handed effort where appropriate;
- plant feet before a strong swing;
- preserve the child’s small scale relative to adults;
- use reaction/comedy rather than portraying the child as superhuman.

The adult action can remain intense while the child's decisive beat is stylized and non-graphic.

---

## Sound Design Layer

Write audio as a separate production layer.

### Rhythm
Synchronize:
- footsteps;
- blocks;
- impacts;
- cuts;
- environmental collisions.

### Foley
Use:
- breath;
- shoe scrape;
- fabric snap;
- grip;
- metal vibration;
- debris;
- surface contact.

### Score
Choose a musical identity that matches the new sequence rather than copying the prior scene.

### Silence
A single beat of silence before a decisive action can make the return hit feel much larger.

Drop music before dialogue when clarity matters.

---

## Image-to-Video Motion Prompt Rule

If a strong source image already defines character, location, palette and lighting, the motion prompt should emphasize:

- performance;
- action mechanics;
- camera;
- environmental reaction;
- timing;
- physics.

Do not waste prompt budget redescribing every visible element.

---

## Continuous Prompt Architecture

For models that respond poorly to timestamps, structure the final prompt as continuous prose in this order:

1. runtime and overall action intent;
2. character lock;
3. location;
4. visual/animation language;
5. opening motion already underway;
6. first exchange;
7. escalation;
8. environmental interaction;
9. decisive action;
10. aftermath;
11. comedy/reaction button;
12. music and sound;
13. hard constraints.

Use transition phrases:
- `SMASH CUT`
- `WHIP CUT`
- `HARD CUT`
- `SNAP ZOOM`
- `CUT TO`
- `IMMEDIATE HARD CUT TO BLACK`

These function as editorial punctuation without timestamping the model.

---

## Negative Rules

Unless the project says otherwise, prevent:
- extra people;
- blood/gore;
- random weapons;
- superpowers;
- costume mutation;
- face drift;
- hairstyle drift;
- height changes;
- prop clipping;
- floating props;
- teleportation;
- slow motion;
- unreadable motion blur;
- duplicated limbs;
- missing hands;
- subtitles;
- random text.

---

---

## Gold-Standard High-Energy Fight Prompt Rules

For a premium short fight, the final prompt should feel like a compact stunt plan plus editorial plan plus sound map.

### Start Mid-Action

Do not waste the opening on preparation.

Prefer:
> The first frame is already mid-action.

The audience should immediately see:
- chase;
- impact;
- attack;
- evasive movement;
- or an imminent collision.

### Precise Camera Language

When useful, specify concrete lens/angle behavior:
- ground-skimming ultra-wide;
- low Dutch tilt;
- side wide;
- telephoto insert;
- overhead plunge;
- snap-zoom;
- whip-pan;
- retreating chase camera.

Numerical lens values may be used when the target model responds well to them, but do not overload the prompt with camera mathematics.

### Escalation

The exchange should become harder, not merely longer.

A strong progression:
1. pursuit or first collision;
2. fast exchange;
3. harder block/counter;
4. grapple or environmental collision;
5. apparent final attack;
6. decisive interruption;
7. physical aftermath;
8. reaction/comedy button.

### Even-Match Rule

If the scene is supposed to feel dangerous:
- both sides must land or nearly land meaningful actions;
- one fighter should not dominate every beat;
- defensive actions must cost effort;
- counters should arise from prior momentum.

### Pose-to-Pose Cadence

For stylized high-energy animation, describe:
- explosive acceleration;
- very short impact holds;
- smear frames between selected strikes;
- instant counters;
- abrupt recovery poses.

If the generator understands animation timing, brief 3–4 frame impact holds can be specified.
If it does not, translate this into:
> a momentary hard pose hold at contact before motion snaps forward again.

### Real-Speed Rule

Unless slow motion is narratively necessary:
> Real speed only. No slow motion.

This avoids models turning every impact into floaty cinematic slow motion.

### Readable Violence

To keep action intense without graphic gore:
- use torso recoil;
- limb compression;
- wall/plaster damage;
- shoe skid;
- cloth snap;
- breath loss;
- stagger;
- collapse;
- pinned wrist / controlled aftermath.

Intensity comes from force and consequence, not blood.

### Decisive Prop Hit

When an improvised object ends the fight:
- establish the object earlier;
- show the character physically grabbing it;
- show planted feet;
- show whole-body rotation;
- specify exact contact location;
- specify the object's vibration/rebound afterward;
- forbid floating and clipping.

### One-Frame Graphic Impact

For stylized hybrid animation, a single impact frame can use:
- high-contrast silhouettes;
- one accent flash;
- radial speed lines;
- print/ink texture if the chosen visual language supports it;
- slight chromatic separation;
- silhouette distortion.

Keep it to one decisive beat. Do not make every hit a graphic splash frame.

### Music as Edit Architecture

The score should be designed with the cut.

Useful structure:
- music from first frame;
- constant rhythmic pressure;
- each major impact on a beat;
- one deliberate silence before the decisive action;
- full score return on the decisive hit;
- music drops before dialogue.

Do not merely request "epic music." Define:
- percussion language;
- bass character;
- string/synth role;
- regional melodic influence if appropriate;
- drop behavior;
- silence behavior.

### Sound Design Layer

Explicitly layer:
- breathing;
- grunts;
- footsteps;
- blocks;
- wall impacts;
- cloth snaps;
- shoe scrapes;
- debris;
- air whooshes;
- metal resonance;
- environmental reverb.

The decisive impact sound should be timed to the strongest musical accent.

### Dialogue Button

After the fight:
- hard cut to stable camera;
- stop or sharply reduce music;
- let breathing and location ambience remain;
- use one short exchange;
- hard cut to black.

Keep dialogue short enough that the action remains the dominant event.

### Identity Continuity at Every Cut

For short multi-cut generations, state:

```text
Faces, proportions, clothing, hairstyle, accessories and height relationships
stay identical across every cut.
```

For fragile details, repeat the exact constraint:
> exactly two braids; exactly two bows.

### Negative Action Constraints

Useful final constraints:
- no extra characters;
- no random text;
- no subtitles;
- no blood unless explicitly requested;
- no guns/knives unless story-required;
- no superpowers unless story-required;
- no face drift;
- no costume mutation;
- no extra limbs;
- no prop clipping;
- no floating props;
- no teleporting;
- no accidental slow motion.


## Agent Output Contract

When invoked, return:

1. **Character locks**
2. **Location geometry**
3. **Action logic**
4. **Camera/edit grammar**
5. **Continuous final video prompt**
6. **Music/SFX layer**
7. **Negative constraints**
8. **Continuity risks**

If the user asks for "prompt only," output only the final generation prompt.

---

## Quality Gate

Before delivering, verify:

- Can every major action be physically traced?
- Does each cut preserve geography?
- Are both fighters' positions understandable?
- Does every hit have a visible consequence?
- Are height/proportion differences preserved?
- Are props physically connected to hands and surfaces?
- Is the location actually used?
- Is the new fight sufficiently different from prior fights?
- Does the comedy occur after, not during, the dangerous exchange?
- Are music and SFX supporting the edit rather than replacing action logic?

---

## Compact Prompt Skeleton

```text
Create a [runtime] fast, readable, physically grounded animated action sequence.

CHARACTER LOCK:
[exact identities, proportions, costumes, height relationships, recurring props]

LOCATION:
[geometry, obstacles, surfaces, environmental motion]

VISUAL LANGUAGE:
[animation finish, shadows, edge treatment, impact language]

The first frame is already in motion.
[continuous action chain written as physical cause-and-effect]

[editorial transition]
[next exchange]

[environment interaction]

[decisive action]

[aftermath and stable reaction/comedy button]

MUSIC / SFX:
[rhythm, score identity, synchronized impacts, silence beat, dialogue space]

CONSTRAINTS:
No identity drift, no extra characters, no teleportation, no floating objects,
no prop clipping, no unreadable motion, no unwanted slow motion, no random text.
```

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
