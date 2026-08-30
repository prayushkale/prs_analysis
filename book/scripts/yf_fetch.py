#!/usr/bin/env python3
"""Fetch daily OHLC from Yahoo Finance for claim verification."""
import json, subprocess, sys, time, urllib.parse

def fetch(symbol, start, end):
    """start/end = 'YYYY-MM-DD'"""
    import datetime
    p1 = int(datetime.datetime.fromisoformat(start).timestamp())
    p2 = int(datetime.datetime.fromisoformat(end).timestamp())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?period1={p1}&period2={p2}&interval=1d&events=div%2Csplit"
    out = subprocess.run(["curl", "-s", url, "-A", "Mozilla/5.0", "-H", "Accept: application/json"], capture_output=True, text=True, timeout=25)
    try:
        d = json.loads(out.stdout)
        res = d["chart"]["result"][0]
        ts = res.get("timestamp", [])
        q = res["indicators"]["quote"][0]
        rows = []
        for i, t in enumerate(ts):
            dt = datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
            off = q.get("timestamp") or res.get("timestamp")
            open_ = q["open"][i]; high = q["high"][i]; low = q["low"][i]; close = q["close"][i]
            if close is None: continue
            rows.append((dt, open_, high, low, close))
        return rows
    except Exception as e:
        return f"ERR: {e} :: {out.stdout[:200]}"

if __name__ == "__main__":
    sym, s, e = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = fetch(sym, s, e)
    if isinstance(rows, str):
        print(rows)
    else:
        for dt, o, h, l, c in rows:
            print(f"{dt}  O={o:.2f} H={h:.2f} L={l:.2f} C={c:.2f}")