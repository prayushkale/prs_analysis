# weekly_108 Report — Dalal Street Week Ahead batch (20 transcripts, Jul–Dec 2025)

## Digest (5 lines)
1. 20/20 transcripts analyzed and written as valid JSONL to `book/analysis/batch_weekly_108.jsonl` (28.7KB, 20 lines, all parse clean); covers weekly previews 2025-07-11 → 2025-12-12.
2. Most notable verifiable events: Trump's 30% Brazil/EU tariffs (Jul 11), 50% India tariff effective Aug 27, GST rationalization announced in the Aug 15 Independence Day speech, Jackson Hole Powell pivot (Aug 22, Dow +~800, US VIX −14%), Trump's $100k H1B fee flip-flop (Sep 19–20), Oct-10 100% China-tariff tweet crash with the largest-ever crypto liquidation, Nifty breakout above the one-year high 25,650 (Oct), Bihar NDA sweep failing to lift markets (Nov 14), rupee at all-time low near ₹89, Q2 GDP 8.2% vs ~7.3% expected (Nov 28), RBI 25bp cut (Dec 5), Nasdaq −2% AI selloff after Broadcom results (Dec 12), quadruple witching Dec 19.
3. Recurring structural claims flagged for verification priority: FIIs 92% short in index futures (record), ₹70,000 crore July FII selling, ₹5 lakh crore since January, six-week red streak (third in 20 years), MTF book >₹1 lakh crore (from ₹60k), GST collections ₹1.96 lakh crore in October.
4. Data quality: good; consistent technical level narration (24,500 → 25,180 → 25,650/26,100 → 26,277) with rare ASR garbles ("benefit" for Bank Nifty in 2912 — claim marked with garble note and verify=true pending check; "Karekudi" likely Karaikudi).
5. Leak log captured per transcript (sponsors "sponsored by Delta.exchange/Delta.exe/Edelta.exe" variants, name variants "Pierre/Pia/PR/P.E.R./P.R. Kundar Sundar", workshop/travel/moneycontrol-event/MCX-BSE personal P&L disclosures, "90% of my investments are in Nifty BeES and Bank BeES") — none entered any content field; 4 transcripts carry near-identical "May-12 → six-month consolidation → October breakout" recaps flagged in `dup_flag` for compiler dedup.

## Acceptance notes
- Speaker's real name never appears outside `leaks` fields; ASR corrections applied in interpretation (GIFT Nifty, SEBI, FIIs/DIIs, Bank Nifty, VIX, ICICI/Axis).
- `levels` populated only with explicitly stated values; FII/DII figures in crore as stated.
- `events` limited to concrete claims; market-internal pattern claims marked `verify:false`.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 assigned transcripts read in full; exactly one JSON line per transcript written in order (ids 2757→2936) to /home/ubuntu/repos/prs_analysis/book/analysis/batch_weekly_108.jsonl; every line parses as valid JSON with the required schema (id/date/type/summary/levels/events/lessons/quote/dup_flag/leaks); findings report written to the authoritative output path."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_108.jsonl",
    "book/analysis/outputs/weekly_108_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c \"import json; [json.loads(l) for l in open('book/analysis/batch_weekly_108.jsonl')]\"",
      "result": "passed",
      "summary": "20/20 lines parse as valid JSON; type=='weekly' and non-empty id asserted for each"
    }
  ],
  "validationOutput": [
    "valid JSON lines: 20",
    "file size 28,748 bytes; 20 records matching the 20 assigned transcript ids in order"
  ],
  "residualRisks": [
    "Two metadata dates (2824 labeled 2025-09-17 vs in-text 'September 28'; 2789 labeled 2025-08-13 vs post-Independence-Day content) may be off by a few days — dates came from publish timestamps and are close enough for chronicle use.",
    "One ASR garble ('benefit' likely = Bank Nifty in 2912) preserved with a garble note in the event claim; verifier should confirm the ~48,000→60,000 index attribution.",
    "Event claims marked verify:false are market-internal patterns (OI, positioning, double tops) that cannot be web-verified and should be used only as dated illustrations."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_weekly_108.jsonl (20 structured records) and its findings report; no other files touched.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch is part of parent-run Phase 2 wave; parent should re-run its batch-coverage check (batch_index.json) to mark weekly_108 complete."
}
```
