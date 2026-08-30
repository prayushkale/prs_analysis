# Batch daily_003 Analysis Report

## Scope
25 transcripts (ids 0300–0342), all post-market daily reports from 30 Mar – 6 May 2021 (India's second COVID wave), analyzed in full.

## Output
- **`book/analysis/batch_daily_003.jsonl`** — 25 JSON lines, validated (all parse; schema keys present; ids in manifest order).
- **84 event claims** extracted for the Phase 3 verification queue (61 flagged `verify:true`).

## Digest
- **Counts:** 25/25 transcripts analyzed; 0 failures.
- **Most notable verifiable events:** RBI's Apr-2021 G-SAP 1 lakh crore + May-5 package (G-SAP 35k crore, MSME restructuring, LTRO, COVID loans); record GST prints (1.24L cr → 1.41L cr); India's COVID daily records (2.75L → 4.2L); HDFC Bank RBI digital-ban + Q4 miss; ICICI/RIL KG-D6 results catalysts; US IP waiver; Yellen rate-remark walk-back; Alibaba $2.8bn fine; Sun TV F&O ban; PowerGrid InvIT ~5x; SEBI margin-rule regime change.
- **Recurring lesson motifs (Part I/II fodder):** knee-jerk vs second-shock asymmetry; "markets bottom before the economy"; crisis-buying ladder (20–25% debt→equity tranches); OI-analysis fails during panic hedging; VIX percentage asymmetry; FII-afternoon clock (1pm candles); futures-discount bottom marker; straddle premium = implied range; support = strike − premium; FII 75–85% long futures = sell zone.
- **Chronicle value (Part VI):** 30-Mar-21 rally, HDFC-banking-outage day (31-Mar), FY22 opener + GST record (1-Apr), three consecutive "Monday Mayhems" (5-Apr, 12-Apr, 19-Apr), 14,213 low defended (19-Apr), bottom cluster (20–28 Apr), Friday free-fall + FII dump (30-Apr), post-election week (3–6-May).
- **Data quality:** transcript text is human-edited (punctuated, clean) vs the raw-ASR .txt era; names garble as "PR Sunder/P. R. Sunder"; recurring garbles: "Bagnifty"→Bank Nifty, "ICSA bank"→ICICI Bank, "India Wix/Bix"→India VIX, "global queues"→global cues, "plot covering"→short covering, "Hero Motocop/Hiro Motokar"→Hero MotoCorp, "toji"→Doji.
- **Leak log highlights (for banned-terms/QA):** sponsor mentions (5paisa/5pixar.com); "workshop.prsunder.com" URL; "my Telegram channel", "my blog", Instagram/YouTube CTAs, 5-lakh-subscriber and sponsor-teaser announcements; personal broker-dispute claims (9-lakh charge — genericize); personal positions (Sun TV 480 lot, Bajaj Finance 5,000 avg, Dec/June 15,000 straddles — genericize as illustrative); Tamil-new-year and wife anecdotes; 0339's extended 10-per-lot broker-plan pitch is the largest promo block (flag `exclude_passages`-worthy at writing time).

## Notable judgment calls
- 0341/0342 (same-day pre/post) retained both with `dup_flag` cross-reference (setup vs outcome).
- 0322 bitcoin-crash and remdesivir black-market claims kept with `verify:true/false` split as appropriate.
- 0335's FII 78%-long positioning recorded as speaker snapshot (`verify:false` — not independently verifiable today).
- Speaker's bold dated call (0341: "Nifty will not even go to last year's high of 12,400") captured in the quote field for the correction log — outcome: Nifty hit ~18,600 by Dec 2021.
