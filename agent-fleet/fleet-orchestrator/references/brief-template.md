# Brief template

Copy this into `PROMPT.txt` for every job. Delegates are weaker than the orchestrator: be literal and complete, and point at exact files and lines.

```text
JOB: <one-line goal>
TIER: DO | THINK            MODE: READ-ONLY | WRITE (job folder only)
TIME CAP: 25 minutes

CONTEXT (only what you need):
- <2–6 facts, with file paths and line numbers>

INPUT FILES (in this folder):
- <file> - <what it is>

YOU MAY CREATE / CHANGE:
- <exact files>
YOU MUST NOT TOUCH:
- <files and folders>; no git commit, no push, no installs, no network unless stated

STEPS:
1. ...
2. ...

GATES (run them and paste the real output; if a gate fails, fix and re-run):
- <command, e.g. tests, linter, `bash -n script.sh`, a JSON/schema validator>

DONE WHEN:
- <observable result, e.g. "out/report.md exists with sections A, B, C and every claim cites file:line">

OUTPUT:
- Write <file>. End your reply with: DONE <file> <one-line summary>, or FAILED <reason>.
- Separate facts (with a cited source) from guesses (marked GUESS). Never invent paths, numbers or results.
```

## Review brief (for a different vendor)

```text
JOB: Review <output file> produced by another agent for <goal>. READ-ONLY.
Check: correctness against the input files, missing requirements from the original brief (below),
invented facts, broken commands, security or privacy problems.
Report a list of: SEVERITY (high/med/low) - file:line - problem - fix. If nothing is wrong, say so and why.
ORIGINAL BRIEF:
<paste>
```

## Runner script for hosts without a shell

When the orchestrator is a chat AI (ChatGPT web, claude.ai, Claude Cowork), it cannot run the agents itself:
- **If it can write files** into a folder the user shared (for example Cowork), it writes the job folder plus this `run-fleet.ps1`.
- **If it cannot write files at all**, it prints **one setup script** in chat. That script creates the job folder, `PROMPT.txt` and `run-fleet.ps1` (for example with PowerShell here-strings), and the user copies and runs it.

Either way, the user runs one command and shares the `out/` files back.

```powershell
# run-fleet.ps1 - run every job tool in parallel, 25-minute cap, UTF-8 output, free-model fallback
$JobDir = $PSScriptRoot; $Out = Join-Path $JobDir 'out'
New-Item -ItemType Directory -Force $Out | Out-Null
$jobs = @(
  Start-Job -ArgumentList $JobDir,$Out {
    param($d,$o) Set-Location $d
    foreach ($m in '<free-model-1>','<free-model-2>') {
      $f = Join-Path $o 'opencode.md'
      opencode run -m $m 'Read PROMPT.txt and follow it.' 2>&1 | Out-File -Encoding utf8 $f
      $txt = Get-Content $f -Raw
      $failed = ($LASTEXITCODE -ne 0) -or ($txt.Length -lt 200) -or
                ($txt -match '(?i)\b(429|402)\b|quota|rate limit|insufficient|model .{0,40}not (found|supported)|socket connection was closed')
      if (-not $failed) { "model: $m" | Out-File -Append -Encoding utf8 $f; break }   # else: try the next free model
    }
  }
)
$jobs | Wait-Job -Timeout 1500 | Out-Null
$jobs | Where-Object State -eq Running | Stop-Job
$jobs | Remove-Job -Force
Get-ChildItem $Out -Filter *.md | ForEach-Object {
  $w = ((Get-Content $_.FullName -Raw) -split '\s+').Count
  if ($w -lt 30) { "[FAILED] $($_.Name) ($w words)" } else { "[OK] $($_.Name) ($w words)" }
}
```

User command: `powershell -ExecutionPolicy Bypass -File "<job-folder>\run-fleet.ps1"`
