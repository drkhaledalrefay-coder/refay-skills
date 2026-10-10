---
name: github-profile-builder
description: Build a professional GitHub profile page (profile README, sidebar bio, pinned repos) for anyone. Developers, and also non-developers who want GitHub to read like a polished LinkedIn page. Use when someone says "make my GitHub professional", "GitHub profile README", "set up my GitHub profile", "GitHub bio", or "pin my repos". Interviews the person, writes a README with verified badges and stats cards, and can publish it only after explicit approval.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# GitHub Profile Builder

Turn a GitHub account into a professional profile page. The page is the README in the special repo `<username>/<username>`, which GitHub shows at the top of the profile.

## Step 1: Gather facts (never invent)

1. Ask for the **GitHub username**, then read the public profile without logging in:
   `curl -s https://api.github.com/users/<username>` and
   `curl -s "https://api.github.com/users/<username>/repos?per_page=100"`.
   Note what's empty (name, bio, location, photo) and which repos are public.
2. Ask the questions below in **one** message. Skip anything already known from files the person shared or from their notes:
   - Full name, and how they want to be titled (one line)
   - **Positioning:** a developer looking for work, or a professional (non-developer) who wants a polished, LinkedIn-style page? This decides the tone. See Step 2.
   - Current role(s), employer (and whether it can be public), years of experience, location
   - 2–4 things they build or make. Projects can be private; describe them by what they do.
   - Tools they actually use (languages, frameworks, databases/cloud, platforms, creative or AI tools)
   - Contact links: LinkedIn, website, email (warn them the email becomes public), X, YouTube
3. If a fact is missing, leave it out or comment it out in HTML. **Never** guess a URL, a number or a skill.

## Step 2: Choose the voice

| Positioning | Header line | Emphasis |
|---|---|---|
| **Developer looking for work** | "Backend Engineer · Go · Distributed Systems" | Stack depth, public repos, stats cards, live demos |
| **Professional / non-developer** | "Pharmacist · Brand Manager · AI Solutions" | Domain expertise first, then "what I build/create", with projects described by outcome. Tools, not "languages I'm learning". |

For non-developers, never present them as a developer looking for work. Describe the work the way they'd describe it on LinkedIn: what they lead, what they build, and what they create.

## Step 3: Write the README

Use `template/README.md` and keep this section order:

1. **Hero:** centered name, one-line title, 2–3 identity badges, profile-views counter
2. **About Me:** 3–4 bullets (who I am · what I build · what I create/work on · current focus)
3. **Selected Work:** tables. Link public repos; mark private ones *(private)* and describe them by outcome. Add a creative/media table if relevant.
4. **Tech Stack & Tools:** four groups (Languages · Frameworks & Libraries/AI Tools · Databases & Cloud · Tools & Platforms). Use one badge style throughout (`for-the-badge`). Only list tools they really use; drop empty groups.
5. **GitHub Stats:** stats card, top-languages card, streak card (`tokyonight`, `hide_border=true`)
6. **Connect:** badge links. Comment out any link you don't have yet.

Rules:
- Don't include confidential numbers, client data or internal figures in the README.
- Badge format: `https://img.shields.io/badge/<Label>-<HEX>?style=for-the-badge&logo=<simpleicons-slug>&logoColor=white`. Some brand logos (LinkedIn, VS Code, Excel) were removed from Simple Icons, so use those badges without a logo. The checker flags these as NO-LOGO.
- Write in plain, short sentences. No hype words.

## Step 4: Verify before showing

Run `bash scripts/check-badges.sh README.md`. Every URL must return 200, and every `logo=` must actually draw an icon. Fix or remove any failures. Then render a preview (`scripts/preview.sh README.md` → `preview.html`) and show it to the person.

Warn them honestly:
- With fewer than ~4 public repos, the stats and top-languages cards look thin. The top-languages card counts public repos only.
- `github-readme-stats.vercel.app` is a shared public server and sometimes rate-limits. If the cards break, the person can deploy their own copy.

## Step 5: Setup guide (give to the person)

- **Sidebar** (Settings → Public profile): name, bio (offer 3 options, each under 160 chars), company, location, website, social links, and a professional square headshot.
- **Turn on** "Include private contributions on my profile" so private work counts on the activity graph.
- **Pinned repos:** pin at most 6, and only repos that have a README, a description and a clear outcome. Fewer strong pins beat six weak ones. Never make a work/internal repo public. Make a cleaned-up copy instead.
- **Per-repo README template:** `template/PROJECT-README.md`.
- **Hygiene:** a description and topics on every repo, a `.gitignore` for secrets, and a secrets scan of the history before making a repo public (if a key leaked, rotate it; rewriting history isn't enough). Commit messages like `feat(scope): …`. Don't force-push shared branches.

## Step 6: Publish (only with explicit "yes")

Publishing is public and outward-facing, so ask first. If they approve:
1. Have **them** sign in. Never type their password.
2. github.com/new → name = username exactly → Public → Add README on → Create.
3. Open `/<user>/<user>/edit/main/README.md`, select all, delete, and paste the README.
4. Check it in **Preview**: the content appears once and GitHub's default "Hi there 👋" text is gone.
5. Commit to `main`. Open the profile and confirm every image loads.
6. Changing the profile settings (name, bio) is a separate account change, so ask again.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
