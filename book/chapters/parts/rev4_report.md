# Rev4 Copy-Edit Report — Chapters 13–18

Pass type: final copy-edit (targeted inline fixes only; no reordering, no heading/numbering changes, no Key Takeaway restructure beyond prose fixes).

## Per-Chapter Fixes

### Chapter 13 (2 fixes)
1. **Facts hygiene / internal consistency**: Changed "returns of roughly 50% on capital" → "roughly 70%" so it agrees with the same paragraph's "₹66 lakh profit on roughly ₹95 lakh capital deployed" (~69%). 
2. **Repetition + prose**: Trimmed the June 2020 expiry-day ₹4→₹23 call-sale example (retold in full in Chapter 18) to a cross-reference ("detailed in Chapter 18"), preserving the lesson; fixed typo "vol spike multiples the loss" → "multiplies".

Unsure: "two lots (1,000 shares total)" for HDFC Bank — internally consistent with a 500-share lot but the actual June 2020 lot size was not independently verified; left as-is (recollection-framed, disclaimer covers the chapter).

### Chapter 14 (1 fix)
3. **Repetition**: Trimmed the ICICI ratio-rescue outcome (planned ₹3,000 loss → ₹2,000 profit per lot), which is told in full in Chapter 18's firefighting section, to a cross-reference ("the full firefighting sequence is in Chapter 18") while keeping the argument-completing sentence.

### Chapter 15 (1 fix)
4. **Voice / video-era artifact**: "In the back-office run shown" → "In the back-office records" (removes visual-presentation artifact; no visual exists in a print book).

