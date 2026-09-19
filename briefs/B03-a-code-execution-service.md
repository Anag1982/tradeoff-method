# B.3 A code execution service

## Candidate's half

Read only this section before starting the clock.

Design the service behind an online coding platform that compiles and runs submitted programs against test cases and returns the results, for programs written by strangers.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

2,000 submissions a second during a contest, 50 on an ordinary day; each runs up to ten test cases with a two-second limit each; a submission's result is expected within thirty seconds; some submissions are hostile.

### Pushes

A submission forks processes until the machine is unusable; what contains it and what do the other submissions on that machine experience? A contest starts and 2,000 a second arrive for ten minutes; what is the queue and the wait? Test cases for a problem change after 10,000 submissions have been judged against the old ones; what happens?

### Twist, at minute thirty

The platform adds a language whose runtime takes eight seconds to start.

### Rubric notes

Turns on isolation against efficiency, with the webhook service of Chapter 10 as the nearest shape. Above the bar at Frame names hostile code on shared machines as the hard part and separates the isolation guarantee from the fairness guarantee. Above the bar at Budget computes machine-seconds per submission and the fleet for the contest peak against the ordinary day, and says what that ratio implies. Above the bar at Stress attacks the design with a submission that is slow rather than hostile, and prices the cost of isolating every submission against sharing.
