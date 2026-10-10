# Contributing to Refay Skills

Thanks for wanting to add a skill. This repo is a curated collection of free, open-source AI agent skills, so every contribution goes through the same format and quality bar. The formal specification lives in [docs/SKILL-STANDARD.md](docs/SKILL-STANDARD.md) — this file is the practical checklist.

---

## 1. Skill format standard

Every `SKILL.md` starts with YAML frontmatter. These five fields are required and must appear **first, in this exact order**:

| # | Field | Required | Notes |
| :-- | :--- | :--- | :--- |
| 1 | `name` | yes | kebab-case, matches the folder name |
| 2 | `description` | yes | what it does + when to use it + trigger phrases |
| 3 | `author` | yes | `Khaled Al Refay` for this repo |
| 4 | `license` | yes | `CC-BY-4.0` |
| 5 | `source` | yes | canonical repository URL |

Any additional fields (e.g. `triggers`) are allowed **after** these five. Do not reorder, rename, or change the values of the required fields.

```yaml
---
name: my-new-skill
description: >-
  One or two sentences on what the skill does, followed by the situations and
  trigger phrases that should invoke it.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---
```

Multi-line `description` values written with `>-`, `|` or `>` are fine — keep the YAML valid and keep the text intact.

---

## 2. Folder layout

```
<category>/
└── my-new-skill/
    ├── SKILL.md          # required — the single entry point
    ├── references/       # optional — long-form docs loaded on demand
    ├── scripts/          # optional — helper scripts the skill runs
    ├── templates/        # optional — files the skill copies or fills in
    └── assets/           # optional — images, covers, sample media
```

Rules:

- **`SKILL.md` is the entry point.** Every skill folder must have one, and it must be at the root of the folder.
- Put long detail in `references/` and link to it from `SKILL.md` instead of bloating the entry point.
- Put reusable, runnable helpers in `scripts/`, fill-in-the-blank files in `templates/`, and media in `assets/`.
- Do not add a separate `README.md` inside a skill folder. `SKILL.md` is the only entry point agents and humans need. The one exception is a folder-level marketing README that GitHub renders when browsing — keep it in sync with `SKILL.md`.

---

## 3. Naming rules

- **Folders:** strictly `kebab-case` — lowercase words separated by single hyphens (`painterly-short-film`).
- **Files:** the entry point is exactly `SKILL.md`, uppercase. Supporting files use `kebab-case` too.
- **Skill names:** `name:` in frontmatter must equal the folder name.
- No spaces, no underscores, no `camelCase`, no version numbers in the folder name.

---

## 4. Quality checklist

Before opening a PR, confirm every box:

- [ ] Frontmatter has `name`, `description`, `author`, `license`, `source` first and in order; other fields come after.
- [ ] Folder and skill name are `kebab-case` and match.
- [ ] `SKILL.md` is the entry point and no stray `README.md` exists inside the skill folder.
- [ ] **No personal data** — no real names, emails, phone numbers, addresses, or private client details.
- [ ] **No company or brand data** — no proprietary brand names, product names, prices, market metrics, or internal documents. Generalise the method, strip the client.
- [ ] **No secrets** — no API keys, tokens, passwords, credentials, or private URLs.
- [ ] **Trigger phrases tested** — the description names the phrases a user would actually type, and you have confirmed the skill fires on them.
- [ ] **Clear steps** — the body is an ordered, executable process an agent can follow without guesswork.
- [ ] Attribution footer present **exactly once**, at the very end of the file:

```markdown
---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
```

- [ ] All relative links in the file resolve to paths that exist.

---

## 5. How to propose a new skill

1. **Open an issue first.** Use the issue to describe the skill, who it is for, the trigger phrases, and the outputs it produces. This avoids a PR that has to be redesigned.
2. **Wait for a go-ahead.** A maintainer will confirm the scope and the category (`cinematic`, `agent-fleet`, `vibe-coding`, or `marketing`).
3. **Add the skill.** Create `<category>/<skill-name>/SKILL.md` following the standard above, plus any optional `references/`, `scripts/`, `templates/`, or `assets/` folders.
4. **Self-review** against the quality checklist in section 4.
5. **Open the PR.** Include: the new skill, a one-line catalog entry for the category README, and a note for the changelog.
6. **Respond to review.** A maintainer will check format, naming, the absence of personal/company data and secrets, and that the attribution footer is present exactly once.

By contributing you agree your work is released under [CC BY 4.0](LICENSE).

---

*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
