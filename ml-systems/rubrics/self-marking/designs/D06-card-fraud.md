# D.6 Card fraud at authorisation

*Worked design · decided on **Bound** · Chapter 12*

Chapter 12's first design, assembling Chapters 2, 5, 6 and 9: hard rules in front, a three-way decision, a one per cent slice of soft declines approved for labels, disputes as an early signal, a weekly retrain, a per-country audit.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Three numbers read together (fraud loss in basis points, false-decline rate, challenge rate); recall at the tolerated false-positive rate on matured labels by country; the blocklist as a rule; small-ticket fraud allowed freely. | | |
| **Bound** (decides) | 10k auth/s; 50 ms split (2 rules, 15 features, 20 model, 3 decision); chargebacks 30–90 days, absent for declines; disputes at 14 days; counters in seconds, entity features nightly, model weekly; 125 TB of logs; a dozen cores. | | |
| **Binds** | The label — late, absent for declines and moved by the model; latency tight but met by Chapter 6's plan; cost nothing. | | |
| **Choose** | Rules first; approve/challenge/decline with the band from the three costs; the slice for labels on declines; disputes beneath chargebacks; weekly cadence; audit by country. | | |
| **Deepen** | The label mechanism: the slice's price and payoff (Exercise 12.2), or the three-way thresholds (Exercise 12.1). | | |
| **Close the loop** | Time-ordered split on matured labels; canary by card for a week on decline and challenge rates; stream counters lost on restart as the silent failure; the model moving fraud to where it scores low; rules, thresholds and model on separate rollback clocks. | | |
| **Recovery** | The 2 a.m. attack answered on three clocks; 'you approve declines on purpose' answered with $16k a day against a $1.8M false-decline bill; the regulator answered with the line already in the suite. | | |

**Numbers the marker should expect to hear:** 0.7% / 24% thresholds; two-way at 3.6%; 2,000 slice approvals a day; $16k/day; 60k labels/month; 180-day log.

**Red flags particular to this brief:** hourly retrain; training on approved only with no slice; a single threshold.
