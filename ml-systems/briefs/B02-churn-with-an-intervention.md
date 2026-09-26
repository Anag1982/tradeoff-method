# B.2 Churn with an intervention

## Candidate's half

Read only this section before starting the clock.

A subscription business wants to predict which customers will cancel next month and offer some of them a discount.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Twenty million subscribers; monthly churn near three per cent; the discount costs a month's revenue; the offer team can send two hundred thousand offers a month; a customer offered a discount who would have stayed anyway is the commonest case; labels are cancellations, observed at month end; the model is scored on the first of the month.

### Pushes

The model's precision at the top two hundred thousand is twelve per cent; is that good? The offer changes whether the customer cancels; what does that do to next month's training set? Finance asks for the return on the programme.

### Twist, at minute thirty

Legal says the discount cannot be offered on the basis of a customer's region, and region is the model's strongest feature.

### Rubric notes

Decided on Objective. Above the bar says that the decision is whom to offer, not who will churn, so the quantity that matters is the uplift from the offer and not the probability of cancelling, and that the two need different labels. Above the bar at Close the loop names the intervention's feedback on the label, a held-out group that receives no offer as the only way to measure the programme, and the region constraint as a harm row with a measurement by group. Above the bar at Bound notes that compute is irrelevant and the label's monthly cadence is the clock.
