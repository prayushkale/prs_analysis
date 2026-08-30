#!/usr/bin/env python3
"""Phase 0: Extract all transcripts to text, build metadata.jsonl.
- Reads 3,288 files from 'PRS Data/' (2,366 .docx + 922 .txt)
- Extracts text (docx via zipfile + XML parse), normalizes mojibake
- Parses ids, dates, series types; detects duplicate numbers
- Writes book/corpus/ID.txt + book/meta/metadata.jsonl + reports
"""
import os, re, json, sys, zipfile
from xml.etree import ElementTree as ET

SRC = "/home/ubuntu/repos/prs_analysis/PRS Data"
OUT = "/home/ubuntu/repos/prs_analysis/book/corpus"
META = "/home/ubuntu/repos/prs_analysis/book/meta"

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

MOJIBAKE_MAP = {
    "Γé╣": "₹", "Γé╣": "₹", "ΓÇô": "-", "ΓÇö": "-", "ΓÇÖ": "'", "ΓÇ£": '"',
    "ΓÇ¥": '"', "ΓÇª": "...", "┬á": " ", "Γÿå": "", "Γÿ║": "", "Γÿ║": "",
    "ΓÇï": "", "ΓÇî": "", "ΓÇì": "", "Γüä": "/", "ΓêÖ": "*", "Γëñ": "<=", "ΓëÑ": ">=",
    "ΓëÑ": ">=", "Γëñ": "<=", "≡ƒÿé": "", "≡ƒöÑ": "", "≡ƒÿÇ": "", "≡ƒÿè": "", "≡ƒÿó": "",
    "≡ƒÿí": "", "ΓÖÑ": "", "ΓÖª": "", "ΓÖú": "", "ΓÖá": "", "ΓÇó": "-", "ΓÇ╣": "<", "ΓÇ║": ">",
    "ΓÇÜ": ",", "ΓÇ₧": '"', "ΓÇÿ": "'", "ΓÇô": "-", "ΓÇö": "-", "ΓÇÿ": "'", "ΓÇÖ": "'",
    "ΓÇ£": '"', "ΓÇ¥": '"', "Γé¼": "EUR", "┬ú": "GBP", "┬Ñ": "JPY", "┬⌐": "(c)",
    "┬«": "(r)", "┬░": "deg", "┬▒": "+/-", "├ù": "x", "├╖": "/", "ΓêÜ": "sqrt",
    "Γê₧": "in", "Γê₧": "in", "Γêæ": "sum", "Γê₧": "in", "Γê₧": "in", "Γê₧": "in", "Γê₧": "in",
    "Γê₧": "in", "Γê₧": "in", "Γê₧": "in", "Γê₧": "in", "Γê₧": "in", "Γê₧": "in", "Γê₧": "in",
}
# generic cleanup: strip leftover non-printable combos
GARBAGE_RE = re.compile(r"[\uFFFD]")
TRAIL_GARBAGE = re.compile(r"[≡ƒ╣][\u0000-\uffff]?")

