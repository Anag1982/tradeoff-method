# B.11 A feature platform for one company

## Candidate's half

Read only this section before starting the clock.

Design the feature platform that thirty models across four teams will read from at serving time and train from, so that a feature means the same thing in both places.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Two thousand features; twenty of them streaming with second-level windows, the rest hourly or nightly; five hundred million entities; ten thousand feature reads a second at peak across the models, with a fifteen-millisecond budget for a batched read; labels arrive from hours to months late depending on the model; a feature is changed about once a week by somebody.

### Pushes

A team changes a feature's definition and three models regress the next day. A model's training set was built from features fresher than serving will have. The streaming store restarts and loses its counters.

### Twist, at minute thirty

A team wants to add a feature computed by a language model over free text, at a cost of a cent per entity.

### Rubric notes

Decided on Bound. Above the bar tiers the features by the window each needs, sizes the online store and the streaming state, and derives the served-feature log's retention from the longest label delay; says that point-in-time correctness is the platform's product and how it is obtained. Above the bar at Close the loop makes the skew monitor the platform's own loop sheet, with a per-feature comparison, a null-rate alarm and a restart check. Above the bar at Choose versions definitions and says what a change costs the consumers.
