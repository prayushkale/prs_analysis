# Batch daily_029 — Analysis Report

## Deliverable
- `book/analysis/batch_daily_029.jsonl` — 25 JSON lines, one per transcript, in batch order (ids 1194→1244), schema-validated.

## Coverage
| Type | Count |
|---|---|
| post_market | 12 |
| pre_market | 11 |
| (weekly) | 0 |
| Total | 25/25 |

Period covered: 23 Aug 2022 – 13 Sep 2022 (weekly expiry cycle spanning the August expiry, Jackson Hole, black-Monday gap-down, one-day reversal, September volatility).

## Notable extractions
- **82 concrete event claims** flagged for verification, including: Jackson Hole 26 Aug 2022 (Powell hawkish), the 29 Aug 2022 gap-down (2nd biggest of 2022), the 30 Aug one-day reversal with FII +₹4,000cr, the ~10% two-day crude crash, export-duty hike on petrol/diesel/ATF, Gazprom's Nord Stream halt (2 Sep), US payrolls 315k (2 Sep), ECB 75bp (8 Sep), Bank Nifty reclaiming 40,000 (first since 28 Oct 2021), Adani Enterprises entering Nifty 50 (eff. 30 Sep), Reliance Jamnagar CDU/FCC shutdown, India CPI ~7% (12 Sep), 10-crore demat accounts milestone, India bond-index inclusion talk (~$30bn).
- **Strategy content captured**: opening Bank Nifty straddle with 60-pt stops (~1% margin risk), call calendar (17,500CE monthly/weekly), far-strike "pocket money" sales (FinNifty 5-6₹ × 5,000 lots), collar construction on Infosys, low-VIX near-strike warning (BN 39,500/39,600 squeeze).
- **Recurring frameworks**: good-news-is-bad-news regime; retracement ladder (50%→61.8%→100%) on S&P; FII short-% as covering fuel (66%→81%); futures premium as froth gauge (100→15-20 pts); support ratchets (16,500→17,000→17,400→17,500).
- **Leak log (banned-term candidates)**: name variants ("P. R. Sundar", "P. R. Sunder", "P F Sunder", "P. S. Sundar"); sponsors (Delta Exchange variants, TaxBuddy ASR garbles "taxbeddy/taxbendy/taxbyd/Taxbytee"); video artifacts (Aquaman anecdote, shirt joke, "my show", Galactica/Sentosa travel); travel/residency hints (Singapore→Chennai flight, Bangkok conference ×2); political content to drop (Pelosi-Nvidia aside, DMK/BJP disclaimer, "bear cartel" speculation); personal holdings mentions (Vodafone Idea shares).
- **Data-quality flags**: 1244 "nearly 1800 point gap up" is an obvious ASR garble (~80-100 points intended) — annotated; 1211 "78 percent move" likely "7-8%"; 1236 "Kaiser Motors" likely Eicher Motors; Suzlon pledge counterparty (SBI Capital clarification) and several index-history dates (BN 41,800 peak / 28 Oct 2021 breakdown) marked `verify:true`.

## Data quality
All 25 files read in full; no extraction errors; JSONL validated (25 lines, order matches batch manifest, 82 event claims, all required fields present).
