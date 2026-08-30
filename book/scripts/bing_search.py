#!/usr/bin/env python3
"""Simple Bing search scraper for claim verification."""
import sys, re, html, subprocess, urllib.parse, json

def search(q, n=5):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=20"
    try:
        out = subprocess.run(["curl", "-s", url, "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36", "-H", "Accept-Language: en-US,en;q=0.9"], capture_output=True, text=True, timeout=25)
        t = out.stdout
    except Exception as e:
        return [("ERROR", str(e), "")]
    # result blocks
    res = []
    # h2 titles with <a href>
    blocks = re.findall(r'<li class="b_algo".*?</li>', t, re.S)
    if not blocks:
        blocks = re.findall(r'<h2><a[^>]*href="([^"]+)"[^>]*>(.*?)</a></h2>\s*(?:<p[^>]*>(.*?)</p>)?', t, re.S)
        for href, ti, sn in blocks[:n]:
            res.append((html.unescape(re.sub('<[^>]+>', '', ti)), html.unescape(href), html.unescape(re.sub('<[^>]+>', '', sn or ''))))
    else:
        for b in blocks[:n]:
            m = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', b)
            t2 = re.search(r'<h2>(.*?)</h2>', b, re.S)
            sn = re.search(r'<p[^>]*>(.*?)</p>', b, re.S)
            if m:
                href = html.unescape(m.group(1))
                ti = html.unescape(re.sub('<[^>]+>', '', m.group(2))) if t2 else html.unescape(re.sub('<[^>]+>', '', m.group(2)))
                res.append((ti, href, html.unescape(re.sub('<[^>]+>', '', sn.group(1))) if sn else ''))
    return res

if __name__ == "__main__":
    q = sys.argv[1]
    for i, (ti, href, sn) in enumerate(search(q)):
        print(f"{i+1}. {ti}\n   {href}\n   {sn[:250]}\n")