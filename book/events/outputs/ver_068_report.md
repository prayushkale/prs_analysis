# Verification Report — Batch ver_068

## Task
Fact-verify 10 claims about Indian/global stock markets (2018–2026) for an anonymized book, using web sources, and write results as JSONL.

## Output
- **Data file:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_068.jsonl` (10 records, validated JSON)
- **This report:** `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_068_report.md`

## Verdict summary

| # | Claim (short) | Verdict |
|---|---|---|
| 1 | US VIX +54% to ~28 on 26-Nov-2021 Omicron | **corrected** — US side verified (Dow -900+, S&P -2%, VIX ~28.6 documented via CNBC/NBC); India VIX +25%/to-20 sub-figure not independently confirmed |
| 2 | HDFC Bank Jan-2025 results + 23,200 call volume "insider" allegation | **corrected** — results date verified (Rs 16,736 cr, 23 Jan 2025); option-volume/insider claim unconfirmed, must be hedged in book |
| 3 | Expiry-day CAS exploitation scenario (₹2-3 ATM options, 20x on ±200-pt auction move) | **verified** — CAS mechanics confirmed (3:15-3:30 order window, random close 3:28-3:30, replaces VWAP close, effective 3 Aug 2026, Groww); 20x scenario flagged as analysis |
| 4 | SBI ~₹11,000 cr VIL exposure; 460→430 correction (Aug 2021) | **corrected** — VIL/bank exposure event verified (₹1.8L cr debt, Moneycontrol/IE Aug 2021); exact ₹ crore + price path unconfirmed |
| 5 | FMCG +1% on 7-Jul-2025, 20-25% below ATH | **corrected** — HUL +3% demerger rally 7-Jul-2025 verified (Value Research); precise index figures unconfirmed |
| 6 | SEC court summons on Adani bypassing govt; AEL -10%, Green -14%, Ports -7% (23-Jan-2026) | **verified** — Reuters/TOI/Moneycontrol confirm SEC filing + $12.5B market-cap loss; per-stock drops consistent with "up to 10-15%" |
| 7 | India VIX +12% over 1-3 Aug 2022, 3-day rise | **unverifiable** — no reachable source; micro-claim, transcript recollection only |
| 8 | SEBI CAS 3:15-3:28/3:30 random freeze; "F&O ends 3:15, equity prints 3:40" | **corrected** — CAS structure verified via Groww/Moneycontrol/NDTV; F&O actually EXTENDED to 3:40 PM (not ended at 3:15); closing price finalized 3:30-3:35 |
| 9 | 2023 US banking crisis SVB→Signature→First Republic(-33% Fri despite $30bn)→Credit Suisse | **verified** — Wikipedia + CNBC (First Republic slid ~33% after $30B infusion, 17-Mar-2023) + Forbes |
| 10 | FIIs sold >₹5,000 cr, DIIs bought ~₹3,500 cr on 24-Jul-2024 | **corrected** — post-Budget-2024 FII selling verified (Business Standard 26-Jul-2024); exact daily split unconfirmed |

## Verdict tally
- verified: 3 (claims 3, 6, 9)
- corrected: 6 (claims 1, 2, 4, 5, 8, 10)
- unverifiable: 1 (claim 7)
- wrong: 0

## Sources used
- Google News RSS (recent/archived items incl. 2021, 2023, 2024, 2025, 2026): CNBC, NBC News, Reuters, TOI, Moneycontrol, Business Standard, NDTV Profit, ET, Livemint, Fortune India, Elets BFSI, Value Research, News18, PIB, Indian Express
- Wikipedia API (2023 US banking crisis)
- Direct publish fetch: Groww "Closing Auction Session (CAS): Meaning, Timings, Process" (fetched HTML, 200 OK; verified 3:15-3:30 session, random close 3:28-3:30, F&O extension to 3:40, VWAP-reference mechanics)

## Constraints encountered
- Bing web search returns degraded/irrelevant results (consent wall) — unusable for verification.
- DuckDuckGo (html/lite), searx.be, Mojeek, Brave blocked or captcha-walled in this environment.
- Google News RSS article links require internal decoding that curl redirects do not expose (Error 400); cited links are the Google News RSS canonical links (title + publisher + date verified from RSS feed metadata).
- Global search engines (Google) blocked; used Google News RSS + Wikipedia API + direct publisher fetches instead.
- Historical daily-flow archives (exact FII/DII crore figures, exact VIX day-over-day percentages) were not reachable; such claims are marked corrected/unverifiable with hedge guidance rather than guessed.

## Residual risks
- Claims marked "corrected" due to unreachable exact figures could in reality be accurate (e.g., SBI ₹11,000 cr, FII ₹5,000 cr on 24-Jul-24); book text should use hedged phrasing ("recalled", "reportedly") until an on-demand verification pass with better tooling confirms them.
- Claim 3's "20x payoff" arithmetic is scenario analysis by the speaker, not a sourced fact — keep as analysis, verify the CAS payoff math internally before print.
- News highlights from Google News RSS include snippets; full-text was not always retrievable, so per-claim rounding is conservative.

## Files changed
- Created `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_068.jsonl` (10 validated records)
- Created `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_068_report.md` (this report)