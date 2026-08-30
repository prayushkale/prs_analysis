# Batch daily_019 — Analysis Report

## Scope
25 transcripts, ids 0847–0889 (Feb 14 – Mar 3, 2022): the Russia-Ukraine invasion window.
Output: `/home/ubuntu/repos/prs_analysis/book/analysis/batch_daily_019.jsonl` (25 lines, schema-validated).

## Counts
- pre_market: 10 · post_market: 15 · weekly: 0
- Event claims extracted: 87 (58 marked verify=true — dateable public events; 29 verify=false — intraday stats/positioning/personal trades)
- Lessons: 48 · Quotes: 24 · Leak strings logged: all 25 files (sponsors 5paisa/Delta Exchange/TaxBuddy/Finbingo on every file; name intros on most; isolated family/promo/political items flagged per line)

## Batch narrative (for Part VI chronicle + Parts II/V/VII)
This window is the single richest "event anatomy" sequence in the corpus — a complete war-cycle playbook:
1. **Standoff whipsaw (Feb 14–18):** headline-driven ±400-pt Dow swings; "certain vs uncertain uncertainties" (0856); India underperformed Russia's own market on the ABG Shipyard ₹22,000-cr fraud (0849/0850); V-shaped round trip when Russia announced troop returns — "₹9 lakh crore lost, ₹9 lakh crore added" (0852).
2. **Escalation (Feb 21–23):** Donetsk/Luhansk recognition, Russian VIX ~92–96 vs Lehman's 85–90 (0870/0871); first 200-DMA break in ~2 years then recovery-on-bad-news bottom signal (0871); FII Feb selling >₹39,000 cr with 3:00–3:15pm basket-sale signature (0874).
3. **Invasion (Feb 24):** Nifty −900/−1,000, Bank Nifty −2,000; India VIX >30, US 37, Russia 127 (0876). The VIX>30-flat rule saved the speaker's book next day (0877).
4. **Sanctions whipsaw (Feb 25–28):** crude/gas excluded from sanctions → Nasdaq +7% low-to-high (0877); SWIFT cutoffs, ruble −50%, Russia's 20% rate hike and foreign-seller ban (0882/0884).
5. **Stabilization attempt (Mar 2–3):** recovery-without-news = negatives priced (0888); Powell 25bp < feared 50bp = relief rally; crude $117 the residual India risk (0889).

## High-value recurring material
- **Method lessons:** VIX>30 exit rule (3 files); 200-DMA as the only technical in crisis (5 files); max-OI expiry-range math (strike ∓ premium) (0874); futures-discount unwinding (0872); recovery-on-bad-news bottoming rule (0871/0888); last-half-hour institutional selling (0858/0874/0888).
- **Verification targets:** Russia-Ukraine timeline (all verify=true claims cluster here), ABG Shipyard ₹22,000 cr (0849), Feb-2022 FII monthly figures (₹39–45k cr), LIC IPO ₹63,000 cr sizing/retail quota, Powell 25bp signal, ruble 80→120, Russia CBR 9→20%, BP-Rosneft $25B, India VIX 27.8–30 prints.
- **Chronicle quotes:** rowdy-gangs crossfire (0861); amateurs-open/professionals-close variant (0874); uncertainty aphorism (0882).

## Data quality
- docx-era transcripts are cleanly punctuated; ASR garbles limited (5paisa variants, "weeks"→VIX, "Quotag"→Kotak, " Crudile"→crude) — all handled per dictionary.
- One classification note: 0874's "3417 cr highest February selling" and 0871's MTD ₹27,000 cr are speaker-computed; flagged verify=true for web cross-check.
- Political/joke passages flagged for exclusion: WhatsApp LIC/LOC joke (0855), thumbnail joke on FII ban (0884), petrol-price election-timing comment (0888), evacuation criticism (0878).

## Acceptance report
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 assigned transcripts (0847-0889) read in full; 25 JSON lines with the required schema written to book/analysis/batch_daily_019.jsonl; no scope widened beyond the batch."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_019.jsonl",
    "book/analysis/outputs/daily_019_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json.loads validation loop over batch_daily_019.jsonl",
      "result": "passed",
      "summary": "25/25 lines parse as valid JSON; ids and type fields conform to schema"
    }
  ],
  "validationOutput": [
    "valid lines: 25",
    "schema fields present on every line: id,date,type,summary,levels,events,lessons,quote,dup_flag,leaks"
  ],
  "residualRisks": [
    "Speaker-computed aggregates (February FII totals, MTD figures) need web cross-check in Phase 3",
    "Two near-duplicate recaps flagged via dup_flag for compiler dedupe"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added batch_daily_019.jsonl (25 structured transcript analyses) and this report; no other files touched",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Batch covers the Russia-Ukraine invasion window - highest-density event teaching sequence in the daily corpus; 58 verify=true claims queued for Phase 3."
}
```