### Chapter 16 (2 fixes)
5. **Repetition**: Trimmed the Infosys iron-butterfly payoff recap (₹3.58 lakh, 710/590 protection — near-verbatim repeat of Chapter 14's worked example) to a construction summary plus cross-reference ("the defined-risk payoff detailed there").
6. **Prose / grammar**: "buy five of the 126,000 call" → "buy five 126,000 calls".

### Chapter 17 (3 fixes)
7. **Repetition**: Replaced the opening restatement of the June 2020 margin figures (₹25,000–32,000 vs ₹80,000–90,000, repeated from Chapter 14, and the "one-third" framing repeated in Chapter 15) with a cross-reference to both chapters.
8. **Prose / filler**: Deleted the orphaned sentence "The trader who stages entries at −10% (50% of capital) and −20% (deploy the FD tranche) has a defined drawdown budget" — unexplained terms, no antecedent in the chapter.
9. **Facts hygiene + repetition**: Harmonized the Reliance figure ₹1,59,000 → ₹1,59,186 (matches Chapter 18's precise figure for the same trade) and added a cross-reference to Chapter 18's full account.

### Chapter 18 (4 fixes)
10. **Repetition**: Replaced the repeated "matchstick" aphorism (verbatim in Chapter 17) with fresh phrasing ("Selling cheap tail options on expiry day is not leverage — it is gambling"), keeping the paragraph's conclusion.
11. **Repetition**: Replaced the repeated "If you want to be successful in the stock market" quote (same frame used to open Chapter 17) with a cross-reference ("As Chapter 17 showed, success needs both edge and hedge — one without the other fails"), keeping the punchline.
12. **Prose**: Key Takeaway 1 — "If no on either" → "If the answer to either is no" (matches the body sentence).
13. **Prose**: Key Takeaway 4 — typo "one spike can multiple the loss" → "can multiply".

## Checks Performed
- **Anonymization**: Grepped for channel/course/workshop/sponsor/family/residence/luxury terms and first-person voice; none present. Only "Dhanraj" (the allowed persona) is named; all quotes attributed to "Dhanraj / he". Clean.
- **Facts hygiene**: All quantitative examples carry dates or "roughly"-style qualifiers; remaining specific figures are recollection-framed (Ch13 carries the illustrative-recollection disclaimer). Cross-chapter figure consistency verified (Reliance ₹1,59,186; ICICI ₹3,000→₹2,000; expiry-call ₹4→₹23) except as flagged below.
- **Voice**: No video-era artifacts found besides the one Ch15 fix. Second-person "you" in instructional prose is a standard trading-book device and not first-person; left untouched to avoid a wholesale rewrite.
- **Length**: Line counts unchanged (281 total); word count moved by a net of roughly −80 words across ~6,900 (≈ 1%), far within the 15% budget.
- **Structure**: No chapter reordering, no heading changes, no Key Takeaway restructure.

## Items Flagged for the Parent (outside my scope or judgment calls)
1. **ch19.md repeats the ICICI 350/380 ratio example but dates it "July 2020"**, while ch14/ch18 (in my part) say "May 2020" for the same trade. The May date is internally consistent across two chapters and ch19's figures match ch14's exactly; ch19 likely carries the date error, but it is not in my assigned files.
2. **ch16 "December 2025" Bitcoin example** ($80K–$92K range, $360–373 margin) may be forward-looking depending on publication date; it is framed as Dhanraj's own illustrative logic, so I left it unhedged.
3. **ch13 "50% → 70%" change** was a judgment call for internal consistency with the ₹66L/₹95L figures; if the 50% figure came from a source, the source value would need to override the in-text ratio.

## Changed Files
- /home/ubuntu/repos/prs_analysis/book/chapters/parts/ch13.md (2 fixes)
- /home/ubuntu/repos/prs_analysis/book/chapters/parts/ch14.md (1 fix)
- /home/ubuntu/repos/prs_analysis/book/chapters/parts/ch15.md (1 fix)
- /home/ubuntu/repos/prs_analysis/book/chapters/parts/ch16.md (2 fixes)
- /home/ubuntu/repos/prs_analysis/book/chapters/parts/ch17.md (3 fixes)
- /home/ubuntu/repos/prs_analysis/book/chapters/parts/ch18.md (4 fixes)

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "13 targeted inline fixes across ch13-ch18 in priority order (anonymization: none needed beyond verification; facts consistency: 2; repetition: 6 trims to cross-references; voice: 1 video-artifact removal; prose: 4 typo/filler/grammar fixes). No reordering, no heading/numbering changes, Key Takeaways touched only for two prose fixes. Chapter length unchanged (0 line moves; ~-80 words net of ~6,900, <15% budget)."
    }
  ],
  "changedFiles": [
    "book/chapters/parts/ch13.md",
    "book/chapters/parts/ch14.md",
    "book/chapters/parts/ch15.md",
    "book/chapters/parts/ch16.md",
    "book/chapters/parts/ch17.md",
    "book/chapters/parts/ch18.md",
    "book/chapters/parts/rev4_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "grep -n 'channel|course|workshop|subscribe|matchstick|If you want to be successful|shown' book/chapters/parts/ch13*.md ch14*.md ch15*.md ch16*.md ch17*.md ch18*.md",
      "result": "passed",
      "summary": "Located the 3 repeating aphorisms/figures and the single video-era artifact across my part"
    },
    {
      "command": "grep -n '\\bI \\|my \\|we \\|our \\|us\\b' ch13-18 | grep -v quotes",
      "result": "passed",
      "summary": "No first-person narrator voice found; only Dhanraj persona references"
    },
    {
      "command": "wc -l && wc -w ch13-18",
      "result": "passed",
      "summary": "281 lines / ~6,892 words across 6 chapters; line counts unchanged, word delta ~-1% (within 15% budget)"
    },
    {
      "command": "grep verification of all 13 edits (70%, multiplies, Chapter 18 refs, back-office records, five 126,000, 1,59,186, answer to either, can multiply)",
      "result": "passed",
      "summary": "All 13 fixes present in final files; no leftover artifacts (matchstick/stages entries removed)"
    },
    {
      "command": "git status -- ch13-ch18",
      "result": "passed",
      "summary": "Files untracked (no git baseline for these new chapter files); nothing staged"
    }
  ],
  "validationOutput": [
    "Full re-read of all six chapters post-edit: prose flows, cross-references point to correct chapters, no duplicate examples/aphorisms remain within the part, no heading or takeaway-list structure altered."
  ],
  "residualRisks": [
    "ch19.md (outside my part) dates the ICICI 350/380 ratio 'July 2020' while ch14/ch18 say 'May 2020' - flagged for parent",
    "ch13 50%->70% return figure change was an internal-consistency judgment call based on the in-paragraph rupee figures",
    "ch16 December 2025 Bitcoin example numbers remain unverifiable (recollection-framed); may merit a hedge if the book ships before that period",
    "HDFC Bank 'two lots (1,000 shares total)' assumes a 500-share lot in June 2020; not independently verified"
  ],
  "noStagedFiles": true,
  "diffSummary": "13 targeted copy-edit fixes across ch13-18: 1 facts-consistency fix, 6 repetition trims to cross-references, 1 voice artifact removal, 3 prose typo/grammar fixes, 1 filler-sentence deletion, 1 figure harmonization with cross-reference. No reordering, no heading changes.",
  "reviewFindings": [
    "no blockers - all fixes applied and verified",
    "flag: ch19.md ICICI date (July 2020) conflicts with ch14/ch18 (May 2020) - outside assigned scope",
    "flag: ch13 return-figure change (50%->70%) is a consistency judgment call"
  ],
  "manualNotes": "Second-person 'you' in instructional prose was left untouched (standard trading-book device, not first-person; converting would be a wholesale rewrite outside copy-edit scope). Files ch13-ch18 are untracked in git; no baseline diff available, verification done via targeted grep and full re-read."
}
```