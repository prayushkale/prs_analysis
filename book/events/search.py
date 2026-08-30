#!/usr/bin/env python3
"""Robust web search via Bing HTML + Google News RSS. Args: query [engine bing|gnews]"""
import sys, re, html, urllib.parse, urllib.request

def bing(q, n=8):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=15&setlang=en-US&cc=US"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'})
    data = urllib.request.urlopen(req, timeout=25).read().decode('utf-8', 'replace')
    blocks = re.split(r'<li class="b_algo"', data)[1:]
    out = []
    for blk in blocks[:n]:
        cite = re.search(r'<cite[^>]*>(.*?)</cite>', blk, re.S)
        title = re.search(r'<h2[^>]*>(.*?)</h2>', blk, re.S)
        sn = re.search(r'<p[^>]*>(.*?)</p>', blk, re.S)
        def clean(x):
            return html.unescape(re.sub(r'<[^>]+>', '', x)).strip()
        url = None
        m = re.search(r'href="(https?://[^"]+)"', blk)
        if m: url = m.group(1)
        elif cite: url = clean(cite.group(1))
        out.append((clean(title.group(1)) if title else '?', url or '?', clean(sn.group(1))[:240] if sn else ''))
    return out

def gnews(q, n=8):
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=en-IN&gl=IN&ceid=IN:en"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req, timeout=20).read().decode('utf-8', 'replace')
    items = re.findall(r'<item>(.*?)</item>', data, re.S)
    out = []
    for it in items[:n]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        ln = re.search(r'<link>(.*?)</link>', it, re.S)
        src = re.search(r'<source[^>]*>(.*?)</source>', it, re.S)
        pub = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        out.append((html.unescape(t.group(1)) if t else '?', ln.group(1) if ln else '?',
                    (src.group(1) if src else '') + ' | ' + (pub.group(1) if pub else '')))
    return out

if __name__ == '__main__':
    q = sys.argv[1]
    eng = sys.argv[2] if len(sys.argv) > 2 else 'bing'
    rs = gnews(q) if eng == 'gnews' else bing(q)
    for t, u, s in rs:
        print(f"TITLE: {t[:150]}")
        print(f"URL: {u[:150]}")
        print(f"EXTRA: {s[:220]}")
        print('---')
    if not rs:
        print('NO_RESULTS')