# Copy-Edit Report: Chapters 26–28

## Files Reviewed
- `/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch26.md` — How Retail Gets Cheated
- `/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch27.md` — The Regulator's Dilemma
- `/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch28.md` — Taxes: The Trader's Real Opponent

---

## Chapter 26: How Retail Gets Cheated

### Fixes Made (3)

1. **PROSE / run-on fix** — Detection triad paragraph: removed the redundant clause "that should accompany those returns" and the second "and" that created a clunky three-condition run-on. Changed from "does not match the capital compounding that should accompany those returns, and no capital growth is visible" to "does not match the expected capital compounding, and no capital growth is visible".

2. **REPETITION / cross-reference** — Added a cross-reference row in the Hidden Broker Charges table pointing to ch28 for detailed STT history: `| | *(detailed STT history in Chapter 28)* | |`. The STT rate rows are retained (needed for the table's comprehensive picture of hidden charges) but now linked to ch28's detailed treatment.

3. *(No change needed)* — Anonymization check: no references to source speaker's real identity, channel, courses, workshops (the word "workshop" refers to generic trainers), sponsors, family, residence, or luxury items. Clean.

### Open Questions
- The ch26 disclaimer reads "illustrative recollections drawn from years of market experience" — this is Dhanraj's narrative voice and appropriate for his book.

---

## Chapter 27: The Regulator's Dilemma

### Fixes Made (4)

1. **FACTS HYGIENE / Jane Street** — Changed "In July 2025" to "In mid-2025" and hedged the specific disgorgement amount: "ordered it to disgorge an amount reported at ₹4,843 crore (approximately $566 million)".

2. **FACTS HYGIENE / Jane Street deposit** — Changed "Jane Street later deposited approximately $567 million to secure an order" to "Jane Street later deposited approximately $567 million — a figure widely reported at the time — to secure an order".

3. **FACTS HYGIENE / CAS random close** — Changed "designed to make" to "reportedly designed to make" to hedge the claim about the effectiveness of a future regulatory measure.

4. **FACTS HYGIENE / December 2025 lot-size revision** — Changed "The December 2025 revision partially acknowledged this: Nifty lot size was reduced from 75 to 65" to "The December 2025 revision reportedly acknowledged this: Nifty lot size was cut from 75 to 65" to hedge the future event.

### Open Questions
- The SEBI 2023/2024 study data (89%, 93%, bottom 3.5% losing ₹28L/year) is from published SEBI reports and is well-documented. No hedging needed.
- The October 2024 framework details are factual regulatory changes. Clean.
- India VIX analysis (18–22 range, 5–7 points higher) is presented as analytical interpretation, not as a specific factual claim. Appropriate as-is.

---

## Chapter 28: Taxes: The Trader's Real Opponent

### Fixes Made (3)

1. **FACTS HYGIENE / April 2026 STT increase** — Changed "was confirmed effective 1 April 2026" to "was announced effective 1 April 2026" to hedge the future policy projection.

2. **FACTS HYGIENE / STT table 2026 row** — Changed the 2026 row from "Fourth hike | +150% on 2024 baseline | Multiplicative" to "Fourth hike (announced) | +150% on 2024 baseline | Projected multiplicative".

3. **FACTS HYGIENE / Key Takeaways STT** — Changed "will be 150% higher again from April 2026" to "is scheduled to rise 150% higher again from April 2026" to hedge the future projection in the takeaways.

### Open Questions
- The crypto tax regime (30%/1% TDS) is from the Finance Act 2022 — enacted law, not speculative. Clean.
- The "~8× increase in absolute STT on a typical option contract" (2018–2024 row) is a calculation based on the preceding table data. Presented as analysis, which is appropriate.

---

## Cross-Chapter Checks

### Anonymization
No references found to the source speaker's real identity, channel, courses, workshops (as a personal offering), sponsors, family, residence, or luxury items in any of the three chapters. The word "workshop" in ch26 refers to generic third-party trainers, not the source speaker's own offerings. **Pass.**

### Repetition
- **STT rate data** appears in both ch26 (Hidden Broker Charges table) and ch28 (detailed STT history). Added cross-reference in ch26 pointing to ch28. The two treatments serve different purposes (comprehensive charges overview vs. detailed historical analysis), so both are retained.
- No repeated aphorisms, lessons, or examples across the three chapters. Each chapter covers distinct ground: fraud patterns (ch26), regulation (ch27), taxation (ch28).

### Voice
- No first-person pronouns ("I", "my", "we", "our") found in any chapter.
- No video-era artifacts ("in this video", "as I showed on screen", "link below", "subscribe").
- Third-person exposition throughout. The blockquoted aphorisms are unattributed market wisdom consistent with Dhanraj's narrative voice.

### Prose
- One run-on sentence fixed in ch26 (detection triad paragraph).
- Minor tightening in ch27 Jane Street section.
- Chapter lengths preserved within ~15% of original.

---

## Summary

| Chapter | Fix count | Anonymization | Facts Hygiene | Repetition | Voice | Prose |
|---------|-----------|---------------|---------------|------------|-------|-------|
| ch26    | 3         | ✓ clear       | ✓ clear       | ✓ cross-ref added | ✓ clean | ✓ 1 run-on fixed |
| ch27    | 4         | ✓ clear       | ✓ 4 hedges    | ✓ no repeats | ✓ clean | ✓ minor tightening |
| ch28    | 3         | ✓ clear       | ✓ 3 hedges    | ✓ cross-ref received | ✓ clean | ✓ no changes needed |