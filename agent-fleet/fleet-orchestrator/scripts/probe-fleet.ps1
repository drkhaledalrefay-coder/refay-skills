<#
probe-fleet.ps1 - find every AI agent CLI on this Windows machine and report its real state.

Part of the fleet-orchestrator skill. Read-only: it never installs, logs in, or edits anything.
For each tool it reports three separate facts, because "installed" is not "usable":
  installed  - found on PATH / npm / known folders (or "broken": package present but launcher missing)
  auth       - a one-line smoke prompt answered (only with -Smoke)
  credits    - the smoke reply was not a quota / billing / model-rejected error (only with -Smoke)

Usage:
  powershell -NoProfile -ExecutionPolicy Bypass -File probe-fleet.ps1            # fast: presence + version
  powershell -NoProfile -ExecutionPolicy Bypass -File probe-fleet.ps1 -Smoke     # + 1 tiny prompt per tool (uses a few free/cheap tokens)
  ... -OutDir <folder>   # where fleet-status.json is written (default: next to this script)

Output: a table on screen and fleet-status.json (UTF-8, no BOM). Secrets, e-mails and tokens are redacted.
#>
[CmdletBinding()]
param(
    [switch]$Smoke,
    [string]$OutDir = '',
    [int]$SmokeTimeoutSec = 90
)
# Default: next to this script ($PSScriptRoot is empty inside param defaults on Windows PowerShell 5.1)
if (-not $OutDir) { $OutDir = if ($MyInvocation.MyCommand.Path) { Split-Path -Parent $MyInvocation.MyCommand.Path } else { (Get-Location).Path } }

# The expected answer (42) is not in the prompt, so a CLI that echoes the prompt can't fake a pass.
$Prompt = 'What is 17 plus 25? Reply with digits only.'

# name | npm package (for broken-launcher detection) | smoke args ({P} = prompt) | tier hint | notes
# Smoke recipes marked "verified" were run on a real Windows machine; others follow the tool's docs - confirm with --help.
$Catalog = @(
    @{ n='claude';       pkg='@anthropic-ai/claude-code'; smoke='-p "{P}"';                                   tier='think+do (paid plan)'; note='verified' }
    @{ n='codex';        pkg='@openai/codex';             smoke='exec --skip-git-repo-check "{P}"';           tier='think (plan quota)';   note='verified; needs empty stdin' }
    @{ n='gemini';       pkg='@google/gemini-cli';        smoke='-p "{P}"';                                   tier='do (free tier with Google login)'; note='documented' }
    @{ n='agy';          pkg=$null;                       smoke='"-p={P}"';                                   tier='think+do (Antigravity)'; note='verified; -p= form' }
    @{ n='cursor-agent'; pkg=$null;                       smoke='-p --trust --output-format text "{P}"';      tier='do (Cursor plan)';     note='verified; .ps1 launcher' }
    @{ n='opencode';     pkg='opencode-ai';               smoke='run -m {FREE} "{P}"';                        tier='do (free models)';     note='verified' }
    @{ n='cline';        pkg='cline';                     smoke='"{P}"';                                      tier='do (free models)';     note='verified' }
    @{ n='kilo';         pkg='@kilocode/cli';             smoke=$null;                                        tier='do (free models)';     note='check: kilo --help' }
    @{ n='qwen';         pkg='@qwen-code/qwen-code';      smoke='-p "{P}"';                                   tier='do (free tier)';       note='documented' }
    @{ n='copilot';      pkg='@github/copilot';           smoke='-p "{P}"';                                   tier='do (free tier)';       note='documented' }
    @{ n='grok';         pkg='@xai-official/grok';        smoke='-p "{P}"';                                   tier='think (xAI plan)';     note='verified' }
    @{ n='crush';        pkg='@charmland/crush';          smoke=$null;                                        tier='do (bring your key)';  note='check: crush --help' }
    @{ n='iflow';        pkg='@iflow-ai/iflow-cli';       smoke=$null;                                        tier='do';                   note='check: iflow --help' }
    @{ n='aider';        pkg=$null;                       smoke=$null;                                        tier='do (bring your key / local model)'; note='pip: aider-chat' }
    @{ n='goose';        pkg=$null;                       smoke=$null;                                        tier='do';                   note='check: goose --help' }
    @{ n='ollama';       pkg=$null;                       smoke='list';                                       tier='do (local, free, private)'; note='smoke = installed models' }
)

function Find-Tool([string]$Name) {
    $known = @(
        (Join-Path $env:LOCALAPPDATA "$Name\$Name.ps1"),
        (Join-Path $env:LOCALAPPDATA "$Name\bin\$Name.exe"),
        (Join-Path $env:USERPROFILE ".$Name\bin\$Name.exe"),
        (Join-Path $env:USERPROFILE ".local\bin\$Name.exe")
    )
    if ($env:APPDATA) { $known = @((Join-Path $env:APPDATA "npm\$Name.cmd")) + $known }
    foreach ($k in $known) { if ($k -and (Test-Path -LiteralPath $k)) { return $k } }
    $c = Get-Command $Name -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($c) { if ($c.Source) { return $c.Source } return $c.Name }
    return $null
}

