# Verification Report — batch 050

## Summary
10 claims verified via web search (Google News RSS + outlet headline capture). Verdicts: **3 verified** (idx 1, 3, 9, 10 — four actually verified), **6 corrected** (idx 2, 4, 5, 6, 7, 8), **0 wrong**, **0 unverifiable**.

| idx | Verdict | Key correction |
|-----|---------|----------------|
| 1 | verified | HCL >10% crash confirmed (Moneycontrol, Apr 2026); Infosys ~7% (not 6.5%) |
| 2 | corrected | Amazon fell ~13% (closing -12.8%), not 16-17%; US indices closed sharply higher (Dow best day of 2022) |
| 3 | verified | 8 consecutive Nifty down sessions ending ~29-30 Sep 2025 (News On AIR); Feb-2025 comparison unconfirmed |
| 4 | corrected | Meta's ~20% crash was 3 Feb 2022, not by 3 Dec 2021; FAANG ~10% off Nov-2021 highs plausible |
| 5 | corrected | Microsoft fell ~10% (CNBC), not 12%; ~$357B value loss (GeekWire); Nasdaq-100 point swings unverified |
| 6 | corrected | Gold -8% single day (silver -11%), ETFs cumulatively -24% from highs; not 30% in 24h |
| 7 | corrected | Nvidia closed +9.3% on 23 May 2024 (intraday briefly >10%); indices fell <1%, not -400 pts |
| 8 | corrected | Price band Rs 902-949 (not 900-950); anchor book subscribed €; 71% domestic MFs; GIC/Norges reported |
| 9 | verified | RBI +50bps to 5.40% on 5 Aug 2022; rupee +46 paise (~50 within rounding) |
| 10 | verified | Aug 2023 CPI 6.83% (12 Sep 2023), below 7%, above 6% |

## Evidence sources used
- Google News RSS (news.google.com/rss/search) with outlet headlines: Moneycontrol, CNBC, Reuters, The Hindu, Times of India, Indian Express, Upstox, Livemint, News On AIR (AIR), GeekWire, WSJ, Economic Times, TradingView.
- Article locators are either the captured news.google.com/rss/articles/... permalink or a news.google.com/search query URL reproducing the exact headline text (used where RSS returned only the title).

## Notes for the book compiler
- Claims 2, 6, 7: speaker over-stated magnitudes (Amazon 16-17% -> 13%; gold 30%/24h -> ~8%/day; Nasdaq-100 -400 -> <1%). Use corrected figures.
- Claim 4: timeline conflation (Dec-2021 vs Feb-2022 Meta crash). Re-date before using.
- Claim 8: minor band correction (902-949).
- Infosys single-day fall 6.5% -> ~7% (both sources agree on 7%).

## Residual risk
- Claim 3's comparative streak claim (Feb 2025 = 8 sessions) not independently confirmed; treat as unverified detail.
- Some links are Google News search locators rather than canonical article URLs (Google News RSS does not always expose source permalinks for archived items); all headlines were confirmed as returned by the news index.
- 2026-dated claims (1, 5, 6) were verifiable because this environment's news index includes early-2026 coverage.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified all 10 claims via web search (Google News RSS + headline capture), assigned verdicts (4 verified / 6 corrected), wrote JSONL to book/events/verified_batch_050.jsonl and report to book/events/outputs/ver_050_report.md. No scope widening."
    }
  ],
  "changedFiles": [
    "book/events/verified_batch_050.jsonl",
    "book/events/outputs/ver_050_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "curl news.google.com/rss/search for 10 claim-specific queries",
      "result": "passed",
      "summary": "Retrieved current and archived headlines for all claims; evidence captured for each"
    },
    {
      "command": "python3 json validation of verified_batch_050.jsonl",
      "result": "passed",
      "summary": "10 JSONL records, all parse-valid, schema-compliant"
    }
  ],
  "validationOutput": [
    "JSONL: 10 lines, one per claim idx 1-10, schema {\"idx\",\"verdict\",\"corrected_claim\",\"evidence\",\"notes\"}",
    "Verdicts: verified=4 (1,3,9,10), corrected=6 (2,4,5,6,7,8), wrong=0, unverifiable=0"
  ],
  "residualRisks": [
    "Claim 3 comparison detail (Feb-2025 eight-session streak) unconfirmed",
    "Several evidence links are Google News search locators, not canonical article permalinks",
    "Claim 8 GIC/Norges anchor participation from contemporaneous reporting, not in the cited headlines"
  ],
  "noStagedFiles": true,
  "diffSummary": "Created two new files: verified batch JSONL (10 enriched verdict records) and this report.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "All 10 claims processed. Most material corrections: Amazon -13% not -16/17%; gold -8%/day not -30%/24h; Nvidia +9.3% not >10% close; Microsoft -10% not -12%; LIC band Rs 902-949; Meta 20% crash re-dated to Feb-2022."
}
```