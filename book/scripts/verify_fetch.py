import json, time, urllib.request, datetime as dt

def fetch(symbol, start, end):
    """start,end: 'YYYY-MM-DD' iso. Returns list of {date, open, high, low, close}."""
    s = int(dt.datetime.strptime(start, "%Y-%m-%d").timestamp())
    e = int(dt.datetime.strptime(end, "%Y-%m-%d").timestamp()) + 86400
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?period1={s}&period2={e}&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode())
    res = data["chart"]["result"][0]
    ts = res["timestamp"]
    q = res["indicators"]["quote"][0]
    out = []
    for i, t in enumerate(ts):
        d = dt.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
        o, h, l, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
        if o is None:
            continue
        out.append({"date": d, "open": round(o,2), "high": round(h,2), "low": round(l,2), "close": round(c,2)})
    return out

import urllib.parse

if __name__ == "__main__":
    import sys
    sym, s, e = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = fetch(sym, s, e)
    for r in rows:
        print(r["date"], "O", r["open"], "H", r["high"], "L", r["low"], "C", r["close"])