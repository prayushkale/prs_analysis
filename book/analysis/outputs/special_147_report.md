# Batch special_147 Report — 10 transcripts (2022-10-29 → 2022-12-10)

**Output:** `book/analysis/batch_special_147.jsonl` — 10 JSON lines, all schema-valid.
**Totals:** 33 event claims (verification queue), 6 strategy entries, 41 identity/promo leaks logged.

## Per-transcript digest

| id | date | subtype | chapter | quality | one-liner |
|----|------|---------|---------|---------|-----------|
| 1324 | 2022-10-29 | general | 29, 1 | 4 | Nikkei's "lost decade" — indices can stay down for decades; long-term risk awareness. Very short. |
| 1334 | 2022-11-05 | strategy | 31, 18, 13 | 3 | Paired BTC bearish+bullish combos, premium-funded (~$100 net); comfort band 16,000–27,000; adjustment by adding short puts. |
| 1335 | 2022-11-06 | general | 26, 27 | 4 | Fake MTM screenshots: paired-account trick, bribe-able verifiers, MTM≠P&L; proposes broker **read-only logins**; lifestyle + MCA filings as real proof. |
| 1343 | 2022-11-12 | outlook | 23, 19, 29 | 5 | Bull case: wall of worry, markets lead 6–12 mo, capital goods as lead indicator (coffee-machine analogy), no-repeat-doubling logic (QT vs QE); targets 18.5–19K / 20.5–21K. |
| 1344 | 2022-11-12 | outlook | 23 | 2 | 2-min clarification of 1343 (35K was clickbait; Moneycontrol headlined 21K). |
| 1355 | 2022-11-19 | investing | 29, 26 | 4 | PSU banks +20%/+32% vs Nifty +1.2%; P/B <1 vs private 3.5–4x; IBC/PCA re-rating; ETF-over-MF, SIP-on-dips; 5–10% sizing rule. |
| 1367 | 2022-11-26 | crypto | 31, 13 | 4 | FTX crash context; BTC short strangle 10,000PE/25,000CE ~$620 credit; order-book tactics; per-exchange 10% cap. |
| 1380 | 2022-12-03 | investing | 30, 12, 29 | 5 | Bharat Bond 7.5% YTM 2033: FD-vs-bond tax math (indexation), SLR framework, AAA PSUs, **pledge-as-collateral** trick, three-story FD bond parable. |
| 1381 | 2022-12-03 | general | 26 | 2 | Apology/trolling self-defense — mostly exclude; salvage only MTM-vs-booked divergence example (dup of 1335). |
| 1392 | 2022-12-10 | strategy | 14, 18, 23 | 4 | Long-dated combo (long 16,000CE Dec-23, short 2×20,000CE + 3×13,000PE, net 150); VIX 20→12 tailwind; roll 13,000PE→15,000PE; Buffett LEAPS; Nov–Feb window. |

## Key lessons surfaced (for chapters)
- **Ch 26/27 (scams/regulation):** the strongest content of the batch — MTM-verification critique (1335), paired-account fraud mechanics, read-only broker login proposal, MTM-vs-realized-P&L divergence (1381 example: −50L MTM vs +4.1cr booked).
- **Ch 30 (bonds):** 1380 is a complete bond-investing chapter seed — tax arbitrage, rate/price mechanics via parable, pledging collateral trick.
- **Ch 23 chronicle (late 2022):** 1343/1344/1392 anchor the Nov–Dec 2022 bull call, VIX collapse 20→12, Moneycontrol targets, US midterm dip.
- **Ch 31 (crypto):** 1367/1334 — FTX aftermath, wide short strangle, paired combos, exchange-risk caps.

## Verification flags (33 claims, highlights)
- Nikkei ~40,000 (1989) vs ~20,000+ today — verify.
- 2008/2020 crash-and-double stats; 2022 sub-20% drawdown — verify.
- PSU bank index +20%/+32%, Canara Bank +88% profit, P/B table (BoB 0.93 vs HDFC 3.6) — verify.
- FTX bankruptcy Nov-2022; BTC 70K→15-16K — verify.
- Bharat Bond FFO Dec-2-8 2022 @7.5% YTM 2033; FD slab tax vs 20% LTCG w/ indexation — verify.
- India VIX 20–21 → 12–13 (Sep→Dec 2022) — verify.
- Moneycontrol targets (18.5–19K Dec-22, 20.5–21K Dec-23) — verify + outcome check.

## Anonymization notes
- 41 leaks logged. Heaviest: **1381** (real name ×6, MCA filings, P&L disclosures, trolls, conference sponsors — recommend heavy exclusion, quality 2) and **1335** (turnover/profit claims, properties, S-Class, Dubai house, follower count).
- **1344/1381** are low-value (dup/clarification, self-defense) — candidates to skip at writing time.
- Personal P&L (portfolio ₹10.6cr in 1380, conference demo profits in 1392) flagged for genericization.

## Residual risks
- 1334's strategy numbers are approximations from memory ("let us say"); marked verify:false where unfalsifiable.
- 1344 duplicates 1343 — compiler should merge.
- ASR errors ("Wald"→Vauld, "Motocop"→MotoCorp, "Quattac"→Kotak) corrected in records.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "batch_special_147.jsonl written with exactly 10 schema-valid JSON records (one per transcript, ids 1324-1392 in order); 33 event claims, 6 strategies, 41 leaks logged; report written to book/analysis/outputs/special_147_report.md"
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_147.jsonl",
    "book/analysis/outputs/special_147_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json validation of batch_special_147.jsonl",
      "result": "passed",
      "summary": "10 lines, 10 parsed, all ids present and ordered"
    }
  ],
  "validationOutput": [
    "lines: 10 | parsed: 10 | ids: 1324,1334,1335,1343,1344,1355,1367,1380,1381,1392",
    "event_claims: 33 | strategies: 6 | leaks: 41 | avg quality: 3.7"
  ],
  "residualRisks": [
    "1334 strategy numbers are speaker approximations; verify:false where unfalsifiable",
    "1344 duplicates 1343 and 1381 is mostly self-defense — both flagged for exclusion/merge at compile time"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added structured analysis for batch special_147 (10 transcripts, Oct-Dec 2022) and its batch report",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Batch completed under low-thinking worker configuration; 1381 recommended for near-total exclusion, 1344 merge into 1343"
}
```