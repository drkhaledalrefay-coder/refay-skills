---
name: product-range-course-builder
description: >-
  Build a complete, premium, evidence-anchored training course for ANY brand's product
  range — for sales representatives, pharmacists, beauty advisers, retail staff, dealer
  networks, or internal teams — from a brand guide plus the range's official source
  documents and assets. Trigger phrases: "build the <RANGE> course for <BRAND>", "new
  range course", "create training for <BRAND> <RANGE>", "make a product training course",
  "build a rep certification course", "turn this range into lessons", "I dropped the
  assets in the brand folder". Industry-agnostic and market-agnostic: reads the brand
  guide, extracts the source documents, inventories the images, writes one Verified Brief,
  and hands everything to a build agent in a single verified prompt. Also use for edits,
  restyles, content reviews, or QA passes on an existing range course.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Product Range Course Builder — Any Brand, Any Market

Turns a product range plus its brand assets into a premium, fact-checked training course in one verified handoff to a build agent. No reinvention. No token waste. No fabricated data.

**Applies to:** any brand, any category, any market — skincare, food and beverage, appliances, electronics, fashion, hardware, financial products, B2B equipment, anything sold through people.

**Source of truth:** the brand's own official documents and assets. Never the model's memory.

---

## Roles (fixed)

| Role | Who | Does |
|---|---|---|
| **Planner** | The chat agent with document access | Reads the brand guide, extracts source documents, inventories images, writes the Verified Brief, art-directs, reviews each phase, approves |
| **Builder** | A separate build agent / terminal session | Receives ONE complete prompt, builds everything, tests, deploys. Never guesses. |

**The Planner does NOT write lesson markup line by line. The Builder does NOT re-discover data.**

### Handoff contract

The Builder receives exactly one prompt and must be able to execute it start to finish without asking a question. If the Builder has to guess anything — a product name, a statistic, an image path, a lesson ID — the Planner failed.

---

## Composed skills (use these — do not reinvent)

Load these instead of building the capability from scratch:

- **Lean-diff discipline** — every code change: laziest working solution, shortest diff
- **Prompt optimisation** — write token-efficient Builder prompts
- **Compressed telegraphic style** — compress the Planner→Builder conversation when volume is high
- **Teaching / learning design** — learning objectives, MCQs, progressive disclosure, retrieval practice
- **Document extraction** — pull text and tables out of the official source PDFs (the factual source of truth)
- **Brand design system** — colours, type, logo, tone rules for the specific brand
- **Design critique** — visual review at each phase, desktop plus narrow mobile (≈390px)
- **Accessibility review** — contrast, touch targets, WCAG AA

---

## Folder convention (define once per brand → then per range)

```
docs/brands/<brand>/
  brand-guide.md          ← colours, type, logo, tone, do/don't — REQUIRED before the first range

<assets-root>/brands/<brand>/
  logo/                   ← logo files
  ranges/<range>/
    products/             ← pack shots + pictograms/iconography (flat, URL-safe names)
    lifestyle/            ← customer / adviser / professional / in-use photography
    banners/              ← course hero + lesson banners
    Source/               ← spec sheets, technical dossiers, clinical or test reports (source of truth)
```

Rules:

- Brand slugs and range slugs are lowercase, single-token, URL-safe.
- `Source/` is **read-only**. Nothing is ever edited there.
- All asset filenames that reach markup must be lowercase, hyphenated, no spaces, no parentheses, no dates.
- Record the real absolute path to the assets root once, per project, in the brief.

---

## PERMANENT CONTENT RULES (apply to every range course, every brand)

### 1. Track labels are configurable; the stored enum is not

Each course declares its tracks in Phase 0. Examples:

| Track | Displayed role title | Language / direction | Typical max lessons |
|---|---|---|---|
| Professional | Representative, Pharmacist, Clinician, Dealer, Technician | market default | 3–4 |
| Front-line retail | Beauty Adviser, Counter Staff, Store Associate | local language, RTL if applicable | 2 |

