# Batch daily_067 Report — 25 transcripts (Sep–Oct 2024 daily reports)

## Counts
- Transcripts processed: 25/25, all read in full
- JSONL records written: 25 (schema-validated, 0 bad lines)
- Types: 11 pre_market, 13 post_market, 1 duplicate-flagged

## Notable events captured (for verification queue)
1. **Union Budget 23-Jul-2024**: STT hiked on futures & options; LTCG 10%→12.5%; STCG 15%→20%; "worst budget in 20-25 years" reaction; VIX crashed >10% on the day, ~25% in two sessions; Nifty -400/-450 intraday then recovered; ITC +50 pts on unchanged tobacco tax; Bank Nifty -600 intraday during speech.
2. **Axis Bank Q1 miss** (25-Jul): close to -7%, dragged Bank Nifty ~250-pt gap down that fully recovered; Tata Motors upgraded by a foreign institution.
3. **Nifty ATH runs**: 26-Jul-2024 ATH close (five lower closes wiped in one day; Nasdaq -8-10% that same week); 26,000 first touched 24-Sep and first closed above 25-Sep; Hyundai ~$3B IPO announced as largest-ever.
4. **Sep 30 SEBI board meeting**: rumors (40-lakh ITR bar, one-contract index-option limit, 5% expiry-day margin) → one of 2024's worst sessions (Nifty ~-400, Bank Nifty ~-1,000; FII -9,791 cr / DII +6,650 cr); board announced no immediate F&O measures; measures formally announced Oct 1 (expiry-day ELM, contract-size increases).
5. **Iran missile attack on Israel** (1-Oct): crude +5-10%, GIFT -300 signal (ADRs contradicted it), retaliation fear premium; GIFT Nifty no longer trades during Indian holidays.
6. **Oct 3 crash**: all indices -2%+, one-way selling; FII -15,000 cr single day (possibly record), -30,000 cr in 3 sessions, -50,000 cr in the week, -55,000+ cr in 7 sessions; 25,500PE 7-8→250; Nifty/Bank Nifty technically flipped bearish (trigger ~25,620, speaker self-corrected a 25,275 misquote).
7. **Election surprise 8-Oct**: BJP won Haryana against exit polls; J&K hung; Nifty +300 off the low, all sectors green except IT (recovered); CLSA China upgrade/India cut; China reopened post-Golden Week; RBI policy Oct 9.
8. **Flow anomalies**: FII selling >1 lakh cr in 2024 YTD against a rising index; IPO-allotment offloading hypothesis for FII "selling"; MSCI ~$5bn inflow expectation (HDFC weight) swamped by the outflow regime; DII absorption (SIP money) as the structural floor.
9. **Microstructure color**: algo stop-hunt spikes (Bank Nifty ±200-250 in a minute on 24-Sep; 11 straight falling 15-min candles 4-Oct); futures-premium divergence as rumor skepticism gauge (450-pt Bank Nifty premium); put 4-5→15 rupees on a 50-pt move; 26,000 straddle ~800 pts for Oct; VIX below 12 during the melt-up; Japan Nikkei -5% (Sep 30, leadership change); China +7-10% stimulus rally.

## Data quality
- ASR garble heavy in this stretch (e.g., "production"=put option, "collection"=call option, "Access Bank"=Axis Bank, "Bankax"=Bank Nifty, "week(s)"=VIX, "MSA"=MSCI, "Kundai"=Hyundai, "Jambu and Kathmandu"=Jammu & Kashmir, "semi-meeting"=SEBI meeting, "lemon-proteur"=Lehman). All normalized in summaries; numbers preserved as stated.
- Two file/date mismatches flagged: 2365b (titled 26-Jul, content = 25-Sep post) and 2366a (titled 25-Sep, content = exact duplicate of the 26-Jul post 2363a). Content-derived dating noted in `dup_flag`/summary.
- 2 transcripts are audio-only variants with heavy garble (2363a/2366a) — content still fully extractable.
- levels: only explicitly stated values captured; FII/DII crore figures captured on 15 records.

## Leaks logged (for banned-terms enforcement)
Every record carries `leaks`: name variants (Pia/Pierre/Piers/P. A./P. S./PR Sunder/PBR Thunder/Pierre Sombre/Px), "sponsored by Delta.exchange" + garbles, interviews (New7 Tamil, Behindwood, Sun News), travel/residency (Sri Lanka, Dubai), family ("my son's company account"), P&L-report video promises, red-shirt video artifact, standard outro lines.

## Residual risks
- Some numeric claims are speaker-asrerted single-source (flagged verify:false): algo spike sizes, OI distributions, daily FII/DII splits, exact premium paths.
- 2363a content-date confidence is high (Aug-series OI + Nasdaq -8% week fits 26-Jul) but should be confirmed in verification phase.
- ASR "6.7%"→"67%" (HDFC fall, 2381) interpreted conservatively and noted.
