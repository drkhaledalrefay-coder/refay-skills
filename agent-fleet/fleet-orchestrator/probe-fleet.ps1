[CmdletBinding()]
param(
    [switch]$Smoke
)

# Helper: locate tool executable across custom paths, npm bin, and PATH
function Find-ToolPath {
    param([string]$Name)

    if ($Name -eq 'dsh') {
        $dshCmd = Join-Path $env:LOCALAPPDATA 'Programs\DeepSeek Harness\resources\runtime\cli\bin\dsh.cmd'
        if (Test-Path $dshCmd) { return $dshCmd }
    }

    if ($Name -eq 'cursor-agent') {
        $caScript = Join-Path $env:LOCALAPPDATA 'cursor-agent\cursor-agent.ps1'
        if (Test-Path $caScript) { return $caScript }
    }

    if ($env:APPDATA) {
        $npmCmd = Join-Path $env:APPDATA "npm\$Name.cmd"
        if (Test-Path $npmCmd) { return $npmCmd }
    }

    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) {
        if ($cmd.Source) { return $cmd.Source }
        if ($cmd.Path) { return $cmd.Path }
        return $cmd.Name
    }

    return $null
}

# Helper: run process with redirected temp files and timeout
function Run-WithTimeout {
    param(
        [string]$FilePath,
        [string]$Arguments = "",
        [int]$TimeoutMs = 20000,
        [string]$WorkingDirectory = $null
    )

    $id = [System.Guid]::NewGuid().ToString('N')
    $stdoutFile = Join-Path $env:TEMP "fleet_${id}_out.log"
    $stderrFile = Join-Path $env:TEMP "fleet_${id}_err.log"

    $targetExe = $FilePath
    $targetArgs = $Arguments

    if ($FilePath -like '*.ps1') {
        $targetExe = "powershell.exe"
        $targetArgs = "-NoProfile -ExecutionPolicy Bypass -File `"$FilePath`" $Arguments"
    } elseif ($FilePath -like '*.cmd' -or $FilePath -like '*.bat') {
        $targetExe = if ($env:ComSpec) { $env:ComSpec } else { "cmd.exe" }
        $targetArgs = "/c `"`"$FilePath`" $Arguments`""
    }

    $pParams = @{
        FilePath               = $targetExe
        RedirectStandardOutput = $stdoutFile
        RedirectStandardError  = $stderrFile
        NoNewWindow            = $true
        PassThru               = $true
    }
    if ($targetArgs) {
        $pParams['ArgumentList'] = $targetArgs
    }
    if ($WorkingDirectory) {
        $pParams['WorkingDirectory'] = $WorkingDirectory
    }

    $timedOut = $false
    $exitCode = -1
    $proc = $null
    $errException = ""

    try {
        $proc = Start-Process @pParams
        $completed = $proc.WaitForExit($TimeoutMs)
        if (-not $completed) {
            $timedOut = $true
            try { $proc.Kill() } catch { }
        } else {
            $exitCode = $proc.ExitCode
        }
    } catch {
        $errException = $_.Exception.Message
    }

    $stdout = ""
    $stderr = ""

    if (Test-Path $stdoutFile) {
        $stdout = Get-Content -Path $stdoutFile -Raw -ErrorAction SilentlyContinue
        Remove-Item -Path $stdoutFile -Force -ErrorAction SilentlyContinue
    }
    if (Test-Path $stderrFile) {
        $stderr = Get-Content -Path $stderrFile -Raw -ErrorAction SilentlyContinue
        Remove-Item -Path $stderrFile -Force -ErrorAction SilentlyContinue
    }

    if ($errException) {
        if ($stderr) { $stderr = "$stderr`n$errException" }
        else { $stderr = $errException }
    }

    return [PSCustomObject]@{
        ExitCode = $exitCode
        Stdout   = if ($stdout) { $stdout.Trim() } else { "" }
        Stderr   = if ($stderr) { $stderr.Trim() } else { "" }
        TimedOut = $timedOut
    }
}

# Helper: scrub secrets, tokens, emails, and ANSI codes
function Sanitize-Text {
    param([string]$Text)

    if (-not $Text) { return "" }
    $clean = $Text -replace '\x1B\[[0-9;]*[a-zA-Z]', ''
    $clean = $clean -replace '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[REDACTED_EMAIL]'
    $clean = $clean -replace '(?i)(bearer|token|secret|api[_-]?key|password)\s*[:=]\s*\S+', '$1: [REDACTED]'
    return $clean.Trim()
}

