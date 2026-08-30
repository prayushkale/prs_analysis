# Batch daily_022 — Analysis Report (25 transcripts, 08–29 Apr 2022)

## Output
- **JSONL written:** `book/analysis/batch_daily_022.jsonl` — 25 lines, one per transcript, all schema-validated (ids 0957–0988, chronological, unique).
- **Coverage:** 13 post_market, 12 pre_market. All read in full.

## Digest (5 lines)
1. **Counts:** 25/25 analyzed, 63 event claims queued for verification (all flagged `verify:true` where externally checkable), 21 transferable lessons, 22 cleaned quotes, leaks logged in every transcript where present.
2. **Most notable events asserted:** Apr-19-2022 panic (Bank Nifty −1300 pts in ~45 min with FIIs net-selling only ~₹2,000 cr net — basket-order timing); Dow −2000 pts Apr 21→25 with Feb-2018 LTCG+inflation parallel; HDFC Bank block deal ₹1,300 cr (Apr 21) flipping headline FII −700 to net +600 ex-deal; Infosys/Alphabet/Meta/Netflix/Amazon results-day gaps (−25% to +20%); Reliance $250B mcap first for India; LIC IPO size cut to ₹20–21k cr; FII 13-day selling streak ending Apr 28 (+750 cr); US Q1 GDP −1.4%.
3. **Recurring method content (gold for book Parts II & VI):** futures-premium contraction law; OI-ladder range definition (strike-minus-premium breakeven math); FII futures long% contrarian map (>80% risk / <45% upside); block-deal-adjusted flow reading; post-2pm basket-order tell; "kangaroo market" 2022 range thesis (17000–18000 / 16800 support); results-asymmetry (good = flat, bad = crash); zero-cost collar and opposite-leg straddle exits.
4. **Data quality:** high — exact strikes, premiums, flows and timings quoted consistently; ASR garbles handled via dictionary (FIA→FIIs, Quotac→Kotak, "Industry nearly where"→IndusInd, SGX 60,850 flagged as garble in 0985); several level claims are speaker-recalled (marked `verify:false`) — India VIX +8%/+15% figures, 17400CE +1 lakh contracts, Bank Nifty ADR math.
5. **Leaks logged for QA:** sponsors (Delta Exchange, TaxBuddy, Finbingo) in 24/25; name variants throughout; personal artifacts (wife-as-secretary, movie/party, YouTube income in 0974, workshop promo in 0962, Adani-video tease in 0987, SEBI-non-registered disclaimers). None copied into JSON content fields; all confined to `leaks` arrays.
