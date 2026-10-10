# The SKILL.md Standard

The formal specification for an AI agent skill in this repository. If you are contributing, read this together with [CONTRIBUTING.md](../CONTRIBUTING.md).

A skill is a folder whose entry point is a single `SKILL.md` file. An AI agent loads that file when the user's request matches the skill's description, then follows the instructions inside it. Everything else in the folder exists only to support that file.

---

## 1. File and folder rules

| Rule | Requirement |
| :--- | :--- |
| Entry point | `SKILL.md`, uppercase, at the root of the skill folder |
| Skill folder | `kebab-case`, must equal the `name` field |
| Category | The skill lives under one of `cinematic/`, `agent-fleet/`, `vibe-coding/`, `marketing/` |
| Encoding | UTF-8 |
| Extra READMEs | Not allowed inside a skill folder — `SKILL.md` is the only entry point |

---

## 2. Frontmatter schema

Every `SKILL.md` opens with a YAML frontmatter block delimited by `---`. These five fields are required, and they must appear **first, in the order below**. Additional fields may follow them.

| Field | Required | Example |
| :--- | :--- | :--- |
| `name` | yes | `painterly-short-film` |
| `description` | yes | `Guide production of a painterly animated short film in Higgsfield Seedance. Use when starting a new painterly short film or asking about @tag, @composition or IDENTITY LOCK.` |
| `author` | yes | `Khaled Al Refay` |
| `license` | yes | `CC-BY-4.0` |
| `source` | yes | `https://github.com/drkhaledalrefay-coder` |

Example block:

```yaml
---
name: painterly-short-film
description: >-
  Guide production of a painterly (Arcane-style 2.5D) animated short film in
  Higgsfield Seedance: project setup, character assets, IDENTITY LOCK, scene
  prompts, continuity and review.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---
```

Field values must not be changed once a skill is published. Multi-line descriptions written with `>-`, `|` or `>` are valid — keep the YAML parseable and the prose intact.

---

## 3. Writing the `description`

The `description` is the single most important line in the skill: it is the trigger the agent matches against. Write it to answer three questions, in this order.

1. **What does it do?** Lead with the capability in plain language.
   > *"Write fast, physically legible, continuity-safe AI-video action prompts."*
2. **When should it be used?** Name the situations, contexts, and file types.
   > *"…for fights, chases, escapes, impacts, stunts, multi-shot action and image-to-video action."*
3. **Which trigger phrases invoke it?** Quote the literal words a user would type.
   > *"'action prompt', 'fight scene', 'chase sequence', 'choreograph this action'."*

Guidelines:

- **Third person, imperative, no fluff.** Describe the skill, do not address the reader.
- **Front-load the trigger.** Agents weight the opening words most heavily.
- **Be concrete.** "Plan a TikTok content calendar" beats "help with marketing".
- **State the boundary.** If the skill must *not* fire in some cases, say so (e.g. "Never use to trigger generation").
- **Keep it tight.** One paragraph, roughly 2–6 sentences or a short bulleted `>-` block.
- **Test the phrasing.** If a user would not say it, it is not a trigger phrase.

---

## 4. Body structure

After the frontmatter, structure the body so an agent can execute it without guessing:

1. **Title and one-line summary** — `# Skill Name` followed by the outcome, in the user's language.
2. **When to use / when not to use** — explicit boundaries, including what to hand off to a different skill.
3. **Prerequisites** — files, access, tools, or context the skill expects.
4. **Steps** — an ordered list. One action per step, in the order it must happen. Prefer imperative verbs.
5. **Outputs** — exactly what the skill produces (a prompt set, a report, a deck, a checklist).
6. **Rules and constraints** — non-negotiables: what to never do, what to always verify, safety and approval gates.
7. **References** — links to files in `references/`, `scripts/`, `templates/` or `assets/` when detail is needed.
8. **Attribution footer** — see section 6.

Keep the body focused on the workflow. Push long tables, rubrics and background material into `references/` so the entry point stays scannable.

---

## 5. `references/`, `scripts/`, `templates/` and `assets/`

Optional support folders — add them only when the skill needs them.

| Folder | Use for | Rules |
| :--- | :--- | :--- |
| `references/` | Long-form knowledge loaded on demand — rubrics, deep guides, lessons learned | One topic per file, `kebab-case` names, linked from `SKILL.md` |
| `scripts/` | Runnable helpers the skill executes | Self-contained, documented at the top, no credentials or secrets, no destructive defaults |
| `templates/` | Files the skill copies or fills in | Placeholders clearly marked |
| `assets/` | Images, covers, sample media | Referenced with relative paths |

Rules that apply to all of them:

- **Link every support file from `SKILL.md`**, otherwise it will never be loaded.
- **Never include secrets**, private URLs, credentials, or personal/company data.
- **Keep paths relative** to the skill folder.
- **Do not duplicate `SKILL.md` content** into a reference file; references extend it.

---

## 6. Attribution footer

Every `SKILL.md` ends with this footer, **exactly once**, as the final content in the file:

```markdown
---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
```

Reproduce it byte-for-byte, including the horizontal rule above it. Do not add a second copy, translate it, or place it anywhere other than the end of the file.

---

*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
