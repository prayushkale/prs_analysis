#!/usr/bin/env python3
"""Google News RSS search helper."""
import sys, urllib.parse, urllib.request, re, html

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

def gsearch(q, n=8, lang="en"):
    url = ("https://news.google.com/rss/search?q=" + urllib.parse.quote(q)
           + f"&hl=en-{lang.upper()}&gl={lang.upper()}&ceid={lang.upper()}:en")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    xml = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
    out = []
    # items contain <item><title>..</title><link>..</link><source>..</source>..<pubDate>..</pubDate>
    for m in re.finditer(r"<item>(.*?)</item>", xml, re.S):
        t = re.search(r"<title>(.*?)</title>", m.group(1), re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", m.group(1), re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", m.group(1), re.S)
        out.append((html.unescape(t.group(1)) if t else "", s.group(1) if s else "",
                    d.group(1) if d else ""))
    return out[:n]

if __name__ == "__main__":
    for t, s, d in gsearch(sys.argv[1], n=int(sys.argv[2]) if len(sys.argv) > 2 else 8):
        print(f"- [{s}] {t} ({d[:16]})")