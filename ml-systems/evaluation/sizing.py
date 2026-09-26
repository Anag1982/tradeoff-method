"""The three evaluation sizes the book derives.

    python sizing.py judged 0.9 0.02          # judged set: rate p, difference to detect
    python sizing.py ab 0.10 0.005 --sd 0.3    # A/B: baseline mean, absolute lift to detect, unit sd
    python sizing.py prevalence 0.0005 0.2     # prevalence sample: prevalence, relative half-width

judged:     n = 4 p(1-p) / d^2, so that 2*sqrt(p(1-p)/n) equals d (Chapter 9).
ab:         per-arm n = 2 (z_a + z_b)^2 sd^2 / lift^2 at 95% two-sided and 80% power;
            for a binary outcome pass --sd sqrt(p(1-p)).
prevalence: n = z^2 (1-p) / (h^2 p) views per period for a 95% interval of relative
            half-width h (Chapter 12, Exercise 4).
"""
import math, sys, argparse

def judged(p, d):
    return math.ceil(4 * p * (1 - p) / d ** 2)

def ab(baseline, lift, sd, alpha=0.05, power=0.8):
    za, zb = 1.96, 0.8416
    n = 2 * (za + zb) ** 2 * sd ** 2 / lift ** 2
    return math.ceil(n)

def prevalence(p, h, z=1.96):
    return math.ceil(z * z * (1 - p) / (h * h * p))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd")
    j = sub.add_parser("judged"); j.add_argument("p", type=float); j.add_argument("d", type=float)
    a = sub.add_parser("ab"); a.add_argument("baseline", type=float); a.add_argument("lift", type=float); a.add_argument("--sd", type=float, default=None)
    pr = sub.add_parser("prevalence"); pr.add_argument("p", type=float); pr.add_argument("h", type=float, nargs="?", default=0.2)
    x = ap.parse_args()
    if x.cmd == "judged":
        n = judged(x.p, x.d)
        print(f"judged set: n = {n} to resolve a difference of {x.d:.3f} at p = {x.p}")
        for m in (300, 1000, 2000, 5000):
            print(f"  a set of {m:>5} resolves about {2*math.sqrt(x.p*(1-x.p)/m):.3f}")
    elif x.cmd == "ab":
        sd = x.sd if x.sd is not None else math.sqrt(x.baseline * (1 - x.baseline))
        n = ab(x.baseline, x.lift, sd)
        print(f"A/B: {n:,} units per arm (sd {sd:.4f}) to detect an absolute lift of {x.lift} on a baseline of {x.baseline}")
        print(f"  relative lift {x.lift/x.baseline:.1%}; at 1,000 units a day per arm that is {n/1000:.0f} days")
    elif x.cmd == "prevalence":
        n = prevalence(x.p, x.h)
        print(f"prevalence sample: {n:,} views per period for a 95% interval of +-{x.h:.0%} at prevalence {x.p}")
        print(f"  at 300 decisions a day that is {n/7/300:.1f} reviewers full time for a weekly read")
    else:
        print(__doc__)
