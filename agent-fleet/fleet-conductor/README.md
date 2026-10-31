# Fleet Conductor

A planning and review skill for delegating a multi-step task to an existing AI fleet. It keeps the conductor in the planner and judge role.

## At a glance

| | |
| :--- | :--- |
| **Use it for** | Use when several AI agents or CLI tools should execute bounded work in parallel and a lead agent should coordinate. |
| **You need** | The desired outcome, constraints and time box, plus the available agent/tool context. |
| **It produces** | A task plan, role assignments, bounded briefs, verification gates and a final status report. |

## How it works

Clarifies the outcome; assigns planning, execution and review roles; dispatches time-boxed jobs; checks delegated outputs against acceptance gates; reports gaps and fallbacks.

## What it does not do

The conductor plans and judges delegated work rather than executing every job itself. Use another workflow for a one-step task or when you do not want delegation.

## Install and use

Load the complete `fleet-conductor` folder using the skills method supported by your AI client. If the client does not support skills, provide [SKILL.md](SKILL.md) as context. Then describe the task and share the inputs listed above.



## Folder contents

- [SKILL.md](SKILL.md) — the instructions the AI assistant follows.







## License

This skill is part of [Refay Skills](../../README.md) and follows the [CC BY 4.0 license](../../LICENSE).
