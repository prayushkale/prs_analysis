#!/usr/bin/env python3
"""GDELT 2.0 doc API query helper. Usage: gdelt.py <startYYYYMMDDHHMMSS> <endYYYYMMDDHHMMSS> <query>"""
import sys, json, urllib.request, urllib.parse

start, end, query = sys.argv[1], sys.argv[2], sys.argv[3]
url = ("https://api.gdeltproject.org/api/v2/doc/doc?query=" + urllib.parse.quote(query) +
       "&mode=artlist&format=json&startdatetime=" + start + "&enddatetime=" + end +
       "&maxrecords=50")
try:
    req = urllib.request.Request(url, headers={"User-Agent": "verify-batch-019/1.0"})
    d = json.load(urllib.request.urlopen(req, timeout=30))
    arts = d.get("articles", [])
    for a in arts[:25]:
        print("-", a.get("title", "")[:130], "|", a.get("domain", ""), "|", a.get("url", "")[:90])
    print("total:", len(arts))
except Exception as e:
    print("ERR:", e)