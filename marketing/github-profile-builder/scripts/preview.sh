#!/usr/bin/env bash
# Usage: preview.sh README.md  -> writes preview.html next to it (GitHub dark style)
f="${1:-README.md}"; out="$(dirname "$f")/preview.html"
{
cat <<'H'
<!doctype html><html><head><meta charset="utf-8"><title>Profile Preview</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
<style>body{background:#0d1117;margin:0}.markdown-body{max-width:900px;margin:24px auto;padding:32px;border:1px solid #30363d;border-radius:6px}</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script></head>
<body><article class="markdown-body" id="c"></article><script type="text/plain" id="md">
H
cat "$f"
cat <<'H'
</script><script>document.getElementById('c').innerHTML=marked.parse(document.getElementById('md').textContent);</script></body></html>
H
} > "$out"; echo "$out"
