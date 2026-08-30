# Verification Report — verified_batch_078 (10 claims)

**Method:** Daily OHLC from Yahoo Finance chart API (`^NSEI`, `^NSEBANK`, `^GDAXI`, `^FCHI`, `BZ=F`, `GC=F`, `ADANIENT.NS`, `INFY.NS`, `TCS.NS`, `HDFCBANK.NS`, `RELIANCE.NS`, `KOTAKBANK.NS`) + Google News RSS corroboration (ET, Livemint, The Hindu, TOI, Moneycontrol, Business Standard). Results written to `book/events/verified_batch_078.jsonl`.

## Verdicts at a glance
| # | Claim (abbrev.) | Verdict |
|---|---|---|
| 1 | Jun-2021 15,800 short straddle 550→20 | **verified** (market context confirmed; premiums are author's records) |
| 2 | Bank Nifty +820 pts, 4-Aug-2021 | **verified** (+820.60 pts; A/D ratio unverifiable) |
| 3 | 29-Mar-2022: EU +3%, Brent -5.5%→~$103.5, gold <$1,900 | **corrected** (EU ✓; Brent -2% to ~$110; gold closed $1,912) |
| 4 | Adani Ent. ~1,550→~2,200 (~40-50%) | **corrected** (magnitude ✓; base low was late-Feb/Mar-7, not mid-March) |
| 5 | Nifty short 19,500 → ~₹60k loss/lot | **verified** (20,686.80 close; 1,187 pts × ₹50 = ₹59,340 ≈ 50% of ₹1.2L) |
| 6 | Heavyweights ~10% below ATH (Dec-2023) | **corrected** (actual 2–12%, avg ~6–7%; Infosys ATH figures off) |
| 7 | 21-Jul-2025: broke 24,970, rallied 200+ | **verified** (low 24,882.3, close +208.4 from low; stock contributions unverified) |
| 8 | 24-Jul-2025 tariff-day: fell 200+, closed +22 | **corrected** (fell 224 intraday BUT closed -158 at 25,062; Bank Nifty -144) |
| 9 | 18-Aug-2025: gap ~300, crossed 25k, fell ~200 | **corrected** (gap +307 ✓, durables ✓; 25k cross uncertain; pullback ~75–145) |
| 10 | FII +₹550 cr Aug-18, Adani block; -₹1,000 cr Aug-19 | **unverifiable** (no corroboration found) |

## Key evidence notes
- **Claim 8 (most material):** Livemint, 24-Jul-2025: "Sensex drops 542 points, Nifty ends at 25,062" — cross-confirms Yahoo close 25,062.1. The claimed "+22 close / +110 Bank Nifty" inverts the actual direction. "Lowest since May 12" also contradicted (18-Jul-2025 low 24,918.7; 12-May-2025 low 24,378.9).
- **Claim 9:** ET/TOI: "Sensex settles 676 pts higher, Nifty tops 24,850" (close 24,876.95 per Yahoo ✓). The Hindu put the Aug-18 high at 24,953.50 vs Yahoo 25,022.00 — "crossed 25,000" flagged uncertain. Livemint (20-Aug): "Nifty reclaims 25,000 after nearly a month" supports no sustained 25k close on Aug-18.
- **Claim 6:** Kotak's Yahoo series appears split-adjusted in absolute level, so only its relative drawdown (−11.8%) was used; Infosys Dec-6 close 1,474.3 (<1,500 ✓) but 2023 high 1,619.75 (not 1,700+) and all-time high ~1,950 (Jan-2022).
- **Claim 10:** No searchable record of the specific FII cash prints for 18/19-Aug-2025 or an Adani Ports block on 18-Aug-2025; marked unverifiable, not wrong.

## Files
- Data written: `book/events/verified_batch_078.jsonl` (10 records, jsonl-validated below)
- Report: this file (`book/events/outputs/ver_078_report.md`)