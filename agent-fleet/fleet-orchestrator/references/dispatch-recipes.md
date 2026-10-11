# Dispatch recipes

Exact ways to run each agent headless from a job folder, plus the traps that break real runs. Every command assumes the current directory is the isolated job folder that holds `PROMPT.txt`. Confirm flags with `<tool> --help`, because CLIs change often.

## Job folder layout

```
jobs/<job-name>/
  PROMPT.txt      # the brief (references/brief-template.md)
  BUNDLE.md       # optional: all inputs pasted into ONE file (for agents that can't list folders)
  <copies of only the files the job needs>
  out/            # one result file per tool: out/<tool>.md
```

## Per-tool commands

| Tool | Read-only job | Write job (inside the job folder only) | Notes |
|---|---|---|---|
| opencode | `opencode run -m <free-model> "Read PROMPT.txt and follow it. Read-only."` | same, without "Read-only" | Needs `-m`: there is no safe default model. Free models can drop the connection, so retry once with another free model. |
| agy | `agy --model "<model>" --mode plan --sandbox --print-timeout 600s "-p=Read BUNDLE.md with the file-read tool only and follow it. Print the result."` | `--mode accept-edits`; file writes may still be auto-denied | Headless agy auto-denies shell, folder listing and often writes. Give it **one bundle file** and use it read-only. Attach the prompt as one quoted `-p=` argument and keep it **last**. |
| cline | `cline -p -c "<dir>" "Read PROMPT.txt and follow it. Read-only."` | `cline -c "<dir>" "..."` | `-p` = plan mode (read-only). On Windows from Git Bash call `cline.cmd`. |
| gemini | `gemini -p "Read PROMPT.txt and follow it. Read-only."` | add the approval flag from `--help` only with the user's OK | |
| qwen | `qwen -p "..."` | as gemini | |
| copilot | `copilot -p "..."` | per `--help` | |
| cursor-agent | `cursor-agent -p --trust --output-format text "Read PROMPT.txt and follow it. Read-only."` | add `--force` only for write jobs | `--trust` is needed in a new folder. On Windows it is a `.ps1`, so launch it from PowerShell (Git Bash can't). |
| codex | bash: `codex exec --skip-git-repo-check -s read-only -m <model> "..." < /dev/null` · PowerShell: `$null \| codex exec ...` | `-s workspace-write` (if the sandbox works on the OS) | It waits on stdin and hangs in the background without the empty-stdin trick. The read-only sandbox can fail on Windows; then send only text-only review jobs, or use another tool. |
| claude | `claude -p --model <small-model> "..."` | per `--help` | Cheap cloud lane for summaries. **Not** a PRIVATE lane: it sends data to the cloud. |
| grok | `grok -p "..."` | per `--help` | One short adversarial pass is usually enough. |
| ollama | bash: `ollama run <model> < PROMPT.txt` · PowerShell: `Get-Content PROMPT.txt -Raw \| ollama run <model>` | n/a (text only) | No file access: put the content inside PROMPT.txt and send it through stdin (never as an argument: Windows' length limit). Fully private. |
| aider | `aider --no-auto-commits --yes-always --message "Read PROMPT.txt and follow it." PROMPT.txt <files>` | same | aider **commits by default**: always pass `--no-auto-commits`. |

## Running jobs in parallel

**bash** (Linux; on macOS install GNU `timeout` with `brew install coreutils`, which provides it as `gtimeout`)
```bash
T=$(command -v timeout || command -v gtimeout)     # empty on a stock Mac: install coreutils first
(
  cd "jobs/<job>" && mkdir -p out
  ( "$T" 25m opencode run -m "$FREE1" "Read PROMPT.txt and follow it." > out/opencode.md 2>&1 ) &
  ( "$T" 25m gemini -p "Read PROMPT.txt and review. Read-only." > out/gemini.md 2>&1 ) &
  wait; wc -w out/*.md
)
```

**PowerShell** (Windows PowerShell 5.1). `Start-Job` starts in your home folder, so pass an **absolute** path.
```powershell
$d = (Resolve-Path "jobs\<job>").Path; New-Item -ItemType Directory -Force "$d\out" | Out-Null
$jobs = @(
  Start-Job { Set-Location $using:d; opencode run -m "<free-model>" "Read PROMPT.txt and follow it." 2>&1 | Out-File -Encoding utf8 out\opencode.md }
  Start-Job { Set-Location $using:d; gemini -p "Read PROMPT.txt and review. Read-only." 2>&1 | Out-File -Encoding utf8 out\gemini.md }
)
$jobs | Wait-Job -Timeout 1500 | Out-Null; $jobs | Stop-Job; $jobs | Remove-Job -Force
Get-ChildItem "$d\out" | ForEach-Object { "$($_.Name): $(((Get-Content $_.FullName -Raw) -split '\s+').Count) words" }
```

## Traps that broke real runs

| Trap | Fix |
|---|---|
| PowerShell 5.1 `>` writes **UTF-16**; other tools then read garbage | `\| Out-File -Encoding utf8` (5.1 adds a BOM, which agents read fine). For a strict tool: `[IO.File]::WriteAllText($path, $text, (New-Object Text.UTF8Encoding $false))` |
| `< NUL` / `< /dev/null` don't work in PowerShell | `$null \| <command>` |
| Windows command line limit ~8,191 chars | Put the prompt in `PROMPT.txt` and pass a short "Read PROMPT.txt" instruction |
| `.ps1` launchers (cursor-agent and others) fail from Git Bash | Launch from PowerShell |
| Paths with spaces break unquoted commands | Always quote paths |
| Exit code 0, empty output | FAILED: re-dispatch to the next model |
| Agent "plans" and stops after one turn in plan/read-only mode | A one-shot run has ended and has no memory. Either resume the same session (the tool's `--continue` / `--resume <id>` / `exec resume` flag, see `--help`), or re-dispatch with the brief plus "Do not stop at a plan: print the final output." |
| Probe says `credits=MODEL` | Only the default model was rejected. Pass `-m <model>` from the probe's model list. |
| `opencode models` prints nothing | It happens on the first run in a new folder: run it again in the same folder |
| Agent reports "0 hits" or "all tests pass" | Check that with your own grep or by running the tests |
| A free model claims a regex matches or a style was dropped | Check the source line before acting on it |
| Quota or model-rejected errors (402, 429, "insufficient", "not supported") | Mark credits=NO, go to the next model in the chain, then re-probe later |
| Sandboxes can't write to cloud-synced drives | Run the job in a local folder, then copy the result back |
| Laptop sleep or network drop looks like a hang | Check the output file timestamps before killing the job or dispatching again |
