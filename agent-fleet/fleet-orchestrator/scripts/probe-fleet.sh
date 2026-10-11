#!/usr/bin/env bash
#
# probe-fleet.sh - find every AI agent CLI on this macOS/Linux machine and report its real state.
#
# POSIX bash port of probe-fleet.ps1. Part of the fleet-orchestrator skill.
# Read-only: it never installs, logs in, or edits anything.
# For each tool it reports three separate facts, because "installed" is not "usable":
#   installed  - found with `command -v` / known folders (or "BROKEN": npm package present but launcher missing)
#   auth       - a one-line smoke prompt answered (only with --smoke)
#   credits    - the smoke reply was not a quota / billing / model-rejected error (only with --smoke)
#
# Usage:
#   ./probe-fleet.sh                    # fast: presence + version
#   ./probe-fleet.sh --smoke            # + 1 tiny prompt per tool (uses a few free/cheap tokens)
#   ./probe-fleet.sh --out-dir DIR      # where fleet-status.json is written (default: this script's folder)
#   ./probe-fleet.sh --timeout SEC      # per smoke prompt timeout, default 90
#
# Output: a table on screen and fleet-status.json. Secrets, e-mails and tokens are redacted.
#
# Notes:
#   * No `set -e`: one failing tool must never stop the scan.
#   * Every CLI call runs in a fresh `mktemp -d` directory with stdin from /dev/null,
#     and is killed after the timeout (via `timeout`, `gtimeout`, or a background kill).
#   * No jq dependency: JSON is built by hand with a small json_escape helper.
#
set -u

# ---------------------------------------------------------------------------
# Defaults / options
# ---------------------------------------------------------------------------
# The expected answer (42) is not in the prompt, so a CLI that echoes the prompt can't fake a pass.
PROMPT='What is 17 plus 25? Reply with digits only.'

SELF="${BASH_SOURCE[0]:-$0}"
SCRIPT_DIR="$(cd "$(dirname "$SELF")" >/dev/null 2>&1 && pwd)"
DEFAULT_OUT_DIR="$SCRIPT_DIR"

SMOKE=0
OUT_DIR="$DEFAULT_OUT_DIR"
TIMEOUT_SEC=90

usage() {
    sed -n '2,25p' "$SELF" 2>/dev/null | sed 's/^# \{0,1\}//'
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        --smoke)   SMOKE=1; shift ;;
        --out-dir) OUT_DIR="${2-}"; shift 2 ;;
        --timeout) TIMEOUT_SEC="${2-}"; shift 2 ;;
        -h|--help) usage; exit 0 ;;
        *)         shift ;;
    esac
done

[ -n "$OUT_DIR" ] || OUT_DIR="$DEFAULT_OUT_DIR"
case "$TIMEOUT_SEC" in
    ''|*[!0-9]*) TIMEOUT_SEC=90 ;;
esac

# ---------------------------------------------------------------------------
# Platform + timeout runner
# ---------------------------------------------------------------------------
case "$(uname -s 2>/dev/null)" in
    Darwin) OS='macos' ;;
    *)      OS='linux' ;;
esac

TIMEOUT_CMD=''
if command -v timeout >/dev/null 2>&1; then
    TIMEOUT_CMD='timeout'
elif command -v gtimeout >/dev/null 2>&1; then
    TIMEOUT_CMD='gtimeout'
fi

ESC="$(printf '\033')"

# ---------------------------------------------------------------------------
# Tool catalog
# name | npm package (for broken-launcher detection) | smoke args ({P} = prompt) | tier hint | notes
# Smoke recipes marked "verified" were run on real machines; others follow the tool's docs - confirm with --help.
# ---------------------------------------------------------------------------
CATALOG=(
    'claude|@anthropic-ai/claude-code|-p "{P}"|think+do (paid plan)|verified'
    'codex|@openai/codex|exec --skip-git-repo-check "{P}"|think (plan quota)|verified; needs empty stdin'
    'gemini|@google/gemini-cli|-p "{P}"|do (free tier with Google login)|documented'
    'agy||"-p={P}"|think+do (Antigravity)|verified; -p= form'
    'cursor-agent||-p --trust --output-format text "{P}"|do (Cursor plan)|verified; shell launcher'
    'opencode|opencode-ai|run -m {FREE} "{P}"|do (free models)|verified'
    'cline|cline|"{P}"|do (free models)|verified'
    'kilo|@kilocode/cli||do (free models)|check: kilo --help'
    'qwen|@qwen-code/qwen-code|-p "{P}"|do (free tier)|documented'
    'copilot|@github/copilot|-p "{P}"|do (free tier)|documented'
    'grok|@xai-official/grok|-p "{P}"|think (xAI plan)|verified'
    'crush|@charmland/crush||do (bring your key)|check: crush --help'
    'iflow|@iflow-ai/iflow-cli||do|check: iflow --help'
    'aider|||do (bring your key / local model)|pip: aider-chat'
    'goose|||do|check: goose --help'
    'ollama||list|do (local, free, private)|smoke = installed models'
)

