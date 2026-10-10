---
name: ugc-campaign-studio
description: Plan and produce a complete AI-generated UGC (user-generated-content style) video campaign for ANY brand — analyze the brand, analyze each product (claims with sources, pack size/scale), then build the campaign: ordinary-people personas (one per video), native-dialect scripts, still-image prompts, "holding the product" scale-reference prompts, Google Flow / Veo clip prompts, and a premium campaign playbook deck (.pptx). Use this whenever the user wants a UGC campaign, "real people" / testimonial-style videos, AI influencer-free product videos, a TikTok/Reels/Instagram grid of product videos, persona prompts for Nano Banana / GPT Image / Veo / Flow, or a UGC playbook — for cosmetics, pharma/dermocosmetics, food, fashion, tech or any consumer brand, in any country or language — even if they don't say "UGC".
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# UGC Campaign Studio

Turn a brand + its products into a production-ready UGC campaign: brand/product analysis → campaign & personas → scripts & prompts → playbook deck. Works for any brand, product category, country and language — everything market-specific comes from the Phase 0 intake, never from defaults. Built from real campaigns (for example a dermocosmetics launch in a hot-climate market); the examples below come from them, and every rule exists because something went wrong without it. Swap every market-specific value for the one from your intake.

## The shape of the work

Four phases, each ending in an approval gate. Do not start the next phase until the user approves the current one — the user's corrections at each gate are the most valuable input you get, and redoing downstream work after a late correction is expensive (personas → prompts → deck all cascade).

| Phase | Output | Gate question |
|---|---|---|
| 0 Intake | `brief.json` (answers to the intake questionnaire) | "Is this brief right?" |
| 1 Brand & product analysis | `analysis.md` + `products.json` (claims + sources + pack scale) | "Are these the products, claims and sizes we use?" |
| 2 Campaign & personas | `content.json` (campaign, N personas, scripts, still prompts) + `persona_prompts.md` | "Approve the people and scripts?" — the user generates stills now |
| 3 Production assets | selected stills, `holding_prompts.md`, clip prompts with SCALE LOCK | "Stills and product scale look right?" |
| 4 Playbook deck | `deck.pptx` + `deck.pdf` + QA report | "Ship it?" |

Work in a scratch folder (e.g. `<scratch>/ugc/<brand>/`) and copy finals to the user's chosen folder only at the end. Never overwrite the user's source files; always write new versions.

## Phase 0 — Intake (ask, don't assume)

Read `references/intake.md` and ask its questions (use a structured question tool if available; batch them, 3–4 per round). The critical ones: market/country and city, language + dialect, cultural dress/modesty rules, target audience & socioeconomic level, number of videos (think in grid multiples: 3, 6, 9, 12), platforms, products list, where the brand guide / product sources / packshots live, which image & video tools they use, and who reviews native-language copy. If a path the user gives has an unfilled placeholder, stop and ask — don't guess.

## Phase 1 — Brand & product analysis

Read `references/brand-and-products.md`. In short:
- Brand: identity (colors, fonts, logo rules, tone, naming/casing rules like "<BRAND> always ALL CAPS"), audience, competitors' UGC patterns if the user wants.
- Per product: what it is, who it's for, the relatable problem, **approved claims only from official sources with page citations** (training PDFs, product sheets, brand site) — never invent or "round" a claim; clinical numbers stay internal (product-truth box), spoken claims are experiential with no numbers.
- **Pack scale**: pack type, volume, approximate real dimensions (cm) and a hand-relative sentence. AI video tools render products far too big or too small unless you lock scale in words and with a reference image.
- Find packshots; flag missing ones as "PACKSHOT PENDING" rather than substituting a different product (e.g. a different SKU of the same range is NOT a substitute — ask).

## Phase 2 — Campaign & personas

