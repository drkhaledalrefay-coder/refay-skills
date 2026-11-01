# Worked example — seven Seedance 2.0 Mini shots

Settings that shipped: 16:9, 720p, 8 s, audio on, Mini, start image = the shot keyframe, references = girl sheet and (except V1) kitten sheet.

Speech warning: the AUDIO blocks below include the Arabic lines that were submitted. The comparison found **no Arabic speech** in the Mini clips. For a new generation, replace the spoken line with silence or English. The picture direction stays.

Seedream stills (generate in order, 16:9):

**Girl sheet**

```
Character design sheet, widescreen 16:9. Premium hand-painted Japanese animated feature-film aesthetic, soft painted textures, warm natural daylight. Character: Ruqayya, a cute 7-year-old Egyptian girl, round face, big warm brown eyes, dark brown hair in two braids with small red hair ties, yellow T-shirt, blue denim overalls, small brown leather crossbody satchel, white sneakers. Front view, side view and back view of the same character standing, plus one close-up of her gently smiling face. Plain warm cream paper background. No text.
```

**Kitten sheet**

```
Animal character design sheet, widescreen 16:9, premium hand-painted Japanese animated feature-film aesthetic. Character: a tiny orange tabby kitten with white paws and a white chest, big green eyes, thin and tired. Show: front view sitting, side view walking, a close-up of its face looking thirsty and weak, and a close-up of it happy and drinking from a small bowl. Plain warm cream paper background. No text.
```

**Keyframe suffix (add to every keyframe):** Premium hand-painted Japanese animated feature-film aesthetic, widescreen 16:9, Egyptian countryside village: dusty stone path, low mud-brick wall, palm trees, green fields, distant mountains. No text.

| Keyframe | Prompt body |
|---|---|
| K1 | Very hot summer noon, harsh bright sun, heat shimmer. Wide shot: Ruqayya walks home along the path toward the camera, small in the frame, wiping her forehead with the back of her hand, holding a blue water bottle. |
| K2 | Hot noon, strong sun with soft shade. Medium shot at eye level: Ruqayya kneels in the shade of the mud-brick wall, concerned, looking at the tiny thin orange kitten lying tired in the shade with its mouth open. |
| K3 | Ground-level close-up in the shade of the wall: the thin orange kitten lies weak and gentle, panting softly, eyes half closed, sad and tired; Ruqayya's hand gently strokes its head from the side. |
| K4 | Medium close-up: Ruqayya kneels by the wall holding her blue water bottle in both hands, looking down at it, hot and thirsty herself, a drop of sweat on her forehead, hesitating; the kitten small and soft-focus in the foreground. |
| K5 | Ruqayya kneels by the wall, the small plastic lid of her lunchbox on the ground in front of the kitten; she pours water from her blue bottle into the lid, a clear sparkling stream; the kitten lifts its head toward the water. |
| K6 | Low eye-level shot: the orange kitten drinks happily from the lunchbox lid, little pink tongue lapping; Ruqayya kneels beside it, smiling with relief, gently stroking its back. |
| K7 | Warm late-afternoon light, gentle breeze moving the palm leaves. Wide shot: Ruqayya walks home along the path with her satchel, looking back over her shoulder and laughing, as the happy kitten trots after her. |

The Mini batch did not have a separate K3 start image. V3 used an alternate K2 still. Prefer a real K3 still when you regenerate.

---

### V1 hot noon (refs: @image1 only)

```
SCENE CONTEXT
A hot summer noon in an Egyptian countryside village. A little girl walks home alone along a dusty path between a low mud-brick wall (camera left) and green fields (camera right).

ACTIVE REFERENCES
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids with red ties, yellow T-shirt, blue denim overalls, brown crossbody satchel, white sneakers, blue water bottle in her right hand. 100% matches the reference.

LOCATION MAP
Foreground: sun-baked stone path. Midground: Ruqayya walking toward camera. Background: palm trees, fields, distant mountains, bright sky. Sun high and behind-right of camera.

FIRST FRAME / BLOCKING
Wide shot, Ruqayya small in the center of the path, walking toward camera, already in motion.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
WS at 47°, gentle depth, painted-animation clarity.

CAMERA
Eye-level, slow dolly-in toward her at 2 km/h, steady.

ACTION
Ruqayya walks slowly at 2 km/h, tired by the heat. At 3s she wipes her forehead with the back of her left hand and squints up at the sun. Palm leaves sway gently; heat shimmer rises off the path.

LIGHTING
Harsh overhead noon sun, 5600K, short hard shadows under her feet, bright bleached sky.

AUDIO
Cicadas buzzing, soft footsteps on dust, warm wind. No music, no speech.

STYLE
Premium hand-painted Japanese animated feature-film aesthetic, soft painted textures, clean line art, 2D animation.

POSITIVE LOCKS
Same girl, same outfit and braids for the whole shot. Water bottle stays in her right hand.
```

