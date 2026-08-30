#!/usr/bin/env python3
"""Simple Bing RSS search helper."""
import sys, urllib.parse, urllib.request, re, html

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

def search(q, n=6):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&format=rss"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        xml = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
    except Exception as e:
        print("ERR", e)
        return []
    items = re.findall(r"<item><title>(.*?)</title><link>(.*?)</link><description>(.*?)</description>", xml)
    out = []
    for t, l, d in items:
        out.append((html.unescape(t), html.unescape(l), re.sub(r"<[^>]+>", "", html.unescape(d))[:200]))
    return out[:n]

if __name__ == "__main__":
    q = sys.argv[1]
    for t, l, d in search(q):
        print(f"- {t}\n  {l}\n  {d}")