# Batch daily_004 Analysis Report

**Batch:** daily_004 | **Transcripts:** 25/25 analyzed (ids 0343–0380) | **Window:** 7–26 May 2021 | **Output:** `book/analysis/batch_daily_004.jsonl` (25 valid JSONL lines, schema-checked)

## Digest
- **Counts:** 25 transcripts (13 pre-market, 12 post-market), covering the May-2021 second-wave recovery leg: corona cases falling 4 lakh→2 lakh/day, Nifty 14,200 → 15,315 (near ATH), India VIX ~20 → ~19 (2021 low), Bank Nifty underperforming then snapping +1,300/+2,000 on SBI results.
- **Most notable events:** US April-2021 NFP shock (266K vs ~1M expected); WHO declaring the Indian Covid variant a global health risk; US CPI 4.2% (13-year high) with the Feb-2018 "Dow -10% in a day" parallel; China crypto restrictions and BTC's $14K intraday range; SBI Q4 results flipping the bank tape; sustained gap-up through the two-month 15,050 ceiling; HDFC Bank RBI card-ban + Macquarie investor-meet drag; Nifty ATH-close figure corrected 15,245→15,315.
- **Strategy content:** live straddle ladder (15,000→15,100→15,200→15,300 rolls), 14,900PE stop-loss trap lesson, and a full hedged SBI credit structure (390/2×420/460 CE + 360/320 PE; net credit 1,200, margin ~1.06L, max P 44K, max L 58K, breakevens 360–450).
- **Recurring lessons:** FII-long% crowding asymmetry (<50% → squeeze fuel; 75–80% → profit-taking ceiling), lead-vs-lag/news-interpretation framing, chameleon position adjustment, block-deal distortion of FII/DII data, max-OI range validation, expiry-day late-hour noise.
- **Data quality:** high — this is the human-edited docx era; clean prose, dense verified numbers. One ASR garble each for 5paisa sponsor variants and "Tan Parma"/"PPCL"/"Indiabulls" (flagged uncertain in-place).

## Verification queue highlights (verify=true)
US NFP 266K (May 7, 2021); WHO B.1.617 designation; US CPI 4.2% (May 12); Feb-2018 Dow -10% one-day claim (likely overstated — flag); IOC GRM $12.5 (uncertain); Japan Q1 2021 GDP -5.1%; RBI HDFC Bank card ban; Macquarie HDFC meet; SBI Life ₹4,000cr block deal; GST ₹1.41L cr; India CPI 4.29%; IIP +22.4%; Nifty closes 15,175/15,245/15,315; Bank Nifty ±800 last-hour whipsaws; BTC 44K→30K→40K day.

## Leak log (for banned-terms list)
Recurring: "P. R. Sundar/Sunder/PR Tunder" variants; sponsors "5paisa / 5PISAR / 5pcet.com / 5PISAN / PhiPySat"; personal: house tour (2,000 sq ft apartment), "my son is the cameraman", wife screenshot, >2 crore profit in one account + 50 lakh donation, Sun TV expert-speaker role, Dr. Priya named viewer, 5paisa tie-up, BSE-sponsored webinar, workshop/seminar promos, Twitter/blog references, Tamil Nadu lockdown artifacts, "not SEBI registered analyst" disclaimers, fake-ID/fake-broker-call warnings (identity mechanics).

## Risks
- Feb-2018 "10% in one day" and IOC GRM $12.5 are speaker assertions likely overstated/garbled — already marked verify=true; suppress unless confirmed.
- Personal P&L and donation claims retained in JSON (genericizable content) but flagged in leaks for scrubbing at book stage.