RULE='A tool is usable only if installed=yes AND auth=yes AND credits=yes (or free local). credits=MODEL means only the default model was rejected: retry with -m <model> before calling the tool unusable. Anything else: say which state failed.'

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Find a tool by name. PATH first (command -v), then well-known install folders.
find_tool() {
    local name="$1" c d
    c="$(command -v "$name" 2>/dev/null || true)"
    if [ -n "$c" ]; then printf '%s\n' "$c"; return 0; fi
    for d in "$HOME/.local/bin" "$HOME/.$name/bin" "$HOME/.npm-global/bin" "/opt/homebrew/bin" "/usr/local/bin"; do
        if [ -x "$d/$name" ]; then printf '%s\n' "$d/$name"; return 0; fi
    done
    return 1
}

# True when an npm package is installed globally but no launcher can be found.
test_broken_launcher() {
    local pkg="$1" root
    [ -n "$pkg" ] || return 1
    command -v npm >/dev/null 2>&1 || return 1
    root="$(npm root -g 2>/dev/null || true)"
    [ -n "$root" ] || return 1
    [ -e "$root/$pkg" ]
}

# Strip ANSI codes and redact e-mails / secrets, then trim.
clean_text() {
    local t="$1"
    t="$(printf '%s' "$t" | sed "s/${ESC}\[[0-9;?]*[a-zA-Z]//g")"
    t="$(printf '%s' "$t" | tr -d '\r')"
    t="$(printf '%s' "$t" | sed -E 's/[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+/[email]/g')"
    t="$(printf '%s' "$t" | sed -E 's/([Bb][Ee][Aa][Rr][Ee][Rr]|[Tt][Oo][Kk][Ee][Nn]|[Ss][Ee][Cc][Rr][Ee][Tt]|[Aa][Pp][Ii][_-]?[Kk][Ee][Yy]|[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd])[[:space:]]*[:=][[:space:]]*[^[:space:]]+/\1=[redacted]/g')"
    printf '%s' "$t" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'
}

# Small, dependency-free JSON string escaper.
json_escape() {
    local s="$1"
    s="${s//\\/\\\\}"
    s="${s//\"/\\\"}"
    s="${s//$'\n'/\\n}"
    s="${s//$'\r'/\\r}"
    s="${s//$'\t'/\\t}"
    printf '%s' "$s"
}

# Render a newline-separated list as a JSON string array.
json_string_array() {
    local data="$1" out='[' first=1 line
    while IFS= read -r line; do
        [ -n "$line" ] || continue
        if [ "$first" = 1 ]; then first=0; else out="$out, "; fi
        out="$out\"$(json_escape "$line")\""
    done <<EOF
$data
EOF
    printf '%s]' "$out"
}

# Truncate a string to N chars, appending "...".
trunc() {
    local s="$1" n="$2"
    if [ "${#s}" -gt "$n" ]; then printf '%s...' "${s:0:$((n - 3))}"; else printf '%s' "$s"; fi
}

# ---------------------------------------------------------------------------
# Run a CLI once, safely.
#   RES_TEXT     - combined stdout+stderr, ANSI-stripped and redacted
#   RES_TIMEDOUT - 1 if killed after the timeout
#   RES_EXIT     - exit code ('' when timed out)
# ---------------------------------------------------------------------------
RES_TEXT=''
RES_TIMEDOUT=0
RES_EXIT=''

invoke_tool() {
    local path="$1" argline="$2" tsec="$3" keep="${4-}"
    local work out err rc t e pid elapsed

    RES_TEXT=''; RES_TIMEDOUT=0; RES_EXIT=''

    if [ -n "$keep" ]; then
        work="$keep"; mkdir -p "$work" 2>/dev/null
    else
        work="$(mktemp -d "${TMPDIR:-/tmp}/fleet-probe-XXXXXX" 2>/dev/null || mktemp -d 2>/dev/null || true)"
    fi
    # near-empty stdin so CLIs that read stdin do not hang
    [ -n "$work" ] && printf '\n' >"$work/in.txt"
    [ -n "$work" ] || return 0
    out="$work/o.txt"; err="$work/e.txt"
    : >"$out"; : >"$err"

    # Split the argument line into words, honouring quotes (same as the PS argument line).
    eval "set -- $argline" 2>/dev/null
    local -a cargs=("$@")

    if [ -n "$TIMEOUT_CMD" ]; then
        ( cd "$work" && "$TIMEOUT_CMD" "$tsec" "$path" "${cargs[@]}" <"$work/in.txt" >"$out" 2>"$err" )
        rc=$?
        case "$rc" in 124|137|143) RES_TIMEDOUT=1 ;; *) RES_EXIT="$rc" ;; esac
    else
        set -m 2>/dev/null
        ( cd "$work" && exec "$path" "${cargs[@]}" <"$work/in.txt" >"$out" 2>"$err" ) &
        pid=$!
        elapsed=0
        while kill -0 "$pid" 2>/dev/null; do
            if [ "$elapsed" -ge "$tsec" ]; then
                RES_TIMEDOUT=1
                kill -TERM -- "-$pid" 2>/dev/null || kill -TERM "$pid" 2>/dev/null
                sleep 1
                kill -KILL -- "-$pid" 2>/dev/null || kill -KILL "$pid" 2>/dev/null
                break
            fi
            sleep 1
            elapsed=$((elapsed + 1))
        done
        wait "$pid" 2>/dev/null
    fi

    t="$(cat "$out" 2>/dev/null || true)"
    e="$(cat "$err" 2>/dev/null || true)"
    RES_TEXT="$(clean_text "$t