def clean_text(t: str) -> str:
    for k, v in MOJIBAKE_MAP.items():
        t = t.replace(k, v)
    t = GARBAGE_RE.sub("", t)
    t = re.sub(r"[\u0300-\u036f]+", "", t)          # stray combining marks
    t = re.sub(r"[\u2028\u2029]+", " ", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

def docx_text(path: str) -> str:
    try:
        z = zipfile.ZipFile(path)
        xml = z.read("word/document.xml")
    except Exception as e:
        return f"[EXTRACTION ERROR: {e}]"
    try:
        root = ET.fromstring(xml)
    except Exception:
        # fall back to crude tag stripping
        raw = xml.decode("utf-8", "replace")
        raw = re.sub(r"<w:p[ >]", "\n<w:p ", raw)
        txt = re.sub(r"<[^>]+>", "", raw)
        return txt
    paras = []
    for p in root.iter(f"{W_NS}p"):
        parts = []
        for node in p.iter():
            tag = node.tag
            if tag == f"{W_NS}t":
                parts.append(node.text or "")
            elif tag == f"{W_NS}tab":
                parts.append("\t")
            elif tag == f"{W_NS}br":
                parts.append("\n")
        paras.append("".join(parts))
    return "\n".join(paras)

MONTHS = {m.lower(): i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
MONTHS.update({m.lower(): i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"])})

def parse_date(title: str):
    """Return (iso_date or None, week or None)."""
    t = title
    # DD-Mon-YYYY or DD-Mon-YY  (09-May-2022 / 06-May-21)
    m = re.search(r"\b(\d{1,2})[-\s]([A-Za-z]{3,9})[-\s](\d{4}|\d{2})\b", t)
    if m and m.group(2).lower()[:3] in MONTHS:
        d = int(m.group(1)); mon = MONTHS[m.group(2).lower()[:3]]
        y = int(m.group(3)); y = y + 2000 if y < 100 else y
        if 2018 <= y <= 2026:
            return f"{y:04d}-{mon:02d}-{d:02d}", None
    # DD_MM_YY or DD-MM-YYYY (02_11_18 / 11-05-2021) in a report title
    if re.search(r"(Pre|Post)[-\s]?Market Report", t, re.I):
        m = re.search(r"\b(\d{1,2})[_-](\d{1,2})[_-](\d{4}|\d{2})\b", t)
        if m:
            d = int(m.group(1)); mon = int(m.group(2))
            y = int(m.group(3)); y = y + 2000 if y < 100 else y
            if 1 <= mon <= 12 and 2018 <= y <= 2026:
                return f"{y:04d}-{mon:02d}-{d:02d}", None
    # Week Ahead: MONTH nth Week YEAR
    m = re.search(r"([A-Za-z]{3,9})\s+(\d)(?:ST|ND|RD|TH)?\s*Week\s*-?\s*(\d{4})", t, re.I)
    if m and m.group(1).lower()[:3] in MONTHS:
        return None, f"{MONTHS[m.group(1).lower()[:3]]:02d} week-{m.group(2)} {m.group(3)}"
    # 'Month nth Week Market Report'
    m = re.search(r"([A-Za-z]{3,9})\s+(\d)(?:ST|ND|RD|TH)?\s*Week\s+Market Report", t, re.I)
    if m and m.group(1).lower()[:3] in MONTHS:
        y = re.search(r"(20(1[89]|2[0-6]))", t)
        return None, f"{MONTHS[m.group(1).lower()[:3]]:02d} week-{m.group(2)} {y.group(1) if y else ''}"
    return None, None

def classify(title: str):
    t = title.lower()
    if "dalal street week ahead" in t or re.search(r"\d(st|nd|rd|th)? week (market report|week)", t):
        return "weekly", "week_ahead"
    if re.search(r"pre[-\s]?market report", t):
        return "daily", "pre_market"
    if re.search(r"post[-\s]?market report", t):
        return "daily", "post_market"
    # specials
    if re.search(r"mission options", t):
        return "special", "education_mission_options"
    if "why no to trading" in t:
        return "special", "education_why_no_trading"
    if "prsimpire" in t or "prsinspires" in t:
        return "special", "inspiration"
    if "askpr" in t.replace(" ", ""):
        return "special", "qa_askprs"
    if any(k in t for k in ["tax", "stt", "itr", "income tax", "presumptive", "advance tax", "gst"]):
        return "special", "taxation"
    if any(k in t for k in ["bitcoin", "crypto", "ethereum", "btc", "eth "]):
        return "special", "crypto"
    if any(k in t for k in ["earnings trade", "results trade", "q1 results", "q2 results", "q3 results", "q4 results", "buyback"]):
        return "special", "earnings_trade"
    if any(k in t for k in ["monthly review", "my trades", "p&l", "pnl", "annual performance", "profit "]) and ("trade" in t or "p&l" in t or "pnl" in t):
        return "special", "pnl_review"
    if "budget" in t:
        return "special", "budget"
    if any(k in t for k in ["election", "satta bazar", "bihar"]):
        return "special", "election"
    if any(k in t for k in ["war", "pakistan", "china", "ukraine", "russia", "border", "terror", "indo pak", "hamburg"]):
        return "special", "geopolitics"
    if any(k in t for k in ["scam", "fraud", "broker", "sebi", "regulat", "ban", "cheat", "loophole", "manipulation", "jane street", "penalty"]):
        return "special", "regulation_scam"
    if "ipo" in t or "offer for sale" in t or "rights entitlement" in t:
        return "special", "ipo"
    if any(k in t for k in ["real estate", "gold", "fd", "bond", "mutual fund", "reit", "invit", "etf", "insurance", "loan", "sip", "elss", "nps"]):
        return "special", "investing"
    if any(k in t for k in ["nifty", "bank nifty", "market outlook", "samvat", "bull", "bear", "crash", "rally", "ath", "all time high", "correction"]) and any(k in t for k in ["target", "outlook", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "nifty @", "nifty at", "nifty will", "nifty might", "k"]):
        return "special", "outlook"
    if any(k in t for k in ["strategy", "spread", "calendar", "ratio", "butterfly", "straddle", "strangle", "collar", "hedge", "covered call", "cash secured", "condor", "synthetic"]):
        return "special", "strategy"
    if any(k in t for k in ["option", "futures", "f&o", "greeks", "delta", "gamma", "vega", "theta", "iv ", "implied volatility", "open interest", "option chain"]):
        return "special", "options_education"
    return "special", "general"

EXCLUDE_PATTERNS = [
    (r"promo\b", "promo"), (r"teaser", "promo"), (r"announcing", "announcement"),
    (r"launching", "announcement"), (r"website launch", "announcement"),
    (r"final call", "announcement"), (r"update!?$", "announcement"),
    (r"webinar", "webinar_admin"), (r"membership", "announcement"),
    (r"charity dinner", "announcement"), (r"conclave", "announcement"),
    (r"conference\b.*\b(update|teaser|recap|launch)", "announcement"),
    (r"penthouse", "personal_luxury"), (r"mercedes", "personal_luxury"),
    (r"s-?class", "personal_luxury"), (r"dream car", "personal_luxury"),
    (r"#shorts", "short"),
    (r"how to (join|rewatch)", "webinar_admin"), (r"didn'?t get link", "webinar_admin"),
    (r"faq", "webinar_admin"), (r"refunds_", "webinar_admin"),
    (r"under sebi scanner", "self_referential"),
    (r"ran away to dubai", "self_referential"),
    (r"p r sundar'(s)? (workshop|company|2021|luxury)", "self_referential"),
    (r"my (dream car|son)", "personal"),
]

def firstpass_exclude(title: str):
    tl = title.lower()
    for pat, reason in EXCLUDE_PATTERNS:
        if re.search(pat, tl):
            return True, reason
    return False, None

def main():
    files = sorted(os.listdir(SRC))
    files = [f for f in files if f.lower().endswith((".docx", ".txt")) and f != ".DS_Store"]
    # group by numeric prefix to detect duplicate numbers
    groups = {}
    for f in files:
        m = re.match(r"^(\d+)\s*-\s*(.*)\.(docx|txt)$", f, re.I)
        if not m:
            print(f"UNPARSED: {f}")
            continue
        num = int(m.group(1))
        groups.setdefault(num, []).append(f)

    meta_rows = []
    errors = []
    for num in sorted(groups):
        flist = sorted(groups[num])
        for idx, f in enumerate(flist):
            m = re.match(r"^(\d+)\s*-\s*(.*)\.(docx|txt)$", f, re.I)
            title = m.group(2).strip()
            ext = m.group(3).lower()
            fid = f"{num:04d}" + (chr(ord("a") + idx) if len(flist) > 1 else "")
            path = os.path.join(SRC, f)
            if ext == "txt":
                with open(path, "r", encoding="utf-8", errors="replace") as fh:
                    raw = fh.read()
            else:
                raw = docx_text(path)
            if raw.startswith("[EXTRACTION ERROR"):
                errors.append((fid, f, raw[:100]))
            text = clean_text(raw)
            with open(os.path.join(OUT, f"{fid}.txt"), "w", encoding="utf-8") as fh:
                fh.write(text)
            iso, week = parse_date(title)
            series, subtype = classify(title)
            excluded, reason = firstpass_exclude(title)
            meta_rows.append({
                "id": fid, "num": num, "file": f, "title": title, "ext": ext,
                "date": iso, "week": week, "series": series, "subtype": subtype,
                "words": len(text.split()),
                "excluded_firstpass": excluded, "exclude_reason": reason,
            })

    with open(os.path.join(META, "metadata.jsonl"), "w", encoding="utf-8") as fh:
        for r in meta_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # stats
    from collections import Counter
    print(f"files: {len(files)}  corpus_written: {len(meta_rows)}  extraction_errors: {len(errors)}")
    print("series:", dict(Counter(r['series'] for r in meta_rows)))
    print("subtypes:", json.dumps(dict(Counter(r['subtype'] for r in meta_rows)), indent=1))
    print("dated:", sum(1 for r in meta_rows if r['date']), " week-only:", sum(1 for r in meta_rows if r['week']))
    print("firstpass_excluded:", sum(1 for r in meta_rows if r['excluded_firstpass']))
    yrs = Counter(r['date'][:4] for r in meta_rows if r['date'])
    print("by year:", dict(sorted(yrs.items())))
    tot = sum(r['words'] for r in meta_rows)
    print(f"total words: {tot:,}")
    if errors:
        print("ERRORS:", errors[:10])

if __name__ == "__main__":
    main()
