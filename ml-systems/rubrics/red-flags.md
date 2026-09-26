# Red flags

A red flag is a sentence or an act that, in the debrief, is quoted before the design is discussed (Section 16.5). One is survivable if the rest of the round is strong; two are not. Each is tied to the chapter that explains why.

| The flag | What it tells the interviewer | Chapter |
|---|---|---|
| A model named before the envelope exists | The design was remembered, not derived; every minute after is spent defending a choice the brief did not make. | 1, 3 |
| "We would evaluate it with AUC" and nothing about the decision | The metric was chosen without the operating point or the costs; the model that wins on it may lose the business money. | 2 |
| A diagram drawn in the first three minutes | The catalogue's shape, before the brief said what shape was needed. | 15 |
| "We would retrain hourly" when the label is weeks late | Freshness of parameters confused with freshness of features; the retrain learns nothing. | 3, 4 |
| "Fresher is better" for every feature | No tiering; a stream processor twenty times larger than the design needs. | 6 |
| A random split of time-ordered data | Leakage the offline number cannot see. | 5 |
| Training on features fresher than serving will have | Skew built into the training set. | 6 |
| An average with no slice | The two-point lift that is a five-point loss on one group; the harm row cannot be filled. | 9 |
| A guardrail as a penalty term in the objective | A constraint turned into a price the ranker can pay. | 10 |
| "We would monitor it" as the whole of the loop sheet | No shipping rule, no silent failure, no feedback row. | 9 |
| Thumbs as the metric for a generative system | A metric that rewards the confident answer; no judged set. | 1, 13 |
| The model calling a write tool directly | No gate; an action the model took cannot be undone with the model. | 13 |
| Own or rent decided without a utilisation number | The bill's largest term decided by preference. | 8 |
| A threshold on the approximate distance at a billion candidates | One number asked to do the index's job and the verifier's. | 12 |
| "It depends" with the dependence not named | The tradeoff seen and not priced. | 3 |
| Defending a decision a push has broken | The recovery row inverted. | 15 |

**Two flags end the discussion on their own:** the candidate cannot say what decision the model makes; the candidate names the harmful category as something to be traded off.

**The sentences interviewers write down when it goes well:** "The label is the design." "Thirteen minutes and no model yet." "Said which line binds and why the others don't." "Changed the serving decision when I corrected the peak." "Wrote the shipping rule before I asked." "Told me what the ranker does to its own labels." "Refused the fraud model with a number."