$toolNames = @('agy', 'cline', 'opencode', 'cursor-agent', 'codex', 'grok', 'claude', 'dsh', 'ollama', 'gemini')

$tierMap = @{
    'agy'          = 'think / do'
    'cline'        = 'do'
    'opencode'     = 'do'
    'cursor-agent' = 'do'
    'codex'        = 'think'
    'grok'         = 'think'
    'claude'       = 'subagent (private data)'
    'dsh'          = 'do / think'
    'ollama'       = 'do / local'
    'gemini'       = 'think / do'
}

$defaultNotes = @{
    'agy'          = 'THINK: Gemini 3.1 Pro (High), Claude Opus 4.6; DO: Gemini Flash Low/Medium'
    'cline'        = 'DO tier: call cline.cmd on Windows; use plan mode (-p)'
    'opencode'     = 'DO tier: *-free models. Note: some paid models fail with insufficient funds (observed 2026-10-09)'
    'cursor-agent' = 'DO tier: verify flags with --help before running'
    'codex'        = 'THINK tier: use if quota permits'
    'grok'         = 'THINK tier: one short adversarial pass only, if authenticated'
    'claude'       = 'Anthropic Haiku subagents for sensitive/private data only'
    'dsh'          = 'DeepSeek Harness CLI (dsh headless). Uses account login (no API key) via ~/.claude/skills/deepseek-delegate/scripts/dsh-run.sh'
    'ollama'       = 'Local model runner'
    'gemini'       = 'THINK / DO tier'
}

$results = @()

