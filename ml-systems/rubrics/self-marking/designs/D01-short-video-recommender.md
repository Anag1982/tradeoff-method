# D.1 Short-video recommender

*Worked design · decided on **Objective** · Chapter 10*

Chapter 10's flagship design, assembled from Chapters 1–8: four merged candidate sources, a two-head-plus ranker with a hide negative, a session stream, guardrails as filters and slots, an hourly index with a live index for new clips.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** (decides) | Names time in app as the proxy that would eat the objective (retention); four heads per user–clip pair with a hide negative; the harmful category as a filter, never a head; the connected floor as a slot. | | |
| **Bound** | A thousand requests a second at peak; 200 ms for the cascade; a billion implicit labels a day with a randomised one per cent; hourly item vectors and a live index; the ranker fleet from 2 µs a candidate batched. | | |
| **Binds** | Latency at the corpus forces the cascade; the feedback loop forces the randomised slice; cost is comfortable and labels are plentiful — said before any model. | | |
| **Choose** | Four merged sources to two thousand, ranked to a hundred, re-ranked to ten; cost as the open vertex; the decision line with the single-watch-time head as the rejected alternative. | | |
| **Deepen** | The feedback loop worked: the ranker learns its own positions, the slice sizes the correction, the staleness of hourly vectors against the session stream; the slice's cost in watch-through derived. | | |
| **Close the loop** | Shipping rule first; the connected floor and publisher share on the same page as return; the live index lagging uploads as the silent failure; the position loop in the feedback row; the category filter measured weekly. | | |
| **Recovery** | The new-user push answered with the popular slice and a new-user row in the suite; the small-app push answered by shrinking the cascade, not the heads. | | |

**Numbers the marker should expect to hear:** 1,000 req/s peak; 2,000 candidates → 100 → 10; 2 µs per candidate batched; 1% randomised slice; hourly index; 200 ms.

**Red flags particular to this brief:** a single watch-time head; the floor as a penalty; 'a two-tower' before the objective sheet.
