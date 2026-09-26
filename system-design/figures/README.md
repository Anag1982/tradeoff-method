# Figures

TikZ source for the 22 figures in *The Tradeoff Method*. Each `fig-*.tex` is a bare `tikzpicture`; `preamble.tex` holds the packages, colours and the shared `archstyles` node styles the architecture diagrams use. `./build.sh` wraps each figure in a `standalone` document and writes a PDF and a 300-dpi PNG to `out/`.

| File | Figure | Chapter |
|---|---|---|
| fig-loop | 1.1 The five-move loop | 1 |
| fig-feasible | 2.1 The feasible region | 2 |
| fig-latency-ladder | 4.1 The latency ladder | 4 |
| fig-axis | 5.1 One row of the tradeoff table | 5 |
| fig-attacks | 7.1 The stress move | 7 |
| fig-pricelist | 8.1 The consistency price list | 8 |
| fig-btree-lsm | 9.1 B-tree and LSM | 9 |
| fig-movement | 10.1 Three ways to move a byte | 10 |
| fig-costmoves | 11.1 The five cost moves | 11 |
| fig-feed | 12.1 Social feed | 12 |
| fig-chat | 12.2 Chat delivery | 12 |
| fig-ratelimiter | 12.3 Rate limiter | 12 |
| fig-video | 12.4 Video platform | 12 |
| fig-marketplace | 12.5 Marketplace | 12 |
| fig-notifications | 12.6 Notification service | 12 |
| fig-retrieval | 13.1 Retrieval service | 13 |
| fig-vector | 13.2 Vector search | 13 |
| fig-payments | 13.3 Payment state machine | 13 |
| fig-analytics | 13.4 Multi-tenant analytics | 13 |
| fig-migration | 14.1 Migration in five stages | 14 |
| fig-regions | 14.2 Multi-region data classes | 14 |
| fig-clock | 15.1 The minute plan | 15 |

The figures are drawn for a greyscale interior: one accent colour for the element the design turns on, three grey fills, nothing that depends on colour to be read.
