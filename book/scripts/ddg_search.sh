#!/bin/bash
# ddg_search.sh - DuckDuckGo HTML search; prints top result titles + snippets
q="$1"
curl -s --max-time 20 "https://html.duckduckgo.com/html/?q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")" \
  -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" \
  | python3 -c "
import sys, re, html
data = sys.stdin.read()
results = re.findall(r'<a[^>]*class=\"result__a\"[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>', data)
snips = re.findall(r'<a[^>]*class=\"result__snippet\"[^>]*>(.*?)</a>', data)
for i, (u, t) in enumerate(results[:6]):
    t = html.unescape(re.sub('<[^>]+>', '', t))
    s = html.unescape(re.sub('<[^>]+>', '', snips[i])) if i < len(snips) else ''
    print(f'{i+1}. {t}')
    print(f'   URL: {u}')
    print(f'   SNIP: {s[:220]}')
    print()
"