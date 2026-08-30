# batch_special_120 — Analysis Report (10 special episodes, Aug–Sep 2020)

## Digest (5 lines)
1. All 10 transcripts read in full; 10 clean JSON records written to `book/analysis/batch_special_120.jsonl` (0 malformed lines).
2. Content mix: 4 evergreen teaching episodes (pre-open auction, option-chain range method, confirmation bias, gambler's fallacy/recovery mindset — the batch's strongest material), 3 instrument/strategy explainers (BULLDEX, covered calls, OI misreads), 2 market-context pieces (moratorium SC case, crash-vs-correction), 1 monthly P&L review.
3. Chapter targets concentrate on 1 (Trader's Mind), 3 (Discipline), 5 (VIX), 6 (Option Chain), 7 (Microstructure), 12 (Margins), 13 (Straddles), 14 (Spreads/covered), 17 (Hedges), 27 (Regulation), 30 (Real assets).
4. Event claims: 14 concrete verifiable assertions captured (Monte Carlo 1913, Leeson/Barings Kobe 1995, Tesla −21% 8-Sep-2020, VIX 15→85 Mar-2020, 12,500CE OI 42k→19 lakh, BULLDEX launch 24-Aug-2020, RBI moratorium, Bank Nifty −2,000 week); 9 flagged verify:true.
5. Identity leaks logged for the scrub list: name variants ("P. R. Sunder", "PR Sunder"), family/business ("my son's company", "Weirwood Securities Private Limited", "Manson Consultancy Private Limited"), Singapore teaching biography, personal P&L/account walkthrough framing in 0148 (heaviest; exclude_passages populated).

## Notable content for the book
- **0153 (quality 5)**: "Recovery mindset" + gambler's fallacy with Monte-Carlo-1913 and Leeson/Barings parables — core Part I material; quote: "If you have lost it, that is the fees you paid to learn the lesson."
- **0141**: complete worked example of pre-open equilibrium-price discovery (cumulative demand/supply tables) — ready-made enhancement box for Chapter 7.
- **0146**: ATM-straddle monthly range method (11,650 ± 410 → 11,200–12,100, ~65% probability) — pairs with the VIX/sqrt(12) method for Chapter 6 enhancement.
- **0149**: classic OI-misread case study (far-OTM OI = margin-hedge buying, not informed flow) — Chapter 6.
- **0148**: genericizable lesson (direction-neutral income on a flat stock) despite heavy self-referential account framing — exclude passages capture the identity material.
- **0145**: portfolio-level stop-loss doctrine and margin-efficiency of futures-based covered calls — Chapters 1/3/12.
- **0144**: "markets don't listen to bureaucrats" — confirmation-bias anchor for Chapter 1.

## Data quality
- All dates present from metadata; no ASR correction dictionary entries needed beyond standard name/garble handling.
- 0148's account narration treated as exclude_passages + leaks; numbers retained only where they teach generic lessons.
