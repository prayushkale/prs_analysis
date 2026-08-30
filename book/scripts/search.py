#!/usr/bin/env python3
"""Search helper: query Bing, extract top result titles/URLs/snippets."""
import sys, re, urllib.parse, subprocess, html, base64

def decode_bing_url(u):
    if "bing.com/ck/a" in u:
        m = re.search(r"u=a1([A-Za-z0-9+/=_-]+)", u)
        if m:
            try:
                s = m.group(1).replace("-", "+").replace("_", "/")
                s += "=" * (-len(s) % 4)
                return base64.b64decode(s).decode("utf-8", "replace")
            except Exception:
                pass
    return u

def search(q, n=6):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=20"
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    try:
        out = subprocess.run(["curl", "-s", "-m", "20", "-A", ua, url],
                             capture_output=True, text=True, timeout=30).stdout
    except Exception as e:
        print("ERR", e); return []
    blocks = re.split(r'<li class="b_algo"', out)
    res = []
    for b in blocks[1:]:
        m = re.search(r'<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if not m: continue
        u = m.group(1)
        t = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        p = re.search(r'<p[^>]*>(.*?)</p>', b, re.S)
        s = html.unescape(re.sub(r'<[^>]+>', '', p.group(1))).strip() if p else ""
        res.append((t, decode_bing_url(u), s[:220]))
        if len(res) >= n: break
    return res

if __name__ == "__main__":
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    for i, (t, u, s) in enumerate(search(q, n), 1):
        print(f"[{i}] {t}\n    URL: {u}\n    {s}\n")