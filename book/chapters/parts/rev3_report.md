# Copy-Edit Pass Report (Rev 3) — Chapters 8–12

**Editor role**: book copy-editor, final quality pass on Part 3 (Options from First Principles).
**Guidelines applied** (priority order): anonymization → facts hygiene → within-part repetition → voice/video-era artifacts → prose.

---

## Per-Chapter Fixes

### Chapter 8 — Why Derivatives Exist
Fixes made: **1**

1. **Repetition (with Ch12)**: The final paragraph referenced the Franklin Templeton debt-fund closure as a fresh example; replaced with a cross-reference to Chapter 12, which carries the full story ("…the Franklin Templeton debt-fund closure later that year, as Chapter 12 details.").

Notes / unsure about: none. The dated crude-oil example (20 April 2020) and the dated MTM worked example (5–9 June 2022) were left intact per the "never remove dates" rule. The "93% of individual F&O traders lose money" claim is attributed to SEBI data via a forward reference to Chapter 27 (outside this part) — kept.

### Chapter 9 — Calls and Puts
Fixes made: **1**

1. **Anonymization / voice**: The opening anecdote was framed as "A caller reached out with a story," which implies the persona runs a call-in platform (channel/audience). Rewrote as a third-person vignette about an anonymous would-be trader ("A would-be trader hears about an options strategy…"), keeping the quoted material ("But the options gave me unlimited profit potential… What went wrong?").

Notes / unsure about: The Virat Kohli analogy is a public-figure illustration, not a persona reference — kept. The forward reference to Chapter 12 on SEBI's hedging-friendly margin framework is a proper cross-reference within this part — kept. The "training" vignette is unverifiable by nature (illustrative anecdote, no date); left as an archetype rather than a specific dated claim.

### Chapter 10 — The Greeks, Demystified
Fixes made: **0**

Notes / unsure about: No anonymization, fact-hygiene, repetition, voice, or prose issues found. The June 2020 call-ratio-spread anecdote is dated, internally consistent with the market levels of that period, and involves an anonymous trader — left intact. "This chapter gives you the same toolkit" is standard educational-book voice, not a video-era artifact — kept.

### Chapter 11 — Implied Volatility
Fixes made: **1**

1. **Facts hygiene**: "In June 2020, Nifty fell 500 points in a week" (specific, undated, hard to verify) hedged to "In June 2020, Nifty reportedly fell roughly 500 points in a week."

Notes / unsure about: The 23 April 2020 claim comparing IV (~55) with 20-day HV (~38) carries an exact date and its own hedging ("roughly"/"about") — kept. The VIX 85.7 print (late March 2020) is a well-documented, dated record — kept. The expiry-week Theta/Gamma discussion overlaps thematically with Chapter 10's Theta–Gamma trade-off section but applies the concept in a distinct IV/expiry-week context rather than repeating the same aphorism — left as is.

### Chapter 12 — Margins, Collateral, and the Machinery
Fixes made: **1**

1. **Facts hygiene**: In the SEBI margin rule-evolution table, the "Jul 2025" entry was stated as fait accompli; marked "(proposed)" since it is a forward-dated regulatory measure ("Jul 2025 (proposed) | Additional Intraday Volatility Margin (AIVM)…").

Notes / unsure about: The "Jan 2026" table entry already carries "Not yet final / Under consultation" — left intact. The Franklin Templeton opening (April 2020) is the authoritative instance of that example within this part and is dated — kept, and Chapters 8 and 30 now defer to it via cross-reference.

---

## Cross-Chapter Checks (per guideline)

- **Anonymization**: No channel/course/workshop/sponsor/family/residence/luxury references remain in Chapters 8–12. Dhanraj is the only allowed name and never appears in this part. Grep checks for course/workshop/channel/subscribe/link-below/in-this-video/caller-reached-out returned zero hits in chapters 8–12.
- **Video-era artifacts**: None found ("watch"/"watched" occurrences are ordinary verbs, not on-screen artifacts).
- **Repetition within part**: Only one true within-part repeat (Franklin Templeton in Ch8 vs Ch12) — resolved via cross-reference. "Most options expire worthless" appears only in Ch9. Gamma/Theta overlap between Ch10 and Ch11 kept as distinct applications.
- **Chapter length deltas**: Ch08 (1,254→1,251 words), Ch09 (1,495→1,486), Ch10 (1,636→1,636), Ch11 (1,526→1,528), Ch12 (1,822→1,823) — all far inside the ±15% band.
- **Headings / numbering / chapter order / Key Takeaways boxes**: untouched.

---

## Unsure-About Items for the Author/Editor

