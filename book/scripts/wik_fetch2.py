#!/usr/bin/env python3
"""Rate-limited Wikipedia extract fetcher. Usage: wik_fetch2.py <title> <outfile> [chars]"""
import sys, time, json, urllib.request, urllib.parse, html

def fetch(title, chars=30000, retries=4):
    url = ("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1"
           "&titles=" + urllib.parse.quote(title) + "&format=json&exlimit=1&redirects=1")
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "verify-batch-019/1.0 (book fact research)"})
            d = json.load(urllib.request.urlopen(req, timeout=25))
            for pid, pg in d["query"]["pages"].items():
                if "extract" in pg:
                    return pg["extract"][:chars]
            return ""
        except Exception as e:
            code = getattr(e, "code", None)
            wait = 8 * (i + 1) if code == 429 else 3
            time.sleep(wait)
    return ""

if __name__ == "__main__":
    t, out = sys.argv[1], sys.argv[2]
    chars = int(sys.argv[3]) if len(sys.argv) > 3 else 30000
    ex = fetch(t, chars)
    open(out, "w").write(ex)
    print(f"{len(ex)} chars -> {out}")