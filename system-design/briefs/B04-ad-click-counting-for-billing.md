# B.4 Ad click counting for billing

## Candidate's half

Read only this section before starting the clock.

Design the pipeline that counts clicks on advertisements so that advertisers are billed for them, at a scale of a hundred billion impressions a day.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

A hundred billion impressions and a billion clicks a day; advertisers see counts in a dashboard that should be current to a minute; billing runs daily and must match the dashboard; about two per cent of clicks are later judged fraudulent and must not be billed; a dispute may be raised up to ninety days later.

### Pushes

A click is delivered to the pipeline twice; what does the dashboard show and what does the bill say? The fraud judgement arrives six hours after the click; how is a count that was already shown corrected? An advertiser disputes a day's count eighty days later; what evidence exists?

### Twist, at minute thirty

Advertisers are offered a real-time bid adjustment based on the last ten seconds of clicks per campaign.

### Rubric notes

Turns on precision against cost and on read cost against write cost, with the exactly-once argument of Chapter 13 applied to counts rather than charges. Above the bar at Frame separates the dashboard's tolerance from billing's and names the correction of already displayed numbers as the hard part. Above the bar at Budget computes the per-second click rate, the storage for ninety days of evidence and the cost of an exact count against an approximate one. Above the bar at Commit chooses where deduplication happens and what it stores, with a size.
