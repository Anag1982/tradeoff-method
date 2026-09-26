# D.3 Marketplace search

*Worked design · decided on **Bound** · Chapter 11*

Chapter 11's first design, assembling Chapter 7's cascade: purchase label with position-corrected clicks beneath, query understanding, merged keyword and vector retrieval, a head cache, a cross-encoder re-ranker carrying the new-seller floor.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Revenue per search subject to the customer finding what they asked for; purchases with clicks as a weak position-corrected signal; zero-result rate and new-seller share as guardrails; prohibited listings as an indexing-time filter. | | |
| **Bound** (decides) | 30k queries/s with a third served by a head cache; 60 ms at p99 split across five stages; purchases one to two per cent of clicks, so sparse; a randomised slice; 50M listing vectors at 13 GB; the re-ranker as half the accelerator bill. | | |
| **Binds** | Latency at the corpus and the label (sparse purchases, biased clicks); the re-ranker is the first thing to cut if the fleet binds. | | |
| **Choose** | Query understanding ahead of merged retrieval; head cache at a ten-minute TTL with the live index merged on read; re-ranker over forty with the seller slot; cost as the open vertex. | | |
| **Deepen** | The label: position propensities from the randomised slice and inverse-propensity weights with a cap; or the cascade's stage sizes from the budget. | | |
| **Close the loop** | Interleaving to choose the candidate, then a two-week A/B on revenue per search; recall on the tail as its own line; sellers learning the ranker watched by the spam guardrail. | | |
| **Recovery** | 'Throwing away 99% of labels': clicks kept as a weak signal, checked on the slice; the typo query: spelling correction then the vector index, measured on the tail slice. | | |

**Numbers the marker should expect to hear:** 30k QPS; 20k reach the cascade; 60 ms; 1,000 candidates at 2 µs; 40 pairs at 0.5 ms; 13 GB of vectors; 500 GB/day impression log.

**Red flags particular to this brief:** a click ranker on raw queries; NDCG on held-out clicks without position correction.
