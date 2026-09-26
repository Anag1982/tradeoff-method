# Platform and infrastructure rubric

For loops whose subject is the serving or feature platform rather than one model (Section 16.4). The rows are the senior rubric's; **Bound** and **Deepen** are weighted toward serving, the Objective row is lighter because the tenants own the objectives, and the harm row does not lighten. Material: Chapters 6, 7, 8 and 13.

| Row | Weight | Above the bar, in this loop | Band | Minute |
|---|---|---|---|---|
| **Objective** | ½ | Cost per unit at the service levels met; tenant fairness named as a guardrail; "the platform trains nothing" said. | | |
| **Bound** | **2** | The decode fleet from bandwidth over model bytes times the batch; the prefill fleet from the compute-bound rate; the in-flight state and the batch it caps; the prefix cache's share; utilisation over the day against the own-against-rent break-even. For a feature platform: tiers by window, the online store, the streaming state, the served-feature log from the longest label delay. | | |
| **Binds** | 1 | Names cost through the two facts (decode memory-bound, prefill compute-bound), or point-in-time correctness for a feature platform, and says why latency and quality are fixed. | | |
| **Choose** | 1 | Two pools with the state handed over; prefix affinity; precision offered per tenant against its judged set; tokens as the unit of fairness; a batch lane for the trough; pinned versions with shadow. | | |
| **Deepen** | **2** | Works the scheduler's tail, the memory limit as streams slow, or the skew monitor as the platform's own loop, to the point where the failure is visible and priced. | | |
| **Close the loop** | 1 | Service levels by class and tenant; starvation; cache hit rate after a prompt change; a version served that a tenant did not validate as the harm, prevented by the pin; rollback per tenant. | | |
| **Recovery** | 1 | Recomputes the fleet aloud when a number changes (context length, precision, peak); says which lever moves which pool. | | |

**The platform loop's red flag:** a tenant served a model version it did not validate. Everything else is a number.
