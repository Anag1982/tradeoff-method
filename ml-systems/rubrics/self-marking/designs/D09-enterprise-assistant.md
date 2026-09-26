# D.9 Enterprise assistant over company documents

*Worked design · decided on **Bound** · Chapter 13*

Chapter 13's first design, Chapter 1's support assistant at 20M documents with permissions: the clause 'among the passages this user may read' is the design; the index snapshot filters, the source of truth decides.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | The ML objective's clause 'among the passages this user may read'; supported-claim rate on a judged set with a model judge audited weekly; leak rate zero on a red-team set; abstention not rising silently. | | |
| **Bound** (decides) | 200k questions/day, 20/s; 2 s first token split (500 ACL lookups in 200 ms); 60M chunks, 46 GB of vectors, ~100 GB indexed; no label — a 2,000-question judged set; revocations enforced at the next question. | | |
| **Binds** | Permissions as a wall, not a vertex; quality without a label is what the design buys. | | |
| **Choose** | Per-source keyword + vector indexes; over-fetch 500 and filter against the source of truth with an ACL cache of minutes; 500-token chunks with headers; the judged set and audit; tenancy on the platform; quality as the open vertex. | | |
| **Deepen** | The permission arithmetic (Exercise 13.1): over-fetch works above f ≈ 4%, scope-and-scan below ~0.7%, and the unsolved middle needs a per-group index. | | |
| **Close the loop** | Leak rate from a synthetic account that owns nothing, continuously; ACL cache age; the judge drifting lenient; employees asking the assistant instead of writing documents, watched by source coverage. | | |
| **Recovery** | 'Put the ACL in the index': the snapshot filters, the source decides; the contractor with 1,000 documents: scope and scan; 'how do you know it is right': the judged set, not thumbs. | | |

**Numbers the marker should expect to hear:** 60M chunks; 500 candidates; f = 5% → 25 permitted; k = 20/f; 750 ms scan at 3M chunks; 11 accelerator-hours a day.

**Red flags particular to this brief:** post-filtering the top 20; thumbs as the metric; a single global vector index.
