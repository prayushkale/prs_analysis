# Verification Report — batch_026 (10 claims)

## Summary
- **verified:** 7 (claims 1, 4, 5, 6, 8, 9, 10)
- **corrected:** 3 (claims 2, 3, 7)
- **wrong:** 0 · **unverifiable:** 0

## Verdicts

| # | Claim (short) | Verdict | Notes |
|---|---|---|---|
| 1 | Maharashtra curbs → Nifty -400 pts (5 Apr 2021) | verified | Nifty 14,867→14,459 low (−408); Maharashtra restrictions confirmed 4 Apr 2021; recovery ~180 pts |
| 2 | Serum fire 21 Jan 2021 → BankNifty -900, Nifty -275 | corrected | Fire confirmed (5 killed). Actual intraday high-low: BankNifty −857, Nifty −236. Close: −357/−54 |
| 3 | Lehman 2008-09: Nifty −50%, then +100% | corrected | Actual peak-to-trough ≈ −60% (6,287→~2,460-2,520 Mar-09); >100% 2009 recovery confirmed |
| 4 | US B-2 + bunker-busters strike Iran nuclear sites | verified | Operation Midnight Hammer, 22 Jun 2025: Fordow/Natanz/Isfahan, GBU-57 MOPs from B-2s, Tomahawks |
| 5 | FII selling Oct-21→mid-22; Nifty 18,000+→15,200 | verified | Nifty peak 18,604 (19 Oct 21) → low 15,183 (17 Jun 22). CY2022 FPI record ₹2.77 lakh cr (Moneycontrol) |
| 6 | 30 Apr 2021 Nifty −250 intraday on COVID fears | verified | High 14,855→low 14,601 = −253.8; overnight gap ~150 (claim said 200) |
| 7 | 21 Dec 2020 "technical glitch" crash | corrected | Primary trigger was new UK COVID variant (Sensex −1,400 intraday); Nifty −646, BankNifty −1,406 intraday. Glitch reports were secondary |
| 8 | 2019 corporate tax 30%→22% | verified | Confirmed; effective ~25.17% incl surcharge+cess; new mfg 25%→15% |
| 9 | 20 Dec 2021 Omicron crash; BankNifty 36.7k→34k | verified | Nifty 17,298→16,410 (−888, ~900); BankNifty low 34,018 on 20 Dec; prior-month low 16,782 |
| 10 | Iran issue: crude → ~$120, cooled ~$90 | verified | 2026 Iran war: Brent peak $118.35 (31 Mar 2026) → $71.57 (1 Jul) → $96.78 (24 Jul); petrol +₹8-9/2 mo consistent |

## Methodology
- **Index levels**: NSE ^NSEI / ^NSEBANK daily OHLC from Yahoo Finance chart API (fetched directly).
- **Policy/event facts**: Wikipedia (en) articles + Moneycontrol archive headline; official PIB context for tax.
- **Search engines**: DuckDuckGo/Mojeek/Google/Ecosia blocked or generic from this IP; used Yahoo API + Wikipedia API + Moneycontrol direct + r.jina.ai reader for page rendering.
- 2–3 targeted searches/fetches per claim; claims classed correctly where distinct sources agreed.

## Files
- Results: `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_026.jsonl` (10 records)
- This report: `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_026_report.md`

## Residual risks
- Claim 10's transcript date context ("recent", ~2025 vs the 2026 spike) was disambiguated using the source date 2026-07-30 → 2026 Iran war; if the speaker actually meant June 2025 (Twelve-Day War), that spike was much smaller (~Brent $66-70) — flag in book text.
- Claims 2/3/7 carry inherent speaker rounding; corrected figures supplied for the book.
- News-source snippets for Dec 2020/Dec 2021 daily events rely on index data + Wikipedia rather than a single dated wire article; magnitudes are authoritative, media attribution for claim 7 is corrected per historical consensus.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified 10 claims via Yahoo Finance index OHLC, Wikipedia articles (2021 in India, 2025 US strikes on Iranian nuclear sites, 2026 Iran war fuel crisis, Stock market crashes in India, BSE SENSEX, Economic liberalisation in India), and Moneycontrol archive headline; wrote verified_batch_026.jsonl with verdicts + sources per the specified schema."
    }
  ],
  "changedFiles": [
    "/home/ubuntu/repos/prs_analysis/book/events/verified_batch_026.jsonl",
    "/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_026_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "curl Yahoo Finance chart API (^NSEI / ^NSEBANK historical daily data)",
      "result": "passed",
      "summary": "Retrieved daily OHLC for 2018-2026 windows incl. 2020-12-21, 2021-01-21, 2021-04-05, 2021-04-30, 2021-12-20, 2022-06-17, 2021-10-19"
    },
    {
      "command": "curl Wikipedia API (action=query extracts/search) for event and policy articles",
      "result": "passed",
      "summary": "Confirmed Serum Institute fire (21 Jan 2021), US strikes on Iran (22 Jun 2025), Brent 2026 peak $118.35, corporate tax cut 30/22, 2008 crash details"
    },
    {
      "command": "curl r.jina.ai reader + Moneycontrol article for FII 2022 record",
      "result": "passed",
      "summary": "URL headline confirms 'FPIs offload record Rs 2.77 lakh crore of Indian shares in 2022'"
    },
    {
      "command": "Search-engine probes (DuckDuckGo/Mojeek/Ecosia/Google/Bing news)",
      "result": "failed",
      "summary": "Blocked or generic from this datacenter IP; substituted with API/data-source verification"
    }
  ],
  "validationOutput": [
    "10/10 claims assigned verdicts (7 verified, 3 corrected, 0 wrong/unverifiable)",
    "All index-level claims cross-checked against raw Yahoo OHLC data",
    "JSONL written to verified_batch_026.jsonl (10 records, schema-compliant)"
  ],
  "residualRisks": [
    "Claim 10 ambiguity: 2026 Iran-war spike ($118.35) vs June-2025 smaller move - flagged for book text",
    "Media attribution for claim 7 (Dec-2020 crash) corrected to UK-variant trigger; secondary glitch reports existed"
  ],
  "noStagedFiles": true,
  "diffSummary": "Created verification output files for batch 026: 10 structured JSONL records with verdicts, corrected claims, evidence URLs and notes.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Search engines were blocked from this IP; used Yahoo Finance API + Wikipedia API + Moneycontrol+jina reader instead. All corrected claims contain the accurate figure for the book text."
}
```