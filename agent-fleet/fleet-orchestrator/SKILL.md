---
name: fleet-orchestrator
description: >-
  Turn the main AI (Claude Code, Cursor, Antigravity, Codex, ChatGPT or any chat AI) into the
  orchestrator of every AI agent on the user's computer: discover which agent CLIs are really
  installed, logged in and funded (never claim "not available" without proof), suggest free
  agents worth installing, then split the task into jobs, route thinking to strong models and bulk
  work to cheap or free ones, brief and dispatch them, and verify every result before reporting.
  Use when the user says "use my agents", "what AI tools do I have", "find free agents",
  "use the fleet", "delegate", "save your tokens", "you are the orchestrator", or on any
  multi-step coding, review, research or writing task. For long multi-agent builds with strict
  time-boxing see fleet-conductor; for videos see motion-forge.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Fleet Orchestrator v2

Most people have several AI agents on their computer and use one. Many of those agents are free. This skill makes the main AI find them all, recruit missing free ones, and run them like an orchestra: the main AI plans and judges, the fleet plays.

## When to use / not use

- **Use** for any task with more than a few steps, any bulk or repetitive work, any review that needs a second opinion, or when the user asks what agents they have.
- **Don't use** for a one-line answer or a tiny edit: delegation overhead is not worth it.
- **Related skills:** `fleet-conductor` adds strict time-boxing and delegated gates for long builds. `motion-forge` runs a fleet for video production. Use those on top of this one.

## The orchestrator's three laws

1. **No lazy "not available".** You may say a tool is missing, logged out or out of credits **only** after running its check and quoting the output. "I don't have access to other agents" is never an acceptable answer before Step 1. If you have no shell, the user runs the check for you (Step 0) and you quote what they paste back.
2. **You think, the fleet works.** Spend your own tokens on planning, briefing and verifying. Bulk reading, scanning, drafting and coding go to the fleet.
3. **Every fleet claim is a hypothesis.** Agents (free ones especially) invent details and report success they did not achieve. Check the files on disk before you believe or report anything.

## Step 0 — Know your host

| Your situation | What you do |
|---|---|
| You can run shell commands (Claude Code, Cursor, Antigravity, Codex, OpenCode…) | Run the probe yourself (Step 1). |
| Chat only, no shell (ChatGPT web, claude.ai, Gemini web, Claude Cowork) | Give the user the probe command to run (Step 1), ask them to paste back the table, and build the fleet from it. For dispatch: if you can write into a folder they shared, write the job folders and **one runner script**. If you can't write files, print **one setup script** in chat that creates them. Then read the outputs they share. See `references/brief-template.md`. |

## Step 1 — Discover the fleet (mandatory, first)

Run the probe. Use `-Smoke` / `--smoke` the first time and whenever a tool fails unexpectedly:

```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -File "<skill-folder>/scripts/probe-fleet.ps1" -Smoke
```
```bash
# macOS / Linux
bash "<skill-folder>/scripts/probe-fleet.sh" --smoke
```

The probe checks ~16 known agent CLIs and writes `fleet-status.json` next to itself. Every tool gets **three separate states**:

| State | Meaning | Typical fix (tell the user; never do it for them) |
|---|---|---|
| `installed` = no / BROKEN | Not on this machine / package present but launcher missing | Install or reinstall (Step 2) |
| `auth` = NO | Installed but not logged in | `<tool> login` (interactive, the user does it) |
| `credits` = MODEL | Only the **default** model was rejected (common after plan changes) | The tool still works: re-run with `-m <model>` from its model list. The probe already retries known models for you. |
| `credits` = NO | Logged in but out of quota or billing | Pick a free model, wait for the reset, or skip the tool |

A tool is **usable** only when all three pass (or it is a free local runner such as Ollama). Re-probe if `fleet-status.json` is older than 12 hours. Also list what lives *inside* your own host: sub-agents, cheaper models, built-in tools. They are fleet members too.

Then **tell the user the fleet in one table**: tool, usable yes/no, which state failed, tier.

## Step 2 — Fill the gaps with free agents (suggest, never install silently)

If the fleet has fewer than two usable vendors, or no free executor, suggest additions from `references/agent-catalog.md`:

