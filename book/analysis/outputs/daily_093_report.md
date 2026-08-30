# Batch daily_093 — Analysis Report

**Scope:** 25 daily pre/post-market transcripts (ids 3199–3224; Jul 14 – Aug 4, 2026; no id 3207 in batch).
**Output:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_093.jsonl` — 25 JSON lines, all schema-valid.

## Digest

- **Counts:** 25/25 transcripts read in full → 25 JSON records (13 post_market, 12 pre_market). 58 event claims captured (42 flagged verify:true), 41 lessons, 7 quotes.
- **Most notable events (era-defining):** Trump's 20% Strait-of-Hormuz "toll" and US–Iran escalation/recession of strikes (crude whipsaw $82→$93→$86, $100 crossed once); five-bank results weekend (HDFC Bank below estimate −5%, Axis −5%, ICICI beat); India CPI at 3.5% (largest monthly drop since 2020); IBM −22% (worst in 65 years) with Infosys ADR collateral; the global AI/semiconductor crash (Korea −40%, ~$2T wiped, SpaceX −50% from high) vs the money-rotation rally in Indian IT (Infosys ADR +15% in 3 days, TCS +20% off lows); FM ruling out LTCG rollback; July expiry closing +125 pts vs the 3% historical norm; four straight months pinned at 24,000±200 (first since 2015); 2026 tracking as the second-worst yearly candle since 1995; SEBI's new Closing Auction Session (3:15–3:30 pm) printing the Nifty ~200 points above the real close on day one, with an expiry-day 20x option-lottery exploit described on day two.
- **Data quality:** High — era is dense with levels (23,800/24,300/24,382/24,600/24,800), FII/DII figures (−4,500 cr worst day; +3,000/+4,000 cr on breakout days), VIX (13), PCR (1.15→1.5) and straddle-implied ranges (Aug 24,000 straddle ≈650 pts). Several ASR garbles corrected per dictionary (GIFT Nifty, FIIs/DIIs, Axis/ICICI/Kotak, Hindustan Unilever, crude oil, Diwali, TSMC/SK Hynix); two uncertain reconstructions flagged in-claim (Jio Financial Services ASR 'geofinance'; five-bank list on 3208). Speaker's own positions (1 lakh+ Dec 23,000 puts = >5% of strike OI; Dec book MTM) recorded but marked genericizable.
- **Leaks logged (all batches):** sponsor mentions on every file ("sponsored by Delta.exchange" + garbles), speaker name variants on every file (Pierre/Pia/P.A./P.F./Piers/P. Epsom), Seychelles sponsor-incentive trip + Chennai/Mumbai travel (3212–3214), Tamil-migration identity aside (3214), personal position/MTM disclosures (3199, 3202, 3208, 3209, 3221, 3222, 3223), social-media self-references, video-production artifacts, outro boilerplate.
- **dup_flag:** 3204, 3205, 3206, 3208, 3210, 3212, 3213, 3214, 3215, 3218, 3220, 3224 flagged as partial repeats of adjacent sessions (pre/post pairs and the persistent 23,800–24,300 range recap) — compiler can compress these heavily; 3199, 3200, 3202, 3211, 3216, 3217, 3219, 3221, 3222, 3223 carry primary content.

## Verification queue highlights (verify:true, for Phase 3)
Trump Hormuz 20% toll; India CPI 3.5% (largest drop since 2020); IBM −22%/65-year record; Korea −40%/$2T + SpaceX −50%; US strikes Iran (9 consecutive nights, 3 US soldiers in Jordan); Iran missiles at US targets; Iran strike on Kuwait desalination plant; five-bank results (HDFC below est.); FM: no LTCG rollback; 2026 second-worst yearly candle since 1995; TSMC +77% profit yet −4-5%; ICICI Lombard −10%; Infosys results good/weak guidance; $17bn FCNR inflow; HDFC ADR −10.5%; SEBI Closing Auction Session mechanics + day-one 200-point distortion; highest-ever monthly auto sales; crude $100 crossing; 20-month 24K consolidation; US 30Y yield 5.2% + Dow −1,000 after Fed hold.

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 batch transcripts read in full; 25 schema-valid JSONL records written to book/analysis/batch_daily_093.jsonl; 58 event claims + 41 lessons + 7 quotes + leak log extracted per batch spec; ASR corrections applied; uncertain reconstructions flagged; identity strings confined to leaks fields; no scope widening."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_093.jsonl",
    "book/analysis/outputs/daily_093_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json.loads validation over batch_daily_093.jsonl",
      "result": "passed",
      "summary": "25/25 lines parse; all ids/dates/types valid"
    }
  ],
  "validationOutput": [
    "valid lines: 25, bad: 0",
    "output file 44,372 bytes, one JSON record per transcript in manifest order (3199..3224, excluding nonexistent 3207)"
  ],
  "residualRisks": [
    "Two ASR-dependent reconstructions flagged in-claim: 'geofinance'->Jio Financial Services (3204) and the exact five-bank Saturday list (3208); both need confirmation or softening before book use.",
    "2026-era events are intrinsically hard to web-verify if sources are sparse; verify:true claims from this batch may need hedging if unconfirmed.",
    "Several numeric passages were garbled in source (e.g., Bitcoin '+100%', TCS 4,500->2,000 framing); garbled magnitudes were excluded from events rather than guessed."
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_daily_093.jsonl (25 structured transcript analyses) and this report; no other files touched.",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "This era (Jul-Aug 2026) contains the SEBI Closing Auction Session rollout and its day-one manipulation - high-value original material for Part VII (Predators & Protectors) and Part II (microstructure). The persistent 23,800-24,300 range recap means ~12 of these 25 files are compressible to one narrative beat each in the Chronicle.",
  "notes": ""
}
```
