# B.11 A feature platform for one company

*Platform brief · decided on **Bound** · Appendix B*

Thirty models read features at serving time and train from them, and a feature must mean the same thing in both places.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Point-in-time correctness as the product; skew incidents as the objective. | | |
| **Bound** (decides) | 2,000 features, 20 streaming; 500M entities; 10k reads/s at 15 ms batched; label delays from hours to months set the log's retention. | | |
| **Binds** | Point-in-time correctness and the served-feature log. | | |
| **Choose** | Tiers by window; one batched read with defaults; the log as training rows; versioned definitions. | | |
| **Deepen** | The log's retention from the longest label delay and its size; the restart check for streaming counters. | | |
| **Close the loop** | The skew monitor as the platform's own loop sheet: per-feature comparison, null-rate alarm, restart check. | | |
| **Recovery** | The LLM-computed feature at a cent per entity priced against 500M entities before being accepted. | | |

**Numbers the marker should expect to hear:** 10k reads/s; 15 ms; 20 streaming features; a cent × 500M.

**Red flags particular to this brief:** everything on the stream; time-travel joins for every model.
