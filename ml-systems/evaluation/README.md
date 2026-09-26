# Evaluation harness templates

The instruments Chapter 9 says a learned system is known by, as templates a team can fill in. Nothing here depends on anything beyond the Python standard library.

| File | What it is |
|---|---|
| [suite_template.md](suite_template.md) | The offline suite as a document: the reference set, the slices, the operating point, the guardrails on the same page, and the shipping rule written before the metric is read. Fill it in per model. |
| [offline_suite.py](offline_suite.py) | A small scorer for a CSV of predictions: log-loss, AUC, recall at a fixed false-positive rate, calibration error, all **by slice**, with the shipping rule checked at the end. `python offline_suite.py --demo` runs it on synthetic data. |
| [sizing.py](sizing.py) | The three sizes the book derives: a judged set from the difference to detect (Chapter 9), an A/B from the lift to detect and the unit's variance, a prevalence sample from the precision wanted (Chapter 12). `python sizing.py judged 0.9 0.02`. |
| [judge_template.md](judge_template.md) | A model-as-judge prompt template for supported-claim judging, the failure checklist from Chapter 9's table, and the weekly calibration protocol. |
| [judge_calibration.py](judge_calibration.py) | Agreement between a model judge and people on the weekly sample: agreement rate, Cohen's kappa, and the judge's bias by direction. `python judge_calibration.py --demo`. |

The rule over all of them, from Chapter 2: a metric is chosen from the decision the model exists to make and its costs, and a metric named without an operating point, a slice or a shipping rule is a red flag on the objective row.
