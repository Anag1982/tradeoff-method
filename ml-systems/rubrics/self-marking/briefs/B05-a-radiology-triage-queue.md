# B.5 A radiology triage queue

*Unworked brief · decided on **Close the loop** · Appendix B*

Scans that probably show an urgent finding are read first, without changing who reads them.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | The model changes the order, not the decision; asymmetric costs set the operating point; sensitivity by site as the suite. | | |
| **Bound** | 4k scans/day across 12 sites; 2% urgent; the label is the report, hours to days, complete; scanners differ by site. | | |
| **Binds** | The loop: automation bias and per-site drift, not compute. | | |
| **Choose** | A per-site calibrated model with a flag rate monitored per site; the operating point from the cost of a miss. | | |
| **Deepen** | The scanner replacement as drift: the flag rate halving overnight and the silent-failure row that catches it. | | |
| **Close the loop** (decides) | Automation bias (unflagged scans read less carefully) as the central feedback loop, measured; the regulator's audit trail. | | |
| **Recovery** | The new-population site answered with a shadow period and a per-site sensitivity gate. | | |

**Numbers the marker should expect to hear:** 4k/day; 80 reads per radiologist; 2%; 95% sensitivity 'at what FPR, on which site'.

**Red flags particular to this brief:** sensitivity quoted without a false-positive rate or a site.
