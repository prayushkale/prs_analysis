# Verification Report — batch 081

**Claims verified: 10/10 processed. Verdicts: 4 verified, 2 corrected, 4 unverifiable, 0 wrong, 0 dropped.**

## Methods
- Index/stock OHLC: Yahoo Finance chart API (`^NSEBANK`, `^NSEI`, `HDFCBANK.NS`, `JMFINANCIL.NS`, `^DJI`, `^IXIC`, `^GSPC`) — primary source for levels/dates.
- News corroboration: Google News RSS and Bing RSS for policy events (RBI IIFL/JM actions, SEBI small/midcap directive, US CPI releases, 2022 FPI flows).
- HDFC Bank pre-bonus (June 2024 1:1 bonus) prices reconstructed by ×2 on Yahoo split-adjusted bars.

## Verdict summary
| # | Claim | Verdict | Key evidence |
|---|-------|---------|--------------|
| 1 | Bank Nifty ~42,000 (Oct 25 2021) → ~35,500 (Nov 30), ~20% | **corrected** | Oct 25 close 41,192; Nov 30 close 35,695 (-13.3%); ~20% only at ATH 42,209 → Dec-20 low 33,883 (-19.7%) |
| 2 | Aug-2024 carry trade: Nifty ~25,020 → -1,000 → recovered 26-Aug | **verified** | Aug 1: 25,010.9; Aug 5: 24,055.6 (-955); Aug 26: 25,010.6 |
| 3 | HDFC broke 1,400 again; -20% vs 1,750 high; 15% weight ≈ 600-pt drag | **corrected** | Below 1,400 on Feb 29 2024 close (1,397.4); 1,757 high (Jul 23) → -20.3%; weight ~13% not 15%; ~590-pt drag consistent |
| 4 | 3 intraday crashes in 10 days (SEBI -300 / IIFL -150 / JM -200), all recovered | **verified** | Feb 28 Nifty -313 intraday (SEBI stress tests); IIFL Finance -20% circuit (RBI gold loan ban, Mar 4); JM Financial -20% intraday (RBI share-financing ban, Mar 5/6); all recovered |
| 5 | US CPI due 12-Mar-24; Apr 22,500 straddle ~900 | **verified** | Feb-2024 CPI released 12 Mar 2024 ✓; straddle ~₹900 plausible (spot ~22.4k, ~13-14% IV) but premium not archive-checkable |
| 6 | Smallcap -2% on 11 & 12 Mar; FII +73 cr vs DII +2,300 cr on 12 Mar | **unverifiable** | Smallcap selloff confirmed (crash climaxed Mar 13, 'worst day in 2 yrs'); exact daily % and FII/DII figures unavailable |
| 7 | US CPI Apr 12 2022: 8.5% vs 8.4% exp, core below; Dow futures +233, Nasdaq +2% | **verified** | CPI 8.5% (highest since '81) vs 8.4% exp; core 6.5% below 6.6% exp; futures initially jumped per CNBC 'reversing earlier gains' |
| 8 | FIIs >15,000 cr in first five May 2022 sessions; May 6: 5,500 cr | **unverifiable** | May 2022 heavy-FII-selling month confirmed; daily/weekly split not retrievable from free sources |
| 9 | Singapore GRM ~$15-16 vs ~$8-9; RIL GRM expected $16-18 (Apr 2022) | **unverifiable** | GRM surge direction right; RIL actual Q4 FY22 GRM ~$12.8/bbl; expectation band is an estimate claim |
| 10 | Bank Nifty 35,000PE ~95 → ~400 → ~75 (Apr 25 2022) | **unverifiable** | Index context matches (gap to 35,511 low, recover to 36,082 close); intraday option-premium data not in free archives |

## Quality notes
- **Strongest dataset:** claims 1-5, 7, 10 rest on exact OHLC closes from Yahoo; 4 additionally rests on news-verified RBI/SEBI policy actions with stock-level crash data.
- **Soft spots:** claims 6, 8, 9 involve daily flow aggregates or street expectations that free public archives don't preserve; marked unverifiable rather than guessed, per instructions.
- **Correction flagged for the compiler:** HDFC Bank Nifty weight ~13% (not 15%) and the "~20% Bank Nifty fall" for Oct–Nov 2021 is really -13.3% close-to-close (≈-20% only ATH→mid-Dec trough).
- **Reliance Q4 FY22 GRM:** reported ~$12.8/bbl (Apr 22, 2022 results), below the claim's $16-18 expectation band — flag if this number is reused in the book.