- The **displayed label** in lesson markup must match the role title the brand actually targets. Put it in the hero eyebrow, the "You will learn" label, and the badge.
- The **stored track value** in the database is a stable enum. Keep it stable across releases even when the display label changes. Only the label moves.
- Badge text = short form of the role title.

### 2. The signature technology / complex appears in EVERY lesson

Every range has a signature element — a proprietary blend, a platform, a formulation technology, an engineering principle, a service guarantee. Call it the **KEY COMPLEX** in this skill.

It must appear as a dedicated section in **every** lesson, with depth increasing across the course:

| Lesson | Complex depth |
|---|---|
| L1 | Overview — what it is, in 4 pillars/components, one benefit each |
| L2 | Reinforcement — how the complex works in THIS specific product |
| L3 | Deep mechanism — component-by-component, with the source-document evidence |

If an official complex image exists → use it. If not → build a **CSS-only card** using brand tokens (brand primary background, accent text). **Never skip the complex section because no image exists.**

In a front-line/retail track written in a local language: explain the complex in plain simple language, ≤3 sentences, no technical terminology.

### 3. Representation and context rules

Every image placement is checked against the target market before it is wired in. Define these in Phase 0, then apply them mechanically:

- **Professional/field track:** the professional is shown *in the field* — visiting a clinic, standing beside a partner at a counter, in a meeting room, on site. Never seated passively behind a service counter or desk.
- **Retail/adviser track:** the adviser is at the shelf, wall unit, gondola, or display — never behind the counter that belongs to the other role.
- **Customer profiles:** match the real customer base of the market. Where the market's norms include visible religious or cultural dress, honour them. Dignity is preserved in every depiction, including when a skin condition, defect, or problem is being shown.
- **Generated imagery:** bake the market's representation rules and the brand tone into every generation prompt. Keep a reusable prompt fragment so consistency holds across dozens of images.
- If a market forbids or discourages synthetic humans for customer-facing material, respect that and source real photography instead.

### 4. Gamification variety — never repeat the same format

Each lesson must use a **different primary interactive element**. Choose one per lesson from the pool:

| Lesson slot | Suggested interactive element |
|---|---|
| L1 | Customer/patient scenario decision tree (click to reveal the recommendation) |
| L2 | Step-sequence exercise (order the usage/application/installation steps) |
| L3 | Comparison reveal or "test yourself" scenario widget |
| Retail L1 | Customer matching game (profile chip → product) |
| Retail L2 | Dialogue completion (3 answer options → reveal the correct script) |
| Any | Before/after slider, hotspot diagram, "spot the error" grid, price-objection calculator |

**All MCQs use one shared click-reveal implementation.** Copy the working JS from an existing verified lesson. Never rebuild quiz JS from scratch, and never let two lessons ship two divergent quiz behaviours.

### 5. Comparison section — the "visiting aid" format

When the source documents contain head-to-head performance data, build a comparison block in the lesson that covers the flagship product (usually L3):

- Two-column card: our product (left, brand primary header) vs the alternative (right, neutral grey header)
- Bold the winning values on our side
- Rows = whatever the source supports: efficacy, tolerance, safety, durability, running cost, warranty, service interval
- Label it "<PRODUCT> vs <generic descriptor>" — always use the **generic/INN/technical descriptor** from the source document, never a competitor's trademark. The brand owner can add a local brand name in brackets after review.
- This comparison repeats across every range and every brand. It is a signature reusable element.

### 6. External market data — allowed, with rules

Lessons MAY include market, epidemiological, or industry data from external sources, provided:

- The stat is cited at the lesson footer: `Source: [publisher, year]`
- It is presented as a separate fact — never mixed into the numbers that came from the official source documents
- It was **verified by search in this session**. Not from memory, not from an older draft, not from a plausible-looking guess

### 7. Local-language content rules

Per course, lock and reuse:

- The correct word for "customer" in that language and market (pick one and never vary it)
- The physical context of the adviser's dialogue, so the script matches where they actually stand
- The complex explanation in simple language, ≤3 sentences
- A hard cap of one sentence of technical science per product in the retail track
- MCQ anchors are always real customer scenarios, never product-knowledge trivia

