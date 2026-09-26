# Senior rubric

Score each row below, at or above the bar. Note the minute at which the row's artefact appeared.

| Row | Below the bar | At the bar | Above the bar | Minute |
|---|---|---|---|---|
| **Objective** (objective sheet) | Takes the prompt's metric as the objective; names a model in the first three minutes; no guardrail. | States a business objective and an ML objective that differ; names an offline and an online proxy; names one guardrail. | Derives the ML objective from the decision the model exists to make; says what the proxy cannot see and guards it; says what may be got wrong and what is not an ML problem; the sheet is complete by minute seven. | |
| **Bound** (envelope) | No arithmetic, or arithmetic without a unit; the label line absent; "we would use a feature store." | Rate, latency budget and storage computed; the label named with its delay; a cost per thousand in a unit. | Every line of the envelope, with the numbers proposed and corrected on few; the label's delay and its bias; freshness by tier; cost in core- or accelerator-seconds derived from Appendix A's ratios; the numbers reappear on the diagram. | |
| **Binds** (one sentence) | Never says which line decides; or "latency" for every brief. | Names one line and gives a reason. | Names the line, dismisses the others with a reason each, and says it before any model is named; names the line that binds next. | |
| **Choose** (table, triangle, decision line) | Offers options and waits; or names a model with no position on an edge and no price; the diagram before the decision. | Chooses with a reason from the envelope; a tradeoff table with both ends; the diagram after the decision. | Decision lines with the alternative and the accepted price; the triangle with its open vertex said; the model as a position on the quality–latency edge with its cost; a decision changed when a number changes, with the reason. | |
| **Deepen** (the binding mechanism) | Adds components; describes a technology; works a part that does not bind. | Works the binding mechanism to the point where its failure mode is visible. | The mechanism, its numbers from the envelope, the failure it prevents and the instrument that would show it, with the sensitivity named unprompted. | |
| **Close the loop** (loop sheet) | No evaluation beyond an offline metric; no harm row; "we would monitor it." | An offline suite and an online test named; one silent failure; one feedback loop; a rollback. | The shipping rule written before the metric is read; the suite by slice; the feedback row naming what the model does to its own data; harm measured by group with a rollback on a clock; the second return edge drawn. | |
| **Recovery** (any minute) | Defends a broken decision; hides a wrong number; argues with a corrected one. | Concedes a push; corrects a number when told. | Attacks the design first; corrects a number aloud and changes the decision it rested on; names the return edge when a push reveals it; says who is paged. | |

**Not scored:** model names; completeness of the diagram on its own.

**Readiness signal:** objective sheet by 7, envelope by 13, binding sentence by 15 with no model named before it, decision line by 20, loop sheet started by 35, without looking at the clock.

**Two flags end the discussion on their own:** the candidate cannot say what decision the model makes; the candidate names the harmful category as something to be traded off.
