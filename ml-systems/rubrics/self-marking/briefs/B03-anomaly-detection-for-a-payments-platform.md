# B.3 Anomaly detection for a payments platform

*Unworked brief · decided on **Bound** · Appendix B*

Be told within a minute when something is going wrong in the transaction flow.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Time to detect and page rate, read together; a page for nothing is the guardrail. | | |
| **Bound** (decides) | 10k tx/s across 200 merchants × 40 issuers × 30 countries; a few dozen incident labels, biased toward what was noticed; nights five times quieter. | | |
| **Binds** | The label: a few dozen labels are not a training set; the design is a forecast per segment with an alarm on the residual. | | |
| **Choose** | Segment forecasts with seasonality; a residual threshold set from the page budget; a rule for known patterns (Sunday's issuer). | | |
| **Deepen** | Segmentation and seasonality worked to the point where Sunday's issuer is explained. | | |
| **Close the loop** | Page rate as a guardrail; the alarm feeding the labels; how a missed incident would be found. | | |
| **Recovery** | 'The incidents we most want are unlabelled' answered without pretending to a classifier. | | |

**Numbers the marker should expect to hear:** 10k/s; 240k segment cells; a minute to detect; four pages a night as the failure.

**Red flags particular to this brief:** a supervised classifier on a few dozen labels.
