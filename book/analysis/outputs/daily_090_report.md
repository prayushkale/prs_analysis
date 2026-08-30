# daily_090 batch report — transcripts 3112–3141 (13 May – 2 Jun 2026, 25 dailies)

## Deliverable
- **Primary output:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_090.jsonl` — 25 valid JSON lines, one per transcript, in order (ids 3112, 3113, 3114, 3115, 3116, 3119, 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3131, 3132, 3133, 3134, 3135, 3136, 3137, 3139, 3140, 3141).
- All records validated as parseable JSON; ids unique and complete vs the batch manifest.

## Period narrative (feeds Part VI chronicle + Part II mechanics + Part V events)
This batch covers the tail of the **Iran crisis May-2026 series** — the most volatile stretch in the corpus so far:

1. **Setup (13–15 May):** PM "worst crisis in 10 years" statement → −400pt Mon, −400pt Tue; Sensex −2,500 in two sessions; five straight down days while US prints ATHs; gold import duty +9%; petrol/diesel +₹3 (15 May) vs feared ₹20–25.
2. **Escalation (18–19 May):** drone attacks on Saudi/UAE; Strait of Hormuz crisis (day ~78); Brent to $111–112; **India VIX crossed 20 and exceeded the US VIX — historic inversion**; Sensex/Bank Nifty ±1,000-point days; rupee record low >96.
3. **The anomaly cluster (19 May–1 Jun):** next-month futures premium collapsed to 70–75 pts (normal ~150) — never seen in 17 years, not even COVID/Lehman; calls pricing 4–5× equivalent puts; later explained by **anticipated MSCI rebalancing flows**. First-ever joint FII+DII buying >₹2,500 cr each (18 May) — then FII selling resumed.
4. **Policy arc (25–27 May):** 4th fuel hike (+₹3, cum ~₹8); RBI $5bn swap for 26 May; **FM says she is "open to discussions on taxation"** — market thumbs down; **Taiwan market cap overtakes India's**; HDFC Bank ₹45-cr compliance issue erases ₹24,000 cr of market cap; India VIX collapses >25% (20→<15).
5. **MSCI day (29 May) — wildest session:** Nifty crosses 24,000, then −500 from high in the last hour (−300 in ten minutes), future bizarrely holds a 225-pt premium; FII −20,000 cr NSE (−21,000 all-exchange) on ~₹2 lakh cr volume (HFT opportunism) vs ~$1bn rebalance need.
6. **Double bottom (2 Jun):** gap-down pierces May low (23,262) by 30–40 pts → +350 short-covering rally; **VIX falls 7% while Nifty is down 800 intraday — the bottoming tell**; RBI policy shifted to Friday (5 Jun), expected non-event.

## Reusable lessons extracted (30+; highlights)
- Markets cannot take uncertainty (₹3 hike vs feared ₹20 = rally).
- Markets never repeat reaction intensity to the same news (COVID wave1 −40% vs wave2 −10%; April-8 +4% caps deal rallies).
- A shrunken next-month futures premium = structural bearishness; premium expansion into expiry = conviction gap.
- Price new lows + VIX refusing to spike = smart money covering (most reliable bottoming tell in batch).
- Weight, not severity: ₹45 cr HDFC Bank issue → ₹24,000 cr market-cap loss → ~500 Bank Nifty points.
- "Know when to stay away": weekend binary (deal or war) → migrate to next-month series.
- Structural bear case: blue chips (HDFC 6y, HUL 5–6y, ITC 3y, TCS 5–6y) ≈ zero returns + rising STT/taxes; trader demand hierarchy = abolish STT first.
- India–US beta asymmetry: +1% vs their +2%; −4% vs their −2%.

## Key verification flags (→ Phase 3 queue)
High-priority verifiable claims: PM crisis statement & 2-day −800; drone attacks on Saudi/UAE; Hormuz crisis start ~Feb 28; Brent $111–112; petrol/diesel +₹3×4; gold duty +9%; RBI $5bn swap (26 May); FM taxation statement (25–26 May); Nvidia China restriction removal +4.5%; Nvidia results 20 May sell-the-news; SBI −25% from high; Taiwan market cap > India; HDFC Bank ₹45cr/₹24,000cr event; MSCI rebalance 29 May (−20,000/21,000 cr); rupee >96 record; Nasdaq 100 >30,000; S&P 7,500 ATH; Infosys −45%/TCS −50% from ATH; Korea +180% 1-yr / +100% YTD; HDFC 52-wk low 725; Adani SEC $18M settlement; RBI policy Friday 5-Jun shift; June 5-week/18-session series; Wipro out of Nifty 50 / BSE in; windfall tax on fuel exports; petroleum export-duty cut; US 30Y 5.2% vs India 7%.

## Data quality notes
- ASR handled per dictionary: GIF-50→GIFT Nifty, weeks/Wix→VIX, MSA→MSCI, FAs/FIA→FIIs, DAAs→DIIs, Kuru Dial→crude oil, "streets of arms"→Strait of Hormuz, Lull Street→Dalal Street, VEPRO→Wipro, "Edelta/indelta/Telta exchange"→Delta Exchange.
- Internal inconsistencies flagged in-record rather than silently corrected: SBI "10,250→~920, >25% fall" (low likely 9,200; −25% doesn't reconcile — needs verification); HDFC Bank "fallen more than 200 percent" (read as 2.00%); 3113 "spot has another 5,500 points to fill gap" (garble); 3120 Bank Nifty "ATH ~61,000... crossed 25,000" (garbled strike/index mix); 3125 Nvidia "$175 to $25" (likely $250); 3131 "26,400 to 2200" Fib base (likely 23,200 area); 3139 "23,300 and 24th" truncated range.
- Identity/promo leaks logged per record: name variants (Pia/Pierre/PR Sundar), Delta Exchange sponsorship in all 25, Bangalore workshop promos (recurring), Chennai/Bangalore, US/Canada travel & age 62 (3113), wife jokes (3126, 3134 STT-divorce joke), Tamil story (3125), "my BJP friends" (3113), family function (3137), personal positions/P&L (3123, 3127, 3133, 3140, 3141).
- dup_flag set where a pre-market largely repeats the prior post-market (standard pattern; heaviest on 3116, 3122, 3124, 3128).

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 assigned transcripts (3112-3141) read in full and extracted into /home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_090.jsonl with the required schema (id/date/type/summary/levels/events/lessons/quote/dup_flag/leaks); findings written to /home/ubuntu/repos/prs_analysis/book/analysis/outputs/daily_090_report.md; ASR corrections applied; identity strings confined to leaks fields; no scope widened beyond the daily_090 task."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_090.jsonl",
    "book/analysis/outputs/daily_090_report.md",
    "book/scripts/build_daily_090.py"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 book/scripts/build_daily_090.py",
      "result": "passed",
      "summary": "Generated 25 JSONL records"
    },
    {
      "command": "python3 -c json-parse validation of batch_daily_090.jsonl",
      "result": "passed",
      "summary": "25/25 lines parse; ids unique and complete in manifest order"
    }
  ],
  "validationOutput": [
    "records: 25; valid lines: 25; all unique: True",
    "ids match batch manifest exactly (3112..3141 incl. gaps 3117/3118/3129/3130/3138 as per batch list)"
  ],
  "residualRisks": [
    "Speaker-stated numbers with internal inconsistencies (SBI drawdown math, a few garbled figures) are flagged in-record and queued for Phase 3 web verification rather than silently corrected",
    "2026-era external events cannot be independently confirmed from training knowledge; all marked verify:true for the Phase 3 web-verification queue"
  ],
  "noStagedFiles": true,
  "diffSummary": "New analysis batch: 25 structured extractions of May-Jun 2026 daily market reports",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "Batch daily_090 complete. Era context: Iran-crisis May-2026 series, India VIX>US VIX inversion, MSCI-rebalance microstructure episode, FM taxation statement, Taiwan-cap-over-India milestone - all high-value chronicle and mechanics material with verification flags set."
}
```
