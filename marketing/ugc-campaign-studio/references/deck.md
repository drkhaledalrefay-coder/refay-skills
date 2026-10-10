# Phase 4 — Playbook deck

## Slide plan (N videos → 7 + 3N slides)
1. Cover — campaign name, brand, market, year; a big number box "N VIDEOS"; one line "Ordinary <people>. One person per video. Not influencers."
2. At a glance — grid (3×3 for 9) — each cell: VIDEO n, name, age · city · job, product, packshot thumbnail. Total runtime.
3. The idea / why real people.
4. Style DNA + Master negative.
5. Workflow — still → select → holding reference → clips → edit (CapCut) → review → post. Mention SCALE LOCK.
6. Invisible cuts.
Per video (3 slides):
- HERO: "VIDEO 0n / 0N" tag; full-height 9:16 persona still (≥3.4×6.0 in) left; packshot (≥3.2×3.2 in, contain-fit on white, thin brand border) centre with setting/length/angle chips + cover text large in native font; right column: who she is, the problem, approved claim (15–16 pt), caption + hashtags + disclosure; product-truth box (internal citations) as a band at 11 pt.
- SCRIPT: full-height table; native dialogue ≥24–28 pt in a proper native font, RTL; transliteration italic; English; on-screen text; DRAFT tags where needed.
- PRODUCTION: still prompt band + one column per clip with a chip "CLIP 1 · 0–8s", body ≥10.5 pt in the body font (not monospace). If it doesn't fit, split into PRODUCTION A/B rather than shrinking below 10.5 pt, or move full prompts to a companion `prompts.md` and show condensed versions.
Closing: dialect glossary · checklist & sign-off (per video: still approved, holding image approved, clips generated, native review, legal/claims check, posted).

## Design
- Brand palette only (+ tints); brand fonts or their installed fallback (Segoe UI on Windows); Arabic → Dubai; set Arabic runs' latin + cs typeface, `rtl="1"`, `algn="r"`. Split runs at Arabic character ranges inside English prompts so quoted lines render in the Arabic font.
- Fix bracket mirroring in RTL headers ("الكلام (عربي)").
- Missing stills/packshots → nude/brand-tint placeholder "IMAGE PENDING" + filename + name; never stretch images; composite transparent PNGs on white; ≤1600 px.
- Generous whitespace, big numbers, strong hierarchy: premium campaign book, not a document dump. No slide should be half empty or overflowing.

## Build & QA (python-pptx)
- Build from a blank 13.333×7.5 in presentation. Split code into small modules (theme / intro / video / outro / main) and produce a first deck early — agents that try to write one giant script stall.
- **Trap: `shape.text_frame` is get-or-add** — reading it on a shape without a txBody silently adds an empty one. Check `shape._element.txBody is not None` first, or read from a separate, never-saved Presentation object.
- Measure text with PIL using the real font files; set `word_wrap=True`, `auto_size=NONE`; shrink 1 pt at a time to the floor, then report — never cut text.
- QA via PowerPoint COM (Windows): open read-only, `DisplayAlerts` off, export every slide PNG (1600×900) + `SaveAs(pdf, 32)`, check `TextRange.BoundHeight/BoundWidth` ≤ shape size, check pairwise overlaps (prefix intentional backgrounds `BG_`), confirm every native string exists in the deck, slide count, size < 50 MB. Wrap COM in a timeout and always `Quit()`. On macOS/Linux use LibreOffice headless for PDF/PNG.
- Then open the PNGs and look: cover, grid, one full video trio, the last video, checklist.
- When editing an existing client deck instead: only add shapes (prefix `IMG_ADD_`), and prove nothing else changed by comparing canonicalized slide XML with added shapes removed.
