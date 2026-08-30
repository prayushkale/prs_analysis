#!/usr/bin/env python3
"""Bing News search helper."""
import sys, re, urllib.request, urllib.parse, json

def search(q, n=8):
    url = "https://www.bing.com/news/search?q=" + urllib.parse.quote(q) + "&setlang=en"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0",
        "Accept-Language": "en-US,en;q=0.9"})
    h = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "replace")
    out = []
    # news cards
    for m in list(re.finditer(r'<a[^>]+class="title"[^>]*>(.*?)</a>', h, re.S))[:n]:
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        out.append(("TITLE", t))
    metas = re.findall(r'<span class="news_dt">(.*?)</span>', h, re.S)[:n]
    for m in metas[:n]:
        out.append(("DATE", re.sub(r"<[^>]+>", "", m).strip()))
    urls = re.findall(r'<a[^>]+class="title"[^>]+href="([^"]+)"', h, re.S)[:n]
    for u in urls[:n]:
        out.append(("URL", u))
    return out

if __name__ == "__main__":
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    for kind, v in search(q, n):
        print(f"{kind}: {v[:160]}")