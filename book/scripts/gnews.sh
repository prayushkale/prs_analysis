#!/bin/bash
# gnews.sh - Google News RSS search; prints top titles + URLs
q="$1"
curl -s --max-time 25 "https://news.google.com/rss/search?q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&hl=en-IN&gl=IN&ceid=IN:en" \
  -A "Mozilla/5.0" | python3 -c "
import sys, re, html, xml.etree.ElementTree as ET
data = sys.stdin.read()
if '<item>' not in data:
    print('NO RESULTS'); sys.exit()
root = ET.fromstring(data)
items = root.iter('item')
for i, it in enumerate(items):
    if i >= 8: break
    t = it.findtext('title')
    l = it.findtext('link')
    d = it.findtext('pubDate') or ''
    s = it.findtext('description') or ''
    s = html.unescape(re.sub('<[^>]+>', '', s))
    print(f'{i+1}. {t}')
    print(f'   URL: {l}')
    print(f'   DATE: {d}')
    print(f'   SNIP: {s[:180]}')
    print()
"