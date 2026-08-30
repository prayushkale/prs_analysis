# Copy-Edit Report: rev5 (Chapters 19–21)

## Summary

Applied 4 targeted edits across 3 chapters. All edits kept within the ~15% length tolerance (actual changes: −5.4%, −0.2%, −4.7%).

---

## Chapter 19 — The Event Playbook (1530 → 1448 words, −5.4%)

**Edits made: 2**

1. **Trimmed opening example to cross-reference (Ch20).** Replaced the detailed descriptions of the 4 June 2024 election crash and 3 December 2023 state-election rally with a brief cross-reference: "As Chapter 20 describes, the 2024 election counting day and the 2023 state-election results produced violent moves…" Kept the hook narrative structure intact.

2. **Trimmed yen-carry unwind example to cross-reference (Ch21).** Replaced the full yen-carry narrative (Nikkei −12.4%, specific straddle prices ~900→~1,800, Nifty gap-down of 400 points) with "As the yen-carry unwind of August 2024 (covered in Chapter 21) demonstrated" — the straddle mechanics lesson survives without repeating the case-file detail from Ch21.

**Not changed:**
- The June 2024 put-spread trade example (lines 48–50) is unique to Ch19 — it illustrates defined-risk premium sale structure, not the election narrative from Ch20. Retained.
- "An experienced trader" / "the same trader" references are persona-neutral identifiers; no real identity or channel/course/sponsor references to remove.

**Unsure about:** The ICICI Bank ratio-spread example (July 2020, ₹2,440/₹1,190 numbers) — specific but dated and hedged with "roughly". Left as-is per the chapter disclaimer.

---

## Chapter 20 — Budgets and Elections — Case Files (1496 → 1493 words, −0.2%)

**Edits made: 1**

3. **Fixed "One week matters" repetition.** Removed the duplicate "One week matters." at the start of the second paragraph, leaving only "One line in a budget document matters." as the correct lead-in.

**Not changed:**
- The Sept 2019 corporate tax cut narrative is retained as the primary instance (Ch20 is the case-files chapter); Ch21 was trimmed to cross-reference this.
- All election crash examples are well-dated and properly sourced by dates. No facts-hygiene issues.
- No anonymization issues found.

---

## Chapter 21 — Wars, Crashes and Black Swans (1600 → 1525 words, −4.7%)

**Edits made: 1**

4. **Trimmed corporate tax cut example to cross-reference (Ch20).** Replaced the full Sept 2019 tax-cut description (30%→22%, Bank Nifty +8%, Nifty +4–5%, "promised but never delivered by Arun Jaitley") with "As Chapter 20 details, the September 2019 corporate tax cut triggered a single-session surge — a positive black swan driven by the same mechanics of surprise, leverage, and forced rebalancing…" The positive-black-swan concept is retained; the historical specifics are deferred to the primary case-file in Ch20.

**Not changed:**
- All war/crash examples are dated and sourced. No facts-hygiene issues.
- The crash-paradox aphorism ("A bull market is born out of pessimism…") is unique to Ch21. Not repeated in Ch19 or Ch20.

---

## Checklist Summary

| Priority | Status | Notes |
|---|---|---|
| 1. Anonymization | ✅ Clean | No real-identity, channel, course, workshop, sponsor, family, residence, or luxury references found in any of the 3 chapters. |
| 2. Facts hygiene | ✅ Clean | All claims with dates are properly dated; remaining specific numbers are hedged ("roughly", "approximately", or covered by chapter disclaimer). |
| 3. Repetition | ✅ Fixed | 3 cross-references introduced for material also covered in sibling chapters. No repeated aphorisms found. |
| 4. Voice | ✅ Clean | Third-person exposition throughout. No video-era artifacts ("in this video", "link below", "subscribe", etc.). No first-person narrative beyond persona-neutral references. |
| 5. Prose | ✅ Fixed | 1 prose fix for repeated phrase. No run-ons or filler sentences identified. All chapters within ~15% of original length. |

## Residual Risks

- The ICICI Bank ratio-spread example includes specific premium numbers (₹2,440 / ₹1,190) without a source citation — acceptable under the "illustrative recollections" disclaimer, but a fact-checker might want to validate.
- The 2025 and 2026 events (Operation Sindoor, Iran war) are the most recent examples and may be harder to independently verify for a print audience.

---

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "4 targeted edits across 3 chapters, all within ~15% length tolerance; no scope expansion (no reordering, no heading changes, no Key Takeaways text altered)"
    }
  ],
  "changedFiles": [
    "/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch19.md",
    "/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch20.md",
    "/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch21.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "wc -w ch19.md ch20.md ch21.md",
      "result": "passed",
      "summary": "Word counts: ch19=1448 (-5.4%), ch20=1493 (-0.2%), ch21=1525 (-4.7%) — all within 15% of original"
    },
    {
      "command": "grep for video-era artifacts / first-person references in all 3 files",
      "result": "passed",
      "summary": "No subscribe/link/video/course/workshop/sponsor/first-person references found"
    }
  ],
  "validationOutput": [
    "All 4 edits applied successfully with edit tool",
    "Cross-references added: Ch19→Ch20 (×1), Ch19→Ch21 (×1), Ch21→Ch20 (×1)",
    "Duplicate phrase removed: Ch20 'One week matters' repetition fixed",
    "No heading numbers, chapter ordering, or Key Takeaways boxes altered",
    "No remaining repetitions across the 3-chapter set"
  ],
  "residualRisks": [
    "ICICI Bank ratio-spread premium figures (Ch19, July 2020) lack external source but are covered by disclaimer",
    "2025-2026 event examples (Operation Sindoor, Iran war) are recent and may be harder for print readers to independently verify"
  ],
  "noStagedFiles": true,
  "diffSummary": "Ch19: opening trimmed to cross-ref Ch20; yen-carry example trimmed to cross-ref Ch21. Ch20: removed duplicate 'One week matters.'. Ch21: tax-cut example trimmed to cross-ref Ch20. Total reduction: 160 words.",
  "reviewFindings": [
    "no blockers: all edits are narrow, scoped, and validated"
  ],
  "manualNotes": "No decisions were needed from supervisor; all edits were clear from the copy-edit brief. The report file at rev5_report.md is the authoritative output."
}
```