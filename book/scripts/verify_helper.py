#!/usr/bin/env python3
"""Fetch google search results page and extract text snippets."""
import sys, re, urllib.parse, urllib.request

def fetch(q, engine="google"):
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    if engine == "google":
        url = "https://www.google.com/search?" + urllib.parse.urlencode({"q": q, "num": 10})
    else:
        url = "https://www.bing.com/search?" + urllib.parse.urlencode({"q": q})
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept-Language": "en-US,en;q=0.9"})
    try:
        html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
    except Exception as e:
        return f"FETCH ERROR: {e}"
    # strip scripts/styles
    html = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", html)
    # keep anchor text and headings, strip other tags
    txt = re.sub(r"<[^>]+>", " ", html)
    txt = re.sub(r"\s+", " ", txt)
    return txt[:6000]

if __name__ == "__main__":
    q = sys.argv[1]
    eng = sys.argv[2] if len(sys.argv) > 2 else "google"
    print(fetch(q, eng))