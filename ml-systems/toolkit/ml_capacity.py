"""Cost-and-capacity toolkit for The Tradeoff Method for ML Systems.

Small calculators that fill the envelope of Chapter 3 and price the levers of
Chapter 8. Unit prices and per-accelerator capacities come from prices.json in
this directory; edit that file, not this one, when prices move. The book
prints quantities and ratios only; this is where the money is.

    python ml_capacity.py demo        # the support assistant's bill and the
                                      # serving platform's fleet, Chapters 8 and 13
    python -c "import ml_capacity as m; print(m.decode_fleet(600_000))"

Every function returns plain numbers in a dict; round them to one
significant figure, as the book does, before saying them aloud.
"""
import json, math, os

_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "prices.json")) as _f:
    P = json.load(_f)

DAY_S = 1e5        # the book's day
YEAR_H = 8760

# ---- 1. fleet from a rate ---------------------------------------------------
def fleet_on_cores(items_per_s, core_us_per_item, target_util=0.7):
    """Cores needed to score items_per_s at core_us_per_item microseconds each."""
    core_s = items_per_s * core_us_per_item / 1e6
    return {"core_seconds_per_s": core_s, "cores_at_util": math.ceil(core_s / target_util),
            "usd_per_hour": core_s / target_util * P["compute"]["core_usd_per_hour"]}

def fleet_on_accelerators(items_per_s, accel_us_per_item_batched, target_util=0.7):
    """Accelerators needed at a batched cost per item."""
    acc_s = items_per_s * accel_us_per_item_batched / 1e6
    return {"accelerator_seconds_per_s": acc_s, "accelerators_at_util": math.ceil(acc_s / target_util)}

def per_thousand(items_per_request, us_per_item, requests=1000):
    """Compute per thousand requests, in core- or accelerator-seconds (unit follows the input)."""
    return {"seconds_per_1000": items_per_request * us_per_item / 1e6 * requests}

# ---- 2. cascade stage sizing (Chapter 7) -------------------------------------
def cascade(budget_ms, stages):
    """Size each stage's candidate count from its latency share and per-item cost.

    stages: list of dicts {name, share_of_budget, us_per_item, parallel} where parallel is
    the number of items scored concurrently (batch on an accelerator, cores on a scatter).
    Returns the items each stage can score inside its share.
    """
    out = []
    for s in stages:
        ms = budget_ms * s["share_of_budget"]
        items = ms * 1000 / s["us_per_item"] * s.get("parallel", 1)
        out.append({"stage": s["name"], "ms": ms, "items_inside_budget": int(items)})
    return out

# ---- 3. generative serving (Chapters 8 and 13) --------------------------------
def decode_rate_single(params_billion, bytes_per_param=2, bandwidth_tb_s=None):
    """Tokens per second for ONE sequence: bandwidth over model bytes (memory-bound)."""
    bw = bandwidth_tb_s or P["accelerator"]["bandwidth_tb_per_s"]
    model_bytes = params_billion * 1e9 * bytes_per_param
    return {"model_gb": model_bytes / 1e9, "tokens_per_s_single": bw * 1e12 / model_bytes}

