"""Capacity toolkit for The Tradeoff Method.

Seven small calculators that fill the envelope of Chapter 4. Unit prices and
capacities come from prices.json in this directory; edit that file, not this
one, when cloud pricing moves.

    python capacity.py demo          # runs the notification-service envelope
    python -c "import capacity as c; print(c.rate(20e6, 5))"

Every function returns plain numbers; round them yourself to one significant
figure, as the book does, before saying them aloud.
"""
import json, math, os

_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "prices.json")) as _f:
    P = json.load(_f)

DAY_S = 1e5          # the book's day: 86,400 rounded to 10^5
MONTH_S = 2.6e6
YEAR_S = 3e7

# ---- rate ----------------------------------------------------------------
def rate(daily_users, actions_per_user_per_day, peak_multiple=5):
    """Average and peak events per second from daily users and actions."""
    avg = daily_users * actions_per_user_per_day / DAY_S
    return {"avg_per_s": avg, "peak_per_s": avg * peak_multiple}

def burst(total_events, window_s):
    """Rate of a burst that must complete inside a window (a campaign, a sale)."""
    return total_events / window_s

# ---- stored --------------------------------------------------------------
def stored(events_per_day, bytes_each, retention_days, replicas=1):
    """Bytes held at the end of the retention period, with replicas."""
    b = events_per_day * bytes_each * retention_days * replicas
    return {"bytes": b, "TB": b / 1e12, "usd_per_month_object": b / 1e12 * P["storage_usd_per_tb_month"]["object"],
            "usd_per_month_block": b / 1e12 * P["storage_usd_per_tb_month"]["block"],
            "nodes_at_usable_disk": math.ceil(b / 1e12 / P["per_node"]["usable_disk_tb"])}

# ---- moved ---------------------------------------------------------------
def moved(events_per_s, bytes_each):
    """Bytes per second and per day, with egress cost at list and CDN rates."""
    bps = events_per_s * bytes_each
    per_day_gb = bps * DAY_S / 1e9
    return {"bytes_per_s": bps, "GB_per_day": per_day_gb,
            "egress_usd_per_day_list": per_day_gb * P["egress_usd_per_gb"]["internet_list"],
            "egress_usd_per_day_cdn": per_day_gb * P["egress_usd_per_gb"]["cdn_negotiated"]}

# ---- latency budget ------------------------------------------------------
def latency_budget(total_ms, hops):
    """Split a budget across named hops; report the headroom left for the tail.

    hops: dict of {name: ms}. Returns the allocation, headroom, and the largest hop.
    """
    used = sum(hops.values())
    largest = max(hops, key=hops.get)
    return {"total_ms": total_ms, "allocated_ms": used, "headroom_ms": total_ms - used,
            "largest_hop": largest, "largest_hop_ms": hops[largest],
            "sequential_repeat_breaks_budget": hops[largest] * 2 + (used - hops[largest]) > total_ms}

def fanout_tail(n, p_slow_each=0.01):
    """Probability a fan-out to n services is slow if each is slow with p_slow_each."""
    return 1 - (1 - p_slow_each) ** n

def chain_availability(n, a_each=0.999):
    """Availability of a synchronous chain of n components each available a_each."""
    return a_each ** n

# ---- cost per thousand ---------------------------------------------------
def cost_per_thousand(cpu_ms=0.0, bytes_stored=0, retention_months=0, bytes_egress=0, cdn=False):
    """Compute + storage + egress per thousand requests, and which term dominates."""
    compute = cpu_ms / 1000 / 3600 * P["compute"]["vcpu_usd_per_hour"] * 1000
    storage = bytes_stored / 1e12 * P["storage_usd_per_tb_month"]["object"] * retention_months * 1000
    rate_e = P["egress_usd_per_gb"]["cdn_negotiated" if cdn else "internet_list"]
    egress = bytes_egress / 1e9 * rate_e * 1000
    terms = {"compute": compute, "storage": storage, "egress": egress}
    return {**terms, "total_usd_per_1000": sum(terms.values()), "dominant": max(terms, key=terms.get)}

def people_cost(hours_per_year):
    """The line candidates omit: engineer hours a year, priced."""
    return {"usd_per_year": hours_per_year * P["people"]["engineer_usd_per_hour"],
            "usd_per_month": hours_per_year * P["people"]["engineer_usd_per_hour"] / 12}

# ---- backlog (Chapter 10) ------------------------------------------------
def backlog(arrival_per_s, service_per_s, duration_s):
    """Queue depth after a burst, and the drain time once arrivals return to arrival_after."""
    depth = max(0.0, (arrival_per_s - service_per_s) * duration_s)
    return {"peak_depth": depth}

def drain_time(depth, service_per_s, arrival_per_s):
    """Seconds to drain a backlog; infinite if service does not exceed arrivals."""
    margin = service_per_s - arrival_per_s
    return math.inf if margin <= 0 else depth / margin

def little(arrival_per_s, time_in_system_s):
    """Little's law: items in the system."""
    return arrival_per_s * time_in_system_s

def workers(events_per_s, seconds_each):
    """Consumer pool size to keep up."""
    return events_per_s * seconds_each

# ---- compare to a capacity ----------------------------------------------
def nodes_for(rate_per_s, per_node_key):
    """How many nodes of a kind (see prices.json per_node) a rate needs."""
    return math.ceil(rate_per_s / P["per_node"][per_node_key])

def sig(x, n=1):
    """Round to n significant figures, the way the book says numbers aloud."""
    if x == 0 or not math.isfinite(x):
        return x
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))

# ---- demo ----------------------------------------------------------------
def _demo():
    print("Notification service (Chapters 3, 4, 10, 12)")
    r = rate(20e6, 5, peak_multiple=5)
    print(f"  rate: {sig(r['avg_per_s'],2)}/s average, {sig(r['peak_per_s'],2)}/s peak")
    b = burst(20e6, 600)
    print(f"  marketing burst: {sig(b,2)}/s for 10 minutes")
    s = stored(100e6, 200, 30)
    print(f"  inbox, 30 days: {sig(s['TB'],2)} TB")
    print(f"  in flight at 20 ms: {sig(little(33000, 0.02))} sends")
    d = backlog(33000, 14000, 600)
    print(f"  backlog peak: {sig(d['peak_depth'],3)}; drain: {sig(drain_time(d['peak_depth'], 14000, 0)/60,2)} min after the burst")
    print(f"  providers at 20k/s clear 20M in {sig(20e6/20000/60,2)} min; the 10-minute window is infeasible")
    print("Video platform (Chapter 12)")
    m = moved(1000, 110e6)
    print(f"  egress: {sig(m['GB_per_day']/1e6,2)} PB/day, ${sig(m['egress_usd_per_day_list'],2)}/day at list, ${sig(m['egress_usd_per_day_cdn'],2)}/day through a CDN")
    print("Fan-out tail: 10 services ->", sig(fanout_tail(10),2), "; chain of 5 at 99.9% ->", sig(chain_availability(5),4))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        _demo()
    else:
        print(__doc__)
