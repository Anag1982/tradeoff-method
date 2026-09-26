# Model-as-judge: template, failure checklist and calibration protocol

A model judge is cheap, fast and consistent, and the instrument most production teams use; it is usable only with the discipline below (Chapter 9, Section 9.3).

## 1. The prompt (supported-claim judging)

Give the judge the reference passages and ask about **support**, not quality. Freeze and version the rubric.

```
You are checking whether an answer is supported by the passages it cites. You are not judging
whether the answer is good, polite or complete.

PASSAGES (the only evidence that counts):
{{passages}}

QUESTION:
{{question}}

ANSWER:
{{answer}}

For each factual claim in the answer, decide: SUPPORTED (a passage states it), UNSUPPORTED
(no passage states it, or a passage contradicts it), or NOT_A_CLAIM (a hedge, a question, an
offer to hand over). Then give one overall verdict:

  SUPPORTED   every claim is supported
  PARTIAL     at least one claim is unsupported
  ABSTAINED   the answer declines to answer and makes no claim
  LEAK        the answer states something the passages do not, presented as fact

Output exactly:
claims: [ {"text": ..., "verdict": ...}, ... ]
overall: SUPPORTED | PARTIAL | ABSTAINED | LEAK
rubric_version: {{rubric_version}}
```

Rules for the caller: shuffle the order of passages; do not show the judge which system produced the answer; run pairwise comparisons in both orders and discard disagreements; use a judge from a different model family than the system being judged.

## 2. The failure checklist (from Chapter 9's table)

| The judge tends to | Do this |
|---|---|
| Prefer longer answers | Control for length in the rubric, or compare at matched length |
| Prefer its own style or family | Use a judge from a different family than the system |
| Be swayed by confident tone | Give it the passages and ask about support, not quality |
| Assert facts it does not have | Judge only properties it can see; route factual claims to reference checks |
| Shift with rubric wording | Freeze and version the rubric; re-calibrate on every change |
| Prefer the first of two answers | Score both orders and average, or discard disagreements |
| Drift lenient over weeks | The weekly calibration below; agreement rate on the dashboard |

## 3. The weekly calibration protocol

1. Each week, sample **300** judged outputs, stratified by verdict (so that PARTIAL and LEAK are not swamped by SUPPORTED).
2. Two people score the same 300 blind, with the same rubric version.
3. Run `judge_calibration.py` on the three columns: agreement rate, Cohen's kappa, and the judge's bias by direction (does it call PARTIAL things people call SUPPORTED, or the reverse?).
4. Put the agreement rate on the dashboard beside the metric the judge produces. A judge whose agreement with people falls below the floor you set (0.85 is a usual starting point) is not measuring what it was calibrated to; the metric it produces that week is not read.
5. Any rubric change resets the calibration: re-run on the same 300 before trusting a number under the new version.

Sizing note: 300 resolves about ±4 points on an agreement rate near 0.9 (`sizing.py judged 0.9 0.04`); pool four weeks for a finer read.