function Test-BrokenLauncher([string]$Pkg) {
    if (-not $Pkg -or -not $env:APPDATA) { return $false }
    return Test-Path -LiteralPath (Join-Path $env:APPDATA ("npm\node_modules\" + $Pkg))
}

function Clean([string]$t) {
    if (-not $t) { return '' }
    $t = $t -replace '\x1B\[[0-9;?]*[a-zA-Z]', ''
    $t = $t -replace '[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+', '[email]'
    $t = $t -replace '(?i)(bearer|token|secret|api[_-]?key|password)\s*[:=]\s*\S+', '$1=[redacted]'
    return $t.Trim()
}

function Invoke-Tool([string]$Path, [string]$ArgLine, [int]$TimeoutSec, [string]$KeepDir = '') {
    $id = [guid]::NewGuid().ToString('N')
    $work = if ($KeepDir) { $KeepDir } else { Join-Path $env:TEMP "fleet-probe-$id" }
    New-Item -ItemType Directory -Force $work | Out-Null      # empty dir: agents cannot touch real files
    $out = Join-Path $work 'o.txt'; $err = Join-Path $work 'e.txt'; $in = Join-Path $work 'in.txt'
    [IO.File]::WriteAllText($in, "`r`n")                       # near-empty stdin so CLIs that read stdin don't hang
    $exe = $Path; $a = $ArgLine
    if ($Path -like '*.ps1') { $exe = 'powershell.exe'; $a = "-NoProfile -ExecutionPolicy Bypass -File `"$Path`" $ArgLine" }
    elseif ($Path -like '*.cmd' -or $Path -like '*.bat') { $exe = $env:ComSpec; $a = "/c `"`"$Path`" $ArgLine`"" }
    $res = [ordered]@{ exit = $null; timedOut = $false; text = '' }
    try {
        $p = Start-Process -FilePath $exe -ArgumentList $a -WorkingDirectory $work -NoNewWindow -PassThru `
             -RedirectStandardOutput $out -RedirectStandardError $err -RedirectStandardInput $in
        if (-not $p.WaitForExit($TimeoutSec * 1000)) { $res.timedOut = $true; try { $p.Kill() } catch {} }
        else { $res.exit = $p.ExitCode }
    } catch { $res.text = $_.Exception.Message }
    foreach ($f in $out, $err) { if (Test-Path $f) { $res.text += "`n" + (Get-Content $f -Raw -ErrorAction SilentlyContinue) } }
    if (-not $KeepDir) { Remove-Item -LiteralPath $work -Recurse -Force -ErrorAction SilentlyContinue }
    $res.text = Clean $res.text
    return $res
}

function Get-Verdict($r) {
    $t = $r.text
    if ($r.timedOut) { return @('unknown', 'unknown', 'timed out') }
    # Success first: CLIs print warnings (e.g. "model metadata not found") even when the answer is fine
    if ($t -match '(?m)^\s*\**42\**\.?\s*$') { return @('yes', 'yes', 'answered') }
    if ($t -match '(?i)not (signed|logged) in|login required|please (log|sign) ?in|unauthori[sz]ed|\b401\b|authenticate') { return @('NO', 'unknown', 'not logged in') }
    # A rejected DEFAULT model is not "no credits": the tool usually works with another model (-m <model>)
    if ($t -match '(?i)model .{0,60}(not supported|not found|does not exist|unknown model|not available)') { return @('yes', 'MODEL', 'default model rejected - try another model') }
    if ($t -match '(?i)insufficient|balance|quota|usage limit|rate limit|\b402\b|\b429\b|out of credits|billing') { return @('yes', 'NO', 'quota/credits') }
    if ($t -match '\b42\b') { return @('yes', 'yes', 'answered') }
    if ($t.Length -lt 3) { return @('unknown', 'unknown', 'empty output = failure') }
    return @('unknown', 'unknown', 'unexpected reply - read details')
}

$rows = @()
foreach ($c in $Catalog) {
    $path = Find-Tool $c.n
    $row = [ordered]@{ tool = $c.n; installed = 'no'; version = ''; auth = '-'; credits = '-'; tier = $c.tier; detail = $c.note; path = $path; models = @() }
    if (-not $path) {
        if (Test-BrokenLauncher $c.pkg) { $row.installed = 'BROKEN'; $row.detail = "package present but launcher missing - reinstall: npm i -g $($c.pkg)" }
        $rows += [pscustomobject]$row; continue
    }
    $row.installed = 'yes'
    $v = Invoke-Tool $path '--version' 20
    $row.version = (($v.text -split "`r?`n") | Where-Object { $_ -match '\S' } | Select-Object -First 1)

    if ($c.n -eq 'opencode') {
        # opencode prints nothing on its first run in a new folder: use one stable folder and retry once
        $ocDir = Join-Path $env:TEMP 'fleet-probe-opencode'
        $m = Invoke-Tool $path 'models' 30 $ocDir
        if ($m.text.Length -lt 5) { $m = Invoke-Tool $path 'models' 30 $ocDir }
        $row.models = @(($m.text -split "`r?`n") | Where-Object { $_ -match '(?i)free|big-pickle' } | ForEach-Object { $_.Trim() } | Select-Object -First 12)
    }
    if ($c.n -eq 'codex') {
        $cache = Join-Path $env:USERPROFILE '.codex\models_cache.json'
        if (Test-Path -LiteralPath $cache) {
            try { $row.models = @((Get-Content -LiteralPath $cache -Raw | ConvertFrom-Json).models | ForEach-Object { $_.slug } | Where-Object { $_ } | Select-Object -First 12) } catch {}
        }
    }
    if ($c.n -eq 'ollama') {
        $m = Invoke-Tool $path 'list' 20
        $row.models = @(($m.text -split "`r?`n") | Select-Object -Skip 1 | Where-Object { $_ -match '\S' } | ForEach-Object { ($_ -split '\s+')[0] })
    }

    if ($Smoke -and $c.smoke) {
        $args1 = $c.smoke.Replace('{P}', $Prompt)
        if ($args1 -match '\{FREE\}') {
            $free = ($row.models | Select-Object -First 1)
            if (-not $free) { $row.detail = 'no free model listed by: opencode models'; $rows += [pscustomobject]$row; continue }
            $args1 = $args1.Replace('{FREE}', $free)
        }
        if ($c.n -eq 'ollama') {
            if ($row.models.Count) { $row.auth = 'n/a'; $row.credits = 'free (local)'; $row.detail = "$($row.models.Count) local model(s)" }
            else { $row.auth = 'n/a'; $row.credits = 'n/a'; $row.detail = 'no local models - try: ollama pull <model>' }
        } else {
            $r = Invoke-Tool $path $args1 $SmokeTimeoutSec
            $verdict = Get-Verdict $r
            $row.auth = $verdict[0]; $row.credits = $verdict[1]
            $first = (($r.text -split "`r?`n") | Where-Object { $_ -match '\S' } | Select-Object -Last 1)
            if ($first -and $first.Length -gt 140) { $first = $first.Substring(0, 140) + '...' }
            $row.detail = "$($verdict[2]): $first"
            # Default model rejected: retry with known models before calling the tool unusable
            if ($verdict[1] -eq 'MODEL' -and $c.n -eq 'codex' -and $row.models.Count) {
                foreach ($mdl in ($row.models | Where-Object { $_ -notmatch 'image|review|reserve' } | Select-Object -First 8)) {
                    $r2 = Invoke-Tool $path "exec --skip-git-repo-check -m $mdl `"$Prompt`"" $SmokeTimeoutSec
                    $v2 = Get-Verdict $r2
                    if ($v2[1] -eq 'yes') { $row.credits = 'yes'; $row.detail = "usable with -m $mdl (config default model rejected)"; break }
                }
            }
        }
    } elseif ($Smoke) { $row.detail = "$($c.note) (no headless recipe - test by hand)" }
    $rows += [pscustomobject]$row
}

try {
    New-Item -ItemType Directory -Force $OutDir -ErrorAction Stop | Out-Null
    [IO.File]::WriteAllText((Join-Path $OutDir '.write-test'), ''); Remove-Item (Join-Path $OutDir '.write-test') -Force
} catch { $OutDir = (Get-Location).Path; Write-Host "Skill folder not writable - saving to $OutDir" }
$report = [ordered]@{
    generated_at = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    os = 'windows'; smoke = [bool]$Smoke
    rule = 'A tool is usable only if installed=yes AND auth=yes AND credits=yes (or free local). credits=MODEL means only the default model was rejected: retry with -m <model> before calling the tool unusable. Anything else: say which state failed.'
    tools = $rows
}
$json = $report | ConvertTo-Json -Depth 5
[IO.File]::WriteAllText((Join-Path $OutDir 'fleet-status.json'), $json, (New-Object Text.UTF8Encoding $false))

$rows | Format-Table -AutoSize -Wrap tool, installed, version, auth, credits, tier, detail
Write-Host "Saved: $(Join-Path $OutDir 'fleet-status.json')"
if (-not $Smoke) { Write-Host 'Tip: add -Smoke to check login and credits with one tiny prompt per tool.' }
