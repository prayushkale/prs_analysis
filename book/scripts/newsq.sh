#!/bin/bash
# usage: newsq.sh "query"
curl -s -m 20 "https://www.bing.com/news/search?q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")&format=rss" -A "Mozilla/5.0" | python3 -c "
import sys, re, html
data = sys.stdin.read()
items = re.findall(r'<item>(.*?)</item>', data, re.S)
for it in items[:6]:
    t = re.search(r'<title>(.*?)</title>', it, re.S)
    d = re.search(r'<description>(.*?)</description>', it, re.S)
    l = re.search(r'url=([^&]+)', it)
    src = re.search(r'<News:Source>(.*?)</News:Source>', it, re.S)
    pd = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    print('•', html.unescape(t.group(1)) if t else '')
    if pd: print('  date:', pd.group(1))
    if src: print('  source:', src.group(1))
    if l: print('  url:', html.unescape(urllib.parse.unquote(l.group(1))))
    if d: print('  ', html.unescape(re.sub('<[^>]+>','',d.group(1)))[:200])
    print()
" 2>/dev/null || true
