# D.12 The assistant with memory

*Worked design · decided on **Objective** · Chapter 13*

Chapter 13's fourth design, the smallest with the most walls: a small gated extractor once per session, distilled versioned facts, a 500-token read cap, user-visible deletion as a wall, memory never training data.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** (decides) | Two decisions (what to write; what to read); the three walls said as walls; 'recalling another user's memory, never: the store is keyed by user'; wrong-recall rate under a ceiling. | | |
| **Bound** | 20M sessions/day; 14 accelerators of extraction in the batch lane; 500 memory tokens = a sixth of the fleet at peak; under a terabyte sharded by user; a 20-ms read in the feature fetch. | | |
| **Binds** | Harm in three walls and the wrong-recall ceiling; then cost, because memory is tokens on every request. | | |
| **Choose** | Write after the session, not every turn; facts, not raw turns; small gated extractor; profile plus five capped at 500 tokens with age; newer supersedes; deletion as a wall; never training data; cost as the open vertex. | | |
| **Deepen** | The two bills and the precision arithmetic (Exercise 13.4): per-turn is 140 accelerators; 0.95⁵ → 23% of requests carry a wrong memory. | | |
| **Close the loop** | Cross-user recall tested with paired synthetic accounts, zero tolerated; a forbidden entry found by the classifier is an incident; a wrong recall recalled with confidence hides the correction signal — the audit is the backstop; bad extractor entries quarantined by version. | | |
| **Recovery** | 'Twenty sessions in the prompt': the whole fleet several times over; 'what does a deletion do': the entry, the summaries, the caches, and nothing else because nothing is trained; a fact about a colleague: not stored unless asked, and under the same list. | | |

**Numbers the marker should expect to hear:** 14 vs 140 accelerators; 10 vs 40 accelerators for 500 vs 2,000 tokens; 99% precision for five memories under 5%; deletion within a day.

**Red flags particular to this brief:** storing raw turns; extracting every turn; fine-tuning on memory.
