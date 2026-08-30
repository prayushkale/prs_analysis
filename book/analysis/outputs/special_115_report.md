# Batch special_115 — Analysis Report

**Scope:** 10 special-episode transcripts (ids 0075–0087, era May–Jun 2020) — full reads completed, structured JSONL written to `book/analysis/batch_special_115.jsonl` (10/10 records, JSON-validated).

## Per-transcript digest
- **0075 | SGX Nifty Explained** — contract sizing (USD 2× index), T/T+1 sessions in IST, moneycontrol vs investing.com data quirks, "+points is vs SGX's own close". Ch 7, 4. Quality 5.
- **0076 | Bharat Bond ETF** — 0.0005% expense, 2023/2030 maturities, ~6.8%/7.6% yields, 20% LTCG with indexation, 5% collateral haircut. Ch 30, 12, 29. Quality 4.
- **0077 | May-2020 P&L review** — 76 lakh/2mo on 95 lakh; 12 lakh in three losses dissected; cash-secured puts; ratio spread; SEBI June-2020 margin shift favors indices. Ch 3, 13, 18. Quality 3 (heavy self-proof framing → exclude_passages).
- **0078 | Reliance follow-up #1** — long futures + rolling straddle ladder: +1.6 lakh vs ~35-40k unhedged on ≤5 lakh margin; "trade to compound, then buy and hold". Ch 17, 18, 29. Quality 4.
- **0080 | New SEBI margin rules** — naked ~1.0-1.3 lakh vs hedged spreads 25-35k; cross-margined straddles ~1.05 lakh; straddle+wings 45-55k; ITM put calendar <30k. Core Ch 12. Quality 5.
- **0081 | Trading taxation** — STCG 15% / LTCG 10%>1L; F&O = business income with expense deduction; individual vs corporate (42% vs 22-25%, MAT ~18% limits set-off). Ch 28. Quality 4.
- **0082 | Liquid BeES vs Nifty BeES** — interest-as-units mechanism, price pinned ~1,000, zero STT/stamp duty; haircut irony 5% vs 10%. Ch 29, 12. Quality 4.
- **0084 | #AskPR 4** — short-selling ban myth (~500 cr cap), confirmation bias, weekly-hedge rollover friction, options-vs-futures MTM/collateral treatment, penalty slabs 0.5/1/5%, small-capital advice. Ch 3, 12, 6, 1. Quality 4.
- **0086 | June 8 market report** — euphoric gap faded; blog call (break 10,200) hit; weighted-average close explains "Doji"; Reliance ATH sold into; FII +813 cr / DII −1,238 cr. Ch 7, 4, 22. Quality 4.
- **0087 | Earnings schedules** — BSE/NSE/Moneycontrol calendars, expected result times, IV-crush positioning, dividend/bonus/split calendars (Colgate 1600%). Ch 19, 7. Quality 3.

## Highlights for the book
- **Best teaching material:** 0080 (margin economics of hedging — the clearest single explainer in the batch), 0075 (SGX reference-price confusion), 0086 (gap/Doji microstructure with weighted-close nuance).
- **Enhancement candidates:** margin comparison table (0080), tax decision table (0081), ETF comparison table (0076+0082), gap taxonomy (0086), IV-crush worked example (0087).
- **Verification queue:** 30 concrete event claims flagged (SEBI margin framework Jun-2020, corporate tax cut Sep-2019, LTCG 2018, MAT rate, Reliance ATH Jun-2020, June-8-2020 flows, Colgate dividend, IndusInd RBI nod, US COVID ATH Jun-2020, short-sale cap, penalty slabs, haircuts, Bharat Bond terms).
- **Leaks captured (all in JSONL `leaks` fields):** name variants on every intro; "my son's company account" (0077/0078); Jaguar car (0077); family company + tax-officer anecdote (0081); blog/Twitter/channel references; broker-endorsement framing (0084). Exclude-passages lists populated for 0077, 0078, 0081, 0084, 0086, 0087.
- **Data quality:** transcripts are human-edited docx-era text (clean punctuation); ASR errors rare here — "NSC"→NSE, "toji"→Doji, "Motocop"→MotoCorp, "shorted"→shot up contexts corrected.
