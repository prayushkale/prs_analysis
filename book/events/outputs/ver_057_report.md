# Verification Report — batch 057 (10 claims)

## Summary
- **verified: 6** (claims 4, 5, 7, 8, 9, 10)
- **corrected: 4** (claims 1, 2, 3, 6)
- **wrong: 0** | **unverifiable: 0**

Primary sources: Yahoo Finance daily OHLC (market-move claims), CNBC/Reuters/BBC/NDTV/TOI/Moneycontrol headlines via Google News, CME FedWatch.

## Per-claim findings

1. **FII budget-day flows (Feb 2024) — CORRECTED.** Jan-2024 FPI outflow was ~₹25,000 cr (NDTV, 2 Feb 2024: "highest in one year"), not ~₹40,000 cr. Budget-day daily ~₹2,000 cr figures not independently confirmable.
2. **SBI Q2 (Nov 2022) — CORRECTED (minor).** SBI's 5-Nov-2022 results verified: highest-ever quarterly profit ~₹13,265 cr, +74% YoY. But PSUBNKBEES was +22.2% YoY (31.26 → 38.19), not ~30% (Nifty PSU Bank index did gain ~33% in CY2022).
3. **Fed hike + Dow (16 Mar 2022) — CORRECTED.** 25bp hike verified (first since 2018). But Dow closed UP ~518 pts (+1.55%, close 34,063); intraday low was only ~260 below open — the "fell 600 then recovered 600" narrative is contradicted by CNBC ('jumps 500 points in relief rally') and OHLC data.
4. **Fed odds / 10-yr yield (early Apr 2024) — VERIFIED.** CNBC 2 Apr 2024: 10-yr hit highest since November as June-cut bets cooled; ~58% June-cut probability and ~4.4% yield are supported.
5. **Bank Nifty ATH ~53,180 (Jun–Jul 2024) — VERIFIED.** ATH 53,180.8 on 27 Jun; new high 53,256.7 on 3 Jul; correction ~1,000 pts then single-session recovery ~900 pts (2 Jul close 52,168 → 3 Jul close 53,089 = +921).
6. **Nvidia/semis (Sep 2024) — CORRECTED.** Nvidia -9.5% (3 Sep) then -1.7% (4 Sep) = -11.1% two-day (record $279bn cap loss, Reuters) — ">10%" ✓. But SOX fell 7.75% on 3 Sep, not ~4%.
7. **200-DMAs (Jul 2022) — VERIFIED.** Bank Nifty 200-DMA 36,426 (~36,400; closed above at 36,739); Nifty 200-DMA 17,056 (~17,000). Computed directly from daily closes.
8. **Amazon/Apple (Aug 2023) — VERIFIED.** AMZN +8.3% close (intraday +11.4%) on strong Q2; AAPL fell ~2–3% after hours on third straight quarterly revenue decline, -4.8% next close.
9. **Reliance +6% (20 May 2022) — VERIFIED.** RELIANCE close +5.8% (intraday +6.6%), Nifty +456.8 pts; ~10.5% weight implies ~100–110 index-pt contribution, consistent with ~120.
10. **Nasdaq -2.5% (3 Jun 2022) — VERIFIED.** -2.47% (-304 pts) after stronger-than-expected May jobs report (+390k). "~350 points" is slightly high; percentage exact.

## Residual risks
- Claims 1, 2, 4 depend partly on aggregate monthly figures; exact daily FII numbers (claim 1) and exact FedWatch % (claim 4) come from summaries, not raw dumps.
- Yahoo Finance is the sole source for intraday high/low/close; a second exchange dataset would reduce remaining risk.
- Claim 2's "~30% in a year" is the speaker's loose phrasing vs +22% ETF data — kept as "corrected" rather than "wrong" because CY2022 PSU index (+33%) supports the order of magnitude.

## Outputs written
- `/home/ubuntu/repos/prs_analysis/book/events/verified_batch_057.jsonl` (10 JSONL lines)
- `/home/ubuntu/repos/prs_analysis/book/events/outputs/ver_057_report.md` (this file)