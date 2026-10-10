---
name: painterly-short-film
description: "Guide production of a painterly (Arcane-style 2.5D) animated short film in Higgsfield Seedance: project setup, character assets, IDENTITY LOCK, scene prompts, continuity and review. Use when starting a new painterly short film, when the user asks for a short film in this style, or for @tag / @composition / IDENTITY LOCK questions."
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# SKILL: PAINTERLY SHORT FILM PRODUCTION
**Trigger:** Any new animated/painterly short film project using Higgsfield Seedance
**Load with:** your Seedance / Higgsfield prompt-writing skill

---

## WHAT THIS SKILL DOES

Guides production of painterly animated short films using Higgsfield Seedance and the Arcane Netflix 2.5D visual language. Covers: character asset building → IDENTITY LOCK creation → scene prompt engineering → continuity management → review and iteration.

---

## WHEN TO USE

Load this skill when the user:
- Starts a new animated/painterly short film project
- Asks to "make a painterly animated short film in this style"
- Wants to generate video with Higgsfield Seedance for a story with multiple characters
- Needs to build character consistency across multiple clips
- Asks about @tag system, @composition references, or IDENTITY LOCK blocks

---

## STEP 1 — PROJECT SETUP (before any generation)

### 1A. Create folder structure
```
projects/[project-slug]/
  README.md
  HANDOFF_PROMPT.md
  01_story/
  02_characters/
    references/           ← approved character reference images
  03_visual_bible/
  04_assets/
  05_storyboards/
  06_shot_list/
  07_video_prompts/
  Master Assets/          ← named: F01.png, M01.png, D01.png, etc.
  Production/             ← clip_01.mp4, clip_01b.mp4, clip_01_APPROVED.mp4
  _archive/
```

### 1B. Lock the visual style
Choose ONE style target and lock it. Do not mix styles.

**Arcane Netflix 2.5D (recommended default):**
- Fortiche Production quality
- Bold brushstrokes, sculpted facial planes
- Dominant palette: amber-gold + jewel teal accents
- NOT Pixar, NOT anime, NOT 3D CGI
- Prompt opener: `Arcane Netflix 2.5D painterly style. Warm amber-gold dominant palette, jewel teal accents. 16:9 cinematic ratio.`

---

## STEP 2 — CHARACTER ASSET BUILDING

### 2A. Generate character sheet images FIRST
Before any video, generate a 5-view character sheet for each character.

**Character sheet prompt template:**
```
Arcane Netflix 2.5D painterly style. Character sheet — 5 views:
front, 3/4 left, side, back, face close-up. Neutral warm background.

SUBJECT: [Character description — age, skin tone, key features]
COSTUME: [Detailed costume — every item, color, material]
[Modesty rules if applicable: hijab color + style, coverage requirements]
NO [prohibited items]. NO [prohibited items].

Arcane painterly quality. Bold brushstrokes. Warm amber-gold lighting from below-right.
```

### 2B. Write IDENTITY LOCK block for each character
```
IDENTITY LOCK — @[tag]: [skin tone]. [hair description — CURLY/straight/etc].
[beard/no beard]. [eye color]. [full costume description — every item + color].
[special rule: BARE HANDS / HAT STAYS ON / NO hijab / etc.]
100% matches reference. Do NOT change: [list 2-3 most drift-prone features].
```

**Common drift prevention:**
- Hair texture/curl: always name it explicitly ("CURLY hair, tight to skull")
- Gloves appearing on hijabi characters: "BARE HANDS — ZERO GLOVES" in IDENTITY LOCK + "bare hand, fingers uncovered" inline in every shot where hands appear
- Extra head covering on characters without hijab: "NO hijab / NO head covering — ever"
- Hat disappearing: "[Color] [type] hat — HAT STAYS ON in every shot"
- Coat color shift: "Do NOT change coat color" explicitly named

---

## STEP 3 — SCENE PROMPT ARCHITECTURE

