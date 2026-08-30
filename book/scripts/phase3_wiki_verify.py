#!/usr/bin/env python3
"""Phase 3: scripted web verification of priority events via Wikipedia search API + high-level headlines.
Produces book/events/evidence_raw.jsonl for parent curation."""
import json, time, urllib.parse, urllib.request

ROOT = "/home/ubuntu/repos/prs_analysis"
API = "https://en.wikipedia.org/w/api.php"

# Canonicalized top events worth verification (entity -> search query)
QUERIES = [
    # elections & government
    ("2024 Indian general election results Nifty crash June 4", "2024 Indian general election"),
    ("2019 Indian general election BJP win", "2019 Indian general election"),
    ("2018 November five state elections BJP loss", "2018 Indian state elections November"),
    ("2023 December five state elections BJP win", "2023 Indian state elections"),
    ("2025 Bihar election NDA seats", "2025 Bihar Legislative Assembly election"),
    ("Bihar 2025 election results NDA 200 seats", "2025 Bihar Legislative Assembly election"),

    # policy / regulation
    ("SEBI F&O contract size minimum 15 lakh 2024", "SEBI derivative contract size"),
    ("SEBI lot size increase 2024 options", "SEBI lot size futures options 2024"),
    ("SEBI one weekly expiry per exchange 2024", "SEBI weekly expiry 2024"),
    ("SEBI 30% upfront margin option buyer 2024", "SEBI upfront premium option buying"),
    ("crypto 30% tax 1% TDS India 2022", "Cryptocurrency and taxation in India"),
    ("STCG LTCG tax rates 2024 budget change", "2024 Indian Union budget"),
    ("STT increase 2024 budget options futures", "Securities transaction tax India"),
    ("Finance Act 2022 digital assets 30%", "Finance Act 2022 (India)"),
    ("Nirmala Sitharaman finance minister 2019", "Nirmala Sitharaman"),
    ("2019 corporate tax cut 30 to 22 percent India", "2019 Indian corporate tax cut"),
    ("Mauritius capital gains tax India 2024", "India Mauritius tax treaty"),
    ("SEBI peak margin rules 2020 2021", "SEBI peak margin"),
    ("NSE co-location case SEBI", "National Stock Exchange of India"),
    ("SEBI F&O study 93 percent traders lose", "SEBI futures and options study"),
    ("Bank Nifty weekly expiry removed 2024", "Bank Nifty"),
    ("Jane Street SEBI order 2025", "Jane Street"),
    ("SEBI short selling ban 2024", "short selling ban SEBI"),

    # corporate / fraud
    ("Adani Hindenburg report 2023", "Hindenburg Research"),
    ("Hindenburg report SEBI chairperson 2024", "Madhabi Puri Buch"),
    ("LIC IPO listing 2022", "Life Insurance Corporation of India"),
    ("HDFC HDFC Bank merger 2023", "HDFC Bank"),
    ("Hyundai Motor India IPO 2024", "Hyundai Motor India"),
    ("Vauld crypto exchange Fraud India", "Vauld"),
    ("Franklin Templeton India debt funds winding up 2020", "Franklin Templeton India"),
    ("IL&FS default 2018", "IL&FS"),
    ("Yes Bank crisis 2020", "Yes Bank"),
    ("Evergrande default 2021", "China Evergrande Group"),
    ("GameStop short squeeze 2021", "GameStop short squeeze"),

    # macro
    ("US Fed 50 basis point hikes 2022", "2022 Federal Reserve"),
    ("US April 2022 CPI 8.3 percent", "2022 United States inflation"),
    ("US CPI June 2022 9.1 percent", "Consumer price index United States"),
    ("US May 2022 CPI 8.6", "2022 United States inflation"),
    ("Fed rate cut September 2024", "Federal Reserve"),
    ("ECB first rate cut June 2024", "European Central Bank"),
    ("US 10 year yield 2022 spike 3 percent", "United States Treasury"),
    ("2024 yen carry trade unwind August 5", "August 2024 global stock selloff"),
    ("Bank of America gold 3000 target 2020", "Gold as an investment"),
    ("Brent crude 2018 12 day decline", "Brent crude"),

    # wars / geopolitics
    ("Kargil war 1999 Nifty", "Kargil War"),
    ("Pulwama attack 2019", "2019 Pulwama attack"),
    ("Balakot airstrike 2019", "2019 Balakot airstrike"),
    ("Uri attack 2016 surgical strike", "2016 Uri attack"),
    ("Russia invasion Ukraine February 2022", "Russian invasion of Ukraine"),
    ("India Pakistan 2025 conflict", "2025 India-Pakistan"),
    ("US China trade war tariffs 2018", "China–United States trade war"),
    ("Trump tariffs Canada Mexico China March 2025", "Second Trump tariffs"),
    ("US 50 percent tariff India 2025", "Tariffs in the second Trump administration"),

    # markets
    ("Nifty 26300 September 2024 all time high", "NIFTY 50"),
    ("Nifty 15000 May 2021", "NIFTY 50"),
    ("March 2020 COVID market crash Nifty", "2020 stock market crash"),
    ("Nifty 52 week low March 2022 15671", "NIFTY 50"),
    ("Sensex 60000 2021 milestone", "BSE SENSEX"),
    ("Nifty 20000 September 2023", "NIFTY 50"),
    ("SSR IPO with stock options 2020", "Securities and exchange board"),
]

def wiki_search(q, limit=2):
    params = {
        "action": "query", "format": "json", "list": "search",
        "srsearch": q, "srlimit": limit, "srprop": "snippet|titlesnippet",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; research/1.0)"})
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read().decode("utf-8"))
        return data.get("query", {}).get("search", [])
    except Exception as e:
        return [{"error": str(e)}]

out = []
seen = set()
for query, entity in QUERIES:
    res = wiki_search(query)
    clean = []
    for r in res:
        clean.append({"title": r.get("title", ""), "snippet": r.get("snippet", "").replace("<span class=\"searchmatch\">", "[").replace("</span>", "]")})
    key = entity.lower()
    if key in seen:
        continue
    seen.add(key)
    out.append({"query": query, "entity": entity, "result": clean, "ts": time.time()})
    time.sleep(0.2)

with open(f"{ROOT}/book/events/evidence_raw.jsonl", "w") as f:
    for row in out:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
print(f"evidence rows fetched: {len(out)}")
print("sample:", json.dumps(out[0], ensure_ascii=False)[:400])