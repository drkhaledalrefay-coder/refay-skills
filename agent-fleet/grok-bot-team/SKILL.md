---
name: grok-bot-team
description: >-
  Organize a substantial project task in Grok Bot by creating a focused team
  room, recruiting suitable agents, and, when a registered machine is available,
  identifying and coordinating installed CLI agents. Use for requests to build
  a project team, delegate a multi-step task, or use local CLI agents with Grok.
  Do not use for small one-step requests or personal operations that need no
  room.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Grok Bot Team

Set up a focused project room and coordinate the agents and optional local CLI tools that Grok Bot can actually access.

## When to use

Use for substantial, multi-step work that benefits from distinct planning, production and review roles. Do not create a room for a quick one-step answer or personal operations such as sending mail or changing a calendar.

## Prerequisites

- Grok Bot with the room, agent and machine tools available in the connected environment. Use only capabilities exposed there; do not assume a tool exists because a name appears in an example.
- A user machine registered and available through Grok Bot to discover local command-line tools.
- Optional CLI agents installed on that machine. If none are found or the machine is unavailable, continue without claiming they ran.

## Workflow

1. **Confirm the outcome.** Briefly restate the deliverable and any known format or deadline. Ask only for missing information that would change the work; group questions into one message.
2. **Classify the work and decide whether a room helps.** Select the smallest useful set of roles. Examples:
   | Task | Possible roles |
   |---|---|
   | Video or reel | Director, editor, visual reviewer |
   | Deck or report | Strategist, writer/designer, fact checker |
   | Website, app or code | Technical lead, builder, code reviewer |
   | Research or analysis | Analyst, researcher, source checker |
   | Campaign or content | Marketer, copywriter, brand reviewer |
   Keep the team to 3–5 members when the available tools support that.
3. **Recruit only through available tools.** Check whether suitable existing teammates can be reused. Create a focused agent only if the connected Grok Bot tools explicitly support it and a role is missing. Do not claim an agent was created unless the tool confirms it. Follow the user's approval rules for external actions.
4. **Discover optional CLI agents on a registered machine.** First confirm that the machine-listing capability is available and the user has a registered machine. Select the intended machine if more than one is available. Run discovery commands only through the connected machine tool and obtain the required approval before each command. Never run a command against an unregistered or inferred computer.

   **Windows PowerShell:**
   ```powershell
   $names = 'claude','codex','gemini','agy','cursor-agent','opencode','cline','aider','grok','copilot','qwen','kimi','ffmpeg'
   foreach ($name in $names) {
     $command = Get-Command $name -ErrorAction SilentlyContinue
     if ($command) { '{0}\t{1}' -f $command.Name, $command.Source }
   }
   ```

   **macOS or Linux (POSIX shell):**
   ```sh
   for name in claude codex gemini agy cursor-agent opencode cline aider grok copilot qwen kimi ffmpeg; do
     command -v "$name" 2>/dev/null || true
   done
   ```

   These commands only locate commands on PATH; they do not prove a tool can authenticate or run. Record only what discovery returns. Route code tasks to suitable coding CLIs, long reading to suitable text agents, and media conversion to ffmpeg when present. Before launching any discovered CLI, explain the proposed command and task to the user and obtain the required approval. Run it in the user's selected project folder, give it a bounded brief and completion check, then inspect its output. Do not install tools or use paid services without explicit authorization.
5. **Open and brief the room.** If room creation is available, use a concise name such as `<Project> — <deliverable>`. Include the deliverable, deadline, format, constraints, source and output locations supplied by the user, roles, discovered CLIs and their proposed work, and review order. Do not invent paths or project details.
6. **Coordinate the work and review.** Use the available room features to share decisions, results and blockers. Follow this order where supported:
   - Plan: lead defines an outline or specification; reviewer checks it against the request.
   - Build: makers and approved CLI agents produce their assigned work.
   - Review: an independent reviewer checks the result and lists any fixes.
   - Deliver: provide the agreed files or links. Do not overwrite earlier versions without permission.
7. **Report accurately.** Summarize what was produced, which agents or CLIs actually participated, what was checked, and any remaining limits. Never claim a machine, agent, command, upload or review succeeded without confirmation from the relevant tool.

## Rules

- Use only tools and actions Grok Bot exposes in the current connection; examples do not establish tool availability.
- Follow the connected tools' approval requirements. Get explicit approval before sending, deleting, publishing, paying, installing software or running a local CLI command.
- Keep the room focused. Share only information needed for the task, and honor the user's privacy and tool restrictions.
- Do not invent results, sources, numbers, agent capabilities or tool credits.
- When tools are unavailable, say what could not be done and continue with the parts that are possible.

## Outputs

A coordinated project room when supported, a concise plan, reviewed deliverables or links, and a clear report of which agents and optional local CLIs actually ran.

---

*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
