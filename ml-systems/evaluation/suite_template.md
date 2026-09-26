# Offline suite: template

One document per model. Fill every field before the first number is read; the shipping rule in particular is written first, because a rule written after the result is a rationalisation (Chapter 9).

## 1. The decision and the metric

- **Decision the model drives:** (threshold / order / candidate set / number / show-or-not)
- **Primary offline metric, derived from the decision:** (e.g. recall at 0.2% false-positive rate; position-discounted gain on purchases; quantile loss at the 80th percentile; supported-claim rate)
- **Operating point, and the costs that set it:** (cost of each error kind, in money or its equivalent)
- **What the metric cannot see:** (the guardrails below exist for this)

## 2. The reference set

- **Source and size:** (n = ; sized by `sizing.py judged p difference`: at p ≈ 0.8 and n = 300 the set resolves about five points and is a regression test, not a leaderboard)
- **Split:** time-ordered, with a gap of at least the label delay; never random on time-ordered data
- **Label provenance and delay:** (matured to how many days; what is missing for declined / unshown items; the randomised slice if any)
- **Judged subset (generative):** questions with the answering passage marked; who judged; rubric version

## 3. Slices

Report every metric on each slice, never only on the average (the two-point lift that is a five-point loss on new users).

| Slice | Why it is a slice | Minimum n |
|---|---|---|
| new users / new items | cold start | |
| by country / language / segment | harm; disparity | |
| by source / category | where the model is weakest | |
| head vs tail | where the average hides the failure | |
| the hard slice (generative) | where a smaller or quantised model loses first | |

## 4. Guardrails, on the same page

| Guardrail | Measured how | Ceiling / floor |
|---|---|---|
| (e.g. false-decline rate by country) | | |
| (e.g. connected floor share; publisher share of a session) | | |
| (e.g. unsupported-claim rate; leak rate) | | zero |
| p99 latency at the operating batch | | |

## 5. The shipping rule (written before the result)

> Ship if the primary metric improves by at least ___ on the whole set **and** on every named slice by at least ___, **and** no guardrail moves past its line, **and** the online read (below) confirms within ___ days. Otherwise do not ship, whatever the average says.

## 6. The online read that follows

- **Unit of randomisation:** (user / session / request / market)
- **Length and size:** (from `sizing.py ab`)
- **Fast read / slow read:** (e.g. disputes at 14 days / chargebacks at 60)
- **Interleaving first?** (for rankers: yes, as the filter before the A/B)

## 7. What is versioned, and the rollback clock

| Component | Versioned with | Reverts within |
|---|---|---|
| thresholds / bands | | minutes |
| prompt / rules / allowed-action list | | the hour |
| model | its heads / calibration layer / judge | the day |
| index / feature definitions | | the day |