$e")"

    [ -n "$keep" ] || rm -rf "$work" 2>/dev/null
}

# ---------------------------------------------------------------------------
# Three-state verdict from the smoke output (same rules as Get-Verdict).
#   VAUTH / VCREDITS / VDETAIL
# ---------------------------------------------------------------------------
VAUTH=''; VCREDITS=''; VDETAIL=''

get_verdict() {
    local t="$1" timedout="$2"
    if [ "$timedout" = 1 ]; then
        VAUTH='unknown'; VCREDITS='unknown'; VDETAIL='timed out'; return 0
    fi
    # Success first: CLIs print warnings (e.g. "model metadata not found") even when the answer is fine
    if printf '%s\n' "$t" | grep -Eq '^[[:space:]]*\**42\**\.?[[:space:]]*$'; then
        VAUTH='yes'; VCREDITS='yes'; VDETAIL='answered'; return 0
    fi
    if printf '%s' "$t" | grep -Eqi 'not (signed|logged) in|login required|please (log|sign) ?in|unauthori[sz]ed|(^|[^0-9])401([^0-9]|$)|authenticate'; then
        VAUTH='NO'; VCREDITS='unknown'; VDETAIL='not logged in'; return 0
    fi
    # A rejected DEFAULT model is not "no credits": the tool usually works with another model (-m <model>)
    if printf '%s' "$t" | grep -Eqi 'model .{0,60}(not supported|not found|does not exist|unknown model|not available)'; then
        VAUTH='yes'; VCREDITS='MODEL'; VDETAIL='default model rejected - try another model'; return 0
    fi
    if printf '%s' "$t" | grep -Eqi 'insufficient|balance|quota|usage limit|rate limit|(^|[^0-9])(402|429)([^0-9]|$)|out of credits|billing'; then
        VAUTH='yes'; VCREDITS='NO'; VDETAIL='quota/credits'; return 0
    fi
    if printf '%s' "$t" | grep -Eq '(^|[^0-9])42([^0-9]|$)'; then
        VAUTH='yes'; VCREDITS='yes'; VDETAIL='answered'; return 0
    fi
    if [ "${#t}" -lt 3 ]; then
        VAUTH='unknown'; VCREDITS='unknown'; VDETAIL='empty output = failure'; return 0
    fi
    VAUTH='unknown'; VCREDITS='unknown'; VDETAIL='unexpected reply - read details'; return 0
}

