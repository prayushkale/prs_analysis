#!/usr/bin/env python3
"""Fetch daily OHLC for a Yahoo ticker between two unix timestamps."""
import sys, json, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch(symbol, p1, p2, interval="1d"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?period1={p1}&period2={p2}&interval={interval}"
    req = urllib.request.Request(url, headers=UA)
    try:
        data = json.loads(urllib.request.urlopen(req, timeout=25).read())
    except Exception as e:
        return f"ERROR {symbol}: {e}"
    r = data.get("chart", {}).get("result")
    if not r:
        return f"NO DATA {symbol}: {data.get('chart', {}).get('error', {}).get('description', '?')}"
    r = r[0]
    ts = r["timestamp"]
    ind = r["indicators"]["quote"][0]
    rows = []
    for i, t in enumerate(ts):
        rows.append((t, ind["open"][i], ind["high"][i], ind["low"][i], ind["close"][i], ind["volume"][i]))
    return rows

if __name__ == "__main__":
    sym, p1, p2 = sys.argv[1], sys.argv[2], sys.argv[3]
    iv = sys.argv[4] if len(sys.argv) > 4 else "1d"
    rows = fetch(sym, p1, p2, iv)
    if isinstance(rows, str):
        print(rows)
    else:
        import datetime
        for t, o, h, l, c, v in rows:
            d = datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d %H:%M")
            c = c if c is not None else 0
            o = o if o is not None else 0
            print(f"{d}  O:{o:.2f} H:{h:.2f} L:{l:.2f} C:{c:.2f} V:{v}")