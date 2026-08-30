#!/usr/bin/env python3
"""Print one evidence URL per query (Google News RSS first match containing a keyword)."""
import sys, urllib.parse, urllib.request, re, html

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0"

def find_link(q, needle, lang="en"):
    url = ("https://news.google.com/rss/search?q=" + urllib.parse.quote(q)
           + f"&hl=en-{lang.upper()}&gl={lang.upper()}&ceid={lang.upper()}:en")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    xml = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")
    for m in re.finditer(r"<item>(.*?)</item>", xml, re.S):
        t = re.search(r"<title>(.*?)</title>", m.group(1), re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", m.group(1), re.S)
        lk = re.search(r"<link>(.*?)</link>", m.group(1), re.S)
        title = html.unescape(t.group(1)) if t else ""
        src = s.group(1) if s else ""
        link = lk.group(1) if lk else ""
        if needle.lower() in title.lower():
            return src, title, link
    return None

if __name__ == "__main__":
    q, needle, lang = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "en")
    r = find_link(q, needle, lang)
    if r:
        print(f"SRC: {r[0]}\nTITLE: {r[1]}\nURL: {r[2]}")
    else:
        print("NO MATCH")