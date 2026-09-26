# B.3 Anomaly detection for a payments platform

## Candidate's half

Read only this section before starting the clock.

A payments platform wants to be told, within a minute, when something is going wrong in its transaction flow, before customers call.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Ten thousand transactions a second across two hundred merchants, forty issuers and thirty countries; approval rate, latency and error rate are the signals; incidents happen a few times a month and were labelled after the fact by the on-call engineer; most of them show as an approval-rate drop in one segment; nights and weekends are quieter by five times.

### Pushes

The model pages the on-call engineer four times a night for nothing; what do you change? One issuer's approval rate drops by two points for an hour every Sunday; is that an incident? A new merchant launches with ten times the platform's average decline rate.

### Twist, at minute thirty

The incidents the platform most wants to catch are the ones nobody has labelled, because they were never noticed.

### Rubric notes

Decided on Bound. Above the bar sees that a few dozen labels are not a training set, that the label is the on-call engineer's judgement and is biased toward what was noticed, and that the design is a forecast of each segment's expected rate with an alarm on the residual, not a classifier. Above the bar at Close the loop makes the page rate a guardrail, names the feedback from the alarm to the labels, and says how a missed incident would be found. Above the bar at Deepen works the segmentation and the seasonality to the point where Sunday's issuer is explained.
