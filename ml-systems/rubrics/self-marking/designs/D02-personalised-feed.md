# D.2 Personalised feed

*Worked design · decided on **Close the loop** · Chapter 10*

Chapter 10's second design, on Volume 1's fan-out store: time in app explicitly not the objective; four heads with a hide negative; the connected floor; post-time classifiers with early counters.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Says time in app is not the objective and why; four heads with hide as a negative; 'a missed harmful category is fixed in the filter, never by a penalty term.' | | |
| **Bound** | 300 ms at p99 with 100 candidates from the fan-out store; posts rankable five minutes after publication; labels from actions on the feed, biased by position. | | |
| **Binds** | The objective and the feedback loop bind; compute does not, because Volume 1 already built the store. | | |
| **Choose** | Value model over the four heads with the floor as a slot and source mix as a re-rank rule; post-time classifiers plus early counters for cold posts. | | |
| **Deepen** | The position loop or the post-time classifiers worked with their numbers and failure. | | |
| **Close the loop** (decides) | The connected floor as a slot; the position loop named in the feedback row; harmful category missed → fix the filter; ranker versioned with its heads; canary by user. | | |
| **Recovery** | Growth wants time in app: the candidate says which guardrail it eats and keeps the objective; a harmful post shown: the filter, not the model, is changed. | | |

**Numbers the marker should expect to hear:** 100 candidates per load; 300 ms p99; five-minute post freshness; four heads.

**Red flags particular to this brief:** adding a penalty for the harmful category; time in app as the objective.
