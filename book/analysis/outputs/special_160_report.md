# Batch special_160 — Analysis Report (10 transcripts)

## Deliverable
`/home/ubuntu/repos/prs_analysis/book/analysis/batch_special_160.jsonl` — 10 lines, 1 JSON object per transcript, schema-conformant (validated: all 10 parse).

## Digest (5 lines)
1. Coverage: ids 2265, 2267a, 2270b, 2286a, 2290a, 2296b, 2300b, 2301a, 2301b, 2312b — all read in full, May–June 2024 event season (election → budget aftermath).
2. Star content: 2286a (election-result playbook: 2019 replay, collar hedge, OI/PCR deconstruction, asymmetry framing — quality 5) and 2270b (Budget-2024 tax teardown + futures-premium collapse signal — quality 4).
3. Exclusions: 2296b (Chandrababu Naidu reminiscence) recommended for full exclusion — pure personal biography, no market content; political-affiliation passages in 2286a and co-host identity in 2312b flagged as leaks/exclude_passages.
4. ~35 event claims queued for verification; highest-value: Budget-2024 tax changes (STT/STCG/LTCG), 2019 FM-appointment Bank Nifty −1,000 pts, Sept-2019 corporate-tax cut, lot-size 50→25, record SIP flows ~₹21–23k cr, DIIs +₹1.25L cr vs FIIs −₹1.25L cr in H1 2024.
5. One metadata correction: 2270b content is post-Budget-2024 (shot Thursday after 23-Jul budget; premium-collapse anecdote) → date recorded as 2024-07-25, overriding the manifest's 2024-05-22 (which contradicts the transcript itself).

## Anonymization actions
- All name variants in these files ("P. R. Sunder", "Pia Sundar", "Pierre Sundar", "PR Sunder") logged in `leaks` only; never in lessons/quotes/summaries.
- Residency hints ("since I am in Dubai", Chennai pricing comparisons), family (son's company account, wife), broker-friend, co-host name, YouTube/Twitter references, DMK affiliation, luxury car anecdote — all captured in `leaks`/`exclude_passages`.
- 2300b's "2009" corrected to 2019 (ASR/context error, matches prior extraction of the same event).
- "Pinchloid" in 2312b identified as Punj Lloyd (infra IPO boom-bust parable) — kept genericized in lessons; IPO anecdotes otherwise not asserted as verifiable claims.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 10 assigned transcripts read in full; 10 schema-conformant JSON lines written to book/analysis/batch_special_160.jsonl (validated by json.loads on every line); findings report written to the authoritative output path. No scope widened: only the assigned batch was processed."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_special_160.jsonl",
    "book/analysis/outputs/special_160_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "wc -l + python3 json.loads validation over batch_special_160.jsonl",
      "result": "passed",
      "summary": "10/10 lines parse as valid JSON with required schema fields"
    }
  ],
  "validationOutput": [
    "10 lines, 10 valid JSON records, one per assigned transcript id",
    "chapter_targets/strategies/event_claims populated; 2296b flagged exclude with empty chapter targets"
  ],
  "residualRisks": [
    "2270b manifest date (2024-05-22) contradicts transcript content (post-23-Jul-2024 budget); JSON records 2024-07-25 — parent may want to fix metadata.jsonl",
    "2312b IPO/company name garbles ('PTM', unnamed doubling debut) were NOT asserted as verifiable claims to avoid false verification targets",
    "2300b/2301a are fragment-length clips; content overlaps 2301b same-day coverage"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added one new batch JSONL (10 records) and one batch report; no existing files modified",
  "reviewFindings": [
    "no blockers",
    "note: 2296b recommended for full exclusion from book (personal biography, zero market content)"
  ],
  "manualNotes": "Batch consumed 2 of 10 reads as full-content reads with dense strategy extraction (2286a is the richest election-event source text found so far); suggest prioritizing it for Part V case files."
}
```