### V2 the kitten (@image1, @image2)

```
SCENE CONTEXT
Hot noon in an Egyptian village. Ruqayya kneels in the shade of a low mud-brick wall (camera left) and discovers a tiny thirsty kitten lying on the ground in front of her.

ACTIVE REFERENCES
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids, yellow T-shirt, blue denim overalls, brown satchel. Sweet child voice. 100% matches the reference.
@image2: tiny thin orange tabby kitten, white paws and chest, big green eyes. 100% matches the reference.

LOCATION MAP
Foreground: kitten lying in the wall's shade. Midground: Ruqayya kneeling, facing the kitten. Background: palm trees and fields in hard sunlight.

FIRST FRAME / BLOCKING
Medium shot, Ruqayya kneels camera right, kitten lies camera left in the shade, she looks down at it.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
MS at 47°, easing to MCU at 29°.

CAMERA
Eye-level with the girl, slow push-in at 1 km/h, then gently lowers toward the kitten's eye level.

ACTION
The kitten pants with its mouth open, lifts its head weakly and gives a tiny faint meow. Ruqayya's brows lift and draw together; she leans closer and whispers.

PERFORMANCE
Soft worried eyes, lips parted, she swallows once before speaking.

LIGHTING
Cool shade on the characters, hot 5600K sunlight in the background.

AUDIO
Cicadas, a faint weak meow. Ruqayya whispers in sweet, natural Egyptian Arabic: "يا حبيبتي... إنتي عطشانة؟"

STYLE
Premium hand-painted Japanese animated feature-film aesthetic, 2D animation.

POSITIVE LOCKS
Same girl and same kitten throughout. Kitten stays lying in the shade.
```

### V3 so thirsty

```
SCENE CONTEXT
Ground-level moment in the shade of a mud-brick wall: Ruqayya gently strokes a weak, thirsty kitten.

ACTIVE REFERENCES
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids, yellow T-shirt, denim overalls. Sweet child voice. 100% matches the reference.
@image2: thin orange tabby kitten, white paws and chest, green eyes. 100% matches the reference.

LOCATION MAP
Foreground: straw and dust on the ground. Midground: kitten lying on its side. Background: the textured mud-brick wall, warm and soft.

FIRST FRAME / BLOCKING
Low close-up of the kitten lying down, Ruqayya's hand entering from camera right touching its head.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
CU at 29°, shallow depth on the kitten.

CAMERA
Ground level, then a slow tilt-up at 1 km/h to Ruqayya's worried face in MCU.

ACTION
The kitten pants softly with its dry little mouth open, sad and weak, eyes half closed, then looks up at her. Her hand strokes its head slowly twice. Camera tilts up to her face; she whispers.

PERFORMANCE
Kitten: gentle, tired, ears relaxed. Ruqayya: eyes glossy, brows pinched upward.

LIGHTING
Soft warm shade, 4500K bounce off the wall, a thin rim of sun on the kitten's fur.

AUDIO
Cicadas, soft panting. Ruqayya whispers in sweet, natural Egyptian Arabic: "مسكينة... مفيش ميه خالص"

STYLE
Premium hand-painted Japanese animated feature-film aesthetic, 2D animation.

POSITIVE LOCKS
Kitten looks sad and weak with a soft gentle face. Same girl and kitten as the references.
```

### V4 the choice

```
SCENE CONTEXT
Ruqayya kneels by a mud-brick wall in the noon heat holding her own water bottle, torn between her thirst and the thirsty kitten in front of her.

ACTIVE REFERENCES
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids, yellow T-shirt, denim overalls, brown satchel, blue water bottle in both hands. Sweet child voice. 100% matches the reference.
@image2: tiny orange tabby kitten, soft-focus in the foreground. 100% matches the reference.

LOCATION MAP
Foreground: kitten soft-focus, camera left. Midground: Ruqayya kneeling. Background: sunlit cracked wall.

FIRST FRAME / BLOCKING
MCU of Ruqayya holding the bottle at chest height, looking down at it.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
MCU at 29°, background softened.

CAMERA
Eye-level, slow push-in at 1 km/h toward her face.

ACTION
A drop of sweat runs down her forehead; she swallows and looks at the bottle, hesitating, then whispers. At 5s she slowly looks toward the kitten; her eyes soften and a small determined smile appears.

PERFORMANCE
Dry lips, a slow breath out, the smile starting at the corners of her mouth.

LIGHTING
Warm noon light from camera right, 5200K, soft shade on her face.

AUDIO
Cicadas, a soft pause. Ruqayya whispers in sweet, natural Egyptian Arabic: "وأنا كمان عطشانة..."

STYLE
Premium hand-painted Japanese animated feature-film aesthetic, 2D animation.

POSITIVE LOCKS
Bottle stays in both hands, closed. Same girl as the reference.
```

