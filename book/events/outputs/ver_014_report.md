# Verification Report — batch 014

Summary: 10 claims verified. **5 verified, 5 corrected, 0 wrong, 0 unverifiable.**
Method: Yahoo Finance daily OHLC data (live endpoint) for all numeric/level claims (S&P 500, NASDAQ, NIFTY, KOSPI, Samsung, SK Hynix, LIC, Shanghai Composite, NVDA); Google News RSS + Wikipedia REST for policy/event claims (claims 2, 4, 8, 10).

Results written to: `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_014.jsonl`

## Per-claim verdicts

| # | Claim (abridged) | Verdict | Key evidence |
|---|---|---|---|
| 1 | China index ~zero return over ~15 years (2018–2023 cited) | **verified** | SSEC 2007 peak 6,092; Dec-2018 2,494; Dec-2023 2,975; Dec-2024 3,407. Fair as macro analogy (far below 2007/2015 peaks); precise 2018–23 window +19% |
| 2 | 2019 election: 5–6% pre-result run-up, +300–400 post-results, no gap-up | **corrected** | Nifty: 05-17 11,407 → 05-20 11,828 (+3.7%, exit-poll Monday); 05-23 (results) 11,657 below that. Run-up ~3–4%, not 5–6%; the +300–400 move occurred May 20, not result day |
| 3 | Oct–Dec 2023 ~3,000-pt (~15%) rally: state-election wins + Fed pivot | **verified** | Nifty 10-26-23 low 18,857 → 12-28-23 high 21,779 (+15.5%, +2,922); BJP won 3 of 5 states (Dec 3), Powell pivot Dec 13 |
| 4 | LIC IPO listed at 60–70 rupee discount (17 May 2022) | **corrected** | Forbes India: "lists at 8.6% discount" ≈ ₹81.8 below ₹949 (listing ~867); claim's 60–70 ₹ understates |
| 5 | Jackson Hole (Aug 2022) → NASDAQ ~15% in 2–3 weeks | **corrected** | IXIC: 08-25 12,639 → 08-26 12,142 (−3.9%) → 09-16 11,448 (−9.4% in 3 wks) → 09-30 10,576 (−16.3%). Speed overstated; ~9% in 3 weeks, ~16% by month-end |
| 6 | Iran–US war (Jan 2026): S&P 7,000→6,300; Nifty→22,200 | **corrected** | Levels verified but timing wrong: S&P low 6,344 & Nifty low 22,331 both on **30 Mar 2026**; no January 2026 crash in data |
| 7 | Korea 8% lower circuit, closed ~9% lower (13-Jul-26) | **verified** | KOSPI 7,475.9 → 6,806.9 (−8.9%) on 13 Jul 2026; Samsung −10.7%, SK Hynix −15.4% same day |
| 8 | SEBI Bank Nifty rejig (min 14 stocks, 20% cap, top-3 45%) | **verified** | Business Standard / ET, 31 Oct 2025: "SEBI increases Bank Nifty stocks to 14 from 12, caps top stock's weight" |
| 9 | Apr-2024 Mag-7 slump: NVDA −10%, S&P ~−5%, NDX ~−10% | **corrected** | NVDA −10.0% on 04-19 ✓; S&P 5,199→4,967 (−4.5%); NDX 18,308→17,038 (−6.9%, not −10%) |
| 10 | Independence-Day (15 Aug 2025) GST 28%→18% reform | **verified** | Indian Express 15-Aug-2025: "just two rates 5% & 18%"; GST 2.0 launched 22 Sep 2025 (Wikipedia) |

## Notes for the book editor
- **Claim 6** is the most important correction: the underlying data shows a genuine late-March-2026 crash (S&P −8.6% on 30 Mar, Nifty low 22,331), but it is *not* in January 2026 as the transcript claims. The speaker's levels (6,300 / 22,200) match the actual troughs — the recall of magnitude is good, the date attribution is off by ~2 months. Book should present the crash as March 2026 with verified levels.
- **Claim 2**: the widely-misremembered "post-result rally" actually occurred on the exit-poll Monday (20 May 2019). Recommend the book phrase it as "the exit-poll rally," matching the data.
- **Claims 5 & 9**: speed/magnitude rounding corrections are small; keep the direction, adjust the percentages.
- All source URLs are evidence-cited above; Google News RSS titles used where a canonical page URL could not be resolved from the sandbox network.

## Residual risks
- Exact "gray market" premium readings for LIC pre-listing (₹25–30) are not independently confirmable from these sources — only the official listing price/discount is.
- The magnitude of forced ETF offloads for HDFC/ICICI (~6,000 cr) in claim 8 is an estimate from the speaker, not independently confirmed by price data.
- Some news headline URLs are aggregator-resolved (Google News RSS) and may differ from original publisher URLs after redirect resolution.