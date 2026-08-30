#!/usr/bin/env python3
"""Fetch Yahoo Finance historical closes for a symbol; print monthly/month range summary."""
import json, sys, urllib.request
from datetime import datetime

def fetch(sym, p1, p2, interval="1d", period="max"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?period1={p1}&period2={p2}&interval={interval}&events=history"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.load(r)
    res = d["chart"]["result"][0]
    ts = res.get("timestamp", [])
    close = res["indicators"]["quote"][0]["close"]
    rows = []
    for t, c in zip(ts, close):
        if c is not None:
            rows.append((datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"), round(c, 2)))
    return rows

if __name__ == "__main__":
    sym = sys.argv[1]
    p1 = int(sys.argv[2]) if len(sys.argv) > 2 else 1500000000
    p2 = int(sys.argv[3]) if len(sys.argv) > 3 else 1800000000
    ival = sys.argv[4] if len(sys.argv) > 4 else "1d"
    rows = fetch(sym, p1, p2, ival)
    # print first/last 5 and all rows if few
    print(f"== {sym}: {len(rows)} rows {rows[0][0] if rows else '-'}..{rows[-1][0] if rows else '-'}")
    for r in rows:
        print(r[0], r[1])
