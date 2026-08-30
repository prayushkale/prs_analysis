# Batch daily_014 Analysis Report — 25 transcripts (Nov 15 – Dec 2, 2021 dailies)

## Digest (5 lines)
1. **Counts:** 25/25 transcripts analyzed (13 post-market, 12 pre-market); 25 valid JSON lines written to `book/analysis/batch_daily_014.jsonl`, all schema-checked.
2. **Arc captured:** the batch covers a complete correction cycle — FII buying resumption hopes (Nov 15-16) → 9:15 basket-raid selloffs (Nov 17-25) → Paytm IPO disaster + farm-law repeal crash (Nov 18-22, Nifty -1,300 from 18,600) → Omicron shock (Nov 26, -600; first >500pt fall since Brexit/demonetization) → Dec 1-2 stabilization (FII selling 5,000cr→910cr, Nifty +350 surprise rally).
3. **Most notable verified-queue events:** Omicron identification timeline + travel bans; Powell "inflation not transitory" testimony; Q2 FY22 GDP 8.4% + GST ₹1.31 lakh crore; USDT depeg to ₹62 on WazirX during crypto-bill panic; Lok Sabha crypto bill bulletin (wording identical to Jan 2021); Kotak RBI promoter-cap relief; Adani market cap > RIL; Star Health IPO 79% subscription; Moderna CEO vaccine-effectiveness comments; first US Omicron case + CBOE VIX >31.
4. **Data quality:** high — levels/FII-DII flows internally consistent across paired pre/post reports; 3 inconsistencies flagged for verification (Sapphire Foods listing date conflated with Paytm day; cumulative FII figures quoted as both 50,000cr/2mo and 75,000cr/2mo in different videos; "Bank Nifty ~20%" vs exact 42,000→35,500). 61 event claims recorded (verify=true: 52).
5. **Leaks logged:** sponsor variants (5pisar/5paisa/5pisa.com, TaxBuddy/taxbeddy.com, Delta Exchange co-sponsor announcement), Vauld affiliation ("I have promoted this exchange"), son's crypto-options profit promo, Mangaay Foundation charity name, Chennai location hints, thumbnail/self-video references, name variants (PR Sunder, P. R. Sunder, P. S. Sundar), Kamal Haasan named mention.

## Teaching-asset highlights for the book
- Complete **FII-basket-raid pattern**: raid times cluster at 9:15 / 1:00 / 1:30 / 2:00 / 2:30 (0702, 0700) — strong Part II microstructure material.
- **Expiry-day rollover premium** adjustment before reading gaps (0695) — concrete numeric example (65pt premium → subtract ~40pts from the indicated gap).
- **Max-OI put strike − premium = seller breakeven floor** worked example (0700: 17,000PE @250-300 → 16,700-16,800 floor).
- **VIX regime ladder** in live use: <15 comfort (0681), >20 caution (0696), US >30 exit/invest (0705-0706) — feeds Part II ch.5.
- **"Two gangsters" FII-vs-DII tug-of-war metaphor** + retail-as-bystander (0701, 0703) — candidate recurring motif for Part II ch.4.
- **Panic-premium harvesting tell**: FIIs selling more puts than calls while net sellers = fear priced to fade (0701).
- **Blab-and-grab / pump-and-dump** market-manipulation taxonomy with Infosys-promoter anecdote (0690) — feeds Part II ch.6 or Part VII.
- **IPO anatomy case study**: Paytm (undersubscribed HNI → -27% debut → -40%), Star Health (79%), plus Infosys/Google undersubscription history (0682, 0683, 0706) — Part VII ch.26 material.

## Data issues
- 0692 has `fii_cr: null` for the session (data not published at recording time; cumulative 87,000cr claim captured as an event instead).
- 0682 Sapphire/Paytm same-day listing claim likely conflates two listings (Sapphire listed Nov 9, 2021) — flagged verify=true with note.
- Speaker's own cumulative FII figures vary across videos (50k vs 75k for Oct-Nov) — verification should reconcile against NSDL data.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 25 assigned transcripts (0677-0706) read in full and exactly one schema-valid JSON line each written to book/analysis/batch_daily_014.jsonl in order; python validation confirms 25/25 lines parse with required keys."
    }
  ],
  "changedFiles": [
    "book/analysis/batch_daily_014.jsonl",
    "book/analysis/outputs/daily_014_report.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python3 -c json-line validation of batch_daily_014.jsonl (parse + required-key assert)",
      "result": "passed",
      "summary": "25/25 lines valid, ids in order 0677-0706, 61 event claims, 52 marked verify=true"
    }
  ],
  "validationOutput": [
    "valid lines: 25, errors: []",
    "count: 25; order: 0677,0678,0679,0680,0681,0682,0683,0687,0688,0689,0690,0691,0692,0693,0694,0695,0696,0699,0700,0701,0702,0703,0704,0705,0706"
  ],
  "residualRisks": [
    "Speaker's cumulative FII-selling figures self-inconsistent across videos (50,000cr vs 75,000cr for Oct-Nov 2021) — needs reconciliation with NSDL data during Phase 3 verification",
    "Sapphire Foods vs Paytm listing-day conflation flagged in 0682 events",
    "ASR garbles (Hrithik stocks = heavyweights, NICA = Nykaa, Tiro Motocop = TVS Motor) resolved by context; residual risk low but Phase 3 should confirm Nykaa market-cap comparison"
  ],
  "noStagedFiles": true,
  "diffSummary": "Added structured analysis JSONL (25 records: summaries, index/flow levels, 61 verifiable event claims, lessons, cleaned quotes, leak logs) and this findings report; no other files touched.",
  "reviewFindings": ["no blockers"],
  "manualNotes": "Batch covers a full correction cycle (FII 6-week selling streak -> Paytm/farm-law crash -> Omicron shock -> Dec stabilization); leak log includes new sponsor variants (5pisar/5pisa.com) and Vauld affiliation disclosure worth adding to the book's banned-terms list."
}
```