### 8. Lesson footer — source credit

Every professional-track lesson ends with a small, centred, muted credit line:

```html
<p class="ls-muted" style="font-size:.8rem; text-align:center; padding:1rem 0;">
  Market data: [publisher, year]. Product and performance data: <BRAND> official source documents.
</p>
```

---

## brand-guide.md — required format

Create this once per brand, before building any range:

```markdown
# <BRAND> Brand Guide

## Identity
- Primary colour: #XXXXXX (name)
- Accent colour: #XXXXXX (name)
- Background: #XXXXXX
- Type: [family] — headings | [family] — body
- Logo: [relative location inside logo/]

## Tone
[1–2 sentences: clinical/scientific? warm/friendly? premium/aspirational? plain-spoken?]

## Voice do
- [rule]

## Voice don't
- [rule]

## Claims posture
[What the brand may and may not claim. Standing legal/regulatory constraints.]

## Design notes
[Layout rules, spacing habits, imagery style, what the brand never does visually]
```

If the brand guide does not exist, stop and create it with the brand owner first. Do not improvise brand tokens.

---

## QUALITY GATES

These gates are hard. Nothing advances past a failed gate, and no gate is waived because of schedule pressure.

| # | Gate | Passes when |
|---|---|---|
| G0 | **Intake complete** | Every Phase 0 field is answered or explicitly marked "not applicable" |
| G1 | **Source extraction** | Every product, ingredient/component, and number traces to a named source document and page/section |
| G2 | **Asset inventory** | Every file reference is a confirmed real path; unknown paths are impossible |
| G3 | **Brief approved** | The brand owner read the Verified Brief and said yes |
| G4 | **Build complete** | All lessons exist, each with its own interactive element, complex section, and footer |
| G5 | **Accuracy** | Zero invented product names, ingredients, specifications, or numbers; every claim is labelled with its source |
| G6 | **Placement** | Every image sits in the intended lesson and section, verified by lesson ID and surrounding heading |
| G7 | **Localisation** | RTL/direction, language field, and translated labels all agree |
| G8 | **Accessibility + responsive** | Contrast passes, touch targets ≥44px, no horizontal scroll at ≈390px |
| G9 | **Automated tests** | The project's test suite is green |
| G10 | **Local visual review** | Screenshots of every lesson reviewed at desktop and narrow mobile |
| G11 | **Deploy verified** | Post-deployment check returns the expected result for every lesson |
| G12 | **Rollback ready** | A named backup branch and a documented restore path exist before deploy |

---

## Phase 0 — MANDATORY INTAKE (the Planner does this; no skipping)

### 0a. Intake form

Fill this in and show it back for confirmation. Unanswered = do not proceed.

```
BRAND:                [name]
CATEGORY / INDUSTRY:  [e.g. personal care, consumer electronics, building materials]
RANGE / LINE:         [name]
MARKET(S):            [country / region / channel]
LANGUAGE(S) + DIR:    [e.g. English LTR; Arabic RTL]
TRACKS:               [professional track role title] + [retail track role title, if used]
AUDIENCE SIZE + ROLE: [who sits the course, what they must be able to do afterwards]
BUSINESS GOAL:        [what changes when they finish — conversion, compliance, fewer returns]
HOST / DELIVERY:      [LMS, static site, slide deck, printed workbook, other]
SOURCE DOCS:          [exact filenames the facts must come from]
ASSET ROOT:           [absolute path]
EXISTING COURSE?      [new build / restyle / content review]
```

### 0b. Load brand identity

Read `docs/brands/<brand>/brand-guide.md`. Set design tokens from it. If absent → create it with the brand owner first (G0 fails until it exists).

### 0c. Extract the source documents

Extract text and tables from every file in `Source/`. Use the available document-extraction skill/tool. If scripting is unavailable in the environment, say so and **ask the brand owner to paste the key data** — never fill the gap from memory.

**Extract and record:**

- Exact product names — every SKU, exactly as the document spells them
- Active ingredients / components / materials, with correct technical names and concentrations
- Performance data: sample size, duration, measured change, study or test design, comparator
- Indications, warnings, contraindications, usage/installation instructions
- The range's KEY COMPLEX name and its components
- Any head-to-head or comparison data