### V5 sharing

```
SCENE CONTEXT
By a mud-brick wall at noon, Ruqayya pours water from her bottle into her lunchbox lid for a thirsty kitten.

ACTIVE REFERENCES
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids, yellow T-shirt, denim overalls, brown satchel, blue water bottle. Sweet child voice. 100% matches the reference.
@image2: thin orange tabby kitten, white paws, green eyes. 100% matches the reference.

LOCATION MAP
Foreground: the small clear plastic lunchbox lid on the dusty ground. Midground: kitten camera left, Ruqayya kneeling camera right. Background: wall and palms.

FIRST FRAME / BLOCKING
MS, Ruqayya kneeling, the lid already on the ground in front of the kitten, bottle open in her hand.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
MS at 47°, then a slight push toward the lid.

CAMERA
Low eye-level, gentle push-in at 1 km/h toward the water.

ACTION
She tilts the bottle and pours a clear thin stream into the lid; the water sparkles in the sun and fills the lid. She whispers. The kitten lifts its head toward the water.

PHYSICS
Water stream bends with gravity, small splashes and ripples in the lid, droplets catch the light.

LIGHTING
Bright noon sun, 5600K, sparkle highlights on the water.

AUDIO
Cicadas, water pouring. Ruqayya whispers in sweet, natural Egyptian Arabic: "خدي... اشربي"

STYLE
Premium hand-painted Japanese animated feature-film aesthetic, 2D animation.

POSITIVE LOCKS
Water goes into the lid. Same girl and kitten as the references.
```

### V6 she drinks

```
SCENE CONTEXT
The kitten drinks from the lunchbox lid while Ruqayya kneels beside it, relieved and happy.

ACTIVE REFERENCES
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids, yellow T-shirt, denim overalls. Sweet child voice. 100% matches the reference.
@image2: orange tabby kitten, white paws and chest, green eyes. 100% matches the reference.

LOCATION MAP
Foreground: the water-filled lid. Midground: kitten drinking camera left, Ruqayya kneeling camera right. Background: wall shade and bright fields.

FIRST FRAME / BLOCKING
Low eye-level MS, kitten already lapping at the water, Ruqayya's hand on its back.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
MS at 47°.

CAMERA
Ground-level, gentle slow drift left to right at 1 km/h.

ACTION
The kitten laps eagerly, little pink tongue flicking, ears perking up. Ruqayya strokes its back with a huge relieved smile and speaks softly. At 6s the kitten looks up at her and gives a happy little meow.

PHYSICS
Small ripples in the lid with each lap, droplets on the kitten's whiskers.

LIGHTING
Warm noon light with soft shade, 5200K.

AUDIO
Soft lapping, cicadas. Ruqayya says softly in sweet, natural Egyptian Arabic: "الحمد لله". A happy meow.

STYLE
Premium hand-painted Japanese animated feature-film aesthetic, 2D animation.

POSITIVE LOCKS
Same girl and kitten as the references, kitten getting livelier through the shot.
```

### V7 walking home

```
SCENE CONTEXT
Late afternoon in the Egyptian village. Ruqayya walks home along the dusty path, and the happy kitten follows her.

ACTIVE REFERENCES
@image1: Ruqayya, 7-year-old Egyptian girl, two dark braids, yellow T-shirt, denim overalls, brown satchel. 100% matches the reference.
@image2: orange tabby kitten, lively, tail up. 100% matches the reference.

LOCATION MAP
Foreground: path. Midground: Ruqayya walking away camera right, kitten trotting behind her camera left. Background: palms, fields, village houses, warm sky.

FIRST FRAME / BLOCKING
WS, Ruqayya walking away along the path, kitten two steps behind her, both already moving.

FORMAT MODE
One continuous shot, the camera does not cut on its own.

OPTICS
WS at 47°, opening to EWS at 63°.

CAMERA
Slow crane-up and pull-back at 2 km/h revealing the peaceful village.

ACTION
Ruqayya walks at 3 km/h, looks back over her shoulder and laughs; the kitten trots after her with its tail up. A gentle breeze moves the palm leaves.

LIGHTING
Warm golden late-afternoon light from camera left, 3800K, long soft shadows.

AUDIO
Soft breeze, light footsteps, a playful meow. No music, no speech.

STYLE
Premium hand-painted Japanese animated feature-film aesthetic, 2D animation.

POSITIVE LOCKS
Same girl and kitten as the references, both walking in the same direction.
```
