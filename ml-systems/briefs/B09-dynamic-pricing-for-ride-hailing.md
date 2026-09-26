# B.9 Dynamic pricing for ride-hailing

## Candidate's half

Read only this section before starting the clock.

A ride-hailing platform wants to set the price of a ride, by place and time, so that riders can get a car and drivers are worth having on the road.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

A million rides a day in one city; a price is quoted before the rider commits; a quote too high loses the rider and too low leaves riders waiting; drivers move toward high prices with a lag of ten minutes; the label is what happened after the quote, which depends on the quote; a regulator caps the price at three times the base in emergencies.

### Pushes

A stadium empties; what does the price do in the next fifteen minutes, and what did the model learn from the last time? The model raises prices in a neighbourhood every evening and drivers now wait there for it. The cap is hit; what does the design do with demand it cannot price?

### Twist, at minute thirty

The city requires that the price be explainable to a rider on request.

### Rubric notes

Decided on Close the loop. Above the bar names the feedback loop three times: the quote changes the label, drivers learn the model, and the cap changes behaviour; and builds the randomised slice of Chapter 5 as the only way to learn the demand curve. Above the bar at Objective says the business objective is completed rides and driver hours, not revenue per ride, and names the guardrail on wait time. Above the bar at Choose sees that the model forecasts supply and demand and a rule sets the price, and defends keeping the rule.
