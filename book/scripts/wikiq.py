#!/usr/bin/env python3
"""wikiq.py - Wikipedia search + extract with retry/backoff; usage: wikiq.py search "query" | wikiq.py page "Title"
Queries are spaced ~3s apart to respect rate limits."""
import sys, json, re, time, urllib.parse, urllib.request

def fetch(url):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "book-factcheck/1.0 (contact: none)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            if getattr(e, "code", None) == 429 or isinstance(e, (TimeoutError, ConnectionError)):
                time.sleep(5 * (attempt + 1))
                continue
            raise
    return None

def wiki_search(q, limit=4):
    url = ("https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch="
           + urllib.parse.quote(q) + f"&srlimit={limit}&format=json")
    d = fetch(url)
    return (d or {}).get("query", {}).get("search", [])

def wiki_extract(title):
    url = ("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&exintro=1&titles="
           + urllib.parse.quote(title) + "&format=json")
    d = fetch(url)
    pages = ((d or {}).get("query", {}) or {}).get("pages", {})
    for p in pages.values():
        return p.get("extract", "")
    return ""

if __name__ == "__main__":
    mode = sys.argv[1]
    q = " ".join(sys.argv[2:])
    if mode == "search":
        for r in wiki_search(q, 4):
            print("-", r.get("title"))
            print("  ", re.sub("<[^>]+>", "", r.get("snippet", ""))[:250])
            print()
    elif mode == "page":
        print(wiki_extract(q)[:2500])