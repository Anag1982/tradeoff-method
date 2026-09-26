"""Offline suite scorer: metrics by slice from a CSV of predictions.

CSV columns: label (0/1), score (probability), and any number of slice columns.

    python offline_suite.py predictions.csv --slices country segment --fpr 0.002 --rule 0.60
    python offline_suite.py --demo

Reports, overall and per slice value: n, positive rate, log-loss, AUC, recall at the
fixed false-positive rate, and expected calibration error (10 bins). The shipping
rule is checked last: recall at FPR must reach --rule on the whole set AND on every
slice with at least --min-n rows. Standard library only.
"""
import csv, math, random, sys, argparse
from collections import defaultdict

def log_loss(y, p, eps=1e-12):
    return -sum(yi * math.log(max(pi, eps)) + (1 - yi) * math.log(max(1 - pi, eps)) for yi, pi in zip(y, p)) / len(y)

def auc(y, p):
    pos = [pi for yi, pi in zip(y, p) if yi == 1]; neg = [pi for yi, pi in zip(y, p) if yi == 0]
    if not pos or not neg: return float("nan")
    ranked = sorted((v, i) for i, v in enumerate(p))
    ranks = [0.0] * len(p); i = 0
    while i < len(ranked):
        j = i
        while j + 1 < len(ranked) and ranked[j + 1][0] == ranked[i][0]: j += 1
        r = (i + j) / 2 + 1
        for k in range(i, j + 1): ranks[ranked[k][1]] = r
        i = j + 1
    s = sum(ranks[i] for i, yi in enumerate(y) if yi == 1)
    return (s - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))

def recall_at_fpr(y, p, fpr):
    neg = sorted((pi for yi, pi in zip(y, p) if yi == 0), reverse=True)
    if not neg: return float("nan"), None
    k = max(int(fpr * len(neg)) - 1, 0)
    thr = neg[k] if neg else 1.0
    pos = [pi for yi, pi in zip(y, p) if yi == 1]
    if not pos: return float("nan"), thr
    return sum(1 for pi in pos if pi > thr) / len(pos), thr

def ece(y, p, bins=10):
    tot = 0.0; n = len(y)
    for b in range(bins):
        lo, hi = b / bins, (b + 1) / bins
        idx = [i for i, pi in enumerate(p) if lo <= pi < hi or (b == bins - 1 and pi == 1.0)]
        if not idx: continue
        conf = sum(p[i] for i in idx) / len(idx); acc = sum(y[i] for i in idx) / len(idx)
        tot += len(idx) / n * abs(conf - acc)
    return tot

def score(rows, slices, fpr):
    y = [int(r["label"]) for r in rows]; p = [float(r["score"]) for r in rows]
    rec, thr = recall_at_fpr(y, p, fpr)
    out = {"n": len(y), "pos_rate": sum(y) / len(y), "log_loss": log_loss(y, p), "auc": auc(y, p),
           f"recall@fpr{fpr}": rec, "ece": ece(y, p)}
    return out, thr

def run(rows, slices, fpr, rule, min_n):
    overall, thr = score(rows, slices, fpr)
    print(f"OVERALL  n={overall['n']}  pos={overall['pos_rate']:.4f}  logloss={overall['log_loss']:.4f}  "
          f"auc={overall['auc']:.4f}  recall@fpr={overall[f'recall@fpr{fpr}']:.3f}  ece={overall['ece']:.4f}")
    failures = []
    for s in slices:
        groups = defaultdict(list)
        for r in rows: groups[r[s]].append(r)
        print(f"\nby {s}:")
        for v, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            m, _ = score(g, slices, fpr)
            flag = ""
            if rule is not None and m["n"] >= min_n and m[f"recall@fpr{fpr}"] < rule:
                flag = "  <-- below the rule"; failures.append((s, v, m[f"recall@fpr{fpr}"]))
            print(f"  {str(v):<16} n={m['n']:<7} pos={m['pos_rate']:.4f}  logloss={m['log_loss']:.4f}  "
                  f"auc={m['auc']:.4f}  recall@fpr={m[f'recall@fpr{fpr}']:.3f}  ece={m['ece']:.4f}{flag}")
    if rule is not None:
        ok = overall[f"recall@fpr{fpr}"] >= rule and not failures
        print("\nSHIPPING RULE:", "PASS" if ok else "FAIL")
        if not ok:
            if overall[f"recall@fpr{fpr}"] < rule: print(f"  overall recall {overall[f'recall@fpr{fpr}']:.3f} < {rule}")
            for s, v, r in failures: print(f"  slice {s}={v}: recall {r:.3f} < {rule}")
            print("  Do not ship, whatever the average says.")

def demo():
    random.seed(1)
    rows = []
    for country in ["IE", "GB", "DE", "BR"]:
        strength = {"IE": 2.0, "GB": 2.0, "DE": 1.8, "BR": 1.0}[country]   # BR: weaker model
        for _ in range(20000):
            y = 1 if random.random() < 0.02 else 0
            z = random.gauss(strength * y, 1.0)
            p = 1 / (1 + math.exp(-(z - 3)))
            rows.append({"label": y, "score": p, "country": country})
    print("demo: synthetic fraud scores, four countries, one of them weaker\n")
    run(rows, ["country"], 0.002, 0.30, 5000)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--slices", nargs="*", default=[])
    ap.add_argument("--fpr", type=float, default=0.005)
    ap.add_argument("--rule", type=float, default=None, help="minimum recall@fpr, overall and per slice")
    ap.add_argument("--min-n", type=int, default=500)
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()
    if a.demo or not a.csv: demo(); sys.exit()
    with open(a.csv) as f: rows = list(csv.DictReader(f))
    run(rows, a.slices, a.fpr, a.rule, a.min_n)
