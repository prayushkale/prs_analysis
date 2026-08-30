#!/usr/bin/env python3
"""Web search helper - Bing (decoded) + Mojeek fallback."""
import sys, re, html as htmlmod, base64, json
import urllib.request, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"

def bing(q, n=5):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=10&setlang=en"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            page = r.read().decode("utf-8", "replace")
    except Exception as e:
        return [("ERROR", str(e), "")]
    results = []
    for m in re.finditer(r'<li class="b_algo".*?</li>', page, re.S):
        block = m.group(0)
        hm = re.search(r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>', block, re.S)
        if not hm:
            continue
        url = hm.group(1)
        # decode bing redirect
        um = re.search(r"u=a1([A-Za-z0-9+/=]+)", url)
        if um:
            try:
                url = base64.b64decode(um.group(1) + "==").decode()
            except Exception:
                pass
        title = re.sub(r"<[^>]+>", "", hm.group(2))
        title = htmlmod.unescape(title).strip()
        sm = re.search(r"<p[^>]*>(.*?)</p>", block, re.S)
        snip = ""
        if sm:
            snip = re.sub(r"<[^>]+>", "", sm.group(1))
            snip = htmlmod.unescape(snip).strip()[:220]
        results.append((title, url, snip))
        if len(results) >= n:
            break
    return results

def mojeek(q, n=5):
    url = "https://www.mojeek.com/search?q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            page = r.read().decode("utf-8", "replace")
    except Exception as e:
        return [("ERROR", str(e), "")]
    results = []
    for m in re.finditer(r'<a class="ob" href="([^"]+)"[^>]*>(.*?)</a>', page, re.S):
        url, title = m.group(1), htmlmod.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        sm = re.search(r'<p class="s">(.*?)</p>', page[m.end():], re.S)
        snip = htmlmod.unescape(re.sub(r"<[^>]+>", "", sm.group(1))).strip()[:220] if sm else ""
        results.append((title, url, snip))
        if len(results) >= n:
            break
    return results

def search(q, n=5):
    res = bing(q, n)
    if res and res[0][0] != "ERROR" and len(res) > 1:
        return res
    return mojeek(q, n)

if __name__ == "__main__":
    q = sys.argv[1]
    for r in search(q):
        print("•", r[0])
        print("  ", r[1])
        if r[2]:
            print("  ", r[2])