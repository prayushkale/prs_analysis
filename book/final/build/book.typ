// book.typ — 6"x9" print book template
#let smallcaps-caps(t) = upper(t)

#set page(width: 6in, height: 9in, margin: (top: 0.8in, bottom: 0.85in, left: 0.8in, right: 0.75in), numbering: "1", footer: context {
  set text(size: 8pt, fill: rgb("#444"))
  align(center, counter(page).display("1"))
})
#set text(font: "Libertinus Serif", size: 9.5pt, lang: "en")
#set par(justify: true, leading: 0.62em)
#set heading(numbering: none)

#show heading.where(level: 1): it => { pagebreak(weak: true); v(2em); text(size: 16pt, weight: "bold")[#it.body]; v(1em) }
#show heading.where(level: 2): it => { v(0.9em); text(size: 12pt, weight: "semibold")[#it.body]; v(0.4em) }
#show heading.where(level: 3): it => { v(0.7em); text(size: 10.5pt, weight: "semibold", style: "italic")[#it.body]; v(0.3em) }
#show quote.where(block: true): it => {
  set text(size: 9pt, style: "italic", fill: rgb("#333"))
  pad(left: 0.3in, right: 0.3in, it.body)
  v(0.4em)
}
#show table: set text(size: 8pt)
#show link: set text(fill: rgb("#1a4b8c"))

#let partpage(body) = {
  pagebreak()
  v(2.2in)
  align(center, text(size: 20pt, weight: "bold", tracking: 0.06em)[#body])
  v(1fr)
}

#let chapterpage(body) = {
  pagebreak()
  v(1.2in)
  block(text(size: 15pt, weight: "bold")[#body])
  v(1.2em)
}

// ---------- TITLE PAGE ----------
#v(2in)
#align(center)[
  #text(size: 26pt, weight: "bold")[The Discipline of Markets]
  #v(0.3in)
  #text(size: 12.5pt, style: "italic")[A Trader's Education from Two Decades of Indian Market Cycles]
  #v(1.2in)
  #text(size: 14pt, weight: "semibold")[Dhanraj]
]
#pagebreak()

// ---------- COPYRIGHT / DISCLAIMER ----------
#set text(size: 8.5pt)
#align(center)[
  #v(2.6in)
  #pad(left: 0.5in, right: 0.5in)[
    This book is a work of synthesis compiled from public market commentary, presented under a pseudonym. Nothing in this book is investment advice or a recommendation to buy or sell any security. Rupee figures attributed to personal experience are illustrative recollections, not audited results. Markets involve substantial risk of loss. Consult a registered financial adviser before acting on any idea in this book.

    #v(0.4in)
    Market events described herein were verified against public records; corrections to the original commentary are logged in Appendix E.
  ]
]
#pagebreak()

// ---------- PREFACE ----------
#chapterpage[Preface]
#pagebreak(weak: true)

// ---------- OUTLINE ----------
#outline(title: [Contents], depth: 1, indent: auto)

// ---------- BODY ----------
#include "body.typ"
