# Rev 8 — Copy-Edit Pass Report (ch29, ch30, ch31)

Pass type: targeted inline copy-edit (no wholesale rewrite, no chapter reordering, no heading/numbering changes, Key Takeaways boxes untouched except prose).

Baseline → final word counts (all within the ~15% tolerance):
- ch29: 1658 → 1643 (−0.9%)
- ch30: 1588 → 1578 (−0.6%)
- ch31: 1796 → 1797 (+0.06%)

---

## Chapter 29 — Investing Versus Trading: Choosing Your Game (3 fixes)

1. **Grammar** — "profit primarily from the growth of the underlying enterprise" → "profiting primarily from the growth of the underlying enterprise" (The Spectrum of Participation).
2. **Grammar** — "profit from timing rather than compounding" → "profiting from timing rather than compounding" (same paragraph).
3. **Prose/filler** — Dropped the computing analogy "In computing, what you see is what you get — Liquid BeES is exactly that:" and capitalized the surviving clause → "…zero STT or stamp duty on transactions. You pay ₹1,000, you get one unit." (removes an out-of-place WYSIWYG aside; the rest of the sentence already makes the point).

Notes on items reviewed and left as-is:
- Crowd-wisdom/contrarian lesson ("taxi drivers and bank managers talking about winnings") appears here in a stock-market context; a sibling instance appears in ch30 about real estate. Judged distinct examples applied to different asset classes, not a duplicate — kept both.
- Nifty 26-year total-return ("roughly eleven times… under 10% per year") and FD ("doubled roughly every six years") claims are dated (1994–2020) and already hedged with "roughly" — kept per the "never remove dates from properly dated examples" rule.
- PE-cycle example (May 2020 PE≈16, Dec 2020 PE past 28, March 2020 Nifty ≈7,500) is fully dated — kept.

## Chapter 30 — The Hard Assets Debate: Real Estate, Gold, and Bonds (1 fix)

1. **Facts hygiene / attribution** — Replaced the vague unattributable quote "As a market observer once put it: 'Whenever there is a problem faced by the entire world, the gold prices will shoot up.'" with a neutral observation: "The pattern is consistent: whenever a global crisis erupts, gold prices shoot up." (Drops an unverifiable quoted attribution while preserving the point.)

Notes on items reviewed and left as-is:
- The Franklin Templeton wind-up (April 2020, ≈₹30,000 crore) is a properly dated public event — kept intact.
- The clubhouse-reclassified-as-mall case is already flagged as "widely reported" (secondhand) — kept, but it lacks a date; see open items below.
- May 2026 gold import duty and the 2018–2026 rental-yield figures sit inside the book's established timeline premise — kept.
- The IT-corridor anecdote is already anonymized ("a South Indian city's arterial road") — kept.

## Chapter 31 — Crypto as a Satellite: Not a Religion (1 fix)