> **Incident to remember (generalised):** in a past build, the Planner wrote lesson content without reading the source document. Entire product names and specifications were fabricated, and the Builder burned a full session correcting fake data. **Source extraction is not optional, and neither is reading what you extracted.**

If extraction returns empty or garbled → stop, tell the brand owner, ask for the data.

### 0d. Inventory every asset

List every real filename under `products/`, `lifestyle/`, `banners/`. No assumed paths.

**Flag immediately:**

- Filenames with spaces, parentheses, dates, or non-ASCII characters → mark for rename, run the renames **before** building
- Nested folders with spaces in their names → copy the needed files flat into `products/` with clean names
- Pattern to hunt for: `Image Jul 19 2026 final (2).png` → `lifestyle-scene-01.png`
- Missing assets → write ready-to-paste generation prompts for the brand owner **before** handing off to the Builder

### 0e. Map every asset to a slot

| Asset file | Lesson | Section | Usage |
|---|---|---|---|
| products/product-a.jpg | L2 | Product card + MCQ | Pack shot |
| lifestyle/customer-01.png | L1 | Profile A | Story photo |
| banners/hero.jpg | Course hero | Header | Full-bleed |

Rules: pack shots → product cards and MCQ answer images; lifestyle → hero sections, profiles, and dialogue cards. **A file that is not in this table never appears in the build.**

### 0f. Write the Verified Brief

```
BRAND: [name]
RANGE: [name]
MARKET(S): [list]
TRACKS: [display label + language + direction]
SCOPE: [exact SKUs in scope — confirmed, not assumed]
HOST / DELIVERY: [where the course will run]

BRAND TOKENS (from brand-guide.md):
  Primary #XXXXXX | Accent #XXXXXX | Type [family]

PRODUCTS (from source docs): [exact list]
KEY COMPLEX: [name] — [components]
KEY ACTIVES / COMPONENTS (from source docs): [name | function | concentration]
PERFORMANCE DATA (from source docs): [result | design | sample | duration | comparator]
COMPARISON DATA (from source docs): [yes/no — if yes: descriptor + stats]
INDICATIONS / SUITABLE FOR (from source docs): [list]
WARNINGS / CONTRAINDICATIONS (from source docs): [list]
EXTERNAL MARKET DATA (searched this session, cited): [stat | source]

CONFIRMED ASSETS (URL-safe):
  [filename] → [L# / section / usage]

MISSING ASSETS (generation prompts):
  - Gap: [description]
    Prompt: "[ready-to-paste prompt carrying brand tokens + market representation rules]"

FILES TO RENAME (URL-unsafe):
  "[old name]" → "[new-url-safe-name.ext]"

LESSON PLAN:
  L1: [topic] — Interactive: scenario decision tree
  L2: [topic] — Interactive: step-sequence exercise
  L3: [topic + protocol + comparison] — Interactive: comparison reveal
  Retail L1: [topic] — Interactive: customer matching game
  Retail L2: [topic] — Interactive: dialogue completion

LESSON COUNT RATIONALE:
  [N] professional lessons justified by [product count / complexity].
  Rule of thumb: 2 products → 3 professional lessons; 4+ products → 4 professional lessons.
  Retail track: max 2 lessons.

QUALITY GATES ACKNOWLEDGED: G1–G12
OPEN QUESTIONS FOR THE BRAND OWNER: [list, or "none"]
```

**Nothing enters the Builder prompt that is not in this brief.** The brand owner approves before any markup is written.

---

## Phase 1 — Build (one comprehensive Builder prompt)

After approval, write a **single** prompt containing:

1. All product names verbatim from the brief
2. All numbers with a source label inline, e.g. `[Source: technical dossier p.4]`
3. Exact, confirmed, URL-safe asset paths **mapped to exact lesson identifiers** — never "add this image somewhere in L3"
4. **Replace vs add** stated explicitly for every image: "**Replace** the existing `<img src=…old…>` with `<img src=…new…>`" — never a bare "add after"
5. Rename commands first, before any markup references the renamed files
6. Full markup structure for every lesson
7. The KEY COMPLEX section in every lesson at the correct depth
8. The comparison block where the data exists
9. The shared quiz implementation reference — do not rebuild it
10. Direction/language attribute requirements for localised tracks
11. The automated test command as a gate
12. An explicit **`STOP — do not deploy`** instruction at the end

The Builder runs tests, reports, and stops. Deployment is a separate, explicitly approved phase.

---

## Lesson structure — professional track

1. **Shock-stat hero** — the number that reframes the problem, sourced and cited
2. **Key concepts or misconceptions** — numbered pill list, one sentence each
3. **Human / quality-of-life impact** — brief callout where relevant
4. **Mechanism or principle** — CSS-only flow diagram; never a fabricated diagram image
5. **KEY COMPLEX — overview / reinforcement / deep** (per the depth rule)
6. **Feature → benefit table** — component | mechanism | benefit | customer type
7. **Strong performance claims** — big editorial stat layout, bold, each source-labelled
8. **Comparison block** (flagship lesson only) — visiting-aid format
9. **Protocol / usage / installation** — table plus cards (standalone / combined / maintenance)
10. **Customer scenarios (3)** — who presents, what to recommend, decision tree
11. **Recommendation-trigger checklist** — when to recommend, when to escalate or refer
12. **Objection handling** — a shared Q&A component, ONE bold takeaway per answer
13. **Primary interactive element** — varied per lesson
14. **4 MCQs** — click-reveal, pack shots as answer images where possible
15. **Lesson footer** — source credit line

## Lesson structure — front-line / retail track (localised)

Maximum 2 lessons per range.

1. **Customer profiles (4)** — e.g. routine seeker / active treatment / post-service / expecting or sensitive
2. **KEY COMPLEX** — plain language, ≤3 sentences
3. **Product explanation in one minute** — dialogue card ("they say / you say")
4. **3 floor dialogues** — covering the main objections plus a cross-sell
5. **3 objections** — common pushbacks plus a confident, non-pushy response
6. **Pre-shelf checklist** — a 5-point self-check before the shift
7. **Primary interactive element** — varied per lesson
8. **4 MCQs** — scenario-based, never product-knowledge trivia

Format: `dir="rtl"` and `lang="ar"` when applicable, a font that actually covers the script, and the course language field set on the record.

---

## Design system — brand-skinned editorial pattern

Do **not** rebuild the CSS system per brand. **Skin it.**

- Map one brand primary, one accent, and one type family into the existing editorial class system.
- Rename tokens, never restructure components.

Keep these brand-agnostic editorial rules:

- Full-bleed alternating sections, big display type, generous whitespace
- Hairline separators, **no nested boxes**
- Editorial stats: big number plus a thin accent underline
- Pill rows, with ONE accent pill per section
- Type floors: body 17px at 1.7 line-height; tips ≥15px; mobile never below 1rem
- Lessons render inline markup (not an external iframe) so the shared stylesheet applies

---

## Phase 2 — QA gates (Builder self-check, Planner verifies)

Run every gate in the QUALITY GATES table. Report each as pass/fail with evidence, not as a claim.

**Accuracy sweep:** re-read the lesson copy against the extracted sources. Every product name, every concentration, every percentage, every sample size must appear in the brief. Anything that cannot be traced is marked `<!-- VERIFY SOURCE -->` and reported — **never smoothed over with invented content**.

**Placement sweep:** for every image, confirm the lesson ID, the section heading it sits under, and that replacement (not duplication) happened where intended.

---

## Phase 3 — Visual review (Planner)

Capture and review screenshots of **every** lesson:

- Desktop
- Narrow mobile (≈390px)
- The longest lesson (worst case for overflow)
- Any RTL track, checking direction, alignment, and mirrored icons

Check: hierarchy, contrast, touch target size, no horizontal scroll, no orphaned headings, no missing alt text, no untranslated strings.

---

## Phase 4 — Deploy (explicit approval only)

Generic sequence — substitute the project's real tooling:

