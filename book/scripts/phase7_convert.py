#!/usr/bin/env python3
"""Convert manuscript_full.md to Typst body with hardened escaping."""
import re

ROOT = "/home/ubuntu/repos/prs_analysis"
md = open(f"{ROOT}/book/final/manuscript_full.md").read()

md = re.sub(r"## Contents\n.*?(?=\n# Appendices\n|\n---\n)", "", md, flags=re.S)
md = re.sub(r"\*\*Appendices\*\*\n\n- A: Glossary\n- B: Strategy Quick Reference\n- C: Verified Market Timeline 2018–2026\n- D: Sources and Verification Notes\n- E: Correction Log\n\n", "", md)
md = re.sub(r"^# Appendices\n", "# APPENDICES\n", md, flags=re.M)

def esc(t: str) -> str:
    for ch in "[]#$@<>~'\"":
        t = t.replace(ch, "\\" + ch)
    return t

def inline(t: str) -> str:
    t = t.replace("\\", "\\\\")
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"#strong[\1]", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"#emph[\1]", t)
    t = t.replace("*", "\\*")
    return t

out = []
table_buf = []

def flush_table():
    global table_buf
    if not table_buf:
        return
    rows = [r for r in table_buf if not re.match(r"^\s*\|[\s:|-]+\|\s*$", r)]
    parsed = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    ncols = max(len(r) for r in parsed)
    out.append("#table(columns: (" + ",".join(["auto"] * ncols) + "), inset: 4pt, stroke: 0.4pt + rgb(\"#999\"), table.header(")
    for i, r in enumerate(parsed):
        cells = r + [""] * (ncols - len(r))
        if i == 0:
            out.append("  " + ",".join("[*" + inline(c) + "*]" for c in cells) + "),")
        else:
            out.append("  " + ",".join("[" + inline(c) + "]" for c in cells) + ",")
    out.append(")\n")
    table_buf = []

first_h1 = True
for ln in md.split("\n"):
    if ln.strip().startswith("|"):
        table_buf.append(ln)
        continue
    flush_table()
    s = ln.rstrip()
    if s.strip() == "---":
        out.append("#v(6pt)#line(length: 30%, stroke: 0.5pt + rgb(\"#888\"))#v(6pt)\n")
        continue
    if s.strip() == "":
        continue
    if s.startswith("# "):
        h = inline(s[2:])
        if first_h1:
            first_h1 = False
            continue
        if h.startswith("PART ") or h.startswith("APPENDICES"):
            out.append("\n#partpage[" + h + "]\n")
        else:
            out.append("\n#chapterpage[" + h + "]\n")
        continue
    if s.startswith("## "):
        out.append("\n== " + inline(s[3:]) + "\n")
        continue
    if s.startswith("### "):
        out.append("\n=== " + inline(s[4:]) + "\n")
        continue
    if s.startswith("> "):
        out.append("\n#quote(block: true)[" + inline(s[2:]) + "]\n")
        continue
    m = re.match(r"^(\s*)[-*]\s+(.*)", s)
    if m:
        out.append("  " * (len(m.group(1)) // 2) + "- " + inline(m.group(2)) + "\n")
        continue
    m = re.match(r"^\d+\.\s+(.*)", s)
    if m:
        out.append("+ " + inline(m.group(1)) + "\n")
        continue
    out.append(inline(s) + "\n")
flush_table()

body = "".join(out)
PRELUDE = """
#let partpage(body) = { pagebreak(); v(2.2in); align(center, text(size: 20pt, weight: "bold", tracking: 0.06em)[#body]); v(1fr) }
#let chapterpage(body) = { pagebreak(); v(1.2in); block(text(size: 15pt, weight: "bold")[#body]); v(1.2em) }
"""
body = PRELUDE + body

open(f"{ROOT}/book/final/build/body.typ", "w").write(body)
print("body.typ written:", len(body) // 1024, "KB")
