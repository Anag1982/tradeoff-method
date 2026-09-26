# B.8 A wake word and intent on a device

## Candidate's half

Read only this section before starting the clock.

A consumer device must respond to a spoken wake word and then understand a short command, with most of the work on the device itself.

---

## Interviewer's half

Give the numbers only if asked. Deliver the three pushes in the questions block whatever the candidate has said, and the twist at minute thirty. Score against the rubric notes below and the sheets in `../rubrics/`; the notes name the row that decides the brief, never the design.

### Numbers, if asked

Ten million devices; the wake-word model runs continuously on a microcontroller with a few hundred kilobytes of memory and a milliwatt budget; a false wake once a day is the complaint threshold; a missed wake is a retry; the command is understood on the device when possible and in the cloud when not; the cloud call costs two hundred milliseconds and privacy; labels come from users who repeat themselves and from an opt-in review programme.

### Pushes

The wake word is a common word in one language. The device wakes on the television. The command model on the device is wrong for a fifth of commands in one accent.

### Twist, at minute thirty

A new wake word is chosen by marketing and must ship in two months.

### Rubric notes

Decided on Bound. Above the bar sees that the envelope is memory and power rather than throughput, that the false-wake rate is the guardrail and its unit is per day and not per utterance, and that the cascade is a tiny model on the device with a larger one behind it. Above the bar at Choose sizes the on-device model from the memory and prices the cloud fallback in latency, privacy and cost. Above the bar at Close the loop names the label problem, repeats and the opt-in programme, and the disparity by accent as a harm row with a measurement.
