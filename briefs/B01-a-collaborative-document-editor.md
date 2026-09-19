# B.1 A collaborative document editor

## Candidate's half

Read only this section before starting the clock.

Design the service behind a document editor in which several people type into the same document at once and each sees the others' changes as they happen.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

Ten million documents; a typical document has one to three concurrent editors and the largest a few hundred; 50,000 concurrent editing sessions at peak; a keystroke every 200 ms per active editor; documents average 50 KB and are kept forever with full history.

### Pushes

Two editors type in the same word at the same moment; what does each see and what does the document say afterwards? An editor loses connectivity for two minutes and keeps typing; what happens on reconnection? The largest document has 300 editors during a company all-hands; what fails first?

### Twist, at minute thirty

Legal requires that every version of every document be reconstructible for seven years, exactly as it was at any second.

### Rubric notes

Turns on consistency against latency with a single-entity scope, and on durability against write latency. Above the bar at Frame names concurrent edits to one document as the hard part and scopes out formatting, comments and permissions. Above the bar at Budget computes the per-document write rate and shows it is small even for the largest document, which redirects the difficulty from throughput to ordering. Above the bar at Deepen works one mechanism for merging concurrent edits to the point where its failure mode is visible, and says what the design gives up compared to the other family of mechanism.
