# B.5 Search autocomplete

## Candidate's half

Read only this section before starting the clock.

Design the service that suggests completions as a user types into a search box, for a product with a large and changing vocabulary of queries.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

200 million searches a day, each preceded by an average of six keystrokes that request suggestions; suggestions must appear within 100 ms of the keystroke; the top suggestions for a prefix are the most popular recent queries; a new trending query should appear in suggestions within a few minutes; some queries must never be suggested.

### Pushes

A query becomes popular in one city only; do users elsewhere see it? A user types a prefix that no one has ever typed; what is returned and how fast? The blocklist gains a term; how quickly does it stop being suggested and what serves the requests in the meantime?

### Twist, at minute thirty

Suggestions must be personalised by the user's own history.

### Rubric notes

Turns on freshness against cost and on latency against throughput. Above the bar at Frame computes the keystroke rate from the search rate and names the 100 ms budget as binding, then names freshness of the popularity ranking as the hard part. Above the bar at Budget sizes the structure that answers a prefix and shows whether it fits in memory on one node or must be partitioned. Above the bar at Axes places the popularity computation on the read-against-write axis with a number for each end.