1. Pick at most 2–3 candidates that fit the user's OS and task.
2. **Re-check the install command against the official page or package registry before showing it.** Catalogs go stale. Never install from memory.
3. Show the command and say what it costs (free tier, own API key or paid) and what it needs (account, Node, Python).
4. **By default, the user runs the install command.** Run it yourself only if the user explicitly asks you to *and* your host asks for approval before running commands. Then re-run the probe. Logins are always done by the user.

## Step 3 — Plan like an architect

1. **Decompose** the task into jobs. Each job has one goal, one owner and its own files. Two agents never edit the same file at once.
2. **Classify** each job:

| Tier | Work | Route to |
|---|---|---|
| THINK | plan, design, debate, adversarial review, final judgement | the strongest models available, used for **few and short** calls |
| DO | read, scan, extract, count, draft, code, convert, format | the cheapest usable executors: free models first |
| PRIVATE | personal data, credentials, billing, private team or customer data | **only** your own host (it already holds the data; use its sub-agents) or a local model such as Ollama. Never another CLI, not even one from the same vendor. |

3. **Choose model IDs from the live probe**, never from memory. Model names change monthly.
4. **Builder vendor ≠ reviewer vendor.** For example: a free OpenCode model builds, then a Gemini model or your own pass reviews.
5. **Spread across vendors.** Run parallel jobs on different tools so one quota cap doesn't stop everything. Two to three parallel jobs per project is plenty.
6. For hard or irreversible decisions, ask two THINK models from different vendors for one plan each (read-only), then decide yourself.

## Step 4 — Brief every job

Write `PROMPT.txt` from `references/brief-template.md`. Every brief contains:

- the goal and the definition of done;
- the context it needs (and nothing more);
- **exact files it may create or change, and files it must not touch**;
- the gate commands to run (tests, lint, a parser check, a validator);
- the output format and the output file;
- the limits: read-only or write, no commits, no installs, no network unless needed, and a time cap.

Agents are weaker than you. Give file paths and line numbers, not "reuse the existing helper".

## Step 5 — Dispatch

Follow `references/dispatch-recipes.md` for exact per-tool commands and the OS gotchas. The essentials:

- **Isolated job folder** per job: copies of the needed files + `PROMPT.txt` + `out/`. Never point a delegate at the user's real folders for write work.
- **Prompts live in files.** Windows limits command lines to ~8,191 characters.
- **Background + time cap.** 25–45 minutes. One output file per tool: `out/<tool>.md`.
- **Fallback chain** for bulk jobs: free model A → free model B → another vendor. Treat quota errors, "model not found", empty output or a one-line early stop as FAILED and move on.

## Step 6 — Verify (zero leniency)

1. **Exit code 0 with empty or tiny output means FAILED.**
2. **Run the gates yourself**, or have a different vendor run them. Don't trust the agent's word that tests passed.
3. **Spot-check the high-impact claims** against the real files: one grep or one line read per claim. If an agent says "0 problems found", check that number with your own search.
4. **Downgrade exaggerated severities.** Reject invented facts.
5. **Uniform perfect results** (14/14 pass, 100% complete) are a red flag. Look closer.

## Step 7 — Report

Report to the user only when something finishes or a decision is needed:

| Tool | Model / tier | Job | Status | Verified by / result |
|---|---|---|---|---|
| opencode | free model / DO | draft docs | done | your grep: 2 wrong paths fixed |

Then: what changed on disk, what failed and why, what the user must do (logins, approvals), and the next step.

## Guardrails (non-negotiable)

- Read-only by default. Writes only inside job folders. Applying changes to the user's real files needs their OK.
- Never send private data to external CLIs. Never paste secrets into prompts.
- Never spend money: no paid models without a clear yes, no buying credits, no subscription changes.
- Never push, publish, deploy, email or post. Delegates never commit; you commit only when the user asks.
- Never bypass an agent's permission system (e.g. "skip all permissions" flags) without the user's explicit OK, and only inside a job folder.

## References

- `scripts/probe-fleet.ps1` / `scripts/probe-fleet.sh`: fleet discovery with the three-state check.
- `references/agent-catalog.md`: known agent CLIs, official install sources, cost model, best use.
- `references/dispatch-recipes.md`: headless commands per tool, OS gotchas, lessons from real runs.
- `references/brief-template.md`: the job brief and the runner script for no-shell hosts.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
