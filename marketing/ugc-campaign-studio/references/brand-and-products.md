# Phase 1 — Brand & product analysis

Output: `analysis.md` (human-readable) + `products.json` (machine-readable, used by later phases).

## Brand section (analysis.md)
- Identity: palette (hex), fonts (+ installed fallback), logo usage, casing/naming rules (e.g. brand name ALL CAPS; range names in English; ® only in titles).
- Voice: how the brand talks vs. how a real customer talks (UGC must sound like the customer, not the brand).
- Audience & market context from the brief.
- Compliance: what can/can't be claimed on social; disclosure line; regulated categories (pharma/dermo: no cure/treatment claims unless approved; no before/after unless approved).
- Optional: 3–5 observations on how competitors do UGC in this market.

## Per product (products.json)
```json
{
  "video": 1,
  "product": "<PRODUCT>",
  "sku": "40 ml jar",
  "for_whom": "<the audience the product is for — e.g. redness-prone skin>",
  "relatable_problem": "<the everyday problem the product removes>",
  "claims": [
    {"text": "<approved claim, e.g. removes makeup, even waterproof>", "source": "<file>", "page": "39", "spoken": true},
    {"text": "<clinical claim with the number, e.g. reduces redness in 64% of patients>", "source": "<file>", "page": "44", "spoken": false}
  ],
  "packshot": "<path or null>",
  "pack": {"type": "jar", "volume": "40 ml", "approx_cm": "5 x 5 x 4", "cap": "screw lid",
            "hand_relative": "small jar that sits in her palm, about 5 cm across",
            "wrong_scale_negative": "not giant, not larger than her hand, not miniature"},
  "usage_action": "scoops with fingertips, massages on dry face, emulsifies with water",
  "flags": []
}
```

## Rules
- **Claims only from provided official sources, with file + page.** If a source can't be read, stop and flag — don't fill from memory. Numbers (%, n=, days) go in `spoken: false` claims for the internal product-truth box; spoken claims are experiential ("my skin stopped turning red"), no numbers.
- Explain any clinical score in plain language wherever it appears.
- **Pack scale**: measure the packshot's non-white bounding box (Pillow) for aspect ratio, combine with volume and pack norms to estimate cm; mark "approx" unless an official dimension exists. Typical: 30 ml dropper ≈ 10–12 cm tall; 40 ml tube ≈ 12–15 cm; 50 ml tube ≈ 14–16 cm; 200 ml bottle ≈ 17–19 cm; 250 ml pump bottle ≈ 19–22 cm incl. pump; small jars 40–50 ml ≈ 5–6 cm wide.
- **Sibling SKU trap**: never swap a product for a similar SKU (Gel vs Gel Sensitive, Balm vs Lotion, 40 ml vs 100 ml) without the user's explicit OK. If they switch a product, the script, claims, action (face vs body), scale and prompts all change — cascade it.
- Packshots with transparency: composite on white before use; resize long side ≤1600 px.
