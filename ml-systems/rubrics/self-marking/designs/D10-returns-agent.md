# D.10 The returns agent

*Worked design · decided on **Close the loop** · Chapter 13*

Chapter 13's second design and its harm design: the model proposes and a rule disposes — a deterministic gate with an allowed-action list, a cap and idempotency keys; an eight-step budget; a replay set judged on final state; compensating actions owned by people.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | The ML objective as a sequence of actions; wrong-action rate under a ceiling on the weekly audit; 'refunding above the cap without a person, never: that is a gate, not a probability.' | | |
| **Bound** | 20k tickets/day; six model calls and four tool calls; 30 s used against minutes allowed; 0.8 accelerator-seconds a ticket; a 1,000-ticket replay set; traces kept a year. | | |
| **Binds** | Harm: an action is not a prediction and cannot be rolled back with the model; then evaluation without a label. | | |
| **Choose** | Router (small for extraction, large for planning); the gate; the budget with escalation as the floor; replay judged on state; compensating actions; prompt before fine-tune; latency as the open vertex. | | |
| **Deepen** | The gate and the cap (Exercise 13.2): at 2% error the cap is not a cost lever; the harm ceiling decides it. | | |
| **Close the loop** (decides) | A canary with every write reviewed before it executes; reopen rate at seven days; a tool changing its response shape seen as escalation rate; the trace teaching itself, broken by auditing escalations; actions compensated by people, never by rollback. | | |
| **Recovery** | '98% right, why not call refund directly': 400 wrong refunds a day and the gate; the retry loop: budget, then escalate with the trace; 'how did you know': replay on final state, then a reviewed canary. | | |

**Numbers the marker should expect to hear:** 20k/day; 8 steps / 20k tokens; $50 cap; $16.8k / $15.8k / $16k a day for the three caps; 300-ticket audit resolves ±1.6 points at 2%.

**Red flags particular to this brief:** the model calling the write tool; judging the reply text; fine-tuning on production traces.
