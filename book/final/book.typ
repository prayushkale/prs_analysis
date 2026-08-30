#set page(
  width: 6in, height: 9in,
  margin: (top: 0.9in, bottom: 0.8in, left: 0.85in, right: 0.75in),
  numbering: "1",
)

#set heading(numbering: (..n) => {
  if n.len() == 0 { " " }
  else if n.len() == 1 { numbering("1", ..n) + ". " }
  else { numbering("1.1", ..n) + " " }
})
#set text(font: "Libertinus Serif", size: 10.5pt)
#set par(leading: 0.35em, justify: true)



= DHANRAJ
#align(center)[
  #text(size: 11pt)[_A Trader's Education: Eight Years of Indian Markets, 2018-2026_]
]

---

*Disclaimer:* The contents of this book are presented for educational and informational purposes only. Trading in futures and options involves substantial risk of loss. All trading anecdotes, P&L figures, and personal stories are presented as illustrative examples and do not represent guaranteed results. This book does not constitute investment advice.

---

== Contents

- Part I: The Trader's Mind (Chapters 1-3)
- Part II: How This Market Works (Chapters 4-7)
- Part III: Options from First Principles (Chapters 8-12)
- Part IV: The Strategy Library (Chapters 13-18)
- Part V: Trading the Events (Chapters 19-21)
- Part VI: A Market Chronicle, 2018-2026 (Chapters 22-25)
- Part VII: Predators and Protectors (Chapters 26-28)
- Part VIII: Wealth Beyond the Screen (Chapters 29-31)
- Appendices A-E

---

#include "book_as_typst.typ"

---

#align(center, text(size: 9pt, fill: luma(130))[
  *DHANRAJ -- A Trader's Education*
  Compiled from public market educational resources.
  Not investment advice.
])