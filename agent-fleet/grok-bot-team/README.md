# Grok Bot Team

![Grok Bot Team project crew](assets/grok-bot-team.jpg)

A skill for Grok Bot that turns a substantial, multi-step task into a focused project room: it selects useful agent roles, checks for suitable existing teammates, and can discover optional CLI agents on a registered user machine.

It keeps the work grounded in the tools actually available to Grok Bot. A machine or CLI is never assumed, and the skill does not claim an agent or command ran unless the connected tool confirms it.

## When to use it

Use this skill when a project has enough moving parts to benefit from a planner, a maker and an independent reviewer—for example, building a small website, preparing a research report, or producing a campaign.

Skip it for a quick one-step request or personal operations that do not need a project room.

## Requirements

- **Grok Bot** with the relevant room, agent and machine tools available in its connected environment.
- **A registered machine** connected to Grok Bot for local CLI discovery. If there is no registered machine, the task can continue without local CLIs.
- **Optional CLI agents** installed and available on PATH, such as coding or text agents. They are not required to use the room.

The exact room and machine features depend on the connected Grok Bot environment. The skill uses only capabilities that are actually exposed there.

## Install

Add the `grok-bot-team` folder to Grok Bot's supported skills location, or provide its `SKILL.md` as skill context if the client supports that method. Follow the installation method documented by the Grok Bot environment in use; this repository does not assume a universal installer.

The folder contains:

- `SKILL.md` — instructions Grok Bot follows.
- `README.md` — this overview and example.

## Example: a project task from kickoff to delivery

Suppose a user asks: “Build a three-page portfolio site for my photography work. Use the images in my project folder, make it mobile-friendly, and give me a preview link by Friday.”

1. Grok Bot restates the three-page site and Friday preview, then asks only for any missing detail that blocks the work, such as which project folder to use.
2. It classifies the work as a website task and proposes a technical lead, a builder and a code reviewer. It reuses suitable existing teammates where possible.
3. If machine access is available, it lists registered machines and checks the selected machine for known coding CLIs. It asks for the required approval before each discovery or execution command. If none is available, it proceeds without them.
4. If room creation is supported, it opens a room with the requested pages, mobile requirements, deadline, approved source folder and preview destination. The lead writes a short plan and the reviewer checks it.
5. The builder and any approved CLI agent implement the pages in the user's project folder. Grok Bot inspects the output and has the reviewer check the links and mobile layout.
6. Grok Bot shares the preview link only if the connected tools actually created one. Its final note identifies the agents and CLIs that participated and flags anything not completed.

This is an illustrative workflow, not a claim that Grok Bot has created a room, run commands or generated a preview.

## Limits

- Local CLI discovery only reports commands found on PATH; it does not confirm sign-in, licenses or successful execution.
- Machine access, room creation, teammate listing and agent creation depend on tools exposed in the connected Grok Bot environment.
- The skill does not install agents, grant permissions, bypass approvals or promise a particular model or service.
- A project may proceed without local CLIs, but Grok Bot must accurately report that they were unavailable or unused.
- Users must provide or approve project locations, commands and any external action according to the connected tools' requirements.

## License

This skill follows the repository's [CC BY 4.0 license](../../LICENSE).
