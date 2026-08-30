# Batch daily_001 — Analysis Report (25 transcripts, ids 0205–0255)

## Scope
Daily post-market reports, 21 Dec 2020 – 11 Feb 2021, plus one same-day companion (0220). Period covers: the 21-Dec-2020 UK-COVID-strain crash and V-recovery, the December rally to 14,000, January's whipsaw (14,800 → 13,700, Bank Nifty −3,200), the 1-Feb-2021 Budget ("Nirmala candle 2.0") melt-up, and the Nifty-15,000 milestone with the 36,000-straddle consolidation arc.

## Deliverable
`book/analysis/batch_daily_001.jsonl` — 25 valid JSON lines (one per transcript, in listed order), schema: id, date, type, summary, levels{nifty, banknifty, vix, fii_cr, dii_cr}, events[]{claim, verify}, lessons[≤2], quote, dup_flag, leaks.

## Highlights captured for the book
- **Crash anatomy (0205–0207, 0241–0242)**: UK strain crash → NSE glitch cascade (cancelled pending orders, margin-call liquidations) → V-recovery; "bull-market corrections are fast and furious" motif with 2003–07 statistics (700% with ten >10% corrections).
- **Mechanics teachables**: max pain + OI pinning (0226), volume-profile supports (0225/0226), VIX-as-fear-not-direction (0225, 0247, 0248), futures-premium exhaustion signal (0248), FII-F&O positioning over cash flows (0232), FII/DII "two rowdies / crossfire" consolidation model (0236, 0241, 0254), straddle-OI as consensus map (0248→0255 arc).
- **Results-season doctrine**: positioning (short covering/long unwinding) beats fundamentals on day one — motorbike-vs-apple expectation analogy (0221), Bajaj-vs-HDFC rotation contradiction (0235), BoB +25% on worst-ever loss (0235).
- **Event playbook material**: Georgia runoffs contra-consensus logic (0221), Budget 2021 expectations dynamic (0242→0247), Fed-night sulk ("crying child", 0241), Yellen candle (0233).
- **Risk parables**: slimming-shop advisory scam (0235), 9,000-short lady (−₹35 lakh), ₹50,000 HNI-tip victim (0252), no-predetermined-stop-loss restaurant analogy (0212).
- **Chronicle events flagged verify=true** (for Phase 3): UK strain + flight bans; $900bn US stimulus; Brexit deal; 5-Oct-2012 Emkay flash crash (~15%, 5,815→4,888); RBI curb on HDFC Bank digital launches; Georgia runoff results; Capitol riot; MSCI deletion of three Chinese telecoms; Hyundai–Apple reports; SC farm-law stay; Trump impeachment + Twitter ban; RBI FSR; HDFC Bank m-cap overtaking RIL (13-Jan-21); CPI 4.59% (Dec-20); JPM/Citi/WFC results-falls; Yellen relief call; Netflix beat; Biden inauguration; Serum Institute fire; BoB ₹3,400 cr loss episode; Budget-2021 measures (PSB privatization, LIC IPO); GameStop collapse; BSE m-cap ₹200 lakh crore; SBI upper circuit; HCL $10bn bonus; NSE margin-funding circular; margin-penalty slabs; Aditya Puri ₹845 cr sale; Pangong Tso disengagement; 1982 Reliance squeeze/BSE 3-day closure.
- **Standalone history lesson (0214)**: 120-year Dow cycle framework (1902–22 flat; 1929 −90%; 1965–85 flat; 1985–2000 15×) — strong Part I/VI chapter spine.

## Data quality & anomalies
1. **0220 date conflict**: metadata date `2021-01-07` (interpolated) vs title "Post Market Report 28-Dec-2x". Content references the Georgia runoffs as imminent → actual recording ≈ 4–5 Jan 2021. JSONL uses `2020-12-28` (title) with the inconsistency noted in dup_flag. Recommend metadata fix to `2021-01-04~05` approx.
2. **Metadata interpolation generally worked** but two titles carry their own dates (0220 handled; no others in this batch).
3. **Speaker factual slips to verify/correct**: "BJP won in 2009, Nifty below 12,000" (0226 — means 2019; BoB ~₹140 figure needs checking against 2020 low); "2004 Nifty fell 30%" (0221 — actual ~13–15% intraday with circuit breaks); Bank of Baroda loss quarter/year (0235 — likely Q3FY18, Feb 2018); GME fall "40% then 50%" (0247 — approximate); flash crash dated "2011" in 0253 (actually 2012); SBI upper-circuit date ambiguous between 4–5 Feb 2021 (0248 vs 0249).
4. **ASR corrections applied throughout**: DIIs/FAAs→DII/FII, "weeks"→VIX, "Toji"→Doji, "SBA"→SBI, "Quotac/Kotech"→Kotak, "Hiro Motocop"→Hero MotoCorp, "Indelco, Ishermota"→IndusInd Bank, Eicher Motors, "shot covering"→short covering, "Singapore Nifty"→SGX Nifty.
5. **Leaks logged** per transcript: name variants (P.R. Sundar / PR Sunder / "we are Sundar"), channel/CTA boilerplate, blog/Twitter references, workshop/course promos (0236 almost entirely promotional — only its first third carries market content), website URL, co-host name ("Ashwin"), personal positions/P&L disclosures (0253/0255 account screenshots, family-member account), production artifacts ("both our cameramen were off").
6. **Repetition map for compiler**: 0206 ⊂ 0207 arc; 0220/0212 same-day pair; volume-profile lesson 0225→0226; straddle-OI arc 0248→0249→0253→0254→0255 (keep 0248, 0253 as canonical, others as confirmations); 2012 flash crash told in full twice (0206, 0253 — keep one).

## Verification-queue count
57 event claims total: 31 verify=true (concrete, independently checkable), 26 verify=false (observational/market-state/positioning claims or approximations).
