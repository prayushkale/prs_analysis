# Verification Report — Batch 069

Task: fact-verify 10 claims from Indian-markets book corpus against web sources.
Output data: `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_069.jsonl` (10 records, valid JSONL).

## Verdict summary

| idx | Claim (short) | Verdict |
|-----|---------------|---------|
| 1 | India 2nd COVID wave peaks >4L cases/day (2021) | corrected |
| 2 | Brexit referendum 2016: Leave wins, consensus said Remain | verified |
| 3 | June-2021 auto sales 'not as good as expected'; auto stocks eased Jun 30 | corrected |
| 4 | FII ~₹3,000 cr / DII ~₹500 cr on 12 Jun 2024 | unverifiable |
| 5 | BF.7 variant cases in India (Gujarat/Odisha) + Nifty −186 pts 21 Dec 2022 | verified |
| 6 | Nifty 21 Nov 2024: low 23,263.2 / close 23,349.9 | verified |
| 7 | Apr-2023 week-ahead calendar (CPI Wed, results, Karnataka election) | verified |
| 8 | Gujarat exit polls 5 Dec 2022, results 8 Dec 2022 | verified |
| 9 | Hindenburg–Adani report 24 Jan 2023 (fraud/manipulation, ~15% value) | verified |
| 10 | Nifty never >4 consecutive monthly falls; Fed 25bp Mar-2023; Buffett talks | verified |

Counts: 7 verified, 2 corrected, 1 unverifiable.

## Key evidence

- **1**: Reuters: "India's daily COVID-19 cases pass 400,000 for first time" — that daily level was reached 30 Apr/1 May 2021 (speaker said "first week of April"). First wave peaked ~97k/day Sep 2020 (speaker said ~1,000/day). Both timings corrected; magnitude right.
- **2**: House of Commons Library "Analysis of the EU Referendum results 2016": Leave 51.9% / Remain 48.1%, turnout 72.2%, referendum 23 Jun 2016.
- **5**: TOI + NDTV (22 Dec 2022): 4 BF.7 cases reported in India (Gujarat + Odisha). Nifty 21 Dec 2022: O 18,435.2 → C 18,199.1 (−186.2 pts) per Yahoo ^NSEI — exact match. Caveat noted: BF.7 first detected in India in Jul 2022 (The Hindu).
- **6**: Yahoo ^NSEI 21 Nov 2024: low 23,263.2, close 23,349.9 — exact match.
- **7**: Karnataka election 10 May 2023 (India Today/TOI). US CPI released Wed 12 Apr 2023 (5.0% vs ~5.2% expected, prior 6.0%); FOMC minutes 12 Apr; TCS 12 Apr / Infosys 13 Apr / HDFC Bank 15 Apr 2023 all consistent with Q4-FY23 calendar.
- **8**: Reuters exit polls 5 Dec 2022; TheWire results 8 Dec 2022 (BJP 156).
- **9**: Al Jazeera 25 Jan 2023 (report dated 24 Jan US): short-Adani citing debt/accounting; ~85% downside estimate; short exposure via US-traded bonds + non-Indian derivs.
- **10**: Computed ^NSEI monthly closes 2000–2023: longest consecutive monthly decline = **3 months** (e.g., Mar–May 2022, Nov 2022–Jan 2023), so "never more than four consecutive months" holds (strictly, never even 4). Fed hiked 25bp 22 Mar 2023 (Reuters poll + Anadolu). Buffett–White House regional-bank talks reported 19 Mar 2023 (Fortune/BI).

## Method notes

- Sources: Google News RSS, Bing, plus Yahoo Finance chart API for Nifty level/monthly data and House of Commons Library via news RSS.
- Unverifiable (4): daily FII/DII split for a single date (12 Jun 2024) is not published in aggregable form; directionally consistent with June-2024 post-election FII selling, but exact ₹ figures remain unconfirmed.
- Corrected (1, 3): magnitude/direction right, dates or specifics off; corrected_claim strings supplied for both.

## Residual risks

- Claim-4 unverifiable: if the compiler wants this flow figure it must either drop or source NSDL/SEBI daily files directly.
- Claim-1 speaker dates are wrong in the source transcript; the corrected version should be used in the book.
- Claim-10's "5th month rallies after a large 4th-month fall" is the speaker's own statistical observation; the underlying streak data supports ≤3 consecutive falls, and no contradiction was found, but we did not validate the conditional pattern itself.