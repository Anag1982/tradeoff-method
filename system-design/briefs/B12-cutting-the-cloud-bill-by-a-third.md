# B.12 Cutting the cloud bill by a third

*staff brief*

## Candidate's half

Read only this section before starting the clock.

“Our cloud bill doubled in a year and the CFO wants it down by thirty per cent within two quarters without slowing product work. Where would you start?”

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked, and only if asked

The bill is $2.4 million a month; roughly 40 per cent compute, 25 per cent storage, 20 per cent egress, 15 per cent managed services; compute fleets average 22 per cent utilisation; 60 per cent of stored data has not been read in a year; egress is mostly media served without a CDN; nobody owns the bill and each team sees only its own services.

### Pushes

A team says its fleet cannot be autoscaled because of a warm-up problem; do you accept that? The CFO asks for the thirty per cent as a commitment; what do you commit to and what do you not? The largest single saving would take a migration that the owning team says is a year of work; what do you do with it?

### Twist, at minute thirty

Halfway through the two quarters, the product team launches a feature that doubles egress.

### Rubric notes

A staff brief in the form of Chapter 14. Turns on the cost model of Chapter 11 and the four verbs of Chapter 14. Above the bar at Frame turns “thirty per cent” into a list of the bill's terms with the largest first, and asks who owns each. Above the bar at Budget computes the saving available from each of the five moves of Chapter 11 against the numbers given, and ranks them by saving per engineer-week. Above the bar at Commit names the three moves it would make first, the one it would not make and why, and what it will tell the CFO it can and cannot promise. Above the bar at Stress names the organisational failure mode, that nobody owns the bill, as the first thing to fix.
