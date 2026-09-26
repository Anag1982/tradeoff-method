"""Agreement between a model judge and people on the weekly calibration sample.

CSV columns: judge, human (verdict labels, any strings). Optional: human2 for
inter-annotator agreement.

    python judge_calibration.py sample.csv
    python judge_calibration.py --demo

Reports agreement rate, Cohen's kappa, the confusion table, and the judge's
bias by direction. Standard library only.
"""
import csv, sys, random
from collections import Counter, defaultdict

def kappa(a, b):
    n = len(a); labels = sorted(set(a) | set(b))
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[l] / n * cb[l] / n for l in labels)
    return (po - pe) / (1 - pe) if pe < 1 else float("nan"), po

def report(judge, human, human2=None):
    k, po = kappa(judge, human)
    print(f"n = {len(judge)}   agreement = {po:.3f}   Cohen's kappa = {k:.3f}")
    if human2:
        k2, po2 = kappa(human, human2)
        print(f"people with each other: agreement = {po2:.3f}   kappa = {k2:.3f}   (a judge cannot beat this)")
    labels = sorted(set(judge) | set(human))
    conf = defaultdict(Counter)
    for j, h in zip(judge, human): conf[h][j] += 1
    print("\nconfusion (rows: people; columns: judge)")
    print("  " + " " * 12 + "".join(f"{l:>12}" for l in labels))
    for h in labels: print(f"  {h:<12}" + "".join(f"{conf[h][j]:>12}" for j in labels))
    print("\nbias by direction (where the judge and people differ):")
    diffs = Counter((h, j) for j, h in zip(judge, human) if j != h)
    for (h, j), c in diffs.most_common():
        print(f"  people said {h:<10} judge said {j:<10} {c:>4} times")
    lenient = sum(c for (h, j), c in diffs.items() if h in ("PARTIAL", "LEAK") and j == "SUPPORTED")
    strict = sum(c for (h, j), c in diffs.items() if h == "SUPPORTED" and j in ("PARTIAL", "LEAK"))
    if lenient or strict:
        print(f"\n  lenient (misses an unsupported claim): {lenient}   strict (flags a supported one): {strict}")
        print("  a judge drifting lenient is the failure that shows nowhere else; watch this number week on week")

def demo():
    random.seed(2)
    truth = random.choices(["SUPPORTED", "PARTIAL", "ABSTAINED", "LEAK"], weights=[70, 20, 8, 2], k=300)
    def noisy(t, lenient=0.0):
        r = random.random()
        if t in ("PARTIAL", "LEAK") and r < 0.15 + lenient: return "SUPPORTED"
        if t == "SUPPORTED" and r < 0.04: return "PARTIAL"
        return t
    judge = [noisy(t, lenient=0.10) for t in truth]
    human2 = [noisy(t) for t in truth]
    print("demo: 300 synthetic verdicts; the judge is drifting lenient\n")
    report(judge, truth, human2)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--demo": demo(); sys.exit()
    with open(sys.argv[1]) as f: rows = list(csv.DictReader(f))
    report([r["judge"] for r in rows], [r["human"] for r in rows], [r["human2"] for r in rows] if "human2" in rows[0] else None)