### Standard prompt structure:
```
Arcane Netflix 2.5D painterly style. Warm amber-gold dominant palette, jewel teal accents.
16:9 cinematic ratio. [X] seconds total. [N] hard cuts. No speed changes.
Tone: [emotional register of this scene].

IDENTITY LOCK — @char1: [description] 100% matches reference.
IDENTITY LOCK — @char2: [description] 100% matches reference.
[... one block per character in this scene]

═══════════════════════════════════════════════

[SHOT 1 — 0:00–0:0X] [SHOT NAME IN CAPS].
[Spatial blocking: who is where, exact screen positions if needed]
[Camera: position, height, angle, movement]
[Action: what happens, timing triggers]
[Detail: key visual elements to include]
CUT.

[SHOT 2 — ...]
CUT.

[SHOT N — ...]

═══════════════════════════════════════════════

AUDIO:
[Shot 1]: [ambient sounds + any flash/impact sounds]
[Shot 2]: [music cue + ambient]
[Shot N]: [resolution sound]

═══════════════════════════════════════════════

Upload order: @char1 FIRST · @char2 SECOND · @location LAST
```

### Shot naming conventions:
Name shots with dramatic titles in caps: `[SHOT 1 — 0:00–0:03] THE AMBUSH.`
This helps Seedance understand the emotional register of each moment.

---

## STEP 4 — MULTI-CHARACTER CONSISTENCY

### 4+ characters in one shot: @composition reference required
1. Generate a STILL IMAGE showing all characters in correct positions on location
2. Upload this still as an additional @reference (last in upload order)
3. Reference it as `@composition` in the IDENTITY LOCK section

### Screen position language:
- Use both physical description AND screen coordinates
- Physical first: "stands left of @father, one step forward"
- Then coordinates: "Screen position: x ~38%"
- Screen X: 0% = far left, 50% = center, 100% = far right

### Upload order rule:
- Main characters first (in order of narrative importance)
- Secondary characters next
- Location/environment reference last
- @composition reference last of all

---

## STEP 5 — DIFFICULT SHOTS

### Color-to-B&W transition (e.g., photo being taken):
Seedance cannot reliably do color→B&W in one clip. Solutions:
- **Option A:** Generate B&W shot as a SEPARATE clip, cut in post
- **Option B:** Generate a B&W still image separately, cut to it
- **Option C:** Write B&W as its own shot with explicit language in BOTH the transition shot AND the result shot

If attempting in one clip: state "NOW IN B&W silver-gelatin tones — NO COLOR anywhere" AND "The image is entirely sepia" in the same shot description. Repetition is required.

### Elderly/aged character without reference:
Do not attempt to generate an aged character's face without a reference. Instead:
- Show only HANDS (aged hands = wrinkles + ring + skin texture)
- No face visible
- This avoids character drift entirely and is more cinematic

### Flash/lighting events:
"A BRILLIANT WHITE FLASH fires FROM [direction] toward [subjects]" — specify direction explicitly relative to where the camera is.

---

## STEP 6 — REVIEW CRITERIA

After each generation, assess:
1. **Character drift** — does each character match their reference?
2. **Prohibited elements** — gloves on bare-handed characters? Wrong head covering?
3. **Spatial logic** — does the camera position make narrative sense?
4. **Timing** — do the cuts happen at the right moments?
5. **Emotional register** — does the scene feel right (warm, funny, tense)?

### Common fixes:
| Problem | Fix |
|---|---|
| Gloves appeared | Add "BARE HANDS" to IDENTITY LOCK + "bare hand, fingers uncovered" inline |
| Character missing from group shot | Add @composition reference image |
| Hair texture changed | Add "Do NOT change: hair curl/wave/texture" to IDENTITY LOCK |
| Camera position illogical | Rewrite camera placement with physical distance + height + angle |
| B&W not working | Generate as separate clip |
| Photo in hands is color not sepia | State "SEPIA — NO COLOR" twice in same shot description |

---

## SESSIONS LOG TEMPLATE

Add to your project memory.md after each project:
```
| [Date] | [Project] | [What was built] | [Key lessons learned] |
```

---

## SKILL ACTIVATION CHECKLIST

Before starting any new painterly short film session:
- [ ] Load your Seedance / Higgsfield prompt-writing skill
- [ ] Read project HANDOFF_PROMPT.md
- [ ] Confirm character references uploaded to Higgsfield
- [ ] Review IDENTITY LOCK blocks for all characters in this scene
- [ ] Check upload order before generating

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
