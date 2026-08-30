#!/usr/bin/env python3
"""Search helper: Bing search -> snippet text via stdin/stdout."""
import sys, re, html, subprocess, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

def bing(q, n=8):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=20"
    try:
        out = subprocess.run(["curl", "-s", "-m", "25", url, "-A", UA,
                              "-H", "Accept-Language: en-US,en;q=0.9"], capture_output=True, text=True).stdout
    except Exception as e:
        return [f"ERR {e}"]
    # extract all result anchors + surrounding text
    items = []
    # b_algo blocks
    for bloque in re.findall(r'<li class="b_algo".*?</li>', out, re.S)[:n]:
        m = re.search(r'<h2[^>]*><a href="([^"]+)"[^>]*>(.*?)</a></h2>', bloque, re.S)
        if not m: continue
        url_ = m.group(1)
        title = html.unescape(re.sub("<[^>]+>", "", m.group(2))).strip()
        sn = re.search(r'<p[^>]*>(.*?)</p>', bloque, re.S)
        snip = html.unescape(re.sub("<[^>]+>", "", sn.group(1))).strip() if sn else ""
        items.append((title, url_, snip))
    if not items:  # fallback: any <h2> anchors
        for m in re.findall(r'<h2[^>]*><a href="([^"]+)"[^>]*>(.*?)</a></h2>', out, re.S)[:n]:
            items.append((html.unescape(re.sub("<[^>]+>", "", m[1])).strip(), m[0], ""))
    return items

def show(q, n=6):
    print("Q:", q)
    for t, u, s in bing(q, n):
        print("  *", t[:95])
        print("   ", u[:110])
        if s: print("    ", s[:160])
    print()

if __name__ == "__main__":
    for q in sys.argv[1:]:
        show(q)