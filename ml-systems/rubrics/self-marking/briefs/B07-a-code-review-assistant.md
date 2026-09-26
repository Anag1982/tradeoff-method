# B.7 A code-review assistant

*Unworked brief · decided on **Close the loop** · Appendix B*

An assistant that comments on pull requests before a human reviews them.

Mark the deciding row first. Then score every row below, at or above the bar against the anchor given, and write the minute the artefact appeared.

| Row | Above the bar on this brief | Band | Minute |
|---|---|---|---|
| **Objective** | Comments acted on as the proxy; comments per PR as the guardrail that eats it; the judged set from historical reviews. | | |
| **Bound** | 2k PRs/day; the label is the author's action within a day, biased by what was shown; tokens per PR priced against the platform; code stays inside the company. | | |
| **Binds** | The measurement (acted-on vs shown) and the private-data wall. | | |
| **Choose** | A retrieval-grounded reviewer with a comment budget; a judged set; no training on the company's history without a gate. | | |
| **Deepen** | The security-bug push: a suggested change that introduces one, and what checks it. | | |
| **Close the loop** (decides) | Correct comments nobody acts on as the failure the proxy sees; the twist (push a fix itself) as a write tool behind a gate. | | |
| **Recovery** | Refuses to let confidence be the gate for pushing a fix. | | |

**Numbers the marker should expect to hear:** 2k PRs/day; a minute per wrong comment; an incident per missed bug.

**Red flags particular to this brief:** letting the assistant push when 'confident'; training on PR history without asking what leaks.
