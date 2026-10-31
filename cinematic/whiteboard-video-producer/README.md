# Whiteboard Video Producer

Plan and assemble an evidence-led whiteboard explainer with a clear script, timed storyboard, hand-drawn visual direction, and a practical production pipeline.

## What it helps create

- A voice-over script in the requested language or dialect
- A timecoded storyboard that preserves the requested order and duration
- Short, readable on-screen text and scene-specific drawing directions
- An asset and claim checklist for brand-sensitive or regulated topics
- FFmpeg-based assembly guidance and a YouTube publishing package

## How to use it

Give your AI assistant a topic, audience, target duration, aspect ratio, source materials, and any existing narration or footage. If those details are already in the conversation, the skill should use them instead of asking again.

For product, medical, scientific, or statistical claims, include the approved source files. The skill should quote only supported claims, preserve study context, and flag gaps.

## Files

- [SKILL.md](SKILL.md) — the workflow and quality rules
- [whiteboard-prompt.md](whiteboard-prompt.md) — reusable production brief
- [scripts/whiteboard_engine.py](scripts/whiteboard_engine.py) — free FFmpeg scene-board assembler

The helper assembles pre-rendered board images against one narration track. It does not generate artwork, create a hand animation, or determine semantic scene boundaries; provide those inputs in the timeline JSON.

## Basic use

1. Create a folder of scene images in the requested aspect ratio.
2. Create a timeline JSON with exact start/end times and image paths.
3. Run the script with FFmpeg installed and available on PATH.
4. Review the rendered video for voice sync, spelling, and visual continuity.

Example:

```powershell
python scripts/whiteboard_engine.py --timeline timeline.json --audio voiceover.mp3 --output final.mp4
```

See the script header for the timeline format. FFmpeg is a separate free command-line tool.

---

*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
