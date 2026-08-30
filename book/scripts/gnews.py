import sys, re, html, urllib.request, urllib.parse

def gnews(query, n=12):
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(query) + "&hl=en-IN&gl=IN&ceid=IN:en"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "replace")
    items = re.findall(r"<item>(.*?)</item>", data, re.S)
    out = []
    for it in items[:n]:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        p = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        out.append({
            "title": html.unescape(re.sub(r"<[^>]+>", "", t.group(1) if t else "")).strip(),
            "date": p.group(1)[:16] if p else "",
            "src": s.group(1) if s else "",
            "link": re.search(r'<link>(.*?)</link>', it, re.S).group(1).strip() if re.search(r'<link>(.*?)</link>', it, re.S) else ""
        })
    return out

if __name__ == "__main__":
    q = sys.argv[1]
    for it in gnews(q):
        print("-", it["date"], "|", it["src"], "|", it["title"][:140])