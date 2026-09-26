# Figures

TikZ source for the 24 figures in *The Tradeoff Method for ML Systems*. Each `fig-*.tex` is a bare `tikzpicture`; `preamble.tex` holds the packages, colours and the shared `archstyles` node styles the minute-fifteen diagrams use. `./build.sh` wraps each figure in a `standalone` document and writes a PDF and a 300-dpi PNG to `out/`.

| File | Figure | Chapter |
|---|---|---|
| fig-chain | 1.1 The chain a learned system is designed along | 1 |
| fig-roc | 2.1 Two fraud models on a zoomed false-positive axis | 2 |
| fig-moves | 3.1 The five moves for learned systems and the two return edges | 3 |
| fig-triangle | 4.1 The budget triangle, with freshness as the fourth axis | 4 |
| fig-labels | 5.1 Label delay on a timeline | 5 |
| fig-features | 6.1 The feature pipeline: offline, online and the served-feature log | 6 |
| fig-cascade | 7.1 The cascade and its stage sizes | 7 |
| fig-batching | 8.1 Throughput and latency against batch size | 8 |
| fig-staleness | 9.1 The staleness curve | 9 |
| fig-recsys | 10.1 The short-video recommender at minute fifteen | 10 |
| fig-feedrank | 10.2 The personalised feed at minute fifteen | 10 |
| fig-search | 11.1 Marketplace search at minute fifteen | 11 |
| fig-ads | 11.2 Ad selection at minute fifteen | 11 |
| fig-eta | 11.3 Delivery-time estimation at minute fifteen | 11 |
| fig-fraud | 12.1 Card fraud at minute fifteen | 12 |
| fig-moderation | 12.2 Content moderation at minute fifteen | 12 |
| fig-neardup | 12.3 Near-duplicate search at minute fifteen | 12 |
| fig-rag | 13.1 Enterprise assistant at minute fifteen | 13 |
| fig-agent | 13.2 The returns agent at minute fifteen | 13 |
| fig-platform | 13.3 The serving platform at minute fifteen | 13 |
| fig-memory | 13.4 The assistant with memory at minute fifteen | 13 |
| fig-consolidation | 14.1 Platform consolidation in five stages | 14 |
| fig-costmandate | 14.2 The inference bill by product, before and after | 14 |
| fig-clock-ml | 15.1 The forty-five-minute plan for a learned system | 15 |

The figures are drawn for a greyscale interior: one accent colour for the element the design turns on, three grey fills, nothing that depends on colour to be read.
