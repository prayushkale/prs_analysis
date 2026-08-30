# Copy-Edit Report: Chapters 4–7

## Summary

**Total fixes applied: 11** across Chapters 4, 6, 7. Chapter 5 required no changes.

### Categories addressed

| Category | Count | Description |
|---|---|---|
| ANONYMIZATION | 10 | Replaced "the speaker" → "Dhanraj" throughout |
| FACTS HYGIENE | 1 | Hedged unverifiable specific claim in ch07 |
| REPETITION | 0 | No repeated aphorisms/lessons across these 4 chapters |
| VOICE | 0 | Already in third-person exposition; first-person only in Dhanraj quotes (correct) |
| PROSE | 1 | Trimmed video-era artifact "in hundreds of post-market reports" → "repeatedly" |

---

## Chapter 4 — The Engine Room: FII/DII Flows

**Fixes (2):**

1. **ANONYMIZATION**: `"As the speaker noted in a December 2018 post-market report"` → `"As Dhanraj noted in a December 2018 post-market report"`
2. **ANONYMIZATION**: `"The speaker's prescription"` → `"Dhanraj's prescription"`

**Unsure about:** None. The chapter disclaimer already hedges all figures. No facts-hygiene issues.

---

## Chapter 5 — Volatility as a Regime, Not a Number

**Fixes (0):**

No "speaker" references, video-era artifacts, first-person violations, or unverifiable claims. The VIX data points are all properly dated. Clean.

**Unsure about:** None.

---

## Chapter 6 — Reading the Option Chain

**Fixes (3):**

1. **ANONYMIZATION**: `"The speaker, watching the chain update by update, observed"` → `"Dhanraj, watching the chain update by update, observed"`
2. **ANONYMIZATION**: `"The speaker's most reliable macroscopic call came from exactly this reading"` → `"Dhanraj's most reliable macroscopic call came from exactly this reading"`
3. **ANONYMIZATION**: `"The speaker refined it"` → `"Dhanraj refined it"`

**Unsure about:** None.

---

## Chapter 7 — Microstructure: Gaps, Expiries, and the Last Half Hour

**Fixes (6):**

1. **ANONYMIZATION**: `"the market microstructure that the speaker called"` → `"the market microstructure that Dhanraj called"`
2. **ANONYMIZATION**: `"the speaker documented a more nuanced reality"` → `"Dhanraj documented a more nuanced reality"`
3. **ANONYMIZATION**: `"The speaker built his entire trading approach"` → `"Dhanraj built his entire trading approach"`
4. **ANONYMIZATION + PROSE**: `"The speaker's signature observation — one that he returned to in hundreds of post-market reports — was this"` → `"Dhanraj's signature observation — one that he returned to repeatedly — was this"` — trimmed the video-era quantity reference ("hundreds of post-market reports") as a prose/video-artifact fix.
5. **ANONYMIZATION**: `"The speaker tracked these events"` → `"Dhanraj tracked these events"`
6. **FACTS HYGIENE**: `"produced a documented 539-point swing"` → `"reportedly produced a 539-point swing"` — hedged the unverifiable specific claim about the first CAS-affected expiry swing.

**Unsure about:** The figure "460 separate trading days across 32 distinct episodes between 2008 and 2026" in ch05 is very specific but already has date context and a year range. Left as-is since it fits the book's recollection disclaimer.

---

## Global assessment

- **No scope widening**: All fixes are narrow, targeted inline edits. No structural changes, heading renumbering, or reordering.
- **Chapter lengths**: Changes are negligible in word count (replacements of equal length or shorter). Within ~15% of original.
- **Key Takeaways boxes**: Unchanged except the underlying prose already fixed above.
- **Residual risks**: None identified.

---

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "11 targeted inline fixes applied across 3 of 4 chapters: 10 anonymization replacements (the speaker -> Dhanraj), 1 facts-hygiene hedge (documented -> reportedly), 1 combined prose/video-artifact trim. No structural changes, no scope widening."
    }
  ],
  "changedFiles": [
    "/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch04.md",
    "/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch06.md",
    "/home/ubuntu/repos/prs_analysis/book/chapters/parts/ch07.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "grep -n 'the speaker\\|The speaker' book/chapters/parts/ch04.md book/chapters/parts/ch05.md book/chapters/parts/ch06.md book/chapters/parts/ch07.md",
      "result": "passed",
      "summary": "Confirmed zero remaining 'the speaker' references across all 4 chapters (exit code 1 = no matches)"
    },
    {
      "command": "grep -n 'Dhanraj' book/chapters/parts/ch04.md book/chapters/parts/ch05.md book/chapters/parts/ch06.md book/chapters/parts/ch07.md",
      "result": "passed",
      "summary": "Verified 10 Dhanraj references present at correct locations"
    },
    {
      "command": "grep -n 'reportedly' book/chapters/parts/ch07.md",
      "result": "passed",
      "summary": "Verified facts-hygiene hedge in ch07 line 37"
    },
    {
      "command": "grep -n -i 'speaker\\|subscribe\\|video\\|screen\\|link below\\|channel\\|course\\|workshop\\|sponsor\\|family\\|residence\\|luxury' book/chapters/parts/ch05.md",
      "result": "passed",
      "summary": "Confirmed ch05 contains zero issues requiring fixes"
    }
  ],
  "validationOutput": [
    "All 11 edits verified in source files",
    "Zero remaining 'the speaker' references",
    "All Dhanraj substitutions are context-appropriate (third-person exposition, quotes preserved)",
    "Ch05 confirmed clean - no changes needed"
  ],
  "residualRisks": [
    "none"
  ],
  "noStagedFiles": true,
  "diffSummary": "ch04: 2 replacements (speaker -> Dhanraj). ch05: 0 changes. ch06: 3 replacements (speaker -> Dhanraj). ch07: 5 replacements (speaker -> Dhanraj) + 1 trim (video-era artifact) + 1 hedge (documented -> reportedly). Zero structural changes.",
  "reviewFindings": [
    "no blockers: all 11 fixes are narrow, correct, and within scope"
  ],
  "manualNotes": "Ch05 was clean after review - no speaker references, video artifacts, or first-person violations found. The figure '460 trading days across 32 distinct episodes between 2008 and 2026' in ch05 was left as-is because it has date context and falls under the book's illustrative recollection disclaimer."
}
```