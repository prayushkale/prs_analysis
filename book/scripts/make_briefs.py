#!/usr/bin/env python3
import json, re, glob, os
from collections import defaultdict, Counter

ROOT = "/home/ubuntu/repos/prs_analysis"
BRIEFS = f"{ROOT}/book/chapters/briefs"
os.makedirs(BRIEFS, exist_ok=True)

chap_lines = open(f"{ROOT}/book/editorial/chapter_map.md").read()
chapters = []
for line in chap_lines.split("\n"):
    if line.startswith("## PART "):
        current_part = line.strip()
    m = re.match(r"^(\d+)\.\s+\*\*(.+?)\*\*", line)
    if m:
        chapters.append({"num": int(m.group(1)), "title": m.group(2).strip(" *"), "part": current_part})

chapter_all = defaultdict(list)
print("Scanning analysis data...")
for f in sorted(glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl")):
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except: continue
        tgts = r.get("chapter_targets") or []
        for t in tgts:
            try: chapter_all[int(t)].append(r)
            except: pass

subtype_to_chapter = {
    "education_mission_options": [8, 9, 12],
    "options_education": [10, 11],
    "strategy": [13, 14, 15, 16, 17],
    "pnl_review": [3, 18],
    "qa_askprs": [1, 3],
    "inspiration": [1, 3],
    "education_why_no_trading": [1, 2],
    "crypto": [31],
    "earnings_trade": [18, 20],
    "budget": [19, 20],
    "election": [19, 20],
    "geopolitics": [21, 22],
    "regulation_scam": [26, 27],
    "taxation": [28],
    "investing": [29, 30],
    "outlook": [24, 25],
    "general": [1, 3],
}
daily_chapters = {"pre_market": [4, 5, 6, 7], "post_market": [4, 5, 7], "week_ahead": [6, 19]}

def cron_ch(y):
    if y <= 2020: return 22
    if y <= 2022: return 23
    if y <= 2024: return 24
    return 25

for f in sorted(glob.glob(f"{ROOT}/book/analysis/batch_*.jsonl")):
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except: continue
        if r.get("chapter_targets"): continue
        t = r.get("type","")
        if t in ("pre_market","post_market","weekly"):
            for ch in daily_chapters.get(t, []):
                chapter_all[ch].append(r)
            if r.get("events"):
                d = r.get("date","")
                y = int(d[:4]) if d and len(d) >= 4 else 2026
                chapter_all[cron_ch(y)].append(r)
        elif t == "special":
            sub = r.get("subtype","")
            for ch in subtype_to_chapter.get(sub, [1,3]):
                chapter_all[ch].append(r)

verified = {}
for f in glob.glob(f"{ROOT}/book/events/verified_batch_*.jsonl"):
    for line in open(f, encoding="utf-8"):
        try:
            ev = json.loads(line)
            verified[ev.get("idx", len(verified))] = ev
        except: pass
print(f"Verified events: {len(verified)}")

for c in chapters:
    n = c["num"]
    sources = chapter_all.get(n, [])
    if not sources:
        print(f"Ch{n:02d}: NO SOURCES")
        open(f"{BRIEFS}/ch{n:02d}.md", "w").write(f"# Ch{n:02d}: {c['title']}\n\nNo transcript sources mapped.\n")
        continue
    
    themes = Counter()
    lessons = []; events = []; quotes = []; enhance = []; strategies = []; levels = []
    src_types = Counter()
    for r in sources:
        src_types[r.get("type","?")] += 1
        for th in (r.get("themes") or []):
            if isinstance(th, str): themes[th] += 1
        for ls in (r.get("lessons") or []):
            if isinstance(ls, str) and len(ls) > 15: lessons.append(ls)
        for e in (r.get("events") or []):
            if isinstance(e, dict) and e.get("claim"): events.append(e["claim"][:120])
        for q in (r.get("quotes") or []):
            if isinstance(q, str): quotes.append(q)
        for en in (r.get("enhance") or []):
            if isinstance(en, str): enhance.append(en)
        for s in (r.get("strategies") or []):
            if isinstance(s, dict): strategies.append(s)
        lvls = r.get("levels") or {}
        for k,v in lvls.items():
            if v: levels.append(f"{k}={v}")

    ids = sorted(set(str(r.get("id","")) for r in sources if r.get("id")))
    top_themes = [t for t,_ in themes.most_common(10)]
    top_lessons = lessons[:6]
    top_quotes = quotes[:3]
    top_enhance = enhance[:6]

    brief = f"# Chapter {n:02d}: {c['title']}\n"
    brief += f"**Part:** {c['part'][:60]}\n"
    brief += f"**Transcripts:** {len(sources)} ({dict(src_types.most_common(5))})\n"
    brief += f"**Source IDs:** {', '.join(ids[:20])}\n"
    if themes:
        brief += f"**Top theme:** {top_themes[0] if top_themes else '?'} ({themes.most_common(1)[0][1]})  \n"
    
    if top_lessons:
        brief += "\n## Key Lessons\n"
        for ls in top_lessons: brief += f"- {ls[:120]}\n"
    
    if top_quotes:
        brief += "\n## Notable Quotes\n"
        for q in top_quotes: brief += f"- \"{q[:80]}\"\n"
    
    if strategies:
        brief += "\n## Strategies\n"
        for s in strategies[:3]:
            brief += f"- {s.get('name','?')}: {s.get('construction','')[:100]}  ({s.get('numbers','')[:80]})\n"
    
    if events:
        brief += f"\n## Event Claims (sample of {len(events)})\n"
        for ev in events[:5]: brief += f"- {ev[:100]}\n"
    
    if top_enhance:
        brief += "\n## Enhancements\n"
        for en in top_enhance: brief += f"- {en}\n"
    
    brief += f"\n## Write\n-~3-5K words\n-Use voice_guide.md\n-Mark unverified claims [VERIFY]\n-End: Key Takeaways box\n"
    open(f"{BRIEFS}/ch{n:02d}.md", "w", encoding="utf-8").write(brief)
    print(f"Ch{n:02d}: {len(sources)} src, {len(top_lessons)} lessons")

print(f"\nDone — {len(chapters)} briefs")