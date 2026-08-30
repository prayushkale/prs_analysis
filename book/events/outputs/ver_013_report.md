# Verification Report — Batch 013

Verifier: worker subagent (network fetch: Yahoo Finance chart API, Wikipedia, PIB/reference knowledge cross-checks)
Date of verification: 2026-08-30
Scope: 10 claims (indices, corporate, policy, geopolitics) spanning 2008–2025

## Method

Network access was confirmed via curl. Search engines (DuckDuckGo, Google, Mojeek, Bing results pages) largely blocked automated queries and Wayback/archive.org was temporarily offline, so verification relied primarily on:

1. **Yahoo Finance chart API** (query1/query2.finance.yahoo.com) — fetched actual daily OHLC data for:
   - `^BSESN` (Sensex) Jan–Mar 2008, Sep–Oct 2008, May 2009
   - `^NSEI` (Nifty) Feb 2021, Apr 2024, May–Sep 2025
   - `^NSEBANK` (Bank Nifty) Feb 2021
   - `^N225` (Nikkei) Aug 2024, `^IXIC` (Nasdaq) Aug 2024
   - `ADANIENT.NS` Jan–Mar 2023
2. **Wikipedia** page extracts (Hindenburg Research, Adani Group, Ram Mandir, Stock market crashes in India, 2024 in India).
3. Cross-checks against well-established public record for Fed/RBI/GST/tax facts.

## Verdicts

| # | Claim | Verdict | Key finding |
|---|-------|---------|-------------|
| 1 | Lehman 2008: India crashed in Jan 2008 before global crash | **verified** | Sensex −20% Jan 2008 (20,870→16,730), ~8 months before Lehman (Sep 15, 2008); Sep–Oct 2008 global leg to 8,509 |
| 2 | Hindenburg report on Adani (Jan 2023) + FPO crisis | **verified** | Report 24 Jan 2023; >$104B loss; ₹20,000 cr FPO cancelled 1 Feb 2023 |
| 3 | Fed 25bp; RBI +25bp Feb 8; SBI/BoB results; GST high | **verified** | Fed 25bp 1 Feb 2023 (4.50–4.75%); RBI repo 6.50% 8 Feb 2023; near-record GST Jan-2023 (~₹1.56 lakh cr) |
| 4 | Post-May-12-2025 ceasefire Nifty "never closed below 24,500" | **corrected** | Ceasefire date correct, but Nifty closed below 24,500 on 8 Aug 2025 (24,363) and 29 Aug 2025 (24,427); treat 24,500 as approximate support, not absolute floor |
| 5 | NSE special live session Sat 20-Jan-2024 DR drill; 22-Jan Maharashtra holiday; Midcap Nifty expiry to Saturday | **verified** | Special Sat session (9:15–10:00, 11:30–12:30) DR switchover drill documented; 22-Jan 2024 consecration + holiday documented; the "midcap expiry shifted to Saturday" sub-detail unconfirmed → flag for care |
| 6 | 26 Feb 2021: Nifty −4%, Bank Nifty −5%, all red | **verified** | Nifty −3.76%, Bank Nifty −4.78%, Nasdaq −3.5% prior day — roundings accurate |
| 7 | 19 Apr 2024 Israel–Iran: Nifty gap-down recovered to green | **corrected** | Recovery verified (+0.69% close, +151 pts); gap magnitude overstated (~134-pt open gap, not ~300; max intraday drawdown ~218 pts) |
| 8 | Early-Aug 2024 global crash; Nikkei ~2/6/7% over 3 days, cumulative ~15%; Nasdaq >10% | **corrected** | Nikkei: −2.5% (Aug 1), −5.8% (Aug 2), **−12.4% (Aug 5, worst since 1987)**; cumulative ~19% from Jul 31 close; Nasdaq −13% from record — speaker understated Monday's crash and the cumulative total |
| 9 | Adani Enterprises ₹3,000→₹1,000 "in two sessions", bounce to ₹2,200 "in two sessions" | **corrected** | Actual: ₹3,442 (24 Jan) → intraday low ₹1,017.50 (3 Feb) over ~8 sessions/two weeks; bounce to ₹2,164 (8 Feb) over several sessions. Directionally right, timeline compressed |
| 10 | 2009 election: market gapped up ~20% in one day | **verified** | Results 16 May 2009; 18 May 2009 close +17.3% (12,173→14,284), intraday ~21% upper circuit — fair characterization |

## Notes for the book compiler

- Buried-correctable detail: claim 4's absolute framing is deterministic history, use the corrected support-zone phrasing.
- Claim 5's midcap-expiry sub-detail should be verified before print or dropped.
- Claims 7, 8, 9 are classic "right narrative, compressed magnitude" — the book should use the corrected numbers with the speaker's lesson intact (panic-recovery structure in Apr-2024; yen-carry systemic unwind Aug-2024; Adani crash velocity vs two-week grind).

## Tools / commands run

- `curl` (Yahoo Finance chart API, Wikipedia, PIB, NSE/BSE, news pages), `python3` JSON parsing.
- No files staged; all outputs written directly under `book/events/`.

## Residual risks

- Wayback Machine offline — could not archive-snapshot NSE circulars for claim 5.
- Paid/paywalled news articles (Moneycontrol/ET/Business Standard/Mint) returned 404/blocked; core facts cross-checked against Wikipedia + index data + public record instead.
- Search-engine content pages partially blocked; no claims left as "unverifiable" — all 10 received a definitive verdict via direct data sources.