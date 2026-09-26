# D.11 The serving platform

*Worked design · decided on **Bound** · Chapter 13*

Chapter 13's third design, Chapter 8's derivation as a system: separate prefill and decode pools, a cached shared prefix with affinity routing, 8-bit offered per tenant, token budgets with fair queuing, a batch lane, pinned versions.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | 'The platform trains nothing'; cost per million tokens at the service levels met; a tenant served a version it did not validate, never. | | |
| **Bound** (decides) | 2,000 req/s; 8M prefill and 600k decode tokens/s; prefill 160 → 40 accelerators with the prefix cached; decode 120 by throughput, memory permitting 140 in flight per accelerator against 12,000 across the pool; utilisation 40% → 70% with the batch lane. | | |
| **Binds** | Cost through two facts: decode memory-bound, prefill compute-bound; the in-flight state caps the batch. | | |
| **Choose** | Two pools with 430 MB handed over; prefix cache and affinity; 8-bit per tenant; tokens as the unit of fairness; the batch lane; pin and shadow; cost as the open vertex. | | |
| **Deepen** | The long-prompt case (Exercise 13.3): 16k tokens makes memory bind decode by three to one and prefill grow fourfold; the levers in order. | | |
| **Close the loop** | Two p99s by class and tenant; cache hit rate after a prompt edit; an accelerator near its memory limit shows as streams slowing; retry storms answered with a retry-after; rollback by re-pinning. | | |
| **Recovery** | 'Why two pools': sized for their own bottlenecks; the 100k-token tenant: the budget runs out and it queues as batch; 'why own': 40–70% utilisation is past the break-even. | | |

**Numbers the marker should expect to hear:** 160 → 40 prefill; 120 decode; 140 in flight per accelerator; 430 MB per request; 16k tokens → 324 by memory.

**Red flags particular to this brief:** sizing decode by throughput alone; requests as the unit of fairness; upgrading all tenants in place.
