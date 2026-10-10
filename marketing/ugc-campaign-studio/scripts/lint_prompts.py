"""Lint UGC campaign prompts in content.json.

Usage: python lint_prompts.py content.json [--market hot-modest|hot|modest|default] [--extra word1,word2]

Walks every string in the JSON, finds still/clip/holding prompts by key name, and checks:
- banned words (market-dependent) in any prompt
- still prompts contain an "Avoid:" line
- clip prompts contain "SCALE LOCK" (warn only if no clip has it yet — Phase 3 adds it)
Exit code 1 on any error.
"""
import json
import re
import sys

BASE = ["cluttered", "messy", "unmade", "rumpled", "half-empty", "dirty", "stained", "peeling",
        "tired", "sad", "blank expression", "charger cable", "sunshade", "second phone in"]
HOT = ["hoodie", "sweatshirt", "sweater", "knit", "fleece", "wool", "cardigan", "jacket", "scarf around"]
MODEST = ["hair showing at", "slipped hairline", "loose strands", "bangs", "fringe of hair"]
MARKETS = {"default": BASE, "hot": BASE + HOT, "modest": BASE + MODEST, "hot-modest": BASE + HOT + MODEST}
# phrases that contain a banned word but are fine (negatives / avoid lines)
ALLOW = [r"avoid:[^\n]*", r"not (?:a )?(?:messy|cluttered|tired|sad)[^,.]*", r"no (?:hair|second phone)[^,.]*",
         r"negative:[^\n]*"]


def prompts(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from prompts(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from prompts(v, f"{path}[{i}]")
    elif isinstance(node, str) and re.search(r"prompt", path.split(".")[-1], re.I):
        yield path, node


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    market = "default"
    extra = []
    if "--market" in args:
        market = args[args.index("--market") + 1]
    if "--extra" in args:
        extra = [w.strip() for w in args[args.index("--extra") + 1].split(",") if w.strip()]
    banned = MARKETS.get(market, BASE) + extra
    data = json.load(open(args[0], encoding="utf-8"))

    errors, stills, clips, clips_with_lock = [], 0, 0, 0
    for path, text in prompts(data):
        low = text.lower()
        for pat in ALLOW:
            low = re.sub(pat, " ", low)
        for w in banned:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                errors.append(f"banned '{w}' in {path}")
        key = path.split(".")[-1].lower()
        if "still" in key:
            stills += 1
            if "avoid:" not in text.lower():
                errors.append(f"missing 'Avoid:' line in {path}")
        if "clip" in path.lower() and "still" not in key:
            clips += 1
            clips_with_lock += "scale lock" in text.lower()

    print(f"market={market} still_prompts={stills} clip_prompts={clips} clips_with_scale_lock={clips_with_lock}")
    if clips and clips_with_lock == 0:
        print("WARN: no clip has a SCALE LOCK line yet (add in Phase 3)")
    elif clips and clips_with_lock < clips:
        errors.append(f"{clips - clips_with_lock} clip prompts missing SCALE LOCK")
    for e in errors:
        print("ERROR:", e)
    print("PASS" if not errors else f"FAIL ({len(errors)})")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