def kv_in_flight(context_tokens, params_billion=10, bytes_per_param=2, kv_bytes_per_token=None, memory_gb=None):
    """How many sequences of context_tokens fit beside the weights on one accelerator."""
    kv = kv_bytes_per_token or P["accelerator"]["kv_bytes_per_token_mid_model"]
    mem = (memory_gb or P["accelerator"]["memory_gb"]) * 1e9
    free = mem - params_billion * 1e9 * bytes_per_param
    per_seq = context_tokens * kv
    return {"free_gb": free / 1e9, "gb_per_sequence": per_seq / 1e9, "sequences_in_flight": int(free // per_seq)}

def prefill_fleet(requests_per_s, input_tokens, cached_prefix_tokens=0, tokens_per_s=None):
    """Accelerators for prefill; cached prefix tokens are not recomputed."""
    tps = tokens_per_s or P["accelerator"]["prefill_tokens_per_s_mid_model"]
    billed = max(input_tokens - cached_prefix_tokens, 0)
    return {"prefill_tokens_per_s": requests_per_s * billed, "accelerators": math.ceil(requests_per_s * billed / tps)}

def decode_fleet(output_tokens_per_s, tokens_per_s=None):
    """Accelerators for decode by throughput alone (check memory with decode_fleet_by_memory)."""
    tps = tokens_per_s or P["accelerator"]["decode_tokens_per_s_mid_model_batched"]
    return {"accelerators_by_throughput": math.ceil(output_tokens_per_s / tps)}

def decode_fleet_by_memory(requests_per_s, seconds_in_flight, context_tokens, **kw):
    """Accelerators for decode by memory: sequences in flight over sequences per accelerator."""
    per = kv_in_flight(context_tokens, **kw)["sequences_in_flight"]
    inflight = requests_per_s * seconds_in_flight
    return {"sequences_in_flight_total": inflight, "per_accelerator": per,
            "accelerators_by_memory": math.ceil(inflight / max(per, 1))}

def token_cost_per_request(input_tokens, output_tokens, cached_prefix_tokens=0):
    """Rented cost of one request, with the shared prefix billed at the cached rate."""
    t = P["tokens"]
    fresh = max(input_tokens - cached_prefix_tokens, 0)
    cost = fresh / 1e6 * t["input_usd_per_million"] + cached_prefix_tokens / 1e6 * t["input_cached_usd_per_million"] \
           + output_tokens / 1e6 * t["output_usd_per_million"]
    out_share = (output_tokens / 1e6 * t["output_usd_per_million"]) / cost if cost else 0
    return {"usd_per_request": cost, "usd_per_1000": cost * 1000, "output_share": out_share}

def accelerator_seconds_per_request(input_tokens, output_tokens, cached_prefix_tokens=0):
    """The book's unit: accelerator-seconds per request from the two rates."""
    a = P["accelerator"]
    pre = max(input_tokens - cached_prefix_tokens, 0) / a["prefill_tokens_per_s_mid_model"]
    dec = output_tokens / a["decode_tokens_per_s_mid_model_batched"]
    return {"prefill_s": pre, "decode_s": dec, "total_s": pre + dec}

# ---- 4. own against rent (Chapter 8) -----------------------------------------
def own_vs_rent(accelerators_at_peak, utilisation):
    """Yearly cost of owning a fleet sized for peak against renting what is used."""
    c = P["compute"]
    own = accelerators_at_peak * YEAR_H * c["accelerator_owned_usd_per_hour_at_full_use"]
    rent = accelerators_at_peak * utilisation * YEAR_H * c["accelerator_rented_usd_per_hour"]
    return {"own_usd_per_year": own, "rent_usd_per_year": rent, "own_is_cheaper": own < rent,
            "breakeven_utilisation": c["accelerator_owned_usd_per_hour_at_full_use"] / c["accelerator_rented_usd_per_hour"]}

# ---- 5. vectors and indexes (Chapters 7, 12) --------------------------------
def index_memory(n_vectors, dims, bytes_per_dim=1, index="cluster"):
    """Memory for the vectors and for an index over them."""
    v = P["vectors"]
    raw = n_vectors * dims * bytes_per_dim
    mult = v["cluster_index_multiple"] if index == "cluster" else v["graph_index_multiple"]
    return {"raw_gb": raw / 1e9, "indexed_gb": raw * mult / 1e9,
            "usd_per_month_in_memory": raw * mult / 1e9 * P["storage"]["memory_usd_per_gb_month"]}

def false_match_budget(uploads_per_day, candidates_tested, wrongful_per_day_ceiling):
    """Per-pair false-match probability the threshold must deliver (Chapter 12, Exercise 5)."""
    return {"per_pair_probability": wrongful_per_day_ceiling / (uploads_per_day * candidates_tested)}

# ---- 6. labels, logs and cadence (Chapters 5, 6, 9) -------------------------
def served_feature_log(items_per_s, bytes_per_row, label_delay_days, training_window_days):
    """Retention and size of the served-feature log that makes training rows point-in-time correct."""
    days = label_delay_days + training_window_days
    per_day = items_per_s * DAY_S * bytes_per_row
    return {"retention_days": days, "gb_per_day": per_day / 1e9, "tb_total": per_day * days / 1e12,
            "usd_per_month_object": per_day * days / 1e12 * P["storage"]["object_usd_per_tb_month"]}

def retrain_cost(core_hours_per_run, runs_per_day, accelerator=False):
    """Daily and yearly cost of a retrain cadence."""
    rate = P["compute"]["accelerator_rented_usd_per_hour"] if accelerator else P["compute"]["core_usd_per_hour"]
    per_day = core_hours_per_run * runs_per_day * rate
    return {"usd_per_day": per_day, "usd_per_year": per_day * 365}

def judged_set_size(p, detectable_difference):
    """Examples needed so that 2*sqrt(p(1-p)/n) equals the difference (Chapter 9)."""
    n = 4 * p * (1 - p) / detectable_difference ** 2
    return {"n": math.ceil(n), "usd_at_human_rate": math.ceil(n) * P["labels"]["human_judgement_usd_each"]}

def prevalence_sample(prevalence, relative_halfwidth=0.2, z=1.96):
    """Views to review per period to estimate prevalence within +-relative_halfwidth (Chapter 12, Exercise 4)."""
    n = z * z * (1 - prevalence) / (relative_halfwidth ** 2 * prevalence)
    reviewers = n / 7 / P["labels"]["reviewer_decisions_per_day"]
    return {"views_per_week": math.ceil(n), "reviewers_full_time": reviewers}

def router_saving(easy_share, small_cost_fraction, false_easy=0.1, false_hard=0.1):
    """Cost of a small/large router as a fraction of all-large (Chapter 7, Chapter 14 Exercise 4)."""
    to_small = easy_share * (1 - false_hard) + (1 - easy_share) * false_easy
    return {"share_to_small": to_small, "cost_fraction": to_small * small_cost_fraction + (1 - to_small),
            "hard_requests_on_small_share": (1 - easy_share) * false_easy}

# ---- demo --------------------------------------------------------------------
def _demo():
    print("Support assistant (Chapter 8): 30,000 questions a day, 4,000 in / 300 out, 3,000 shared prefix")
    a = accelerator_seconds_per_request(4000, 300)
    print(f"  {a['total_s']:.2f} accelerator-seconds per request; "
          f"{a['total_s']*30000/3600:.1f} accelerator-hours a day; {a['total_s']*3:.2f} accelerators at 3 req/s")
    t = token_cost_per_request(4000, 300, cached_prefix_tokens=3000)
    print(f"  rented: ${t['usd_per_1000']:.2f} per thousand, output tokens are {t['output_share']:.0%} of the bill")
    o = own_vs_rent(2, 0.07)
    print(f"  own two accelerators at 7%: ${o['own_usd_per_year']:,.0f}/yr vs rent ${o['rent_usd_per_year']:,.0f}/yr "
          f"-> {'own' if o['own_is_cheaper'] else 'rent'} (break-even {o['breakeven_utilisation']:.0%})")
    print("\nServing platform (Chapter 13): 2,000 req/s, 4,000 in / 300 out, 3,000 cached")
    print("  prefill, no cache:", prefill_fleet(2000, 4000)["accelerators"], "accelerators")
    print("  prefill, cached:  ", prefill_fleet(2000, 4000, 3000)["accelerators"])
    print("  decode by throughput:", decode_fleet(2000 * 300)["accelerators_by_throughput"])
    m = decode_fleet_by_memory(2000, 6, 4300)
    print(f"  decode by memory: {m['accelerators_by_memory']} ({m['per_accelerator']} sequences per accelerator)")
    m16 = decode_fleet_by_memory(2000, 6, 16300)
    print(f"  at 16k tokens: {m16['accelerators_by_memory']} by memory ({m16['per_accelerator']} per accelerator) -- memory binds")
    print("\nCard fraud (Chapters 6, 12): served-feature log")
    print(" ", served_feature_log(10000, 800, 90, 90))
    print("\nNear-duplicate search (Chapter 12): per-pair false-match budget for 100 wrongful matches a day")
    print("  over 2B candidates:", false_match_budget(5e6, 2e9, 100)["per_pair_probability"])
    print("  over 20 verified: ", false_match_budget(5e6, 20, 100)["per_pair_probability"])
    print("\nJudged set to see a two-point regression at 90%:", judged_set_size(0.9, 0.02)["n"])
    print("Prevalence at 0.05% to +-20%:", prevalence_sample(0.0005))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        _demo()
    else:
        print(__doc__)