Read `references/personas.md` — it holds the hard-won rules. The essentials:
- **One different ordinary person per video** (women, men, parents, seniors — whoever the brand's buyers are). Not influencers, not models, not a recurring cast. Vary age, job, city, look, style, home.
- **Ethnicity must match the market explicitly.** Image models drift to a default look for the region (e.g. one country's typical face when asked for a neighbouring country's woman or man). Describe the local features positively AND add a negative naming the drift.
- **Naturally attractive**, warm friendly expression. The problem the product solves is shown mild and realistic — never exaggerated.
- **Socioeconomic realism**: match the audience (e.g. a middle-class-to-affluent market → modern, clean, tasteful homes and cars). "Real/raw" means phone-camera look, not poverty or mess.
- **Climate- and culture-correct clothing** from the intake (hot city → light fabrics, no hoodies), inside any modesty rules the market has (e.g. head covering fully hiding hair with an under-cap). If the market has no such rules, skip them — don't import one market's rules into another.
- The product category changes the story, not the method: skincare shows the face/skin, food shows eating/cooking, tech shows the device in use, household shows the chore. Pick the use-moment a real customer would film.
- Every still prompt ends with an `Avoid:` line.
- Scripts: native dialect, short (2–3 clips, ~16–24 s), hook → problem → product moment → result. Use `templates/content.schema.md` for structure. Any line you (or an agent) write in a language the user must review is tagged `needs_native_review`.
- Show the user the persona table + scripts at the gate; then hand them the still prompts to generate (they usually generate stills themselves).

## Phase 3 — Production assets

Read `references/video-prompts.md`.
1. **Select stills**: when the user drops generated images (often several per persona), view every candidate and pick the best by: modesty/rules → market-correct attractive face → mild concern → clean setting, no AI artifacts (hands, second phone) → usable video reference. Copy winners to `selected/` with clean names; flag any persona that needs regeneration and say why.
2. **Holding-product reference (do this before any video)**: image-to-image prompt with 2 references (the selected still + packshot) → the same person holding the product at the true scale, label facing camera. This single step prevents most wrong-scale videos.
3. **Clip prompts**: per clip, paste-ready English for Flow/Veo: references, style DNA, persona descriptor (consistent with the still), action by seconds, dialogue line in the native language, camera, light, audio, end-of-clip transition (invisible cut), **SCALE LOCK sentence**, negative. Keep descriptors identical across a video's clips.
4. Run `python scripts/lint_prompts.py content.json --market <default|hot|modest|hot-modest> [--extra word1,word2]` — it fails on banned words (messy/old settings, "tired"/"sad" expressions; plus winter clothes for hot markets and visible hair for modest markets) and on missing Avoid/SCALE LOCK lines. Add market- or brand-specific words with `--extra`.

## Phase 4 — Playbook deck

Read `references/deck.md`. Build a new deck from scratch with python-pptx (never patch an old one). Structure: cover with the big video count → campaign-at-a-glance grid (one cell per video, matches the social grid) → idea / why real people → style DNA + master negative → production workflow (incl. the holding-reference step) → per video exactly 3 slides (HERO: big 9:16 persona still + big packshot + her story, claim, cover text, caption; SCRIPT: full-slide dialogue table, native script in a proper font, RTL where needed; PRODUCTION: still prompt + clip prompts, readable ≥10.5 pt) → glossary (dialect terms) → checklist & sign-off. Use the brand's colors/fonts; if the brand font isn't installed, use the brand guide's fallback; Arabic → Dubai (ships with Windows/Office), set `rtl="1"` + right-align.

QA is not optional: export every slide to PNG via PowerPoint COM (or LibreOffice), check text bounds vs. box sizes, overlaps, that every native-language string survived, slide count, file size; then **look at the PNGs yourself**. See `references/deck.md` for the known python-pptx traps.

## Who does the work — detect the fleet

Read `references/fleet.md`. At the start, detect which agent CLIs exist (`cursor-agent`, `codex`, `agy`, and Claude subagents). Default roles:
- **You = director**: write briefs, hold the gates, verify everything independently, talk to the user.
- **Thinking/writing agent** (analysis, personas, scripts): strongest reasoning model available (e.g. Cursor Grok xhigh, Codex high, or an Opus subagent).
- **Builder agent** (deck code, QA, file ops): a solid implementation model (e.g. Cursor Grok high, Codex, or a Sonnet subagent).
- **Reviewer** (optional second opinion): a different vendor than the builder.
If no external CLI exists: Opus = director, Codex (if present) = deputy/reviewer, Sonnet subagents = implementation. If nothing but you exists, do it yourself phase by phase.

Never trust an agent's self-report: re-run the checks, read the diff/outputs, render slides and look. Two agents must never write the same file at the same time — give parallel agents disjoint output files and merge afterwards.

## Language with the user

Reply in the user's language. Keep status updates short: what's done, what's running, what you need from them.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
