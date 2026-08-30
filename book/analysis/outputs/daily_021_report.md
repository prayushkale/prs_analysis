# Batch daily_021 — Analysis Report (2022-03-23 → 2022-04-08)

## Deliverable
- **Data file:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_021.jsonl` — 25 JSON lines (one per transcript), schema-validated.
- **Coverage:** ids 0928–0956 (all 25 assigned transcripts read in full): 13 pre-market, 12 post-market reports.

## Window narrative
This 13-session window captures the **March-2022 expiry into the HDFC merger shock**:
1. **Mar 23–25:** Violent range days (17,000–17,500) around the **Kotak Mahindra Bank block deal** (Canadian pension fund, 4 cr shares, ~₹6,800 cr, executed ~₹1,700–1,715). Key teaching: strip block deals from FII data; net institutional flow stayed ~+300 cr despite the sale.
2. **Mar 29–31:** Russia's Kyiv scale-back → relief rally; **US yield-curve inversion (2s10s)** noted as a forward recession signal; **both FIIs and DIIs bought >₹1,000 cr on consecutive days** (rare); most-volatile March series (15,700–17,500) closed at the top; US **SPR release 1M bbl/day**.
3. **Apr 1:** Flat-open one-way rally (+350), **India VIX −10%**, SEBI >9-month-expiry margin release, FIIs third straight >₹1,000 cr day.
4. **Apr 4–8:** **HDFC–HDFC Bank merger announcement** → upper circuits, Nifty >18,000 (+250 pts from the Twins), then a full round trip back to pre-announcement levels in four sessions (HDFC 2,450→2,950→2,450). Extraordinary futures premium anomaly (Nifty ~90 pts, Bank Nifty ~200) — "either spot catches up or the market falls." Fed minutes ($95B/month runoff), Brainard hawkish, Nasdaq −5%/2d, FII flips to selling (−₹5,000 cr on 7-Apr).

## Recurring lessons captured (book-relevant)
- Price↑+OI↓ = short covering vs price↑+OI↑ = fresh longs (0948/0950); price↓+OI↓ = long unwinding (0954).
- Sellers' breakeven ceiling = strike + collected premium (0953).
- Block-deal distortion of FII data (0931/0932/0954); weight × discount = opening drag (0930).
- Gap taxonomies: no-news gap-ups fade from the first candle (0938/0944/0951); flat-open rallies sustain (0945).
- Futures-premium anomalies as regime signals (0938/0944/0955/0956).
- VIX regimes: India VIX 28→18 path; falling-VIX-on-red-day = limited downside (0932/0937).
- Positive black swans (0949): May-2018 RBI FII-window event, 2019 corporate-tax-cut candle.
- 2022 "beach horse" / trader's-year thesis (0933/0955); Dec-2022 18,000 straddle @~2,500.

## Verification queue highlights (verify=true)
Kotak block deal terms & price; Hero MotoCorp ₹1,000 cr IT finding & company denial; Russia Kyiv scale-back (29-Mar); 2s10s inversion (29-Mar/1-Apr); SPR 1M bbl/day; China PMI 49.5; Axis–Citibank India retail deal; HDFC merger 4-Apr-2022; FY22 FII selling ~₹2.5 lakh cr; HDFC Bank 20-quarter loan growth; GST ₹1.42 lakh cr; Musk 9% Twitter stake; Fed $95B/month runoff; FII flow figures (481/600/−1740/+2091/+50/+1357/+1200/+3100/+1145/+1910/+1152/−2280/+633/−2000/−5000).

## Identity/promo leaks logged (for scrub pass)
Name intro variants in every file ("P. R. Sundar/Sunder"); sponsors: TaxBuddy/taxbeddy, FinBingo/swinbingo/finbingo, 5paisa (5pcet/5pisa/pi pisat), Delta Exchange; supertrend course promo with "link in the description" (0941); personal P&L claims (0945: 30 lakh day / 7 cr margin / 25 cr year target) — flag to genericize; "going for a party" (0955); video-glitch artifact (0951). FM's retail-vs-FII public comment (0953) kept as market context, not politics.

## Data quality
All 25 read fully; ASR corrections applied (taxbeddy→TaxBuddy, swinbingo→FinBingo, 5pcet/5pisa→5paisa, Hrithik/heretic→heavyweight framing, Bagniti→Bank Nifty). Two ASR-damaged passages (0929 "bank FTE", 0950 partial garbles) interpreted from context; flagged uncertain OI/premium figures as verify=false where only speaker-stated.
