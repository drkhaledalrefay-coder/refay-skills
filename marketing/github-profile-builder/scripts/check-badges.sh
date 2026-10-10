#!/usr/bin/env bash
# Usage: check-badges.sh README.md
# Checks every image URL returns 200 and every Shields logo actually renders.
f="${1:-README.md}"; fail=0
for u in $(grep -oE 'https://(img\.shields\.io|komarev\.com|github-readme-stats\.vercel\.app|streak-stats\.demolab\.com)[^" )]+' "$f" | sort -u); do
  code=$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 20 "$u")
  if [ "$code" != 200 ]; then echo "FAIL $code $u"; fail=1; continue; fi
  if [[ "$u" == *img.shields.io*logo=* ]] && ! curl -s --max-time 20 "$u" | grep -q '<image'; then
    echo "NO-LOGO $u"; fail=1
  fi
done
[ $fail = 0 ] && echo "All badges OK" || exit 1
