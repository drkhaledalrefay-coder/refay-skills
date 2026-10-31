# Fleet Orchestrator

A main-agent workflow for discovering available AI tools, planning delegated work and checking every result before reporting.

## At a glance

| | |
| :--- | :--- |
| **Use it for** | Use for multi-step coding, research, review or writing when you want the assistant to inspect and coordinate available agents. |
| **You need** | The task and constraints; authorization to inspect local tool availability if discovery is needed. |
| **It produces** | An evidence-based inventory, division of work, briefs, checked deliverables and a completion report. |

## How it works

Checks the host and installed/sign-in evidence; suggests optional free tools without installing; plans jobs; dispatches to available agents; independently verifies results.

## What it does not do

Does not silently install tools or claim an agent is available without evidence. Local discovery is platform-specific and must only run where authorized.

## Install and use

Load the complete `fleet-orchestrator` folder using the skills method supported by your AI client. If the client does not support skills, provide [SKILL.md](SKILL.md) as context. Then describe the task and share the inputs listed above.



## Further guidance

[Agent catalog](references/agent-catalog.md) · [Brief template](references/brief-template.md) · [Dispatch recipes](references/dispatch-recipes.md)

## Folder contents

- [SKILL.md](SKILL.md) — the instructions the AI assistant follows.




- `references/`, `scripts/` — agent catalog, brief/dispatch guidance and platform-specific discovery commands.


## License

This skill is part of [Refay Skills](../../README.md) and follows the [CC BY 4.0 license](../../LICENSE).
