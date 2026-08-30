# Batch daily_005 — Analysis Report

**Batch:** daily_005 (25 daily pre/post-market transcripts, 27 May – 14 June 2021)
**Output data:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_005.jsonl` (25 JSON lines, schema-validated, 25/25 valid)

## Digest

- **Counts:** 25/25 transcripts analyzed (10 pre-market, 15 post-market); 25 unique ids; 61 event claims (≈70% flagged verify); 23 lessons; 5 quotes; leak strings logged on every file.
- **Period story:** Continuous ATH run after Wave-2 COVID subsides — Nifty 15,315 → 15,800, India VIX collapses from ~20 to 14 (first sub-15 print of 2021), FII futures long pinned at 82–88% with shorts nearly absent (the batch's most-cited risk), Bank Nifty glaringly flat (expiry-to-expiry +500 Nifty vs −50 BN), PSU banks/SBI/RIL/IT leading.
- **Most notable verifiable events:** FY21 GDP −7.3% vs −8% expected (0391); SEBI 75%-of-peak-margin norm effective 1 Jun 2021 (0393); US May CPI 5.0% vs 4.7% expected with US markets closing green (0409); AMFI May-2021 flow rotation ₹44,500cr debt→equity (0407); DHFL delisting-to-zero with upper-circuit buying (0405); IndusInd −7% on a year-old Hinduja Cayman news item (0396); three FPI demat accounts frozen holding ~₹45,000cr Adani stocks (0416); G7 15% global minimum tax (0402); PM free-vaccine announcement (0404); US May payrolls 560k vs 650k (0398).
- **Standout transferable lessons for the book:** chameleon roll-with-the-market straddles (0382); absence-of-shorts makes corrections violent (0393); VIX measures speed not direction (0407); asymmetric binary-event risk (0410, with the Feb-2018 CPI case study and a ₹3cr personal loss anecdote — genericize per policy); simplicity beats complexity (0398, Kamal-Rajni analogy); management-statement timing as accumulation/distribution signal (0409); post-DDT death of the HNI dividend trade (0393/0416); delisting-bound shares always go to zero (0405).
- **Data quality:** docx-era transcripts are clean, punctuated, levels/crore figures explicit and consistent across pre→post pairs. Uncertainties flagged inline: "infra output 56%" (0391, likely garbled core-sector figure), Maruti/M&M/Muthoot single-day % moves, Adani Power percentages, Sun TV/IndusInd strike narratives, and the Buffett-LEAPS framing (verify nuance). One near-duplicate thread: US-CPI caution repeated across 0404/0406/0408 (marked in dup_flag).

## Leak log (batch-level, for banned-terms enforcement)

- **Name:** "PR Sundar / P R Sunder / P. R. Sundar" in every file; "Mr. Sundar" (0409, 0416).
- **Sponsors:** 5paisa.com ("sponsored by 5 paisa dot com / 5paisar.com / pi paisa dot com / 5pisar.com") in 0382, 0384, 0390, 0392, 0394, 0396, 0398, 0403, 0405, 0409, 0411.
- **Business identity:** "Manson Consultancy Private Limited" (0398 — company name + capital disclosure ₹10–15cr + "our workshop"); 5paisa franchisee onboarding promos (0382, 0403); India Infoline platform walkthrough (0411); BSE-sponsored webinar (0392).
- **Personal/lifestyle:** wife anecdotes (0384), "I asked one girl" (0416), party-at-home COVID framing (0384).
- **Status claims:** "I am not a SEBI registered research analyst" (0389, 0391, 0404, 0406, 0416).
- **Platform artifacts:** "my YouTube channel", "I am a verified YouTuber", Twitter polls, back-office screen-shares, "hope you enjoyed watching" outros — throughout.
- Public figures appearing as market facts (kept, policy-compliant): Sucheta Dalal (0416), Warren Buffett (0398), RBI/PM references.

## Compiler handoff notes

- Strong feed for: Part II (4, 5, 6, 7 — FII/DII flows, VIX regime collapse, OI reads, expiry anatomy), Part V (19, 21 — event-risk playbook, Feb-2018 case study), Part VI (23 — 2021 boom chapter), Part I (2, 3 — 0407 buffalo analogy, 0410 risk-reward discipline), Part III (9, 12 — margin-rule era), Part IV (13, 17 — straddle practice, hedge importance).
- Personal P&L passages (0398/0411) must be genericized to illustrative anecdotes per approved policy; company/broker names never enter the book.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 assigned transcripts read in full; 25 JSON lines written to book/analysis/batch_daily_005.jsonl in required schema; findings report written to the authoritative path book/analysis/outputs/daily_005_report.md; JSONL validated 25/25 lines parse and contain all required keys."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_005.jsonl",
    "book/analysis/outputs/daily_005_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json parse/validate of batch_daily_005.jsonl",
      "result": "passed",
      "summary": "25/25 lines valid JSON with required keys; 25 unique ids"
    }
  ],
  "validationOutput": [
    "valid lines: 25, bad: []",
    "ids: 25, unique: 25"
  ],
  "residualRisks": [
    "A few speaker-stated figures are internally uncertain (e.g. 'infra output 56%', single-day midcap % moves, Adani Power percentages) — flagged with verify flags for Phase 3 web verification",
    "Buffett-LEAPS claim needs source nuance check before quoting in the book"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch analysis JSONL (25 records) and batch report for daily_005 (27 May–14 Jun 2021 dailies)",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Docx-era transcripts are cleanly punctuated with explicit levels; pre/post same-day pairs are complementary (marked dup_flag where thematic repetition occurs). Leak log consolidated at batch level in the report."
}
```
