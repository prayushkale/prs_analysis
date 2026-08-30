#!/usr/bin/env python3
"""Fetch Wikipedia extract (plaintext) for a given title."""
import sys, json, urllib.request

def fetch(title):
    url = ("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1"
           "&titles=" + urllib.parse.quote(title) + "&format=json&redirects=1")
    req = urllib.request.Request(url, headers={"User-Agent": "verify-batch-019/1.0 (book fact-check)"})
    d = json.load(urllib.request.urlopen(req, timeout=20))
    pages = d["query"]["pages"]
    for pid, pg in pages.items():
        if "extract" in pg:
            return pg["extract"]
    return ""

if __name__ == "__main__":
    import urllib.parse
    t = sys.argv[1]
    ex = fetch(t)
    print(ex[:8000] if ex else "NO_EXTRACT")