# B.7 A code-review assistant

## Candidate's half

Read only this section before starting the clock.

An engineering organisation wants an assistant that comments on pull requests before a human reviews them.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Two thousand pull requests a day; a comment is useful if the author acts on it; reviewers ignore assistants that comment too much; the code base is private and the assistant may not send it outside the company; a wrong comment costs a minute, a missed bug costs an incident; there is no label until the assistant exists, except the human reviewers' historical comments.

### Pushes

The assistant's comments are correct and nobody acts on them. A comment suggests a change that introduces a security bug. The organisation asks whether the assistant can be trained on its own history of pull requests.

### Twist, at minute thirty

The assistant is to be allowed to push a fix itself when it is confident.

### Rubric notes

Decided on Close the loop. Above the bar names the proxy, comments acted on, and the guardrail, comments per pull request, and says why the second eats the first; builds the judged set from historical reviews and says what it cannot see. Above the bar at Bound sees that the label is the author's action, arrives within a day and is biased by which comments were shown, and prices the tokens per pull request against the serving platform of Chapter 13. Above the bar on the twist treats a push as a write tool behind a gate, with the design of Chapter 13's agent, and refuses to let confidence be the gate.
