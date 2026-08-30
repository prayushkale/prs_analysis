# Batch weekly_109 Report — Dalal Street Week Ahead, Dec 2025 – May 2026 (20 transcripts)

## Counts
- Transcripts read in full: 20/20 (ids 2946–3138, weekly preview series)
- JSONL records written: 20 (all valid single-line JSON, schema-compliant, verified by parser)
- Output: `book/analysis/batch_weekly_109.jsonl`

## Notable events extracted (for verification queue)
1. **Infosys ADR whipsaw (Dec 2025)**: ~38–56% intraday spike on NYSE with repeated halts, settled ~+5.5% on no news; algorithmic GIFT-Nifty hedging amplified Indian markets.
2. **India VIX record low (~9.5, Dec 2025)** → single-digit VIX; speaker closed long-term option positions (~₹25–30 lakh profit).
3. **2025 record FII selling ~₹3.06 lakh crore** reframed as partly IPO-listing-gain rotation against record ₹2 lakh crore IPO fundraising.
4. **US enters Venezuela, arrests president (Jan 2026)** — minimal market reaction.
5. **Jan 2026 FII selling >₹40,000 crore** (highest monthly since Jul–Aug 2025); PCR 0.49 extreme.
6. **US Supreme Court rules Trump tariffs illegal (Feb 2026)**; Trump invokes another provision → 10%→15% across-the-board (15% = statutory cap); India shifts from 50% discriminatory to uniform 15%.
7. **Indo-US trade deal (Feb 2026)**: GIFT Nifty +2,000 indicated, settled ~+1,000; doubts on Russian-crude commitment and zero-tariff agri; formal agreement due mid-March.
8. **Iran–US/Israel war (begins late Feb–Mar 2026)**: Iranian leader killed; Dubai (Burj Khalifa, airport) hit; Kharg Island (90% of Iran's crude exports) attacked by US; Hormuz closed — 80% of India's oil transit at risk; Brent $95→$126→$115.
9. **Nifty path 2026**: 26,000 consolidation → Jan slide to 22,200 (Mar low) → +10% April rebound → IT earnings drag (HCL −10%, Infosys −12%/3d) → MSCI weight cut 20%→12% passive selling → pinned below 24,000 after FM's "willing to listen" remark.
10. **FII cumulative selling since Jan 2024: ₹7–7.5+ lakh crore (rising to ~₹8 lakh crore)**; monthly record ~₹1.11 lakh crore (Mar 2026), beating Oct-2024's ~₹91–92k crore.
11. **RBI actions**: bank forex exposure cap ($100M by Apr 10); broker/prop-funding restrictions; excise duty cut ₹10 on petrol/diesel.
12. **India VIX golden rule**: >30 → exit everything; both 25-year instances reversed only after 85+ with Nifty lower circuits.
13. **Structural**: India's EM index weight 20%→12% forcing passive selling; semiconductor-led global rally excludes India; dabba-trading warning (10× illegal volume); NSE's ₹80 crore payout halt (broker fraud).

## Recurring lessons (strategy-relevant)
- Zero-downside HNI structures: index ETF + long-dated put funded by far call (2989, 3056).
- Fibonacci retracement ladder as panic map: 50% (24,300) → 61.8% (24,800) → 100% (21,700).
- Straddle-premium arithmetic as implied range; put discounts/close asymmetry as conviction reads.
- Broken supports become resistances; "hope is the worst enemy."
- Post-huge-candle consolidation ±2–3% for months (May-12-2025 ceasefire template).

## Data quality
- High: dates, index levels, FII flows, VIX, premiums consistently stated.
- Garbles corrected via dictionary (FAA→FII, weeks→VIX, ICSA/ICC→ICICI, MSA→MSCI, Garg Island→Kharg Island, "straight of armus/farmers"→Strait of Hormuz, RBS→RBI, "debit reading"→dabba trading, "Larsen and Dubro"→L&T, "Emphasis"→Infosys).
- Ambiguous figures flagged: "ITC fell more than 50%... almost 20%" (2968 — likely 5%→20% cumulative); "Larsen... falling 700 percent" (3066 — clearly 7%); Bank Nifty "78 percent" fall (3056 — actually ~3.5%); FII "1.11 crore" (3083 — clearly ₹1.11 lakh crore). Marked in summaries conservatively.

## Identity/promo leaks logged (verbatim, for scrub list)
- "sponsored by Delta.exchange / Delta Data Exchange / Intel Data Exchange / Delta Tech Change" (every file)
- Workshop promos: Chennai/Mumbai (2946–2977), Bangalore end-May + early-bird (3098, 3118, 3138), charity dinner Mar 21 + sponsor solicitation (3024), "contact our office... numbers in description" (all)
- Residence/travel: "I am in Dubai... explosions near my apartment" (3047, 3056), "in Toronto, Canada" (3098), "Mission, Abbotsford, Toronto, London" (3110), "NRI in Singapore" bond anecdote (3083)
- Personal: own P&L disclosure ₹8L profit/₹13L charges (3092), new camera purchase (3092), Tamil-channel interview (3118), follower-message anecdote (3036), Tamil proverb references (3092)
- Platform: "audio podcast" framing (multiple), "yesterday's video" (3118)

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 20 assigned transcripts read in full; 20 schema-compliant JSON lines written to book/analysis/batch_weekly_109.jsonl (validated by parser); report written to book/analysis/outputs/weekly_109_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_weekly_109.jsonl",
    "book/analysis/outputs/weekly_109_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json-validate batch_weekly_109.jsonl",
      "result": "passed",
      "summary": "20 valid JSON records, required keys present, ids in expected order 2946..3138"
    }
  ],
  "validationOutput": [
    "valid JSONL records: 20",
    "ids: ['2946','2957','2964','2968','2977','2989','3013','3024','3036','3047','3056','3066','3077','3083','3092','3098','3102','3110','3118','3138']"
  ],
  "residualRisks": [
    "A few garbled figures (ITC fall magnitude, L&T '700 percent', Bank Nifty '78 percent', FII '1.11 crore') were interpreted conservatively and need web verification before book use"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added 20-record structured analysis JSONL + batch digest report for weekly previews Dec-2025 to May-2026",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "This batch covers the 2026 Iran-war arc and the 2026 FII/MSCI structural story - high-value chronicle material. Speaker name variants and sponsor strings logged in leaks fields per anonymization contract."
}
