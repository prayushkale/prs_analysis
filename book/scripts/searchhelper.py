#!/usr/bin/env python3
"""Minimal Wikipedia helper: throttled search + article extract."""
import json, sys, time, urllib.parse, urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) FactCheckBot/1.0"
_last = [0.0]

def throttle(gap=4.0):
    wait = gap - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()

def get_json(url):
    throttle()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)

def wiki_search(query, limit=5):
    url = ("https://en.wikipedia.org/w/api.php?action=query&list=search&format=json"
           f"&srsearch={urllib.parse.quote(query)}&srlimit={limit}")
    try:
        d = get_json(url)
        return [(i["title"], i.get("snippet", "")) for i in d.get("query", {}).get("search", [])]
    except Exception as e:
        return [("ERROR", str(e))]

def page_extract(title, sentences=15):
    url = ("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json"
           f"&exsentences={sentences}&titles={urllib.parse.quote(title)}&redirects=1")
    try:
        d = get_json(url)
        pages = d.get("query", {}).get("pages", {})
        for p in pages.values():
            return p.get("extract", "")
        return ""
    except Exception as e:
        return f"ERROR: {e}"

if __name__ == "__main__":
    mode = sys.argv[1]
    q = sys.argv[2]
    if mode == "s":
        for title, snip in wiki_search(q):
            print(f"* {title}\n  {snip[:220]}")
    elif mode == "e":
        txt = page_extract(q)
        print(txt[:1500])