# Build one JSON object for a tool row.
row_obj() {
    local tool="$1" installed="$2" version="$3" auth="$4" credits="$5" tier="$6" detail="$7" path="$8" models_json="$9"
    printf '    {\n'
    printf '      "tool": "%s",\n' "$(json_escape "$tool")"
    printf '      "installed": "%s",\n' "$(json_escape "$installed")"
    printf '      "version": "%s",\n' "$(json_escape "$version")"
    printf '      "auth": "%s",\n' "$(json_escape "$auth")"
    printf '      "credits": "%s",\n' "$(json_escape "$credits")"
    printf '      "tier": "%s",\n' "$(json_escape "$tier")"
    printf '      "detail": "%s",\n' "$(json_escape "$detail")"
    if [ -n "$path" ]; then
        printf '      "path": "%s",\n' "$(json_escape "$path")"
    else
        printf '      "path": null,\n'
    fi
    printf '      "models": %s\n' "$models_json"
    printf '    }'
}

# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------
ROWS_JSON=()
TABLE_LINES=()

hdr_tool='TOOL'; hdr_inst='INSTALLED'; hdr_ver='VERSION'; hdr_auth='AUTH'; hdr_cred='CREDITS'; hdr_tier='TIER'; hdr_det='DETAIL'
line=$(printf '%-14s %-9s %-16s %-7s %-9s %-34s %s' "$hdr_tool" "$hdr_inst" "$hdr_ver" "$hdr_auth" "$hdr_cred" "$hdr_tier" "$hdr_det")
sep=$(printf '%.0s-' $(seq 1 100) 2>/dev/null || printf -- '----')
TABLE_LINES+=("$line")
TABLE_LINES+=("$sep")

for rec in "${CATALOG[@]}"; do
    name=''; pkg=''; smoke=''; tier=''; note=''
    IFS='|' read -r name pkg smoke tier note <<EOF
