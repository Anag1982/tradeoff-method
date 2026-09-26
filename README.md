# The Tradeoff Method for ML Systems: companion material

Companion material for *The Tradeoff Method for ML Systems: Machine learning and GenAI system design interviews* by Avishek Nag (2026), the second volume of the Tradeoff Method. The book teaches five moves, name the objective, bound the problem, find what binds, choose under it, close the loop, that turn any ML or GenAI design brief into a decision a candidate can defend under a clock, and runs fourteen designs through them. This directory holds the things a reader uses alongside the book. It sits beside the Volume 1 material in the same repository.

| Folder | What it holds | Status |
|---|---|---|
| [`templates/`](templates/) | The five printable artefact sheets (objective sheet, envelope, tradeoff table with the budget triangle, decision line and diagram, loop sheet) and the two sheets of Chapter 15's mock protocol (timing sheet, self-scoring sheet). A4, one page each (`artefacts.pdf`), with the LaTeX source. | ready |
| [`briefs/`](briefs/) | The twelve unworked briefs of Appendix B in Markdown, each split into a candidate's half and an interviewer's half. No solutions, by design. | ready |
| [`figures/`](figures/) | TikZ source for all 24 figures in the book, with a standalone preamble and a build script that renders each to PDF and PNG. | ready |
| `rubrics/` | The senior and staff rubrics of Chapter 16, the applied-scientist and platform variants, the red-flag list, and the fourteen self-marking sheets for the designs of Part III with every row filled in. | to come |
| `toolkit/` | The cost-and-capacity toolkit for ML serving: a spreadsheet and a Python module reading one price file — fleet from QPS on cores or accelerators, cascade stage sizing, prefill and decode fleets from the memory-bound arithmetic, token cost with prefix caching, own-against-rent break-even, index sizing, retraining cost by cadence, served-feature log size from label delay. | to come |
| `evaluation/` | The evaluation harness templates: an offline suite skeleton by slice, the judged-set and A/B sizing calculator, and a model-as-judge template with its failure checklist and weekly calibration. | to come |
| [`ERRATA.md`](ERRATA.md) | Corrections to the printed book, by printing. | — |

## Practising with this material

1. Print `templates/artefacts.pdf`.
2. Pick a brief from `briefs/`. Read only the candidate's half.
3. Set a 45-minute timer and run the protocol in Chapter 15, filling the sheets in order. Say nothing about a model before the envelope is complete.
4. Have a partner hold the timing sheet and write down the minute each artefact was finished and the minute a model was first named; write your own guesses before you look.
5. Score the run on the self-scoring sheet against Chapter 16's rubric, both of you, and compare row by row. The row that decides the brief is named in its rubric notes.

## Updating the numbers

The book prints quantities and ratios, never prices. Prices live in one place, the toolkit's price file, and the calculators read from there.

## Building the figures

```
cd figures && ./build.sh
```

needs `pdflatex` with TikZ, Latin Modern and `adjustbox` (any full TeX Live has them). Output lands in `figures/out/`.

## Reporting a correction

Open an issue, or a pull request against `ERRATA.md`. Say the printing (on the copyright page) and the page.

## Licence

Text, briefs, rubrics, templates and figure sources: CC BY-NC-SA 4.0. Code: MIT. See `LICENSE`.
