# Batch daily_000 Report

**Scope:** 25 daily transcripts (23 post-market, 1 pre-market, 1 re-recorded post) — ids 0004–0023 (2018 Oct–Nov series), 0033 (Apr 2020), 0174–0201 (Oct–Dec 2020).
**Output:** `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_000.jsonl` — 25 JSON lines, schema-validated (levels/summary/events/lessons/quote/dup_flag/leaks), IDs in manifest order.

## Digest
- **Counts:** 25/25 analyzed, 25/25 valid JSON lines. Zero extraction issues; transcripts were clean, human-edited text (docx era).
- **Most notable events captured for verification:** Oct-2018 FII selling >30,000cr (highest since Jan-2008); RBI–Government Section 7 standoff and Coal India FPO; Brent's 12-consecutive-day fall (30-year record) to <$65; Nov-2018 five-week series 10,030→10,880 (~9%); Bank Nifty +700 on 19-Oct-2020 without HDFC Bank (Jet Airways revival, ICICI ₹1,000cr loan); Pfizer/BioNTech >90% efficacy day (9-Nov-2020) with Nifty ATH cross; MSCI rebalancing ~₹18,000cr; DII+FII simultaneous >₹1,000cr selling (13-Apr-2020); futures-premium erosion signal (11-Dec-2020); Georgia Senate runoff trigger (5-Jan-2021).
- **Lesson density:** strong — 15 of 25 carried transferable lessons (regime mapping, max-OI conviction, binary-event handling, lead-vs-lag indicator, V-shaped recovery tells, premium decay on down days, pre-holiday square-off flows).
- **Levels captured:** Nifty/Bank Nifty/VIX/FII/DII values recorded only where explicitly stated (FII/DII on 20 of 25).
- **Leaks logged:** real-name variants ("P R Sunder", "P. R. Sundar", "PR Sunder") from 0033 onward (docx-era pre-strip headers removed; in-text greetings remain), channel CTAs ("subscribe and like") on ~20 files, two media/social references (BTVI interview 0023, Twitter posts 0023/0179/0194/0201), one family reference (0179 "joking with my son"), one language-identity proverb framing (0174).
- **Dup flags:** none — adjacent-day reports are complementary (pre-market sets levels, post-market reports outcomes), not repeats.

## Data quality notes
- 2018 files have recurring ASR artifacts ("Quattac/Quotaq/Kotaq"→Kotak, "India Bix"→VIX, "collection"→call option, "IAP/IEP"→IIP, "SGX/ESGX/Singapore Nifty"→SGX Nifty) — interpreted per dictionary, not echoed.
- Two uncertain figures marked verify=false: Divi's Labs +15% (0006), MCA-report HFC selloff detail (0011).
- 0004 contains no identity strings at all; earliest files (0006–0011) carry only CTA leaks.
