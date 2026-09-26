# D.4 Ad selection and auction

*Worked design · decided on **Objective** · Chapter 11*

Chapter 11's second design: the ML objective row says *calibrated* because the auction multiplies by money; hourly retrain on delay-corrected labels; a per-segment calibration layer; an exploration floor for new campaigns; the auction as a rule.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** (decides) | 'Calibrated, because the auction multiplies by money'; calibration error by segment as the offline proxy; the auction, pacing and the exploration floor as not ML problems; 'a segment ten per cent high is every advertiser in it overcharged by ten per cent.' | | |
| **Bound** | 300k req/s × 200 eligible = 60M scores/s; 20 ms; clicks in seconds, conversions days late; hourly retrain costing as much as serving — freshness as a wall. | | |
| **Binds** | Calibration and freshness together; latency and cost comfortable. | | |
| **Choose** | Calibration layer refit hourly per segment; hourly retrain with streaming ad counters; a bounded exploration boost sized by clicks; the delay correction for conversions; the auction as a rule. | | |
| **Deepen** | The calibration layer or the exploration floor worked with the overcharge arithmetic. | | |
| **Close the loop** | Calibration by segment hourly as the alarm; return on spend as the slow read; automatic revert on a calibration breach; click fraud fed to a filter ahead of the label. | | |
| **Recovery** | A segment overcharged: calibration first, then the segment scheme; a new campaign with no impressions: the floor, sized by clicks not impressions. | | |

**Numbers the marker should expect to hear:** 60M scores/s; 10 µs on cores → ~860 cores, a fifth on accelerators; 20 ms; hourly retrain; 1% click rate; $500k/day for a 10% high segment on 10M clicks.

**Red flags particular to this brief:** 'rank by pCTR' with no mention of calibration; learning the auction.
