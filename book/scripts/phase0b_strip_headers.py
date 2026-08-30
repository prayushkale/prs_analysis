#!/usr/bin/env python3
"""Phase 0b: Strip identifying headers from corpus files; capture timestamps/video ids.
Header format (docx-derived only):
  <title line>
  <02 November 2018, 07:22:01 PM>
  Video ID: czyEVRwz1kA
"""
import os, re, json

CORPUS = "/home/ubuntu/repos/prs_analysis/book/corpus"
META = "/home/ubuntu/repos/prs_analysis/book/meta"

MONTHS = {m.lower(): i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"])}

HDR = re.compile(
    r"^(?P<title>.*)\n(?P<dt>\d{1,2}\s+[A-Za-z]{3,9}\s+\d{4},\s+\d{1,2}:\d{2}:\d{2}\s*[AP]M)\nVideo ID:\s*(?P<vid>\S+)\n")

def main():
    rows = [json.loads(l) for l in open(os.path.join(META, "metadata.jsonl"), encoding="utf-8")]
    by_id = {r["id"]: r for r in rows}
    stripped = 0
    dated_added = 0
    for fname in os.listdir(CORPUS):
        if not fname.endswith(".txt"):
            continue
        fid = fname[:-4]
        path = os.path.join(CORPUS, fname)
        text = open(path, encoding="utf-8").read()
        m = HDR.match(text)
        if not m:
            continue
        r = by_id.get(fid)
        dt = m.group("dt").replace(",", "")
        parts = dt.split()
        d = int(parts[0]); mon = MONTHS[parts[1].lower()]; y = int(parts[2])
        iso = f"{y:04d}-{mon:02d}-{d:02d}"
        vid = m.group("vid").strip()
        body = text[m.end():].lstrip()
        open(path, "w", encoding="utf-8").write(body)
        stripped += 1
        if r:
            r["video_id"] = vid
            r["publish_ts"] = iso
            r["words"] = len(body.split())
            if not r.get("date"):
                r["date"] = iso
                dated_added += 1
            r["header_stripped"] = True
    with open(os.path.join(META, "metadata.jsonl"), "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"headers stripped: {stripped}, undated->dated via header: {dated_added}")
    from collections import Counter
    yrs = Counter(r['date'][:4] for r in rows if r['date'])
    print("dated by year:", dict(sorted(yrs.items())))
    print("still undated:", sum(1 for r in rows if not r.get('date')))

if __name__ == "__main__":
    main()
