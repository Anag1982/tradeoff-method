# B.10 Recommendation candidate generation

*AI-adjacent brief*

## Candidate's half

Read only this section before starting the clock.

Design the service that, for each user opening a streaming product's home screen, produces the few hundred candidate titles that a ranking model will order, using both the user's long-term history and what they did in the last few minutes.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

Two hundred million users; fifty thousand home screen loads a second at peak; a catalogue of two hundred thousand titles; the candidate set must reflect a title watched in the last minute; the ranking model needs 300 candidates and 50 ms; the long-term model is retrained nightly.

### Pushes

A user watches a title thirty seconds before opening the home screen; which part of the design ensures it affects the candidates, and what does that part cost per second across the fleet? A new title is released and has no history; how does it become a candidate? The nightly retraining fails; what is served in the morning?

### Twist, at minute thirty

The product must explain, on request, why each title was recommended.

### Rubric notes

Turns on freshness against cost and on read cost against write cost. Above the bar at Frame separates the long-term signal from the session signal and names the join of the two at 50,000 loads a second as the hard part. Above the bar at Budget computes the feature reads per second and the storage for two hundred million users' recent activity. Above the bar at Stress names how candidate quality is measured and what the alert is when it falls, since a wrong candidate set raises no error.
