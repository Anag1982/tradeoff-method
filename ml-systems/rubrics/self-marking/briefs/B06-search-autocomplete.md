# B.6 Search autocomplete

*Unworked brief · decided on **Bound** · Appendix B*

Suggestions under a search box as the user types.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Selection as the proxy; the blocklist as a wall; freshness for trending prefixes as a second objective. | | |
| **Bound** (decides) | 20k keystrokes/s; 50 ms; 10M queries cover 90%; a third of prefixes unseen; hourly change on news days. | | |
| **Binds** | Latency at the keystroke: a precomputed structure for the head and a cheap model for the tail. | | |
| **Choose** | A trie or similar for the head, a small model for the tail, a fast path for trending prefixes, the blocklist reviewed. | | |
| **Deepen** | The head/tail split priced, and the personalisation twist on the same 50 ms. | | |
| **Close the loop** | Suggestions shown are the ones selected — the feedback row; the offensive-suggestion push as the harm row with its review loop. | | |
| **Recovery** | The trending celebrity answered by the fast path and its staleness bound. | | |

**Numbers the marker should expect to hear:** 20k/s; 50 ms; 10M head queries; a third unseen prefixes.

**Red flags particular to this brief:** one model for every prefix on 50 ms; no blocklist.
