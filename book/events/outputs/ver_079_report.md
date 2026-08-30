# Verification Report — Batch 079

Task: verify 10 market-event claims (Indian + US markets, 2018–2026) against web sources for the anonymized "Dhanraj" book project.

## Method
- Used Bing web search and Google News RSS (`news.google.com/rss/search`) via curl to find reputable sources (Reuters, CNBC, PBS, The Hindu, NDTV, Bloomberg, ET Auto, Bitcoin Magazine).
- 1–3 queries per claim; verdicts: verified / corrected / wrong / unverifiable.
- Granular intraday option-chain detail (claims 5, 6, 9) is not confirmable from public news sources → marked `unverifiable` (treated as speaker recollection; book policy: do not state as verified fact).

## Results summary
| # | Claim | Verdict |
|---|-------|---------|
| 1 | Crude ~$70-71, gold down, rupee <76 (Dec 21 2021) | verified |
| 2 | Dow -~500 Fri Sep 30 → +~750 Mon Oct 3 2022 | verified |
| 3 | BTC ~$21k → ~$17.6k (Jun 18 2022) | verified |
| 4 | LIC bought aggressively 2015; low never retested | corrected |
| 5 | Dec-series options calls -100/120, puts +20/30 (May 22) | unverifiable |
| 6 | Call writing 21,700-22,000; ~70-75 premium (Jan 2 2024) | unverifiable |
| 7 | Adani SC verdict Jan 3 2024 (gamma effect) | verified |
| 8 | BTC >$45k Jan 2 2024, then near $40k; cryptos -5-15% | verified |
| 9 | Nasdaq-100 ATM straddle >$10 into Feb 14 2023 CPI | unverifiable |
| 10 | Bank Nifty ~-1,000 pts over Feb 16-17 2023 | unverifiable (plausible for the week) |

## Key notes for the book
- Claim 4 correction is important: the "low was never retested" framing is inaccurate for Nifty (Feb 2016 lower low ~6,825); use as a corrected/recollected anecdote, not established history.
- Claims 7/8 verified via strong sources (Reuters/NDTV on SC verdict; CNBC on BTC >$45k) — safe to state.
- Claims 5/6/9/10 involve granular intraday numbers that only the source-speaker would know; the book should attribute them as recollections or omit.

## Files
- Results: `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_079.jsonl` (10 lines, valid JSONL)
- Report: `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_079_report.md`

## Residual risks
- Bing/Google News snippets provide partial text only; exact intraday index levels and option strike prices are inherently unverifiable from press coverage.
- Dates in the environment (2026) mean some searches return future-dated articles; claims were matched against the historical event anchors described, not the article dates.