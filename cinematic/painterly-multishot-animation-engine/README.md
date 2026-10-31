# Painterly Multi-Shot Animation Engine

Break a story and its visual references into self-contained, timecoded multi-shot prompts that stay consistent across separate AI video generations.

## At a glance

| | |
| :--- | :--- |
| **Use it for** | Use for painterly or stylized animation sequences, especially when a story spans several generated clips. |
| **You need** | The story beat, character/location references, desired clip length and project style/continuity rules. |
| **It produces** | One standalone timecoded prompt per generation, with continuity anchors and an ordered shot sequence. |

## How it works

Breaks the story into generations; locks identity/location details; reads references; designs shots; writes and trims each prompt; checks continuity across generations.

## What it does not do

Prompt-writing workflow; the user generates the clips. Each prompt is self-contained rather than relying on hidden context from a previous generation.

## Install and use

Load the complete `painterly-multishot-animation-engine` folder using the skills method supported by your AI client. If the client does not support skills, provide [SKILL.md](SKILL.md) as context. Then describe the task and share the inputs listed above.



## Folder contents

- [SKILL.md](SKILL.md) — the instructions the AI assistant follows.







## License

This skill is part of [Refay Skills](../../README.md) and follows the [CC BY 4.0 license](../../LICENSE).
