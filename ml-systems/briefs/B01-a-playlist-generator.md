# B.1 A playlist generator

## Candidate's half

Read only this section before starting the clock.

A music service wants a button that builds a playlist of thirty tracks from one seed track, for a listener who will hear it in order.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Sixty million tracks; a hundred million listeners; five million playlists a day; the first track must start within a second; skips, completions and saves are logged; a fifth of listeners have under ten plays of history; licensing forbids more than three tracks from one artist in any twenty.

### Pushes

The listener skips the second track; does the rest of the playlist change, and how fast? A new artist releases an album at midnight; when can it appear? Marketing wants sponsored tracks in the first five positions.

### Twist, at minute thirty

The service launches in a market where listening is offline for most of the day: the playlist must be built before the listener leaves the network.

### Rubric notes

Decided on Objective. Above the bar names the decision as a sequence rather than a set, says what completing a playlist is a proxy for and what skips are evidence of, and treats the artist limit as a slot rule and not a term. Above the bar at Bound finds that the cost is nothing and the freshness of the catalogue and the session are what bind. Above the bar at Close the loop names the feedback loop between what is played and what is learned, and the sponsored slot as a guardrail with its own measurement.
