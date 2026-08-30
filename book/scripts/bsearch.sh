#!/bin/bash
# bsearch.sh "query" [max_results]
Q=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$1")
MAX=${2:-6}
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
curl -s -m 25 "https://www.bing.com/search?q=${Q}&count=${MAX}" -A "$UA" \
 | python3 -c "
import sys, re, base64, urllib.parse, html
data = sys.stdin.read()
for m in re.finditer(r'<h2[^>]*><a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>', data):
    href = m.group(1)
    title = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    real = href
    mu = re.search(r'u=a1([A-Za-z0-9+/=]+)', href)
    if mu:
        try:
            real = base64.b64decode(mu.group(1) + '=' * (-len(mu.group(1)) % 4)).decode('utf-8', 'ignore')
        except Exception:
            real = href
    if real.startswith('http'):
        print(f'TITLE: {title}\nURL: {real}\n---')
"