# B.8 A game leaderboard

## Candidate's half

Read only this section before starting the clock.

Design the leaderboard for a mobile game with fifty million players, showing the global top hundred and each player's own rank, updated as scores are submitted.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

50 million players; 20,000 score submissions a second at peak; the top hundred is viewed a million times a minute; a player's own rank is viewed on every game end; ranks may be a few seconds stale; leaderboards reset weekly and past weeks remain viewable.

### Pushes

A player's rank is 23,417,206; how is that number computed and how often? Two players submit the same score; who is ranked higher and is the answer stable? The weekly reset happens at midnight while 20,000 scores a second are arriving; what do players see during the reset?

### Twist, at minute thirty

The game adds a leaderboard per country and per friend group, with a player in one country and up to five hundred friend groups.

### Rubric notes

Turns on precision against cost, with the exact rank of a mid-table player as the test of whether the candidate prices what the brief asks for. Above the bar at Frame asks whether a mid-table rank must be exact and proposes an answer. Above the bar at Budget computes the memory for fifty million entries and the cost of an exact rank query against an approximate one. Above the bar at Commit chooses a structure and states what it gives up at the tail of the table.
