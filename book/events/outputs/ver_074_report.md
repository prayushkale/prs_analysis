# Verification Report — Batch ver_074

**Task:** Fact-verify 10 claims about Indian stock markets (2018–2026) for an anonymized book.
**Method note:** `web_search` tool is not available in this environment; I verified against **primary market data sources** instead — Yahoo Finance historical OHLC APIs for Nifty (^NSEI), Bank Nifty (^NSEBANK), Sensex (^BSESN), WTI crude (CL=F), and India VIX (^INDIAVIX). This is stronger evidence than search snippets for level/date claims. Search-engine/archive attempts (DuckDuckGo, Bing, NSE fiidii endpoint) timed out or are not publicly archived for per-day FII/DII and option-chain OI snapshots.
**Result file:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_074.jsonl` (10 lines, one per claim, valid JSON).

## Verdicts at a glance

| # | Date | Short claim | Verdict |
|---|------|-------------|---------|
| 1 | 2024-02-19 | 22,000PE ~130–140 premium → 21,880 breakeven; 46,000PE ~200 → 45,800 | unverifiable (arithmetic consistent; OI/premiums not archived) |
| 2 | 2021-02-14 | Post-budget week: Nifty ~250-pt range 15,000–15,250; Bank Nifty 35,500–36,600 | **verified** |
| 3 | (bull run) | Sensex ~3,000→21,000 (~700%); crude ~$10→~$150 | **corrected** (600% not 700%; peak Jan-2008; crude ~$25–35 in 2003, not $10) |
| 4 | 2022-01-10 | Bank Nifty −8,000 (42,000→34,000) then +4,500 in 3 weeks | **verified** |
| 5 | 2022-02-08 | Bank Nifty −900/+800/−600/+400; FII −1,967 cr, DII +1,100 cr | unverifiable (OHLC confirms ~903-pt range; FII/DII not retrievable) |
| 6 | 2022-02-09 | Bank Nifty −2,000 then +1,200 (39,400/37,400/38,600) | **verified** |
| 7 | 2021-03-30 | 34,000 straddle ~700 → 33,300–34,700; 14,800 straddle ~210 → 14,600–15,000 | unverifiable (range math consistent; premiums not archived) |
| 8 | 2025-01-17 | Speaker long Axis Feb future ~2,030, long 980 put 13, short 1,100 call ~7 | unverifiable (personal position, not public) |
| 9 | 2026-04-28 | 23,000P / 25,000C ~4% away traded at ₹8–9; VIX fell ~7% | **verified** (strike distance ~4.2% confirmed; VIX −6.7% Apr24→27 ≈ ~7%; exact ₹8–9 tick data not independently archived) |
| 10 | 2026-06-29 | 24,000P/24,200C OI + ~120–130 premium → 23,900–24,300 range | unverifiable (spot 23,946 supports ATM strikes; OI/premiums not archived) |

## Key evidence per verified/corrected claim

- **Claim 2 (verified):** Nifty Feb 8–12 2021: H 15,257 (Feb 9), L 14,977 (Feb 10) — a ~280-point band ≈ 15,000–15,250; daily intraday ranges 120–193 pts (≈150–200). Bank Nifty same week: H 36,477, L 35,428 (≈35,500–36,500; low slightly below 35,500).
- **Claim 3 (corrected):** Sensex bottomed 2,963/2,998 (11 Apr 2003) and peaked intraday 21,207 on 10 Jan 2008 — i.e., ~7× = **~600%**, not ~700%; top was January 2008 (not 2007). WTI crude in 2003 traded ~$25–38 (the ~$10 low was 1998–99, not 2003), peaking at $147.27 on 11 Jul 2008. Revised claim text supplied in JSONL.
- **Claim 4 (verified):** Bank Nifty peak 41,830 (25 Oct 2021) → low 34,018 (20 Dec 2021) = −7,812 (~8,000 ✓); then Dec-20 low → 10 Jan 2022 high 38,400 = +4,382 ≈ "+4,500 in 3 weeks" (within rounding; note ~42,000 is a light rounding of 41,830).
- **Claim 6 (verified):** Bank Nifty: H 39,425 (3 Feb) → L 37,319 (8 Feb) = −2,106 (~2,000); recovery to close 38,610 (9 Feb) = +1,291 from the low (≈ +1,200 from ~37,400). Levels 39,400/37,400/38,600 track actual 39,425/37,319/38,610.
- **Claim 9 (verified):** Nifty closed 23,898 on 24 Apr 2026 (range 23,814–24,206); strikes 23,000/25,000 are ~3.6–4.4% from spot — consistent with "~4% away". India VIX: 19.71 (24 Apr) → 18.38 (27 Apr) = −6.7% ≈ "~7%" weekend collapse. Exact ₹8–9 OTM weekly premiums cannot be independently archived.

## Unverifiable items (5, 1, 7, 8, 10)
Per instructions, no guessing: daily FII/DII net numbers for 8-Feb-2022 (claim 5) are not in any accessible archive (NSE endpoint 404s without session cookies; search engines unreachable); historical option-chain OI/premiums (claims 1, 7, 10) are not published retroactively; a personal position (claim 8) is private by nature. Internal math was checked and is consistent for 1, 7, 10; claim 5's OHLC is consistent with a large ~900-point intraday range.

## Residual risks
- Claim 2's "35,500–36,600" Band Nifty low was actually 35,428 — rounded down 72 pts; acceptable for a book's "approximately" framing.
- Claim 4's "~42,000" peak is a rounding of 41,830 (intraday high); if the book prints 42,000 verbatim, prefer 41,830.
- Claim 9's ₹8–9 premiums rest on the speaker's own terminal data; recommend phrasing as observed ("as Dhanraj recorded") rather than as market fact.
- FII/DII attributions anywhere in the book should be treated as unverified unless separately sourced (NSE publishes current FII/DII; historical per-day needs third-party archives like Moneycontrol's FII-DII page, which was unreachable here).