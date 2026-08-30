#!/usr/bin/env python3
"""Search helper: query Google News RSS + Bing RSS, print top results."""
import sys, urllib.parse, urllib.request, re, html

def fetch(url, ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", "replace")

def parse_rss(xml, n=8):
    items = re.findall(r"<item>(.*?)</item>", xml, re.S)
    out = []
    for it in items[:n]:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<description>(.*?)</description>", it, re.S)
        # google news uses <guid> for URL sometimes; links may be google news redirect
        def clean(x):
            return html.unescape(re.sub(r"<[^>]+>", "", x or ""))
        out.append({"title": clean(t.group(1) if t else ""),
                    "link": clean(l.group(1) if l else ""),
                    "desc": clean(d.group(1) if d else "")[:200]})
    return out

def search(q, n=6):
    qq = urllib.parse.quote(q)
    out = []
    try:
        gn = fetch(f"https://news.google.com/rss/search?q={qq}&hl=en-IN&gl=IN&ceid=IN:en")
        for it in parse_rss(gn, n):
            it["src"] = "gnews"
            out.append(it)
    except Exception as e:
        out.append({"src": "gnews", "title": f"ERR {e}"})
    try:
        bing = fetch(f"https://www.bing.com/search?format=rss&q={qq}")
        for it in parse_rss(bing, n):
            it["src"] = "bing"
            out.append(it)
    except Exception as e:
        out.append({"src": "bing", "title": f"ERR {e}"})
    return out

if __name__ == "__main__":
    q = " ".join(sys.argv[1:])
    for it in search(q):
        print(f"[{it.get('src')}] {it['title'][:130]}")
        if it.get("desc"): print("    ", it["desc"][:180])
        if it.get("link"): print("    ", it["link"][:120])