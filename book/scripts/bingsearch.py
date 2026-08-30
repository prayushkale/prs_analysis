#!/usr/bin/env python3
"""Compact Bing news + web search helper for claim verification."""
import sys, urllib.request, urllib.parse, re, html
import xml.etree.ElementTree as ET

HDRS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}

def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def news(q, n=6):
    url = "https://www.bing.com/news/search?format=rss&q=" + urllib.parse.quote(q)
    try:
        root = ET.fromstring(fetch(url))
    except Exception as e:
        return []
    out = []
    for item in root.iter("item"):
        d = {"pub": item.findtext("pubDate") or "", "title": item.findtext("title") or "",
             "desc": item.findtext("description") or ""}
        for ch in item:
            if "Url" in ch.tag.split("}")[-1] or ch.tag == "link":
                d["url"] = ch.text or ""
                break
        out.append(d)
        if len(out) >= n: break
    return out

def web(q, n=6):
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(q)
    try:
        t = fetch(url)
    except Exception:
        return []
    blocks = re.findall(r'<li class="b_algo".*?</li>', t, re.S)
    out = []
    for b in blocks:
        m = re.search(r'<a[^>]*href="(http[^"]+)"[^>]*>(.*?)</a>', b, re.S)
        if m:
            title = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
            snippet = html.unescape(re.sub(r"<[^>]+>", " ", b))
            out.append((m.group(1), re.sub(r"\s+", " ", title), re.sub(r"\s+", " ", snippet)[:280]))
        if len(out) >= n: break
    return out

if __name__ == "__main__":
    q = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "news"
    for item in (news(q) if mode == "news" else web(q)):
        print("*", item.get("pub", item[0] if isinstance(item, tuple) else ""), "|", item.get("title", item[1] if isinstance(item, tuple) else ""))
        print("  ", (item.get("desc") or item[2] if isinstance(item, tuple) else "")[:220])