1. **Facts hygiene** — Hedged the unsourced performance claim "crypto option selling has produced consistent monthly returns" → "…has reportedly produced consistent monthly returns…" (matches the manuscript's established hedge style used in ch02, ch07, ch11; the claim had no date or source).

Notes on items reviewed and left as-is:
- BTC/ETH price history (2018 low, Nov 2021 peak, 2022 winter) is publicly known and dated — kept.
- FTX collapse (Nov 2022) and the worked TDS example are dated/public-record — kept.
- 2025–2026 price ranges and FIU-platform claims are part of the book's 2018–2026 timeline premise — kept.

## Cross-chapter checks

- **Anonymization:** No reference to any source speaker's real identity, channel, courses, workshops, sponsors, family, residence, or luxury found in any of the three chapters. "Dhanraj" is the only allowed name; it is not needed in these chapters. The FTX and Franklin Templeton references are public entities/events, not persons.
- **Video-era artifacts:** No "in this video", "link below", "subscribe", "as I showed on screen" strings present.
- **Voice:** All chapters are third-person exposition. The chapter-opening rhetorical questions ("am I an investor or a trader?", "should I put money into hard assets…") use the reader's first-person voice, not Dhanraj's anecdotes — left intact.
- **Repetition within part:** Only the crowd-wisdom contrarian lesson appears in both ch29 and ch30 (different asset classes, different wording) — kept both as distinct examples.
- **Key Takeaways:** No edits made to any Key Takeaways box.

## Items I was unsure about

- ch30 "widely reported" clubhouse case lacks a date; it is already hedged as secondhand so I did not alter it, but a date would strengthen it.
- ch29 counterfactual SIP example ("returns of 200–300% over the subsequent four years" from March 2020) has a date anchor but no source; I left it as an illustrative example rather than hedge, since the book's timeline extends to 2026.
- The chapter-opening first-person rhetorical questions are borderline under the "third-person exposition" rule; I treated them as reader-voice devices, not Dhanraj anecdotes.

---

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Made narrow inline fixes only in the 3 assigned chapters (ch29, ch30, ch31): 2 grammar corrections and 1 filler/analogy removal in ch29, 1 unattributed-quote replacement in ch30, 1 facts-hygiene hedge in ch31. No wholesale rewrites, no chapter reordering, no heading/numbering changes, no Key Takeaways content edits. Word counts stayed within ~15% (ch29 −0.9%, ch30 −0.6%, ch31 +0.06%)."
    }
  ],
  "changedFiles": [
    "book/chapters/parts/ch29.md",
    "book/chapters/parts/ch30.md",
    "book/chapters/parts/ch31.md",
    "book/chapters/parts/rev8_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "wc -w book/chapters/parts/ch29.md book/chapters/parts/ch30.md book/chapters/parts/ch31.md",
      "result": "passed",
      "summary": "Word counts: 1643, 1578, 1797 — within ~15% of baseline (1658, 1588, 1796)"
    },
    {
      "command": "grep -rn 'Dhanraj|subscribe|link below|in this video|as I showed|my channel|my course|my workshop|my family|my home' book/chapters/parts/ch2{9,30,31}.md",
      "result": "passed",
      "summary": "No anonymization or video-era artifacts found in any assigned chapter"
    },
    {
      "command": "git diff --cached --name-only",
      "result": "passed",
      "summary": "No staged files"
    },
    {
      "command": "grep -n 'You pay' ch29.md; grep -n 'pattern is consistent' ch30.md; grep -n 'reportedly produced' ch31.md",
      "result": "passed",
      "summary": "All 5 edits verified present in the source files"
    }
  ],
  "validationOutput": [
    "ch29: 'profiting primarily from' and 'profiting from timing' confirmed; WYSIWYG analogy removed, 'You pay ₹1,000, you get one unit.' now a clean standalone sentence.",
    "ch30: 'As a market observer once put it' quote replaced with neutral 'The pattern is consistent: whenever a global crisis erupts, gold prices shoot up.'",
    "ch31: 'has reportedly produced consistent monthly returns' hedge applied, matching manuscript style (ch02/ch07/ch11).",
    "No changes to headings, chapter order, or Key Takeaways boxes."
  ],
  "residualRisks": [
    "ch30 'widely reported' clubhouse case still lacks a date (already hedged as secondhand).",
    "ch29 counterfactual SIP returns example (200–300%) kept un-hedged as an illustrative example.",
    "Chapter-opening rhetorical first-person questions ('am I an investor or a trader?') retained as reader-voice devices, per voice judgment."
  ],
  "noStagedFiles": true,
  "diffSummary": "5 targeted inline edits across ch29 (2 grammar, 1 filler removal + capitalization fix), ch30 (1 quote-attribution removal), ch31 (1 facts-hygiene hedge). No structural changes.",
  "reviewFindings": [
    "no blockers",
    "no anonymization violations found in ch29/ch30/ch31",
    "no video-era artifacts found",
    "minor: ch30 'widely reported' case lacks a date (optional strengthening)"
  ],
  "manualNotes": "Full per-chapter detail is in the report body above. All three chapters are untracked new files in the parts/ directory; no staged changes."
}
```
