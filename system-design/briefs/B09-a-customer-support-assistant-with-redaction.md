# B.9 A customer-support assistant with redaction

*AI-adjacent brief*

## Candidate's half

Read only this section before starting the clock.

Design a retrieval-augmented assistant that helps support agents answer customer tickets from past tickets and the knowledge base, where past tickets contain customers' personal data that must not appear in a response for a different customer.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes and the rubric sheets in `../rubrics/`.

### Numbers, if asked

Twenty million past tickets, ten thousand knowledge-base articles; five thousand agents; two hundred questions a minute; personal data in tickets is not labelled; the model is a hosted API; regulators may ask how a given answer was produced.

### Pushes

A past ticket contains a phone number in free text; how is it kept out of another customer's answer, and how sure is the design? An agent asks a question whose best answer is in a ticket from the same customer; is it allowed? A regulator asks what the model was shown for a particular answer last March; what exists?

### Twist, at minute thirty

The company acquires another with its own ticket history in a different language.

### Rubric notes

Turns on precision against cost and on the measurement row that the AI-adjacent rubric adds. Above the bar at Frame names unlabelled personal data as the hard part and separates redaction at ingest from filtering at query time, with the price of each. Above the bar at Budget computes the model cost per question and the one-time cost of processing twenty million tickets. Above the bar at Deepen says how the design knows its redaction works, with a measured rate and a set it is measured on, and what the residual risk is.
