# Verification Report — batch ver_021 (10 claims)

Method: Google News RSS search (plain-HTML, works without API key) as primary discovery channel; news titles and headlines cross-checked. Sources preferred: Reuters, Economic Times, CNBC, Moneycontrol, Business Standard, Investopedia, MarketWatch, Times of India.

## Verdict summary

| idx | Verdict | One-line result |
|-----|---------|-----------------|
| 1 | verified | S&P first close >5,000 on 9 Feb 2024; NVDA/MSFT ATHs; NVDA $100→$700 path correct. |
| 2 | unverifiable | Aug-2022 expiry-day intraday numbers not independently confirmable. |
| 3 | verified | 7 IPOs/Rs 30,000+ cr week opening ~6 Oct 2025 (Tata Capital, LG Electronics) confirmed. |
| 4 | corrected | Selloff sessions were 20–21 Sep 2023 (not 19–20); ~600 pts/~3.5% combined decline; NVDA ~15–18% off record. |
| 5 | verified | March 2026 record FII outflow, full month Rs 1.14 lakh crore (ET/CNBC/Upstox). |
| 6 | verified | HDFC results 16 Jan 2024 evening; 17 Jan crash details (HDFC −8.5%, Sensex −1,628, Nifty −460, Bank Nifty −1,500+). |
| 7 | verified | Fed 75bp hike 21 Sep 2022; fell → rallied in presser → sold off into close (MarketWatch/Reuters). |
| 8 | verified | RBL Bank CEO change over 25–26 Dec 2021 weekend; −20% on 27 Dec; Vishwavir Ahuja on leave. |
| 9 | corrected | S&P fell ~1.7% (~66 pts to ~3,789), not 80–90 pts / >2%; timing & presser arc accurate. |
| 10 | verified | Mauritius tax-treaty trigger confirmed; ~990 pts / ~4.3% drop from 1-Apr record to ~21,777 on 19 Apr 2024. |

## Key corrections for the book (material discrepancies → endnote candidates)
- **Claim 4**: shift dates to 20–21 Sep 2023 for the two-session Nasdaq selloff; FOMC met 19–20 Sep.
- **Claim 9**: S&P −1.7% (~66 pts), not −2% / 80–90 pts; Dow −522 (−1.7%), Nasdaq −1.8%.
- **Claim 6 nuance**: "Nifty never closed above 22,000 after 16 Jan 2024" is true only as of the transcript date (12 Feb 2024); Nifty reclaimed 22,000 in early March 2024 — the book should date-stamp this statement.
- **Claim 5 nuance**: full-month March 2026 FII outflow was Rs 1.14 lakh crore (the ~57,000 cr cited was mid-month); both true, differently dated.

## Residual risks
- Evidence URLs are Google News search-result links (reliable discovery URLs that resolve via Google News), not canonical publisher pages; acceptable for the sources appendix, but canonical URLs would require fetching each article page.
- Claim 2 was judged unverifiable through available channels; recommend either dropping the specific intraday numbers or keeping them as an unattributed, apparently-missing-source anecdote with a hedge.
- Claim 1's $900-strike NVDA call premium (~$6) is from the transcript only.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Verified exactly the 10 claims in the task (no scope change); wrote the JSONL result file and the required report; verdicts, corrections, and evidence are grounded in Google News RSS headlines from Reuters/ET/CNBC/Moneycontrol/News18/Investopedia."
    }
  ],
  "changedFiles": [
    "/home/ubuntu/repos/prs_analysis/book/events/verified_batch_021.jsonl",
    "/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_021_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "curl -s https://news.google.com/rss/search?q=<query> (multiple targeted queries per claim)",
      "result": "passed",
      "summary": "Used Google News RSS as search channel; returned article titles that confirmed/corrected claim details"
    },
    {
      "command": "curl -s https://r.jina.ai/<url> for page fetches",
      "result": "passed",
      "summary": "Fetched News18 article shell (nav only); headlines confirmed via search titles"
    },
    {
      "command": "python3 - json validation of written JSONL",
      "result": "passed",
      "summary": "verified_batch_021.jsonl parses as valid JSONL (10 lines)"
    }
  ],
  "validationOutput": [
    "JSONL written: 10 records, one per claim, schema-conformant",
    "Verdict counts: 7 verified, 2 corrected, 1 unverifiable",
    "Every verified/corrected verdict has at least one evidence item; unverifiable claim (idx 2) flagged in notes"
  ],
  "residualRisks": [
    "Evidence URLs are Google News search links, not canonical publisher URLs",
    "Claim 2 intraday numbers unverifiable; recommended hedged or dropped",
    "Claim 1 NVDA option premium is transcript-only detail"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added verification results for batch 021 (10 claims) as JSONL plus this human-readable report with verdicts, corrections, evidence, and residual risks.",
  "reviewFindings": [
    "no blockers: all 10 claims assigned verdicts with evidence; corrections surfaced for claims 4 and 9 and nuances for 6 and 5",
    "note: claim 2 remains unverifiable and should be handled per residual-risks guidance"
  ],
  "manualNotes": "Google News RSS worked reliably as the no-API search channel; JSONL is ready for ingestion into book/events/verified DB. Recommend downstream fetch of canonical URLs for the sources appendix when feasible."
}
```