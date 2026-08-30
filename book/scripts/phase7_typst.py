#!/usr/bin/env python3
"""Convert manuscript.md to book.typ for Typst compilation."""
import re, os

MD = "/home/ubuntu/repos/prs_analysis/book/final/manuscript.md"
TYP = "/home/ubuntu/repos/prs_analysis/book/final/book.typ"

text = open(MD, encoding="utf-8").read()

# Headers
# # The Indian Market... (book title) → skip, will be titlepage
# # Part I: ... → = Part I: ... (level 1 for parts)
# # Chapter N: ... → == Chapter N: ... (level 2 for chapters)
# Part heading: note Part I: → stays level 1

# Replace
text = re.sub(r'^#\+', '#+-+', text)  # protect existing
text = re.sub(r'^# Part (.*)$', '= Part \\1', text, flags=re.MULTILINE)
text = re.sub(r'^# Chapter (\d+): (.*)$', '== Chapter \\1: \\2', text, flags=re.MULTILINE)

# Headings within chapters
text = re.sub(r'^## Themes$', '=== Themes', text, flags=re.MULTILINE)
text = re.sub(r'^## Lessons$', '=== Lessons', text, flags=re.MULTILINE)
text = re.sub(r'^## Strategies$', '=== Strategies', text, flags=re.MULTILINE)
text = re.sub(r'^## Market Mechanics$', '=== Market Mechanics', text, flags=re.MULTILINE)
text = re.sub(r'^## Verified Context$', '=== Verified Context', text, flags=re.MULTILINE)

# Level-4 headings
text = re.sub(r'^### (.*)$', '==== \\1', text, flags=re.MULTILINE)

# Replace --- with pagebreak
text = text.replace('\n---\n', '\n#pagebreak()\n')
text = text.replace('---\n', '#pagebreak()\n')
text = text.replace('\n---', '\n#pagebreak()')

# Bold/italic markers (keep as-is, Typst uses same * and _)
# JSON code blocks: wrap in ```typc? no, keep as raw text with mono font
# The JSON strategy blocks are currently in paragraph format starting with -
# They're bullet lists. That's fine.

# Sources line: *Sources: N transcripts* → italic
text = re.sub(r'\*Sources: (.*)\*', '_Sources: \\1_', text)

# Build full Typst document with template
template = """#import "@preview/tango:0.2.0": *

#set page(
  paper: ("6in", "9in"),
  margin: (top: 1in, bottom: 1in, left: 1in, right: 0.8in),
  numbering: "1",
  number-align: center,
)

#set text(font: "Noto Sans", size: 10pt)

#show heading.where(level: 1): it => [
  #pagebreak()
  #v(1em)
  #set text(size: 16pt, weight: "bold")
  #it
  #v(0.5em)
]

#show heading.where(level: 2): it => [
  #v(0.8em)
  #set text(size: 13pt, weight: "bold")
  #it
  #v(0.3em)
]

#show heading.where(level: 3): it => [
  #v(0.5em)
  #set text(size: 11pt, weight: "bold", style: "italic")
  #it
  #v(0.2em)
]

#show heading.where(level: 4): it => [
  #v(0.3em)
  #set text(size: 10pt, weight: "bold")
  #it
  #v(0.1em)
]

#show list: it => {
  it
  #v(0.1em)
}

#set par(justify: true, leading: 0.2em)

#align(center, text(size: 24pt, weight: "bold")[The Indian Market Trader's Handbook])
#v(0.5em)
#align(center, text(size: 14pt)[*By Dhanraj*])
#v(1em)
#align(center, text(size: 9pt, style: "italic")[_Compiled from trading education transcripts spanning 2018-2026_])
#pagebreak()

#show: tango.with-theme()
#set table(width: 100%)

{table.of-contents(title: [Contents])}
#pagebreak()

{content}
"""

# Content lines to indent lists properly in Typst
def indent_lists(t):
    """Indent sub-list items (not needed for Typst - it handles lists natively).
    Just return the text."""
    return t

content = indent_lists(text)

full = template.replace("{content}", content)

with open(TYP, "w") as fh:
    fh.write(full)

print(f"Written book.typ ({len(full)//1024}KB)")