```
1. Create a named backup branch
2. Commit with a descriptive message
3. Push
4. DEPLOY — only after explicit in-chat approval from the brand owner
5. Apply content changes through the host's supported sync mechanism
6. Verify every lesson with a request that returns an expected status/body
```

**Where content lives in a database, treat the database as the live source of truth.** Do not re-seed from repository files, because that silently reverts content that was hot-fixed in place. Use the host's supported sync path.

**Never assume a filesystem is readable from the deployment runtime.** Files excluded from the deployment bundle read as empty there, and a silent empty write looks like success. Verify content length after any sync.

---

## Common failure modes — check before every build

| Failure | Cause | Fix |
|---|---|---|
| White gap or unstyled hero | The hero section class has no rule in the stylesheet | Add the hero block rules before building |
| Error page on the quiz/results screen | Formatting a null completion date | Use optional/null-safe formatting with a fallback, e.g. `optional($attempt->completed_at)->format('d M Y') ?? '—'` |
| CTA renders as a full-width bar | Link styled as a block without inline constraint | `display:inline-block` with explicit padding and radius inside a centred wrapper |
| Image landed in the wrong lesson | Placement described as "L3" only | Always include the lesson ID plus the exact anchor heading |
| Image duplicated instead of replaced | Instruction said "add after" | Instruction must say "**Replace** X with Y" |
| Localised lesson renders LTR | Direction set in markup but not on the record, or vice versa | Set both: the language field on the record **and** a wrapping element with `dir` and `lang` |

---

## Quiz vs assessment — when to use which

| Type | When | How |
|---|---|---|
| **Per-lesson quiz** | The lesson teaches a testable skill | A short quiz record linked to the lesson |
| **Course assessment** | Course completion — 8–15 questions across the whole range | A separate assessment record |

---

## Output formats

| Format | Use when | Notes |
|---|---|---|
| LMS-ready rich-text lesson body | Default for hosted training | Inline markup so the shared stylesheet applies |
| Static HTML bundle | No LMS available | Self-contained, relative asset paths |
| Slide deck (PPTX/Google Slides) | Live, presenter-led training | One idea per slide, speaker notes carry the depth |
| Print workbook (PDF) | Field teams with poor connectivity | QR codes to the interactive elements |
| One-page "visiting aid" | Field reference during calls | Distilled from the comparison block and protocol table |
| Facilitator guide | Train-the-trainer | Timings, discussion prompts, answer key, common wrong answers |

**Content rules that apply to every format:**

- **Never invent** a statistic, product name, component, or specification. If it is not in the extracted source, it does not exist.
- **One bold takeaway** per objection answer — never bold whole paragraphs.
- **Preserve fact-checked copy** through any restyle.
- **Every image reference must be a path confirmed in Phase 0d.** No placeholder paths, ever.
- **Mark anything unverifiable** `<!-- VERIFY SOURCE -->` rather than inventing it.

---

## Guardrails

- Never touch unrelated projects or shared files.
- The project's test suite stays green after every change.
- Build before visual review; test locally before deploying.
- One phase per Builder run; back up before risky operations.
- The brand owner's approval is required at G3 (brief) and at deploy. No silent deploys.

---

## Worked example (fictional)

> *Brand:* Aurora Botanics — invented, illustrative only.
> *Range:* PureCalm — three SKUs.
> *Tracks:* Representative (EN) + Beauty Adviser (AR).
> *Key complex:* a fictional three-component complex named in the source dossier.
> *Assets:* pack shots, two lifestyle photos, one hero banner, one spec PDF.
> *Plan:* three representative lessons (scenario tree → step-sequence → comparison reveal) plus two Arabic adviser lessons (matching game → dialogue completion).
> *Outcome shape:* one brief, one Builder prompt, twelve gates passed, deployed after approval.

---

## Reference lineage

Generalised from a real, multi-range training-course build for a specialised consumer brand, then stripped of all brand-specific content so it works for any category, any market, any language. The method — brief, extract, inventory, one-prompt build, gate, review, deploy — is the part that transfers.

---

*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
