# Batch daily_007 Report — 25 transcripts, 1–19 July 2021 (Nifty 15,500–16,000 consolidation era)

## Counts
- 25/25 transcripts processed (13 post-market, 11 pre-market, 1 pre-market tax-tip open + full coverage of the window 0451→0484)
- JSONL written: `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_007.jsonl` (25 valid JSON lines, schema-checked)
- Event claims queued for verification: 27 (17 high-value)
- Identity/promo leaks logged: every file (sponsor + name variants + platform artifacts)

## Most notable content for the book
1. **ATH breakout anatomy (15 Jul 2021, 0478)**: Nifty first closing record since Feb 2021 broke WITHOUT Infosys/Reliance — led by HDFC twins pre-results short covering + IT. "Market hits all-time high when people least expect it."
2. **The 9:20-straddle hunt (12–13 Jul 2021, 0472/0473)**: 150-pt flash fall with stop-losses blown 100+ pts past limits; crowded-strategy predation thesis ("if everybody knows, it is no more a secret") — strong Part II/IV material.
3. **FII positioning rule (0466/0471)**: FII index-futures long >80% historically preceded 300–400 pt corrections; July 2021 unwind 82%→54% documented.
4. **Fragile-setup checklist (0465/0466)**: FII cash selling + DII selling + crowded FII futures longs + low VIX = no cushion. Delta-variant UK >30k/day case study.
5. **Structures shown with real numbers**: ITM put calendar (sell Jul 16,000PE ~400 / buy Dec 16,000PE — both legs profitable, >10%), Infosys call ratio spread (1,540 long vs 1,580/1,600 short, near-zero cost), HDFC Bank results straddle, 3,250 TCS straddle + IV-crush payoff.
6. **VIX discipline (0480/0483)**: India VIX 11.7 multi-year low → near-strike selling tail risk, validated by the 19 Jul gap-down.
7. **Verification flags**: 2018 "Dow -10% in one day" (0476 — likely wrong, correction candidate); freak 900-pt Nifty futures trade >100cr (0459); Kotak MSCI 1,400→2,000 run (0479); GST ₹92,000cr June 2021 (0462); Adani FPI frozen/unfrozen CDSL saga (0484).
8. **Tax nugget (0452)**: F&O turnover = profits + absolute losses — Part 28 material.

## Data quality
- Speaker's own numbers (flows, strikes, OI, VIX) internally consistent across the window; recurring themes: FII-vs-DII tug-of-war, 15,700–15,900 pendulum around 15,750 equilibrium, results-season trigger thesis.
- ASR noise moderate: Kotak ("Quattag/Quotac"), 5paisa ("5pcet/5paisar"), TaxBuddy ("taxbeddy"), "Adhani". Personal/named-individual content (Olympic shooter anecdote 0480) flagged for exclusion.
- dup_flag set on 4 files (recurring tug-of-war / operator-hunt continuation) — dedupe handled by compiler.
