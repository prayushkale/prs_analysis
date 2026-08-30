# Batch daily_013 Report — 25 transcripts (0642–0675, Oct 22 – Nov 12, 2021)

## Output
- **JSONL:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_013.jsonl` — 25 valid JSON lines, ids in manifest order, coverage 25/25.
- Identity strings ("P. R. Sundar/Sunder" variants, sponsors TaxBuddy/5paisa, workshops/travel mentions) logged verbatim in `leaks` fields only; zero identity content in summaries/lessons/quotes.

## Counts
- 25 pre/post market reports: 12 post_market, 13 pre_market, 0 weekly (weekly appeared as dup context only).
- Event claims extracted: 60 (all flagged `verify:true` unless market-internal like premium/OI moves).
- Transcription quality: mixed; 0650 contains two merged takes of the same pre-market (noted in dup_flag); 0660 starts with a mic-off fragment; 0653 is audio-only with heavy run-ons. Numbers are mostly consistent and cross-corroborate (FII daily figures sum correctly across consecutive days).

## Most notable events in this window (for Phase 3 verification priority)
1. **Expiry-day crash Oct 28, 2021**: Nifty ~−350 to ~17,800; Bank Nifty ~−1,400 (−2,500 pts in 3 sessions); BSE mcap −₹5 lakh crore; Adani Ent −10%, PNB −10%, Adani Ports −7%, ITC −5-6% on results.
2. **IRCTC whipsaw**: −25% intraday on railway revenue-share proposal, withdrawn same session (late Oct 2021).
3. **FPI tax notices** on STCG-vs-LTCG set-off (Oct 2021) — speaker links to 2019 corporate-tax-cut precedent.
4. **IndusInd "evergreening"** via Bharat Financials (ex-SKS Microfinance), 84,000 accounts, −10% stock (Nov 8, 2021).
5. **Bank of Baroda foreign-remittance scam reports** (Oct 28, 2021).
6. **US Oct-2021 CPI 6.2%** (multi-decade high, above India's) and **Baltic Dry Index −50% in a month**.
7. **FII flow arc**: ~₹25,000 crore sold in Oct 2021; 20,000+ crore cumulative; Nov 1 first buy day; Nov 12 +500 crore.
8. **Paytm ₹18,000-crore IPO opening Nov 8, 2021**; SIP inflows >₹10,000 cr/month.
9. **Tata Motors ~₹4,000 cr quarterly loss, ADR +6%** (very-bad-news-is-good-news case).
10. **SBI results-day whipsaw Nov 3** (245→225 short-covering) and Sun TV +20% on Annaatthe release.

## Best transferable lessons harvested
- "Markets won't crash twice for the same reason" (0644).
- Long-term = economy, short-term = short covering/long unwinding (0648).
- Silent market = pending big move (0649).
- Expiry-at-month-low can mark multi-month low (0651, Sep-2020 parallel).
- FII-significance-decline thesis with April/July selling-vs-Nifty receipts (0652).
- Futures-premium as short-covering tell; premium erosion = health (0658/0659).
- Confluence resistance: Fib + 20-DMA + max-OI + premium (0667).
- Weight × fall index attribution (0668); concentrated vs broad selling (0670).
- Freight (Baltic Dry) as goods-inflation leading indicator (0673).
- Rally confirmation requires engine participation (banks lagging) (0675).

## Data quality & residual risks
- ASR noise per dictionary handled ("global queues", "Quotac", "weeks", "BeES", "taxbeddy"); residual garbles flagged where uncertain ("Hiram Muttakap" ≈ Hero MotoCorp, not asserted).
- Speaker's own positions (31 collars, PSU BeES +20%, call-ratio) captured as content, genericizable later.
- 0650's duplicated takes and 0661's mic-off fragment do not affect extraction.
- Dates: all from metadata + content cross-check (expiry weekdays align); exact event dates (e.g., IRCTC Oct 28 vs 29) left to Phase 3 web verification.
