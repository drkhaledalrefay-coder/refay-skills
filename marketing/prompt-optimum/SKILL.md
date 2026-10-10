---
name: prompt-optimum
description: "Rewrites a chat message or prompt the user is about to send (to Claude or any other LLM/tool) into the most token-efficient version that still gets precise, high-quality results. Use this whenever the user says \"optimize this prompt,\" \"tighten this,\" \"make this more efficient,\" \"run prompt_optimum,\" or hands over a rough/verbose draft of something they are about to ask an AI to do and wants it compressed without losing precision. Learns the user's recurring phrasing and context patterns over time via a local pattern log, so later rewrites need less re-explaining. Only asks a clarifying question when the input is genuinely ambiguous — never for polish."
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Prompt_optimum

Rewrite the user's draft message into the leanest prompt that still produces a precise, high-quality result. Optimize for signal density, not brevity for its own sake — cutting a word that carries information is a bug, not a win.

## Why this matters

Every filler word, redundant qualifier, and unstated-but-obvious instruction costs tokens on every single call — and for someone who prompts constantly across brand work, data analysis, and dashboard builds, that adds up fast. A prompt that's 30% shorter but equally precise compounds into real savings and faster turnaround.

## Process

1. **Read the draft.** Identify the actual task, the constraints that matter, and the output format the user wants.
2. **Check `references/patterns.md`** (if it exists) for phrasing shortcuts and recurring context the user has already established — e.g. standing rules they always mean implicitly (a brand name always written in caps, a preferred data source, a house framing) that don't need to be re-stated in every prompt because they already live in the user's project instructions/rules file. Do not re-inject those into the rewritten prompt — they're already active; restating them would waste tokens.
3. **Strip, don't summarize:**
   - Remove hedging ("I was wondering if maybe you could possibly...") → keep the direct ask.
   - Remove restated context that's already in the user's standing memory (project names, brand colors, tool stack) unless the task is genuinely ambiguous without it.
   - Collapse multi-sentence throat-clearing into one clean instruction.
   - Keep every constraint that changes the output: format, audience, length, deadline, data source, what NOT to do.
   - Keep specificity (file names, exact metrics, product names) — these are load-bearing, never cut them.
4. **Clarify only if blocked.** If the rewrite would be ambiguous or could go two meaningfully different directions (e.g., unclear whether the user wants a file or a chat answer, unclear which brand/market), ask ONE tight question. Do not ask about stylistic preferences already covered by their standing rules (concise, structured, business-first — assume these). This should be rare.
5. **Output only the optimized prompt** in a code block, ready to copy/paste or send. No rationale, no before/after diff, no commentary — unless the user asks for one.
6. **Log the pattern.** If this rewrite reveals a recurring shortcut worth remembering (a phrase the user always uses that maps to a specific longer instruction, a context they always omit because it's implicit), append a short entry to `references/patterns.md`. Keep entries terse — one line each. Don't log one-off, non-recurring edits.

## What "token-efficient" does NOT mean here

Efficient is not the same as short. Never drop information that changes what gets produced. If the draft is already tight and precise, say so and return it mostly unchanged rather than cutting for the sake of cutting.

## Pattern log

`references/patterns.md` is the user's accumulated shorthand — check it every time, update it when you learn something new. If the file doesn't exist yet, create it on first use with a one-line header.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
