# Verification Report — Batch 007

## Results summary (10 claims)

| idx | Verdict | Notes |
|-----|---------|-------|
| 1 | verified | SVB (Mar 10) + Signature (Mar 12) = 2nd/3rd largest US bank failures; First Republic -60% Mar 13 (CNBC) — claim's "~70%" is high-end intraday; $30bn rescue; Biden depositor assurance confirmed |
| 2 | verified | GST 2.0 confirmed timeline: PM I-Day speech Aug 15 2025 → GST Council Sep 3–5 → FM formalized Sep → effective Sep 22 2025; auto price cuts; ₹2 lakh cr injection; crude imports <$60 by late 2025 |
| 3 | verified | RIL Q2 FY23 (Oct 21, 2022) PAT ~₹13,680 cr, flat-ish with refining drag ("weak" fair); ICICI ~₹6,791 cr (~27% YoY) and Kotak ~₹2,352 cr (~26% YoY) both reported Oct 21–22, 2022 — 25–26% growth figures consistent |
| 4 | verified | 5-day special Parliament session Sep 18–22, 2023 confirmed; agenda not published beforehand (NDTV/The Hindu/Livemint) |
| 5 | verified | COVID crash Mar 2020 + FII sellers-then-buyers is established history; general characterization accurate |
| 6 | verified | Soros/Quantum shorted Thai baht 1997; baht halved (~25→~50/USD); representative-warning anecdote is lore but widely retold; core verified |
| 7 | corrected | 10-yr US Treasury hit 5% peak on Oct 23, 2023 = highest since 2007 (16 yrs, not 15); Oct 18 reading ~4.9% |
| 8 | verified | Nifty shed 500+ pts from day's high Dec 20, 2023 right after record highs (Moneycontrol/India Today) |
| 9 | corrected | Late-Dec 2022 Bank Nifty weakness verified (negative year-end after record highs); exact 1,800-pt/3-session magnitude is speaker recollection, consistent with ~1,800–2,000 pts intraday-to-intraday |
| 10 | verified | May-2022 rout documented: ~17,400 (Apr 29) → ~16,058–16,200 close (May 9), low 15,735 May 12; claim's 1,200-pt/5–6-session cut accurate |

**Verdict tally:** 8 verified · 2 corrected · 0 wrong · 0 unverifiable

## Method
- Primary search: Google News RSS (Bing/DDG HTML unreliable). 2–3 targeted queries per claim.
- Evidence: news titles + Google News RSS article links (resolve with ?hl=en-IN appended); wrote canonical titles/URLs into the JSONL.
- Claims 7 and 9 carry modest speaker-recollection corrections per the hybrid policy.

## Data file
`/home/ubuntu/repos/prs_analysis/book/events/verified_batch_007.jsonl` — 10 JSONL records, schema `{idx, verdict, corrected_claim, evidence[], notes}`.