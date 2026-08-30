# Verification Report — batch_056

**Task:** Fact-verification of 10 claims about Indian stock markets (2018–2026) for an anonymized book.
**Output data file:** `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_056.jsonl` (10 records, one per claim, JSONL, valid).
**Verdict distribution:** 5 verified · 5 corrected · 0 wrong · 0 unverifiable.

## Method
- Web sources: Google News RSS (with date windows where supported), Bing News, Wikipedia, Yahoo Finance historical OHLC data, PIB/ECI coverage.
- Verification standard: reputable outlets (Reuters, CNBC, Business Standard, Livemint, The Hindu, India Today, EcoTimes group), primary market data (Yahoo Finance daily series), government sources (PIB).
- Evidence URLs are stable, verifiable links (Yahoo Finance quote/history pages for numeric claims; Google News search listings carrying publisher + headline + date for news claims — publisher URLs were not reliably resolvable from the search feed in this environment, so the search listing is cited as URL of record).

## Findings per claim

| # | Date-focus | Verdict | Basis |
|---|-----------|---------|-------|
| 1 | Jun 2021 | **corrected** | LICHF -5.1% on 16 Jun 2021, close 495.05 (≈"near 500"); stock slid to ~470 by 18 Jun; Q4 FY21 results disappointment confirmed by the tape. "HDFC fell ~100" collateral detail not independently confirmable (HDFC Ltd delisted at Yahoo). |
| 2 | 24-25 Jun 2021 | **corrected** | RIL 44th AGM on 24 Jun 2021; Aramco chairman Yasir Al-Rumayyan inducted to board; ~₹75,000 cr new-energy push and Jio 5G plans announced; JioPhone Next unveiled with Sundar Pichai. RIL fell ~2.4% on AGM day and ~2.3% next day (≈4.5% combined); "~3%" is approximate. |
| 3 | late Jun 2023 | **corrected** | DAX fell 6 consecutive sessions (16→26 Jun 2023: 16,357.63→15,813.06) ✓. Nikkei fell in 6 of 7 sessions Jun 19–27 but its consecutive streak was only 4 — claim's "Japan down 5–6 sessions" is right as a count, not as consecutive. |
| 4 | 19-25 Nov 2021 | **verified** | Reliance & Aramco decided 19 Nov 2021 to re-evaluate the $15bn O2C stake deal; Reuters (25 Nov) reported it called off; NDTV/Indian Express (20–23 Nov) tied the O2C demerger plan and reported it shelved. |
| 5 | 16 Mar 2024 | **verified** | ECI announced 2024 Lok Sabha schedule 16 Mar 2024 (7 phases, counting 4 Jun) — PIB/The Hindu/TOI/WION. VIX below 15 (period band ~12–14) consistent. |
| 6 | 21-25 Apr 2022 | **verified** | Dow −2,169 points peak-to-trough (21-Apr high 35,492.22 → 25-Apr low 33,323.37) ≈ "~2,000 from Thursday afternoon to Monday"; close-to-close only −743 (Friday alone −981). |
| 7 | 28 Apr 2022 | **verified** | US Q1 2022 GDP −1.4% annualized (BEA advance estimate, 28 Apr 2022) — CNBC/Guardian. |
| 8 | Nov 2024 | **corrected** | FII selling streak was **38 sessions**, ending 25 Nov 2024 (FIIs net bought ~₹9,948 cr that day, CNBC-TV18) — not "30–35". 12 Nov daily sell ~₹3,500 cr band (approximate). |
| 9 | 3 Jul 2024 | **verified** | HDFC Bank +4% to record high after FII holding slipped below 55% (June-QT filing), MSCI weight-increase expectations with ~$3–4bn inflow estimates; MSCI raised the weight in Aug-2024 review. |
| 10 | 25-29 Jan 2024 | **corrected** | RBI allowed LIC to raise HDFC Bank stake to 9.99% (reported 25–26 Jan 2024, BS/Upstox). Shares +1.4% close-to-close (~2% intraday) on 29 Jan. ADR "~3.5%" could not be pinned to an official figure (reports ~3–4%). |

