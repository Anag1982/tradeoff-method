# B.2 A workflow orchestration engine

## Candidate's half

Read only this section before starting the clock.

Design a service that runs multi-step workflows, each a sequence of calls to other services with retries and branches, so that a workflow started is always either completed or reported as failed, even if the engine itself crashes midway.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

5,000 workflow starts a second at peak; an average workflow has eight steps and runs for two minutes, the longest for a week; steps call external services that fail one time in fifty and time out one in five hundred; a million workflows in flight at any moment.

### Pushes

The engine crashes between issuing a step's call and recording its result; what happens to that step? A step's external service is down for an hour; what does the million-workflow backlog look like and how does it drain? A workflow needs to wait six days for a human approval; where does that state live and what does it cost?

### Twist, at minute thirty

Workflows must be able to be changed while running, so that a workflow started under version 3 of its definition completes under version 4.

### Rubric notes

Turns on durability against write latency and on the delivery guarantees of Chapter 10, with Chapter 13's payments state machine as the nearest shape. Above the bar at Frame names “exactly once per step against services that time out” as the hard part and states what the engine guarantees and what the steps must guarantee themselves. Above the bar at Budget computes the state writes per second and the storage for a million in-flight workflows. Above the bar at Commit says where the step's idempotency lives and accepts that it is not the engine's to provide.
