#!/usr/bin/env python3
"""Fetch Yahoo Finance daily OHLC for verification claims."""
import json, urllib.request, urllib.parse, time

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

def fetch(symbol, p1, p2, interval="1d"):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
           f"?period1={p1}&period2={p2}&interval={interval}")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def daily_rows(symbol, p1, p2):
    d = fetch(symbol, p1, p2, "1d")
    res = d["chart"]["result"][0]
    ts = res["timestamp"] or []
    q = res["indicators"]["quote"][0]
    out = []
    for i, t in enumerate(ts):
        try:
            o = q["open"][i]; c = q["close"][i]; h = q["high"][i]; lo = q["low"][i]
        except Exception:
            continue
        import datetime
        dt = datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
        out.append((dt, o, h, lo, c))
    return out

def sma200(rows, target_date):
    """200-day SMA of closes strictly before target_date."""
    closes = [r[4] for r in rows if r[0] < target_date]
    if len(closes) < 200:
        return None, len(closes)
    return sum(closes[-200:]) / 200, 200

import sys
task = sys.argv[1] if len(sys.argv) > 1 else "all"

if task in ("all", "dow"):
    print("== DOW Mar 2022 ==")
    for r in daily_rows("%5EDJI", 1646870400, 1648166400):
        print(r[0], "O=%.0f H=%.0f L=%.0f C=%.0f" % (r[1], r[2], r[3], r[4]), "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)

if task in ("all", "nasq"):
    print("== NASDAQ May30-Jun7 2022 ==")
    for r in daily_rows("%5EIXIC", 1653868800, 1654560000):
        print(r[0], "O=%.0f H=%.0f L=%.0f C=%.0f" % (r[1], r[2], r[3], r[4]), "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)

if task in ("all", "nifty_may22"):
    print("== NIFTY May 2022 (Reliance day) ==")
    for r in daily_rows("%5ENSEI", 1652659200, 1653350400):
        print(r[0], "O=%.1f H=%.1f L=%.1f C=%.1f" % (r[1], r[2], r[3], r[4]), "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)
    print("== RELIANCE May 2022 ==")
    for r in daily_rows("RELIANCE.NS", 1652659200, 1653350400):
        print(r[0], "O=%.1f H=%.1f L=%.1f C=%.1f" % (r[1], r[2], r[3], r[4]), "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)

if task in ("all", "dma"):
    print("== BANK NIFTY 2021-06..2022-08 (200-DMA calc) ==")
    rows = daily_rows("%5ENSEBANK", 1622505600, 1659312000)
    print("rows fetched:", len(rows))
    v, n = sma200([r for r in rows if r[0] <= "2022-07-22"], "2022-07-22")
    print("BankNifty 200-DMA as of 2022-07-22:", round(v, 1) if v else "n/a", "n=", n)
    for r in rows:
        if "2022-07-2" in r[0] or "2022-07-1" in r[0]:
            print("  ", r[0], "C=%.1f" % r[4])
    print("== NIFTY 200-DMA as of 2022-07-22 ==")
    rows2 = daily_rows("%5ENSEI", 1622505600, 1659312000)
    v2, n2 = sma200(rows2, "2022-07-22")
    print("Nifty 200-DMA:", round(v2, 1) if v2 else "n/a", "n=", n2)

if task in ("all", "bnk_jul24"):
    print("== BANK NIFTY Jun24-Jul24 (ATH claim) ==")
    for r in daily_rows("%5ENSEBANK", 1718841600, 1720569600):
        print(r[0], "O=%.1f H=%.1f L=%.1f C=%.1f" % (r[1], r[2], r[3], r[4]))

if task in ("all", "nvda"):
    print("== NVDA Aug29-Sep6 2024 ==")
    for r in daily_rows("NVDA", 1724889600, 1725667200):
        print(r[0], "O=%.1f H=%.1f L=%.1f C=%.1f" % (r[1], r[2], r[3], r[4]), "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)
    print("== SOX (semis) Aug29-Sep6 2024 ==")
    try:
        for r in daily_rows("^SOX", 1724889600, 1725667200):
            print(r[0], "C=%.1f" % r[4], "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)
    except Exception as e:
        print("SOX error:", e)

if task in ("all", "amzn"):
    print("== AMZN Aug 2023 ==")
    for r in daily_rows("AMZN", 1690848000, 1691452800):
        print(r[0], "O=%.1f H=%.1f L=%.1f C=%.1f" % (r[1], r[2], r[3], r[4]), "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)
    print("== AAPL Aug 2023 ==")
    for r in daily_rows("AAPL", 1690848000, 1691452800):
        print(r[0], "O=%.1f H=%.1f L=%.1f C=%.1f" % (r[1], r[2], r[3], r[4]), "chg%%=", round((r[4]/r[1]-1)*100, 2) if r[1] else 0)