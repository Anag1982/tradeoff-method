# D.5 Delivery-time estimation

*Worked design · decided on **Objective** · Chapter 11*

Chapter 11's third design, Chapter 2's quantile in full: one predicted distribution read twice — a high quantile before the order, the smoothed median during tracking — decomposed per stage, with the shown-time feedback loop.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** (decides) | 'Search is a position, ads a probability, delivery a promise'; the quantile derived from the cost of late against the cost of slow; two surfaces, two readings of one distribution. | | |
| **Bound** | Per-stage labels (kitchen, pickup, travel) within the hour; streaming load features; compute irrelevant — one machine. | | |
| **Binds** | The objective binds: which number to show; nothing else is close. | | |
| **Choose** | Per-stage quantile model over the routing engine's travel time; 80th percentile shown pre-order, smoothed median live; pooling for new restaurants. | | |
| **Deepen** | The feedback loop: kitchens and couriers pace to the promise; converges at 1/(1−slope); the randomised slice measures it; a shown-time feature at a reference value breaks it. | | |
| **Close the loop** | Late rate by shown-time bucket; refund cost by restaurant; the feedback row naming the loop; canary by city. | | |
| **Recovery** | 'Why a distribution?' answered with the two surfaces; a new restaurant answered with pooling at a wider quantile for two weeks. | | |

**Numbers the marker should expect to hear:** 80th percentile pre-order; median live; 0.3 slope → ~40% inflation; per-stage decomposition.

**Red flags particular to this brief:** a mean-squared-error model that shows the mean; one number for both surfaces.
