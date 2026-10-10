# Fleet discovery and routing

## Probe (one call)

```bash
for c in codex grok cursor-agent agent cline agy claude opencode aider; do
  p=$(command -v $c 2>/dev/null) && echo "$c: $p ($($c --version 2>&1 | head -1))"; done
find ~/.claude/skills ~/.codex/skills ~/.agents/skills -maxdepth 1 -type d -name '*-delegate*' 2>/dev/null
command -v ffmpeg ffprobe; python -c "import faster_whisper" 2>/dev/null && echo whisper-ok
```

PowerShell equivalent:
```powershell
foreach ($c in 'codex','grok','cursor-agent','agent','cline','agy','claude','opencode','aider') {
  $p = Get-Command $c -ErrorAction SilentlyContinue
  if ($p) { "{0}: {1} ({2})" -f $c, $p.Source, ((& $c --version 2>&1) | Select-Object -First 1) } }
Get-ChildItem ~/.claude/skills, ~/.codex/skills, ~/.agents/skills -ErrorAction SilentlyContinue |
  Where-Object Name -like '*-delegate*' | Select-Object FullName
Get-Command ffmpeg, ffprobe -ErrorAction SilentlyContinue | Select-Object Source
```

Relay pattern: find the `<agent>-delegate` skill in `~/.claude/skills`, `~/.codex/skills` or
`~/.agents/skills` (do not assume one root), then run its `scripts/relay.mjs`, e.g.
`node <skill-dir>/scripts/relay.mjs --brief B.txt --cd <repo> --out-dir <dir> --timeout 30m`
Flags differ per relay — run `--help` once and note them (e.g. `--out-dir` not `--out`;
Codex `--read-only` is sandbox-enforced; AGY `--read-only` = plan mode; Cline `--plan`).

## Roster by fleet size

| Agents available | Builder | Reviewer | Fallback |
|---|---|---|---|
| 1 | it | same agent, read-only run, fresh session | — (time-box hard) |
| 2 | A | B (read-only) | the other one |
| 3+ | strongest free/included executor | different vendor, read-only | chain of the rest |
| many | split by output file ownership (opening / body / audio) | cheap cross-checker on every important output | chain |

Observed strengths (update as you learn):
- **Grok**: reliable ffmpeg/edit executor, has vision on contact sheets, uses local whisper. Best default builder.
- **Codex (gpt-*-sol)**: strongest reviewer/planner; built-in image generation for plates; credits run out → never the only path. Its sandbox may not write some drives.
- **AGY (Gemini)**: good image/PDF reader. If headless needs permission skipping, ask the director
  once and use it only inside a disposable work folder with the brief's write allowlist; otherwise
  route to another agent.
- **Cursor**: solid builder via PowerShell; plan mode may stop early → resume "implement now".
- **Cline free models**: bulk/cheap checks; daily caps → never the only path.

## Credit / limit handling

- Codex usage-limit message gives a reset time — queue the job after it, or reroute now.
- A relay "completed" with an empty final message = check events tail for the real error.
- Classifier/tool hiccups on your side: retry once, then tell the director in one line.

## Cross-session work

If another session owns part of the product (e.g. a separate motion video), message it with
`SendMessage` (first line = the point). Never edit its files; copy read-only. When a peer corrects
scope, re-read the director's own words — only the director decides ownership.
