# Batch special_153 Report — 10 transcripts (ids 1663–1714, May–Jun 2023)

## Digest
1. All 10 transcripts read in full; 10/10 JSON records written to `book/analysis/batch_special_153.jsonl`, validated line-by-line as JSON.
2. **Source-quality finding:** ids 1663, 1665, 1672, 1678, 1683, 1705 are ~700-byte truncated stubs **in the source .docx files themselves** (5 paragraphs: title, timestamp, video ID, one body paragraph) — verified against original docx XML (780 total chars). Not an extraction bug; flagged `quality:1`.
3. **Duplicates:** 1672 == 1665 content; 1683 == 1678 content (re-uploads) — `dup_of` set, prevents double-counting in the book.
4. **Exclusion recommendation:** 1705 is a pure workshop-announcement promo (`recommend_exclude: true`).
5. **High-value content:** 1702 (fund-manager capacity parable, quality 5 — chapter 29/1), 1714 (Nifty 22,000 roadmap with 10 verifiable event claims, quality 5 — chronicle ch. 24/25), 1679 (Vauld bankruptcy + SLR capital-allocation principle — ch. 31/29), 1690 (elections-as-market-events — ch. 20/19; political opinion passages flagged for exclusion per approved policy).

## Verification queue highlights (from event_claims)
- Vauld: liquid assets ≈36% of liabilities; reverse Dutch auction mechanism; 3-4 month timeline.
- 2023: Karnataka result, 19-party Parliament boycott, SEBI 50-50 cash-component rule + banker's-guarantee loophole.
- 1714 track-record claims: 2020 7,500/15,000 call outcome; gold $3,000 BofA call failure; Moneycontrol 19,000 vs 18,900 high; FIIs 3-lakh-crore 2021-22 selling; RBI deputy-governor black-swan paper; FII 30k-crore monthly buy + 16,800→18,800; China-below-pre-Lehman comparison; GST/PMI/bond-index 2023.

## Anonymization
- Leaks logged: name variants ("P. R. Sunder", "PR Sunder"), "brand value in YouTube", workshop business + "Kings Club" venue, "I promote Delta Exchange", Moneycontrol interview framing, follower counts, "my tweet/timeline".
- Political-opinion passages in 1690 (party-by-party analysis, Congress internal critique) flagged in `exclude_passages` per the approved exclude-political-opinion decision; market-frame content (stability, FII reaction, option premium impact) retained.

## Residual risks
- The 4 stub transcripts lost their headline stories at the source (e.g., 1678/1683's actual single-day loss narrative is absent); the book can only use the surviving fragments, or recover via alternate uploads if any exist elsewhere in the corpus (none found by title here).
- 1702's fund-manager identity is intentionally unnamed in source; verification of the 700→1,400 crore claim is not possible without naming — treat as anecdote, not fact.
