#!/usr/bin/env python3
"""Search helper: Bing HTML search + URL text fetch. Usage: py_search.py "query" [n]"""
import re, sys, urllib.parse, urllib.request

def search(q, n=6):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=20"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"})
    html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    # Bing organic results: <a href="URL" h="...">TITLE</a> inside <h2>
    out = []
    # capture <h2><a href="...">title</a></h2> and cite URLs
    for m in re.finditer(r'<h2><a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a></h2>', html):
        title = re.sub(r"<[^>]+>", "", m.group(2))
        out.append((m.group(1), title))
        if len(out) >= n:
            break
    # also grab cite urls in <cite> tags if h2 count is low
    if len(out) < n:
        for m in re.finditer(r'<cite[^>]*>(.*?)</cite>', html):
            c = re.sub(r"<[^>]+>", "", m.group(1))
            if c not in [o[0] for o in out]:
                out.append((c, ""))
            if len(out) >= n:
                break
    return out

if __name__ == "__main__":
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    for url, title in search(q, n):
        title = title or url
        print(f"{title[:110]} :: {url}")