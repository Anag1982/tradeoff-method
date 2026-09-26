# B.11 Splitting a shared database between two teams

*migration brief*

## Candidate's half

Read only this section before starting the clock.

Two teams share one relational database. The catalogue team and the orders team each want their own store, and the orders table joins to the catalogue table on every order-history page. Plan the split.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

The shared database holds 3 TB, of which the catalogue is 200 GB; the join runs 5,000 times a second; both teams deploy daily; the database is at 50 per cent capacity and is not the reason for the split; there is no deadline except that the teams are blocking each other's schema changes weekly.

### Pushes

The join crosses the new boundary; what serves the order-history page after the split, and how stale may the catalogue data it shows be? A catalogue schema change breaks the orders team's copy; who finds out and how? The split is half done and a serious bug is found in the new catalogue store; what is the rollback and how long is it available?

### Twist, at minute thirty

A third team announces that it also reads both tables, through a reporting query nobody had catalogued.

### Rubric notes

Turns on coupling against velocity, and on the reversibility row the migration rubric adds. Above the bar at Frame finds that the objective is the teams' independence and not capacity, and asks whether the join can become a copy. Above the bar at Budget is a budget of stages and rollback windows, not of requests. Above the bar at Stress names the irreversible step, places it last, and has a flag for every stage before it. Above the bar throughout names what it will not do, and gives a reason from the brief.
