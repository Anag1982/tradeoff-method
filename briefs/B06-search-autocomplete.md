# B.6 Search autocomplete

## Candidate's half

Read only this section before starting the clock.

Design the suggestions that appear under a search box as the user types.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Twenty thousand keystrokes a second at peak; fifty milliseconds from keystroke to suggestions or the box feels broken; ten million distinct queries cover ninety per cent of traffic; a suggestion is judged by whether it was selected; the head of the distribution changes hourly on news days; some queries must never be suggested; a third of prefixes have never been seen before.

### Pushes

A celebrity's name trends and the suggestions are an hour old. A prefix that has never been seen; what appears? A journalist finds an offensive suggestion under a common prefix.

### Twist, at minute thirty

The product wants suggestions personalised to the user's own history, on the same fifty milliseconds.

### Rubric notes

Decided on Bound. Above the bar finds that latency binds at the keystroke and forces a precomputed structure for the head and a cheap model for the tail, and prices both; sees that freshness is the second constraint and puts a fast path for trending prefixes on the envelope. Above the bar at Close the loop makes the blocklist a wall with its own review loop, and the selection feedback loop, in which suggestions shown are the ones selected, the feedback row. Above the bar at Choose says what the tail model may get wrong and what it must not.
