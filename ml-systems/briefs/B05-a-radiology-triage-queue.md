# B.5 A radiology triage queue

## Candidate's half

Read only this section before starting the clock.

A hospital network wants scans that probably show an urgent finding read first, without changing who reads them.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Four thousand scans a day across twelve sites; a radiologist reads eighty a day; urgent findings are two per cent; the label is the radiologist's report, which arrives when the scan is read, hours to days later; a missed urgent finding is the worst outcome and a scan wrongly flagged costs a few minutes; the scanners differ by site and were replaced at two sites last year; a regulator audits any software that influences clinical order.

### Pushes

The model is 95 per cent sensitive on the held-out set; the interviewer asks at what false-positive rate and on which site. A site's scanner is replaced and the model's flag rate there halves overnight. A radiologist says she no longer looks carefully at unflagged scans.

### Twist, at minute thirty

The network wants to expand to a site whose population differs markedly from the training sites'.

### Rubric notes

Decided on Close the loop. Above the bar says that the model changes the order and not the decision, names the automation bias the third push describes as the design's central feedback loop, and builds the silent-failure row around a per-site flag rate. Above the bar at Objective names the asymmetric costs, sets the operating point from them, and makes sensitivity by site the suite. Above the bar at Bound sees that the label is late but complete, which is rarer than it sounds, and that the scanner change is the drift to watch.
