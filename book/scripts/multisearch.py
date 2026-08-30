#!/usr/bin/env python3
"""Multi-engine search: Brave HTML + Bing RSS + Bing News, returns (title, url, snippet)."""
import sys, re, html as htmlmod, urllib.request, urllib.parse, time

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def _fetch(url, headers=None, timeout=20):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as e:
        return None

def brave(q, n=6):
    page = _fetch("https://search.brave.com/search?q=" + urllib.parse.quote(q) + "&source=web")
    if not page:
        return []
    res = []
    # result blocks
    for m in re.finditer(r'snippet-title[^>]*title="([^"]+)"[^>]*>', page):
        title = htmlmod.unescape(m.group(1))
        # find nearest following href
        seg = page[m.end():m.end() + 3000]
        hm = re.search(r'href="(https?://[^"]+)"', seg)
        if not hm:
            continue
        url = hm.group(1)
        sm = re.search(r'snippet-description[^>]*>(.*?)</p>', seg, re.S)
        snip = ""
        if sm:
            snip = htmlmod.unescape(re.sub(r"<[^>]+>", "", sm.group(1))).strip()[:200]
        if any(g in url for g in ("brave.com", "bravecreative", "youtube.com")):
            continue
        res.append((title, url, snip))
        if len(res) >= n:
            break
    return res

def bing_rss(q, n=6):
    page = _fetch("https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&format=rss")
    if not page:
        return []
    res = []
    for it in re.findall(r"<item>(.*?)</item>", page, re.S)[:n]:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<description>(.*?)</description>", it, re.S)
        if not (t and l):
            continue
        res.append((htmlmod.unescape(t.group(1))[:120], htmlmod.unescape(l.group(1)),
                    htmlmod.unescape(re.sub("<[^>]+>", "", d.group(1)))[:200] if d else ""))
    return res

def bing_news(q, n=6):
    page = _fetch("https://www.bing.com/news/search?q=" + urllib.parse.quote(q) + "&format=rss")
    if not page:
        return []
    res = []
    for it in re.findall(r"<item>(.*?)</item>", page, re.S)[:n]:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"url=([^&]+)", it)
        d = re.search(r"<description>(.*?)</description>", it, re.S)
        src = re.search(r"<News:Source>(.*?)</News:Source>", it, re.S)
        if not (t and l):
            continue
        url = htmlmod.unescape(urllib.parse.unquote(l.group(1)))
        res.append((htmlmod.unescape(t.group(1))[:130], url,
                    htmlmod.unescape(re.sub("<[^>]+>", "", d.group(1)))[:190] if d else "",
                    src.group(1).strip() if src else ""))
    return res

def search_all(q, engines=("brave", "bing_rss", "bing_news"), n=5):
    out = []
    for e in engines:
        try:
            fn = {"brave": brave, "bing_rss": bing_rss, "bing_news": bing_news}[e]
            out.extend(fn(q, n))
        except Exception as ex:
            out.append(("ERROR-" + e, str(ex)[:80], ""))
        time.sleep(0.4)
    return out

if __name__ == "__main__":
    q = sys.argv[1]
    seen = set()
    for r in search_all(q):
        if r[1] in seen:
            continue
        seen.add(r[1])
        print("•", r[0])
        print("  ", r[1])
        sn = "  " + (r[-1] if isinstance(r[-1], str) else "")
        body = sn if False else ("  " + r[2][:150] if len(r) > 2 and r[2] else "")
        print(body)