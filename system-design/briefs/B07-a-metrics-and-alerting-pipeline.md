# B.7 A metrics and alerting pipeline

## Candidate's half

Read only this section before starting the clock.

Design the pipeline that collects metrics from a company's fleet and fires alerts when a metric crosses a threshold, so that an on-call engineer is paged within thirty seconds of the condition.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

A hundred thousand hosts each reporting 200 metrics every ten seconds; 50,000 alert rules, most over one series, some over aggregates across a thousand hosts; thirteen months of retention for dashboards; the alerting path must work when the dashboard path is down.

### Pushes

A rule aggregates over a thousand hosts every ten seconds; what does evaluating 50,000 such rules cost? The pipeline's own storage fails; do alerts still fire? A host's clock is wrong by an hour; what happens to its series and its alerts?

### Twist, at minute thirty

Alerts must also fire on the *absence* of a metric, a host that stops reporting.

### Rubric notes

Turns on latency against throughput and on isolation against efficiency between the two paths. Above the bar at Frame separates the alerting path's requirements from the dashboard path's and names the thirty-second budget as the alerting path's binding constraint. Above the bar at Budget computes the sample rate, the compressed storage and the evaluation cost of the aggregate rules, which is the number that decides the design. Above the bar at Stress attacks the design with the alerting path depending on something the dashboard path owns.