## Corrections that the book should apply (hybrid policy)
- Claim 2: state RIL fell ~2.3–2.4% per session around the AGM (two-day ≈ −4.5%), not a flat "~3%".
- Claim 3: DAX 6 consecutive sessions ✓; Japan "fell in 6 of 7 sessions" rather than "5–6 consecutive".
- Claim 8: FII sell streak = 38 consecutive sessions ending 25 Nov 2024.
- Claims 1 & 10 minor: "near ₹500" → 495.05 (16 Jun 2021); HDFC Bank +1.4% close (+2% intraday) on 29 Jan 2024; ADR move left hedged ("~3–4%").

## Residual risks
- Numbers in claims 1 and 10 quickly checked against published levels but the "HDFC fell ~100" (claim 1) and exact ADR % (claim 10) sub-details rest on approximate sourcing.
- Google News RSS is skewed to recent coverage; older-claim evidence uses RSS titles/dates (dated publisher articles) + Yahoo Finance data, which is adequate for the verdicts given.

---
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified all 10 claims against web sources (Google News RSS/Bing News/Yahoo Finance OHLC/PIB coverage), assigned verdicts (5 verified, 5 corrected, 0 wrong, 0 unverifiable), wrote corrected_claim with accurate numbers/dates for every corrected item, and cited 1-3 titled sources per claim. Scope unchanged: this batch's 10 claims only."
    }
  ],
  "changedFiles": [
    "/home/ubuntu/repos/prs_analysis/book/events/verified_batch_056.jsonl",
    "/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_056_report.md"
  ],
  "testsAddedOrUpdated": [
    "python3 JSON validation of verified_batch_056.jsonl (10 records, schema check on verdict/corrected_claim/evidence)"
  ],
  "commandsRun": [
    {
      "command": "python3 -c 'json validate verified_batch_056.jsonl'",
      "result": "passed",
      "summary": "10/10 records valid; verdicts: 5 verified, 5 corrected"
    },
    {
      "command": "curl Yahoo Finance v8 chart API (^DJI, ^GDAXI, ^N225, LICHSGFIN.NS, RELIANCE.NS, HDFCBANK.NS)",
      "result": "passed",
      "summary": "Retrieved daily OHLC used for numeric confirmation of claims 1, 2, 3, 6, 10"
    },
    {
      "command": "python3 book/scripts/gnews.py (Google News RSS searches) + bingnews.py",
      "result": "passed",
      "summary": "Located dated publisher articles corroborating claims 2, 4, 5, 7, 8, 9, 10"
    }
  ],
  "validationOutput": [
    "verified_batch_056.jsonl: 10 lines, each with idx/verdict/evidence (+corrected_claim where required); json.loads passes for all 10",
    "ver_056_report.md written to authoritative path with per-claim basis table + correction notes"
  ],
  "residualRisks": [
    "Claim 1 'HDFC fell ~100' sub-detail not independently confirmed (HDFC Ltd unavailable at Yahoo)",
    "Claim 10 ADR +3.5% exact figure not pinned (reports ~3-4%); kept hedged in corrected_claim",
    "Google News RSS skews recent; older articles cited via dated RSS listing + price data",
    "Evidence URLs for news claims use Google News search listings (publisher redirects not resolvable) plus live Yahoo Finance data URLs"
  ],
  "noStagedFiles": true,
  "diffSummary": "Created verified_batch_056.jsonl (10 claims verified/corrected with evidence+sources) and ver_056_report.md (findings, basis table, correction notes, acceptance report).",
  "reviewFindings": [
    "no blockers: all 10 claims dispositioned; 5 corrected items carry precise corrected_claim values"
  ],
  "manualNotes": "Claim 4 (RIL-Aramco Nov 2021 shelved/called-off deal) verified - matches speaker claim including 19 Nov 2021 announcement date. Claim 8's streak updated to 38 sessions (the number the book should use)."
}
```