#!/usr/bin/env bash
# usage: bg.sh "search query" [max_results]
Q=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$1")
MAX=${2:-6}
timeout 25 curl -s "https://www.bing.com/search?q=${Q}&count=10&setlang=en-US" \
  -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept-Language: en-US,en;q=0.9" | python3 -c "
import sys, re, html
data = sys.stdin.read()
blocks = re.findall(r'<li class=\"b_algo\".*?</li>', data, re.S)
seen = set()
count = 0
for b in blocks:
    m = re.search(r'<h2><a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a></h2>', b, re.S)
    if not m: continue
    url = m.group(1)
    if url in seen or 'bing.com/ck' in url: continue
    seen.add(url)
    t = html.unescape(re.sub('<[^>]+>','',m.group(2))).strip()
    sn = re.search(r'<p[^>]*>(.*?)</p>', b, re.S)
    s = html.unescape(re.sub('<[^>]+>','',sn.group(1))).strip()[:220] if sn else ''
    print(f'TITLE: {t}')
    print(f'URL: {url}')
    print(f'SNIP: {s}')
    print('---')
    count += 1
    if count >= $MAX: break
if count == 0:
    print('NO_RESULTS')
"