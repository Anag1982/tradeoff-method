# B.2 Churn with an intervention

*Unworked brief · decided on **Objective** · Appendix B*

Predict who will cancel next month and offer some of them a discount.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** (decides) | Whom to offer, not who will churn: uplift, not probability; the two need different labels; a held-out group with no offer as the only measurement. | | |
| **Bound** | 20M subscribers, 3% churn, 200k offers a month, a discount worth a month's revenue; labels at month end; compute irrelevant. | | |
| **Binds** | The label's monthly cadence and the intervention's effect on it. | | |
| **Choose** | An uplift model with a randomised holdout; region removed as a feature and audited as a group. | | |
| **Deepen** | The return on the programme from uplift × offers − discount cost, with the holdout's price. | | |
| **Close the loop** | The offer changes next month's training set; the holdout kept forever; false discounts measured. | | |
| **Recovery** | Legal's region constraint answered as a harm row with a measurement by group. | | |

**Numbers the marker should expect to hear:** 600k churners a month; 200k offers; 12% precision at the top.

**Red flags particular to this brief:** precision of churn prediction as the metric; no holdout.
