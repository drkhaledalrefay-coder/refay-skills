# Detached "it's done" watcher. Usage (survives the agent session):
#   Start-Process powershell -WindowStyle Hidden -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File','<this file>','-Path','<final.mp4>'
param([Parameter(Mandatory = $true)][string]$Path)
while (-not (Test-Path -LiteralPath $Path)) { Start-Sleep 20 }
do { $a = (Get-Item -LiteralPath $Path).Length; Start-Sleep 15; $b = (Get-Item -LiteralPath $Path).Length } while ($a -ne $b)
Invoke-Item -LiteralPath $Path
Add-Type -AssemblyName PresentationFramework
[System.Windows.MessageBox]::Show("$(Split-Path -Leaf -LiteralPath $Path) is ready (written, not yet reviewed)", 'Motion Forge') | Out-Null
