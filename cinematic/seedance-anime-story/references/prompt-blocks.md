# Seedance blocks for this anime short

Source: the Seedance prompt method, narrowed to what the kitten film used. Do not add gear names, director names, or a style prefix above SCENE CONTEXT.

## Order

```
SCENE CONTEXT
ACTIVE REFERENCES
LOCATION MAP
FIRST FRAME / BLOCKING
FORMAT MODE
OPTICS
CAMERA
ACTION
PERFORMANCE
PHYSICS
LIGHTING
AUDIO
STYLE
POSITIVE LOCKS
```

Drop PERFORMANCE or PHYSICS when the shot has no acting beat or no liquid.

## What each block holds

**SCENE CONTEXT.** One or two sentences. Where, when, who, and which side of frame the wall or the path sits on.

**ACTIVE REFERENCES.**

```
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids, yellow T-shirt, blue denim overalls, brown satchel. 100% matches the reference.
@image2: tiny thin orange tabby kitten, white paws and chest, big green eyes. 100% matches the reference.
```

Add the blue bottle or the lunchbox lid only when that prop is in the shot. Add "Sweet child voice" only if the shot has a spoken line. Omit `@image2` when the kitten is absent (V1).

**LOCATION MAP.** Foreground, midground, background. Where the sun sits relative to the camera.

**FIRST FRAME / BLOCKING.** Who is where, already in motion if they walk. The first frame is not empty.

**FORMAT MODE.** `One continuous shot, the camera does not cut on its own.`

**OPTICS.** Abbreviation plus FOV degrees. Steps used here:

| FOV | Role on this film |
|---|---|
| 63° | Wider observation (V7 opens toward this) |
| 47° | Neutral human perspective (wides and mediums) |
| 29° | Portrait compression (close-ups and MCU) |

Shot sizes: CU face or kitten, MCU head and shoulders, MS about to the waist, WS full figure, EWS the village.

**CAMERA.** Height, move, speed in km/h. State it as operator behavior, not as a camera brand.

**ACTION.** What changes during the 8 seconds. Put a time on a beat when it matters (V1: at 3s she wipes her forehead; V4: at 5s she looks toward the kitten; V6: at 6s the kitten looks up).

**PERFORMANCE.** Muscle-level. Example from V4: dry lips, a slow breath out, the smile starting at the corners of her mouth.

**PHYSICS.** Only where something must obey weight. V5: the stream bends with gravity, small splashes, droplets catch the light. V6: ripples with each lap, droplets on the whiskers.

**LIGHTING.** Source, direction, kelvin. Noon shots used 5600K harsh sun or 5200K. Shade bounce on V3 was 4500K. V7 late afternoon was 3800K from camera left.

**AUDIO.** Ambience in English. Speech: either none, or English. The submitted Mini prompts contained Arabic lines; those lines did not produce Arabic speech. Do not repeat that if the goal is Arabic.

**STYLE.**

```
Premium hand-painted Japanese animated feature-film aesthetic, soft painted textures, clean line art, 2D animation.
```

**POSITIVE LOCKS.** Same girl and same kitten as the references. Name the prop state (bottle in the right hand, bottle in both hands and closed, water goes into the lid, kitten stays lying in the shade).

## Write the visible

"Worried" becomes: brows lift and draw together, she leans closer, lips parted, she swallows once. "Hot" becomes: she wipes her forehead, heat shimmer on the path, short hard shadows.

Left and right are from the camera.

## Tag rule

Reference image sets appearance. Text sets the action. Both are required. A long appearance paragraph fights the sheet. If the user names tags, use those names. If not, `@image1`, `@image2` in load order.
