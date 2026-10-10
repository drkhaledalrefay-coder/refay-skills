---
name: fleet-orchestrator
description: "Route work to a local AI CLI fleet so your coding agent only orchestrates. Use when the user says \"use the fleet\", \"delegate\", \"save your tokens\", \"you are the orchestrator\", or on any multi-step review/coding/research task. Probes which CLIs work, sends thinking/debate to strong models and inspection/coding to cheap or free models, then verifies the results."
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Fleet Orchestrator

## Role
The orchestrating agent acts strictly as an **orchestrator**:
- Scopes the task and breaks it into discrete subtasks.
- Prepares isolated working directories and `PROMPT.txt` files.
- Launches local fleet CLIs in the background with timeouts.
- Spot-checks claims against actual source files.
- Synthesizes findings in a single concise pass.
- **NEVER** read whole files or perform bulk analysis directly. Reserve tokens for orchestration and verification.

## Step 1: Probe Fleet
Before dispatching work, verify local CLI availability:
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$HOME\.claude\skills\fleet-orchestrator\probe-fleet.ps1"
```
- Add `-Smoke` for a live 1-prompt test of primary tools.
- Read `fleet-status.json` located next to the probe script.
- Re-probe if `fleet-status.json` is older than 12 hours or when a CLI fails unexpectedly.

## Step 2: Routing Table by Tier

| Tier | Purpose | Recommended CLIs & Models |
|---|---|---|
| **THINK** | Planning, debate, adversarial review, final synthesis, advisor | `agy --model "Gemini 3.1 Pro (High)"`<br>`agy --model "Claude Opus 4.6 (Thinking)"`<br>`codex` (if quota permits)<br>`grok` (one short adversarial pass only, if authenticated) |
| **DO** | Inspection, extraction, counting, drafting code, reformatting | `agy --model "Gemini 3.8 Flash (Low)"` or `(Medium)`<br>`opencode run -m opencode/<any *-free model>`<br>`cline` (default free provider)<br>`cursor-agent`<br>`dsh headless` (deepseek-flash via account login, no API key; verified 2026-10-10) |
| **PRIVATE** | Sensitive personal memory, billing, credentials, private team data | In-agent subagents (small/fast model) only. **NEVER** send private data to external CLIs. |
| **PAID/BLOCKED** | Depleted accounts / paid credits | `opencode/minimax-m3` returned "Insufficient account funds" on 2026-10-09 — skip it unless the user tops up. Never buy credits or change subscriptions on the user's behalf. |

## Step 3: Invocation Recipes (Windows)
Always run from an **isolated working directory** containing ONLY copies of needed files plus a `PROMPT.txt`:
- **Argument limit**: Windows command line limit is ~8191 characters. Never inline large prompts; put all instructions in `PROMPT.txt`.
- **Background execution**: Run fleet calls with background execution (`run_in_background`) and a timeout; redirect output to `<dir>\out\<tool>.md`.

### Recipes:
- **agy**:
  ```bash
  agy --model "<model>" --mode plan --sandbox --print-timeout 600s -p "Read PROMPT.txt and follow it. Read-only."
  ```
  *(Use `--mode accept-edits` only when the task is to write files inside that isolated directory.)*
- **cline**:
  ```bash
  cline.cmd -p -c "<dir>" "Read PROMPT.txt and follow it. Read-only."
  ```
  *(Call `cline.cmd` explicitly; Git Bash cannot resolve bare `cline`. Note: `--auto-approve false` blocks file reads in non-TTY; plan mode `-p` is the safe read-only route.)*
- **opencode**:
  ```bash
  opencode run -m opencode/<free-model> "Read PROMPT.txt and follow it."
  ```
  *(Run with cwd set to the isolated directory.)*
- **cursor-agent**:
  ```powershell
  powershell -File "$env:LOCALAPPDATA\cursor-agent\cursor-agent.ps1" -p "Read PROMPT.txt and follow it."
  ```
  *(Verify flags with `--help` before running.)*
- **dsh (DeepSeek Harness)**: run with cwd set to the isolated directory. Call the exe directly, because Git Bash → `dsh.cmd` breaks on the space in "DeepSeek Harness":
  ```bash
  bash "$HOME/.claude/skills/deepseek-delegate/scripts/dsh-run.sh" "<isolated-dir>" "<dir>/PROMPT.txt" "<dir>/out/dsh"
  ```
  *(The wrapper sends the brief through stdin, captures final.md, stderr.txt and result.txt, and flags a missing credential. For the full implementer loop, see the `deepseek-delegate` skill if it is installed.)*
  *(Only flags are `--json` and `--session-id`; there's no cwd, model or permission flag. Permission mode and model come from the app's profile (GUI default "Workspace Write"), so it can write in cwd: always use an isolated dir. Auth = the user's account login via the wrapper's `account.patch.yml` overlay; no API key needed (verified 2026-10-10).)*

## Step 4: Verification Rules
- **Every fleet claim is a hypothesis**: Never accept external output as ground truth. Free/cheap models hallucinate details (e.g. 2026-10-09: a free model claimed regex `r="48"` matches `r="487"` and styles were dropped; both false).
- **Spot-check high-impact claims**: Check source lines directly before taking action.
- **Downgrade exaggerated severities**: Verify whether alleged bugs or critical alerts are genuine.
- **Record attribution**: Track which tool produced which finding.

## Guardrails
- **Read-only by default**: Never mutate user data or run write/apply paths without the user's explicit approval.
- **Privacy protection**: Never send emails, account IDs, billing, family, credentials, or private team data to external CLIs.
- **Zero expenditure**: Never spend paid credits or modify subscriptions.
- **No external publishing**: No `git push`, publish, or remote modifications.

## Cost Rule
- Strong models for few, short, high-leverage calls (plan, debate, final critique).
- Cheap models for many, long, mechanical calls.

## Output
Produce a short table summarizing fleet actions and verification status:

| Tool | Model / Tier | Subtask | Execution Status | Verification Result |
|---|---|---|---|---|
| agy | Gemini 3.8 Flash (Low) | Inspect regex matching | Done | Verified (claim r="48" matching r="487" was false) |

## Lessons (2026-10-09)
- agy headless auto-denies the "command" permission: it cannot list directories or run shell, and multi-file prompts may fail with "no output produced". Concatenate inputs into ONE bundle file (e.g. BUNDLE.md) and tell it: "read only BUNDLE.md with the file-read tool; do not list or run commands; print result to stdout".
- Always check output size after a fleet chain; an rc=0 with 0 words is a failure.
- codex exec waits on stdin ("Reading additional input from stdin...") and hangs in background: always append `< /dev/null`.

## Lessons (2026-10-10)
- agy headless WRITE tasks fail ("write_file permission ... auto-denied") unless the user approves `--dangerously-skip-permissions`. Use agy for read-only; route writes to opencode or codex.
- codex `-s workspace-write` is the safe write lane, but quota runs out ("usage limit ... try again at <time>"). Check before relying on it.
- opencode free models can drop the connection mid-run ("socket connection was closed"). One retry with a different free model worked (`opencode/mimo-v2.6-flash-free` wrote 4 docs files correctly; one wrong command was caught in review).

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
