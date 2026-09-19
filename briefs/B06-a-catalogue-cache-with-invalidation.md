# B.6 A catalogue cache with invalidation

## Candidate's half

Read only this section before starting the clock.

Design the caching layer for a retailer's product pages, where prices and stock change often and a stale price is a legal problem.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

Fifty million products; 100,000 page views a second at peak; a product page assembles data from six services; prices change a million times an hour during promotions; a stale price must not be shown for longer than five seconds; stock may be a minute stale.

### Pushes

A promotion changes the price of a million products at once; what happens to the cache and to the origin? The cache fleet restarts empty at peak; what do users see for the next minute? A price change is written to the store and the invalidation message is lost; how long is the wrong price shown and how is it found?

### Twist, at minute thirty

Prices become personalised per customer segment, of which there are two hundred.

### Rubric notes

Turns on freshness against cost, with the two different tolerances in the brief as the test. Above the bar at Frame notices that price and stock have different freshness requirements and designs for each rather than the stricter for both. Above the bar at Budget computes the invalidation rate against the view rate and the origin's capacity under a cold cache. Above the bar at Commit chooses a mechanism by which a lost invalidation is bounded rather than hoped against, and prices it.