$rec
EOF

    path="$(find_tool "$name" || true)"
    installed='no'; version=''; auth='-'; credits='-'; detail="$note"; models=''

    if [ -z "$path" ]; then
        if test_broken_launcher "$pkg"; then
            installed='BROKEN'
            detail="package present but launcher missing - reinstall: npm i -g $pkg"
        fi
        TABLE_LINES+=("$(printf '%-14s %-9s %-16s %-7s %-9s %-34s %s' "$name" "$installed" "$(trunc "$version" 16)" "$auth" "$credits" "$(trunc "$tier" 34)" "$detail")")
        ROWS_JSON+=("$(row_obj "$name" "$installed" "$version" "$auth" "$credits" "$tier" "$detail" "$path" '[]')")
        continue
    fi

    installed='yes'

    invoke_tool "$path" '--version' 20
    version="$(printf '%s\n' "$RES_TEXT" | awk 'NF{print; exit}')"

    if [ "$name" = 'opencode' ]; then
        # opencode prints nothing on its first run in a new folder: use one stable folder and retry once
        oc_dir="${TMPDIR:-/tmp}/fleet-probe-opencode"
        invoke_tool "$path" 'models' 30 "$oc_dir"
        if [ "${#RES_TEXT}" -lt 5 ]; then invoke_tool "$path" 'models' 30 "$oc_dir"; fi
        models="$(printf '%s\n' "$RES_TEXT" | grep -Ei 'free|big-pickle' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | head -n 12)"
    fi
    if [ "$name" = 'codex' ] && [ -f "$HOME/.codex/models_cache.json" ]; then
        models="$(grep -o '"slug"[[:space:]]*:[[:space:]]*"[^"]*"' "$HOME/.codex/models_cache.json" | sed 's/.*"\([^"]*\)"$/\1/' | head -n 12)"
    fi
    if [ "$name" = 'ollama' ]; then
        invoke_tool "$path" 'list' 20
        models="$(printf '%s\n' "$RES_TEXT" | sed -n '2,$p' | awk 'NF{print $1}')"
    fi

    if [ "$SMOKE" = 1 ] && [ -n "$smoke" ]; then
        args1="${smoke//\{P\}/$PROMPT}"
        case "$args1" in
            *'{FREE}'*)
                free="$(printf '%s\n' "$models" | awk 'NF{print; exit}')"
                if [ -z "$free" ]; then
                    detail='no free model listed by: opencode models'
                    TABLE_LINES+=("$(printf '%-14s %-9s %-16s %-7s %-9s %-34s %s' "$name" "$installed" "$(trunc "$version" 16)" "$auth" "$credits" "$(trunc "$tier" 34)" "$detail")")
                    ROWS_JSON+=("$(row_obj "$name" "$installed" "$version" "$auth" "$credits" "$tier" "$detail" "$path" "$(json_string_array "$models")")")
                    continue
                fi
                free="$(printf '%s' "$free" | tr -cd 'A-Za-z0-9._/@:+-')"
                args1="${args1//\{FREE\}/$free}"
                ;;
        esac

        if [ "$name" = 'ollama' ]; then
            if [ -n "$models" ]; then
                count="$(printf '%s\n' "$models" | awk 'NF{c++} END{print c+0}')"
                auth='n/a'; credits='free (local)'; detail="$count local model(s)"
            else
                auth='n/a'; credits='n/a'; detail='no local models - try: ollama pull <model>'
            fi
        else
            invoke_tool "$path" "$args1" "$TIMEOUT_SEC"
            get_verdict "$RES_TEXT" "$RES_TIMEDOUT"
            auth="$VAUTH"; credits="$VCREDITS"
            first="$(printf '%s\n' "$RES_TEXT" | awk 'NF{line=$0} END{print line}')"
            if [ "${#first}" -gt 140 ]; then first="${first:0:140}..."; fi
            detail="$VDETAIL: $first"
            # Default model rejected: retry with known models before calling the tool unusable
            if [ "$credits" = 'MODEL' ] && [ "$name" = 'codex' ] && [ -n "$models" ]; then
                for mdl in $(printf '%s\n' "$models" | grep -Evi 'image|review|reserve' | head -n 8); do
                    mdl="$(printf '%s' "$mdl" | tr -cd 'A-Za-z0-9._-')"
                    invoke_tool "$path" "exec --skip-git-repo-check -m $mdl \"$PROMPT\"" "$TIMEOUT_SEC"
                    get_verdict "$RES_TEXT" "$RES_TIMEDOUT"
                    if [ "$VCREDITS" = 'yes' ]; then credits='yes'; detail="usable with -m $mdl (config default model rejected)"; break; fi
                done
            fi
        fi
    elif [ "$SMOKE" = 1 ]; then
        detail="$note (no headless recipe - test by hand)"
    fi

    TABLE_LINES+=("$(printf '%-14s %-9s %-16s %-7s %-9s %-34s %s' "$name" "$installed" "$(trunc "$version" 16)" "$auth" "$credits" "$(trunc "$tier" 34)" "$detail")")
    ROWS_JSON+=("$(row_obj "$name" "$installed" "$version" "$auth" "$credits" "$tier" "$detail" "$path" "$(json_string_array "$models")")")
done

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
mkdir -p "$OUT_DIR" 2>/dev/null
if [ ! -w "$OUT_DIR" ]; then OUT_DIR="$PWD"; printf 'Skill folder not writable - saving to %s\n' "$OUT_DIR"; fi
JSON_FILE="$OUT_DIR/fleet-status.json"

GEN="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null)"
if [ "$SMOKE" = 1 ]; then SMOKE_BOOL='true'; else SMOKE_BOOL='false'; fi

tools_json=''
first_row=1
for r in "${ROWS_JSON[@]}"; do
    if [ "$first_row" = 1 ]; then first_row=0; else tools_json="$tools_json"$',\n'; fi
    tools_json="$tools_json$r"
done

{
    printf '{\n'
    printf '  "generated_at": "%s",\n' "$GEN"
    printf '  "os": "%s",\n' "$OS"
    printf '  "smoke": %s,\n' "$SMOKE_BOOL"
    printf '  "rule": "%s",\n' "$(json_escape "$RULE")"
    printf '  "tools": [\n'
    printf '%s' "$tools_json"
    printf '\n  ]\n}\n'
} >"$JSON_FILE"

# Table
for l in "${TABLE_LINES[@]}"; do printf '%s\n' "$l"; done

printf 'Saved: %s\n' "$JSON_FILE"
if [ "$SMOKE" != 1 ]; then
    printf 'Tip: add --smoke to check login and credits with one tiny prompt per tool.\n'
fi
