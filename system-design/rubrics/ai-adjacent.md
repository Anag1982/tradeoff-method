# AI-adjacent rubric

For retrieval services, vector search, recommendation pipelines and any brief where the system's failures are silent: a wrong answer, a missing neighbour, a stale candidate set, rather than an error. The senior rows apply, with one row added and two anchors changed.

| Row | Below the bar | At the bar | Above the bar | Minute |
|---|---|---|---|---|
| **Frame** | Treats the model as the design. | States an objective in terms of answer or retrieval quality. | States the objective as a measurable quality number; names the non-negotiable that is not about quality (permissions, cost, freshness); scopes the model's own behaviour out. | |
| **Budget** | Budgets requests and storage only. | Prices the model or the index. | Finds that tokens, memory for vectors, or the scan is the dominant term, and says what it implies (make the context small; the store is chosen by memory). | |
| **Axes** | Lists models and vector databases. | Names precision against cost. | Names precision against cost with the knob that moves along it (context size, candidate set, quantisation) and the measurement that would justify moving it. | |
| **Commit** | Picks the largest model or the fanciest index. | Chooses with a reason. | Chooses the cheapest point that meets the quality constraint and names the price paid (recall, freshness, memory); names the second defensible answer. | |
| **Deepen** | Describes the pipeline. | Works one mechanism. | Works the mechanism that makes the non-negotiable hold (the pre-filter plus verification; the fresh index and rebuild; the key query) and shows its failure mode. | |
| **Measurement** (added) | Cannot say how the system knows it is working. | Names a quality metric. | Names the labelled set, the metric (recall at k, supported answers), how often it runs, and what alert fires when it falls; treats a change to the corpus or model as something the measurement must re-approve. | |
| **Stress** | Attacks throughput. | Runs the four attacks. | Attacks quality first ("what fails silently?"), then the four; names who is paged on a quality drop and what they compare. | |

**Below the bar however good the pipeline:** a candidate who cannot answer "how do you know it is broken?" with a measured number.
