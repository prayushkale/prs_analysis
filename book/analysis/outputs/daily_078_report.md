# daily_078 analysis report — 25 transcripts, July 2025 daily market reports

## Scope
Ids 2736–2766 (25 transcripts; 12 pre-market, 13 post-market), 30 Jun – 18 Jul 2025.

## Output
- `book/analysis/batch_daily_078.jsonl` — 25 valid JSON lines (one per transcript, in order), validated with `json.loads`.

## Counts
- 25/25 transcripts read in full and converted; 0 unreadable, 0 skipped.
- 68 event claims extracted (all tagged verify true/false), 6 marked not-verifiable (internal OI/strategy positioning).
- 30 transferable lessons; 22 quotes ≤30 words; 25 leak entries.

## Most notable events in this window (for the verification queue)
1. **SEBI bans Jane Street** (Jul 4) — recurring across 2746/2747/2750/2751; broker/infra stocks (Nuvama, Angel One, BSE, CDSL) -5-10%; claimed JS profits ~$1bn/$2.3bn and daily volumes ₹45-50k cr.
2. **Trump tariff escalation**: Jul 9 deadline passed with no India deal; 35% Canada, 30% EU/Mexico, 19% Indonesia, 500%-on-Russian-oil threat; new rates effective Aug 1.
3. **TCS Q1 FY26 miss** (Jul 10) → Nifty broke 25,200 (Jul 11); Infosys ADR -4%; IT index ~-20% from highs; HCL/Wipro/Axis followed weaker; HUL leadership change (Priya Nair) +4%.
4. **Macro**: India June CPI 2.1% (~5-yr low); US PPI soft, CPI in line, strong payrolls; record SIP inflows ~₹27,000 cr (June) vs FII MTD sales ~₹17,330 cr.
5. **Market structure quirks**: Bank Nifty futures premium collapsed ~150 pts in a day (Jul 16); Nifty defended 25,000 (Jul 14, max-OI strike); HDFC Bank bonus+special-dividend reports; SBI QIP ~₹811; NVIDIA ~$165→world's most valuable company; Trump-Powell firing report (Jul 16).

## Data quality
- ASR garbles handled per dictionary: Wix→VIX, FAs/FIAs→FIIs, DAAs→DIIs, ICSA→ICICI, Quotac→Kotak, blog deals→block deals, Lull Street→Dalal Street, Jane Strait/JN Street/Gen3→Jane Street, "industry and deliver"→Hindustan Unilever (context), "24,400/24,44"→25,400 context.
- Numbers in claims kept as stated; speaker exaggerations (e.g., "~50% GST on autos") tagged verify:true for web check rather than silently corrected.
- Personal trades (put calendar, 25,400 straddle, TCS cash-secured put, Bank-BeES collar) captured as content with verify:false.

## Leaks observed (all flagged in `leaks` fields)
- Name variants: "Pia Sundar", "Pierre Sundar", "Pierre Sondar", "PR Sundar", "Pia Sunda".
- Sponsor: "sponsored by Delta.exchange" (+ "Delta Data Exchange", "DeltaDat.exe", "Delta.dex sales") in all 25.
- Promos: workshops Bangalore (Jul 19-20) & Chennai, fee "50,000 plus GST", "contact our office", "check the description".
- Personal/platform: hacked YouTube channels (English+Tamil), son mentioned as computer engineer, "interview on Tamil channels", "according to some of my known sources".

## Residual risks
- Two numbers uncertain from ASR: "broke 24,400" (likely 25,400) and "power league" (festive-season term, left out of events). HDFC Bank "+30% rally" claim marked verify:false pending exact price history.
- Block-deal specifics (2742) kept at company level only.