foreach ($name in $toolNames) {
    $path = Find-ToolPath $name
    $available = [bool]($path -ne $null)
    $version = $null
    $models = @()
    $smokeResult = $null
    $notes = $defaultNotes[$name]

    if ($available) {
        $vRes = Run-WithTimeout -FilePath $path -Arguments "--version" -TimeoutMs 20000
        if ($vRes.Stdout) {
            $firstLine = ($vRes.Stdout -split "`r?`n" | Where-Object { $_ -match '\S' } | Select-Object -First 1)
            $version = Sanitize-Text $firstLine
        } elseif ($vRes.Stderr) {
            $firstLine = ($vRes.Stderr -split "`r?`n" | Where-Object { $_ -match '\S' } | Select-Object -First 1)
            $version = Sanitize-Text $firstLine
        }

        if ($name -eq 'agy') {
            $probeRes = Run-WithTimeout -FilePath $path -Arguments "--model __probe__ -p hi" -TimeoutMs 20000
            $probeOutput = "$($probeRes.Stdout)`n$($probeRes.Stderr)"
            $lines = $probeOutput -split "`r?`n"
            $captureModels = $false
            foreach ($line in $lines) {
                $cleanLine = Sanitize-Text $line
                if ($cleanLine -match 'Available models:') {
                    $captureModels = $true
                    continue
                }
                if ($captureModels) {
                    if ($cleanLine -match '^[-*•]\s*(.+)$') {
                        $models += $Matches[1].Trim()
                    } elseif ($cleanLine -ne '' -and $line -match '^\s+') {
                        $models += $cleanLine
                    } elseif ($cleanLine -eq '' -and $models.Count -gt 0) {
                        break
                    }
                }
            }

            if ($Smoke) {
                $smokeRun = Run-WithTimeout -FilePath $path -Arguments '--model "Gemini 3.8 Flash (Low)" --mode plan -p "Reply with OK"' -TimeoutMs 60000
                if ($smokeRun.ExitCode -eq 0 -and -not $smokeRun.TimedOut) {
                    $msg = Sanitize-Text $smokeRun.Stdout
                    if ($msg.Length -gt 200) { $msg = $msg.Substring(0, 200) }
                    $smokeResult = [PSCustomObject]@{
                        status  = 'ok'
                        message = if ($msg) { $msg } else { 'OK' }
                    }
                } else {
                    $rawErr = if ($smokeRun.TimedOut) { 'Timed out after 60s' } elseif ($smokeRun.Stderr) { $smokeRun.Stderr } else { $smokeRun.Stdout }
                    $cleanErr = Sanitize-Text $rawErr
                    if ($cleanErr.Length -gt 200) { $cleanErr = $cleanErr.Substring(0, 200) }
                    $smokeResult = [PSCustomObject]@{
                        status = 'fail'
                        error  = $cleanErr
                    }
                }
            }
        }

        if ($name -eq 'opencode') {
            $mRes = Run-WithTimeout -FilePath $path -Arguments "models" -TimeoutMs 20000
            if ($mRes.Stdout) {
                foreach ($line in ($mRes.Stdout -split "`r?`n")) {
                    $cleanLine = Sanitize-Text $line
                    if ($cleanLine -match '(?i)free|minimax') {
                        $models += $cleanLine
                    }
                }
            }

            $authRes = Run-WithTimeout -FilePath $path -Arguments "auth list" -TimeoutMs 20000
            if ($authRes.Stdout) {
                $authSummary = @()
                foreach ($line in ($authRes.Stdout -split "`r?`n")) {
                    $cleanAuth = Sanitize-Text $line
                    if ($cleanAuth -ne '') {
                        $authSummary += $cleanAuth
                    }
                }
                if ($authSummary.Count -gt 0) {
                    $joinedAuth = $authSummary -join '; '
                    if ($joinedAuth.Length -gt 150) { $joinedAuth = $joinedAuth.Substring(0, 150) + "..." }
                    $notes = "$notes | Auth: $joinedAuth"
                }
            }

            if ($Smoke) {
                $firstFree = $null
                foreach ($m in $models) {
                    if ($m -match '(?i)free') {
                        $firstFree = ($m -replace '^[-*•]\s*', '').Trim()
                        break
                    }
                }
                if (-not $firstFree) { $firstFree = 'opencode/free' }

                $smokeRun = Run-WithTimeout -FilePath $path -Arguments "run -m $firstFree `"Reply with OK`"" -TimeoutMs 60000
                if ($smokeRun.ExitCode -eq 0 -and -not $smokeRun.TimedOut) {
                    $msg = Sanitize-Text $smokeRun.Stdout
                    if ($msg.Length -gt 200) { $msg = $msg.Substring(0, 200) }
                    $smokeResult = [PSCustomObject]@{
                        status  = 'ok'
                        message = if ($msg) { $msg } else { 'OK' }
                    }
                } else {
                    $rawErr = if ($smokeRun.TimedOut) { 'Timed out after 60s' } elseif ($smokeRun.Stderr) { $smokeRun.Stderr } else { $smokeRun.Stdout }
                    $cleanErr = Sanitize-Text $rawErr
                    if ($cleanErr.Length -gt 200) { $cleanErr = $cleanErr.Substring(0, 200) }
                    $smokeResult = [PSCustomObject]@{
                        status = 'fail'
                        error  = $cleanErr
                    }
                }
            }
        }
    } else {
        if ($Smoke -and ($name -eq 'agy' -or $name -eq 'opencode')) {
            $smokeResult = [PSCustomObject]@{
                status = 'fail'
                error  = 'Tool not found on PATH or known directories'
            }
        }
    }

    $toolObj = [PSCustomObject]@{
        name       = $name
        path       = $path
        version    = $version
        available  = $available
        tier_hint  = $tierMap[$name]
        models     = $models
        smoke      = $smokeResult
        notes      = $notes
    }

    $results += $toolObj
}

$targetDir = $PSScriptRoot
if (-not $targetDir) {
    $targetDir = (Get-Location).Path
}

$statusFile = Join-Path $targetDir "fleet-status.json"

$fleetReport = [PSCustomObject]@{
    generated_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    tier_hints   = [PSCustomObject]@{
        think = @("Gemini 3.1 Pro (High)", "Claude Opus 4.6 (Thinking)", "codex", "grok")
        do    = @("Gemini Flash Low/Medium", "opencode *-free", "cline", "cursor-agent")
    }
    tools        = $results
}

$jsonText = $fleetReport | ConvertTo-Json -Depth 5
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($statusFile, $jsonText, $utf8NoBom)

$results | Format-Table -Property @(
    @{ Label = "Tool"; Expression = { $_.name }; Width = 14 },
    @{ Label = "Available"; Expression = { $_.available }; Width = 11 },
    @{ Label = "Version"; Expression = { if ($_.version) { $_.version } else { "-" } }; Width = 18 },
    @{ Label = "Tier"; Expression = { $_.tier_hint }; Width = 22 },
    @{ Label = "Smoke"; Expression = { if ($_.smoke) { $_.smoke.status } else { "-" } }; Width = 8 }
) -AutoSize
