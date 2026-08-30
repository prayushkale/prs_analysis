#!/usr/bin/env python3
"""Generate .typ file from manuscript.md with 6x9 book layout."""
import re, os

MAN = "/home/ubuntu/repos/prs_analysis/book/final/manuscript.md"
TYP = "/home/ubuntu/repos/prs_analysis/book/final/book.typ"

text = open(MAN).read()

# Extract title from YAML front matter
title = "The Dhanraj Book"
subtitle = "Markets, Options, and the Trader's Edge"
author = "Dhanraj"

# Remove YAML front matter
text = re.sub(r"^---\n.*?\n---\n", "", text, 1, re.DOTALL)

# Split into sections by part structure
lines = text.split("\n")

typ_parts = []
# Prepend book template
typ_parts.append(r"""#let page-size = "6in x 9in"
#set page(paper: page-size, margin: (top: 0.8in, bottom: 0.8in, left: 0.9in, right: 0.7in), numbering: "1", number-align: center)
#set text(font: ("Noto Sans", "DejaVu Sans"), size: 10pt, leading: 0.35em)
#set heading(numbering: "1.1")

#align(center)[#text(size: 24pt, weight: "bold")[The Dhanraj Book]]
#align(center)[#text(size: 16pt)[Markets, Options, and the Trader's Edge]]
#align(center)[#text(size: 12pt)[Dhanraj — August 2026]]
#pagebreak()

#set heading(numbering: "1.1.1")
""")

for line in lines:
    if line.startswith("---") and "Appendix" not in line:
        continue
    if line.startswith("# The Dhanraj Book"):
        continue
    if line.startswith("## Disclaim"):
        typ_parts.append(r"\*Disclaimer\* This book is compiled from educational trading transcripts. All profit/loss figures cited are genericized illustrations. Nothing in this book constitutes financial advice.")
        typ_parts.append("")
        continue
    if line.startswith("## Preface"):
        typ_parts.append("# Preface\n\nThis book distills thousands of hours of market commentary and trading education — daily market reports, weekly previews, and in-depth strategy sessions spanning 2018 to 2026. The material has been organized into thematic chapters, verified against web sources for factual accuracy, and enhanced with worked examples where complex topics arise.")
        typ_parts.append("")
        continue
    if line.startswith("## Contents"):
        typ_parts.append("")
        typ_parts.append("# Table of Contents")
        typ_parts.append("#lorem(10)")  # placeholder
        typ_parts.append("#pagebreak()")
        continue
    if line.startswith("## Chapter"):
        # Extract chapter number and title
        m = re.match(r"^## Chapter (\d+):\s*(.*)", line)
        if m:
            cn = m.group(1)
            ct = m.group(2).strip()
            typ_parts.append(f"= Chapter {cn}: {ct}")
            typ_parts.append("")
        continue
    if line.startswith("### "):
        typ_parts.append(f"== {line[4:].strip()}")
        typ_parts.append("")
        continue
    if line.startswith("*Chapter"):
        continue
    if line.startswith("---"):
        continue
    if line.strip() == "":
        typ_parts.append("")
        continue
    
    # Regular paragraph
    stripped = line.strip()
    if stripped.startswith("- ") and not stripped.startswith("- ["):
        typ_parts.append(stripped)
    elif stripped.startswith("- ["):
        typ_parts.append(stripped)
    elif stripped.startswith("*"):
        typ_parts.append(stripped)
    elif stripped.startswith(">"):
        typ_parts.append(stripped)
    else:
        typ_parts.append(stripped)

with open(TYP, "w") as f:
    f.write("\n".join(typ_parts))

print(f"Written: {TYP} ({os.path.getsize(TYP)} bytes)")