1. **Ch09 "training" vignette**: The ₹50,000→₹30 lakh promise is archetypal and undated; I kept it as an illustrative anecdote rather than hedging or dropping. If the book's fact policy requires every quantitative anecdote to be dated, this one would need a "reportedly/by recollection" tag or removal.
2. **Ch12 "Jan 2026" entry**: Marked "Under consultation / Not yet final" in the source; if the manuscript's publication date precedes any final SEBI decision on that item, the wording is already safe.
3. **Ch11 "reportedly" hedge**: I used "reportedly" per the guideline's allowed hedge vocabulary; an alternative that some style guides prefer is "by recollection" — flagging in case the house style settles on one form.

---
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Made only the five targeted copy-edit fixes in the priority order and scope defined in the task: (1) Ch09 opening rewritten to remove the caller/platform anonymization leak; (2) Ch08 Franklin Templeton mention trimmed to a cross-reference to Ch12 (within-part repetition); (3) Ch11 'Nifty fell 500 points in a week' hedged with 'reportedly roughly'; (4) Ch12 'Jul 2025' SEBI entry marked '(proposed)'; (5) Ch10 required no changes. No reordering of chapters, no heading-numbering changes, Key Takeaways boxes untouched (prose only), chapter lengths unchanged within ±15%. No product/architecture/scope decisions introduced."
    }
  ],
  "changedFiles": [
    "book/chapters/parts/ch08.md",
    "book/chapters/parts/ch09.md",
    "book/chapters/parts/ch11.md",
    "book/chapters/parts/ch12.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "grep -riE 'course|workshop|channel|subscribe|link below|in this video|on screen|caller|reached out' book/chapters/parts/ch{08,09,10,11,12}.md",
      "result": "passed",
      "summary": "No anonymization or video-era artifact hits in the five target chapters"
    },
    {
      "command": "wc -w book/chapters/parts/ch08.md ch09.md ch10.md ch11.md ch12.md",
      "result": "passed",
      "summary": "Word counts 1251/1486/1636/1528/1823 - all within 15% of originals (1254/1495/1636/1526/1822)"
    },
    {
      "command": "git status -- book/chapters/parts/ch08.md ... ch12.md",
      "result": "passed",
      "summary": "Target files untracked; nothing staged; no staged files present"
    }
  ],
  "validationOutput": [
    "Verified each edit by re-reading the edited regions: ch08.md (cross-reference line), ch09.md (rewritten opening paragraph), ch11.md (hedged sentence), ch12.md (SEBI table row).",
    "Confirmed Ch09 rewritten opening flows into the following paragraph and the quotes remain coherent.",
    "Confirmed the Franklin Templeton example now has a single authoritative instance (Ch12) with Ch08 deferring to it.",
    "Confirmed headings, chapter ordering, and Key Takeaways sections are byte-identical to the originals except for the targeted prose lines."
  ],
  "residualRisks": [
    "Ch09's undated '₹50,000 to ₹30 lakh' training anecdote remains unverifiable by nature (kept as illustrative archetype) - flagged in report as unsure item",
    "Ch08 cross-reference says 'as Chapter 12 details' - requires Chapter 12 to remain the canonical Franklin Templeton narrative (it is; confirmed in this pass)",
    "Ch11 hedge uses 'reportedly' - house style may prefer 'by recollection'"
  ],
  "noStagedFiles": true,
  "diffSummary": "Four files edited with a total of 4 inline text replacements (no structural changes): ch08 (1 line reworded to cross-reference Ch12), ch09 (opening paragraph rewritten from caller-framing to anonymous third-person vignette), ch11 (1 sentence hedged with 'reportedly roughly'), ch12 (1 table cell annotated '(proposed)'). ch10 unchanged. Net word-count delta across all five chapters: -11 words.",
  "reviewFindings": [
    "no blockers",
    "anonymization: ch09.mdx:3 - 'A caller reached out' removed (platform implication); verified no other personal/platform references in ch08-ch12",
    "facts hygiene: ch11.md obj paragraph - unverifiable 500-point claim hedged; ch12.md SEBI table - forward-dated Jul 2025 row flagged '(proposed)'",
    "repetition: ch08.md:76 - Franklin Templeton mention trimmed to cross-reference (canonical instance is ch12.md opening)",
    "voice: no video-era artifacts found in any of the five chapters"
  ],
  "manualNotes": "Report written to book/chapters/parts/rev3_report.md as directed. All edits are prose-only inline replacements; no headings, numbering, or chapter order changed. Ch10 required no changes: it was clean across all five review categories."
}
```