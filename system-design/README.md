# The Tradeoff Method: companion repository

Companion material for *The Tradeoff Method: System design interviews as decisions you can defend* by Avishek Nag (2026). The book teaches a five-move loop, frame, budget, axes, commit, stress, that turns any system design brief into a decision a candidate can defend under a clock, and runs twelve designs through it. This repository holds the things a reader uses alongside the book.

| Folder | What it holds |
|---|---|
| [`templates/`](templates/) | The four printable artefact sheets: brief sheet, envelope, tradeoff table, decision lines and stress. A4, one page each (`artefacts.pdf`), with the LaTeX source. |
| [`briefs/`](briefs/) | The twelve unworked briefs of Appendix B in Markdown, each split into a candidate's half and an interviewer's half, for solo practice or study groups. No solutions, by design. |
| [`rubrics/`](rubrics/) | Four mock-interview scoring sheets (senior, staff, AI-adjacent, migration) that score the five moves rather than the diagram. |
| [`toolkit/`](toolkit/) | The capacity toolkit: `capacity_toolkit.xlsx` (unit prices in one tab; envelope, latency budget, cost per thousand and backlog calculators) and `capacity.py`, a small Python module with the same calculators reading `prices.json`. |
| [`figures/`](figures/) | TikZ source for all 22 figures in the book, with a standalone preamble and a build script that renders each to PDF and PNG. |
| [`ERRATA.md`](ERRATA.md) | Corrections to the printed book, by printing. |

## Practising with this repository

1. Print `templates/artefacts.pdf`.
2. Pick a brief from `briefs/`. Read only the candidate's half.
3. Set a 45-minute timer and run the protocol in Chapter 15, filling the sheets as you go. Record yourself.
4. Score the recording against the matching sheet in `rubrics/`, writing the minute each artefact appeared.
5. In pairs, the interviewer holds the interviewer's half: the numbers given only if asked, three pushes for the questions block, and a twist at minute thirty.

## Updating the numbers

Every reference figure in the book is an order of magnitude checked in September 2026. Prices move faster than latencies. `toolkit/prices.json` and the *Unit prices* tab of the spreadsheet are the single place to change them; the calculators read from there.

## Building the figures

```
cd figures && ./build.sh
```

needs `pdflatex` with TikZ, Latin Modern and `adjustbox` (any full TeX Live has them). Output lands in `figures/out/`.

## Reporting a correction

Open an issue, or a pull request against `ERRATA.md`. Say the printing (on the copyright page) and the page.

## Licence

Text, briefs, rubrics and figures: CC BY-NC-SA 4.0. Code (`toolkit/capacity.py`, `build_toolkit.py`, `figures/build.sh`): MIT. See `LICENSE`.
