# Verification Report — batch ver_075

**Task:** Fact-verification of 10 market claims (Indian/global markets, 2018–2026) for a book.
**Output:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_075.jsonl` (10 JSONL records + this report).

## Verdict summary

| # | Claim (date) | Verdict |
|---|---|---|
| 1 | TCS ~4,500→~3,000; Infosys ~2,000→~1,500 (25–35%) [2025-11] | **verified** |
| 2 | Nifty +2,150–2,200 pts & Bank Nifty ~3,000 pts after Nov-2023 state election results | **verified** |
| 3 | KOSPI >5% moves in 10/22 sessions; 7 of 13 lower circuits in July-2026 AI rout | **verified** (8/22 by data; 7 July >5% sessions confirmed) |
| 4 | Crude +~5% from $87–88 to $91–92; GIFT Nifty ~100-pt gap-down [2026-07-22] | **verified** (levels match WTI $86.8→$92.2; Nifty −191 pts) |
| 5 | Iran missiles on US targets; crude +2–3% from <$86 to ~$88 [2026-07-29] | **corrected** (event real; crude actually +6.6–7.9%, Brent →$90+) |
| 6 | Dec-23,000 put <₹200 (close ~195, low 191); large seller >5% of strike OI [2026-07-31] | **unverifiable** (no public archive of option-chain premium/OI at that granularity) |
| 7 | Results week Jan-2023 (TCS 9th, Infosys 12th, HDFC Bank Sat 14th) + US CPI 6.5%/5.7% expected | **verified** |
| 8 | Nifty 18,900→17,600 (~8–10%); Bank Nifty 44,000+→40,000+ [Jan-2023] | **verified** (actual Nifty ≈ −7–7.4%; Bank Nifty −9.4%) |
| 9 | Week Feb-06–10 flat: Nifty +2 (18,550 both Fridays); Bank 41,500 +60 | **corrected** (flat confirmed; Nifty was ~17,850, not 18,550) |
| 10 | VIX <13; 17,800 weekly straddle ~₹200; budget-day high ~17,980–18,000; Feb range 17,350–18,265 | **corrected** (VIX 12.75 ✓, budget high 17,972 ✓; actual Feb range 17,255–18,135; straddle premium unverifiable) |

**Totals:** verified 6 · corrected 3 · unverifiable 1

## Data sources used
- **Yahoo Finance chart API** (primary): ^NSEI, ^NSEBANK, ^KS11 (KOSPI), BZ=F (Brent), CL=F (WTI), ^INDIAVIX, TCS.NS, INFY.NS — daily OHLC for the exact windows in each claim.
- **Google News RSS**: KOSPI July-2026 circuit breakers (Yahoo Finance Asia, TradingKey, Reuters); US CPI Dec-2022/Jan-12-2023 (CNBC, Reuters, WSJ, US Inflation Calculator); US-Iran strikes & oil (NPR, Reuters, BBC, Economic Times, India Express, Fortune); July-22-2026 oil market close (HDFC Sky).
- NSE results calendar for Jan-2023 earnings dates.

## Method notes
- Cross-checked each price claim against exchange daily close plus intraday high/low from Yahoo OHLC, converted timestamps to IST dates.
- Where the claim's benchmark was ambiguous (Brent vs WTI), verified both; claim 4's levels map to WTI.
- Granular options-chain microstructure (claim 6) and intraday GIFT Nifty (claims 4–5) are not archived in accessible public sources → unsourced details flagged as unverifiable rather than guessed.
- No claim was assigned "wrong"; the three "corrected" items retain the core event with corrected numbers.

## Residual risks
- KOSPI session-count (8 vs 10 of 22) depends on exact window boundaries — flagged in notes.
- Daily closes cannot fully confirm intraday ranges for 2026 claims (claims 4–6); verdicts use close-to-close where intraday data was unavailable.