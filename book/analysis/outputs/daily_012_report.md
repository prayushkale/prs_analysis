# Batch daily_012 — Analysis Report

**Transcripts:** 25 (0611–0618, 0622–0629, 0633–0641) · **Window:** 4 Oct 2021 – 22 Oct 2021 · **Type:** daily pre/post market reports
**Output:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_012.jsonl` (25/25 valid JSON lines, source order, 83 event claims, 66 lessons, 70 leak strings)

## Digest

1. **Coverage:** 25/25 transcripts analyzed; 15 pre-market, 10 post-market (one session, 20 Oct, missing its pre-market in this batch; 0633/0634 span a travel day from Coonoor, 0637 recorded from Coimbatore airport).
2. **Most notable events:** Nifty's first-ever 18,000 close (11–13 Oct) then 18,500+ (18–19 Oct); TCS Q2 miss vs Infosys beat; TPG's $1bn into Tata EV unit (Tata Motors ADR +13%); hot US CPI 5.4% vs 5.3%; Brent >$81 (7-yr high); Facebook ~6-hour outage; 7-straight-day rally; mid-month momentum crash (Tata Power +16%→−13%, IRCTC −15% + F&O ban); Bank Nifty +500 vs Nifty −90 divergence day (21 Oct, Kotak +7%); Intel −8% after-hours; FII/DII flow whipsaws recorded on 8 of 25 days.
3. **Dominant threads:** (a) "good local cues vs bad global cues" regime; (b) sectoral rotation IT→banks/autos explained via the 7-heavyweight 50–60% index-weight framing; (c) retail as the marginal buyer (SIP/demat/IPO 20-yr highs, "first time I see retail conviction exceed institutions"); (d) result-season mechanics — pre-result run-ups, post-result falls, positioning-vs-fundamentals; (e) max-OI migration as a support ladder (17,000→18,300); (f) premium behavior tell-tales (futures premium spike = bearish, put-collapse/call-flat on VIX drops, dip-buying call buyers).
4. **Highest-value lessons:** "operation successful, patient died" (right view, wrong instrument); "futures no future, options plenty of options" (leverage math on 10–15% margins); third-day-low-of-correction rule; "when making money feels easy, the correction comes"; gap taxonomy (flat opens produce rallies); straddle-implied consolidation ranges (18,200–18,800).
5. **Data quality:** high — dates and session context unambiguous; levels mostly explicit (18,000/18,200/18,500 legs verified in-text); FII/DII crore figures stated on 8 days; two claims marked uncertain (Wipro ADR −7% phrasing in 0628; "PCS result −6%" in 0623 — latter dropped from events as unidentifiable). ASR corrections applied per dictionary (Quotac→Kotak, Wix→VIX, bees→ETF, global queues→cues, FAs/FAs→FIIs/DIIs).

## Notes for compiler
- 0617 and 0629 are heavily personal (S-Class booking story; travel/positions/3-lakh profit) — content usable only after stripping per banned-terms list; 0617's "stock market as business" message is the salvageable core.
- 0627 title "Tata Bye Bye to the last bear" and char-dinner/workshop promos recur in nearly every file — standard scrub.
- Strong Part II (option chain, flows) and Part V (result-season playbook) feedstock; chronicle entries for 2021 bull-run chapter (Part VI).

## Residual risks
- "PCS result" (0623) unidentifiable → excluded from events.
- 0628's Wipro ADR "fell more than 7%" is ambiguous (fell vs was shorted); marked verify=true for web check.
- 0616's Bitcoin "+78%" weekly move likely garbled (~+30-40% actual); captured in events with the $40k→$55k anchor for verification.
