"""Disposable Rulers, Persistent Institutions — the reset tax.

One instrument runs through every study: strategic institutional capacity is a
stock that accumulates continuously and is knocked down at random by changes of
government. Formally a piecewise-deterministic Markov process,

    dK = (u - delta K) dt  -  chi K dN,      N ~ Poisson(lambda),

where u is the annual investment in continuity (expertise, memory, alliances,
half-built reforms), delta the ordinary depreciation, lambda the rate at which
governments change, and chi the fraction of the stock lost at each change. The
expected long-run stock has a closed form,

    K* = u / (delta + lambda*chi),

so a democracy's strategic disadvantage relative to a long-lived autocracy is
governed not by how often it changes leaders (lambda) but by the PRODUCT
lambda*chi, the "reset tax." Politicians can stay disposable (high lambda) while
the institutions stay persistent (low chi).

Four studies, all the same process:
  1. reset_tax       the decomposition and the lever: cut chi, not lambda
  2. horizon         the planning horizon a democracy can finance, tau*(chi)
  3. drift           why electoral alternation is not self-correcting
  4. two_clocks      the dominance of the reset route over the tenure route

Run `uv run run_all.py`. Seeded (SEED) so the Monte-Carlo confirmation of the
analytic mean is reproducible to the last digit.
"""
from __future__ import annotations

import numpy as np

SEED = 20260621

# Illustrative operating points (annual rates). u is normalised to 1, so K* is
# read as a multiple of one year's investment; only ratios are interpreted.
U = 1.0
DELTA = 0.05            # ordinary depreciation common to both regimes
RHO = 0.05             # ordinary discount rate for the reform-horizon study

# Three reference regimes from the seed's worked example.
DEM_HIGH = dict(name="high-reset democracy", lam=0.25, chi=0.80)  # 4-yr spells
DEM_LOW = dict(name="low-reset democracy", lam=0.25, chi=0.10)   # same removability
AUTOCRACY = dict(name="autocracy", lam=0.05, chi=0.10)            # 20-yr spells


def kstar(lam: float, chi: float, u: float = U, delta: float = DELTA) -> float:
    """Closed-form expected long-run strategic stock."""
    return u / (delta + lam * chi)


def eff_decay(lam: float, chi: float, delta: float = DELTA) -> float:
    return delta + lam * chi


# --------------------------------------------------------------------------- #
# Study 1 — the reset tax: decomposition and lever                            #
# --------------------------------------------------------------------------- #
def _simulate_pdmp(lam: float, chi: float, n_paths: int, horizon: float,
                   rng: np.random.Generator) -> np.ndarray:
    """Exact inter-jump propagation of the PDMP; returns terminal stocks.

    Between turnovers the stock relaxes toward u/delta:
        K(t+s) = u/delta + (K(t) - u/delta) * exp(-delta*s)
    and at a turnover K -> (1-chi)K. Inter-arrival times are Exponential(lam).
    Terminal stocks sampled past a long horizon approximate the stationary law.
    """
    target = U / DELTA
    K = np.full(n_paths, kstar(lam, chi))  # start near the mean to cut burn-in
    t = np.zeros(n_paths)
    # advance each path event by event until it passes the horizon
    for i in range(n_paths):
        ti, Ki = 0.0, K[i]
        while True:
            dt = rng.exponential(1.0 / lam)
            if ti + dt >= horizon:
                s = horizon - ti
                Ki = target + (Ki - target) * np.exp(-DELTA * s)
                break
            Ki = target + (Ki - target) * np.exp(-DELTA * dt)
            Ki = (1.0 - chi) * Ki
            ti += dt
        K[i] = Ki
    return K


def reset_tax(rng: np.random.Generator) -> dict:
    regimes = {r["name"]: r for r in (DEM_HIGH, DEM_LOW, AUTOCRACY)}
    ks = {n: kstar(r["lam"], r["chi"]) for n, r in regimes.items()}
    gd = {n: eff_decay(r["lam"], r["chi"]) for n, r in regimes.items()}

    kd_high, kd_low, ka = (ks["high-reset democracy"], ks["low-reset democracy"],
                           ks["autocracy"])
    ratio_high = kd_high / ka          # democracy capacity as a fraction of autocracy's
    ratio_low = kd_low / ka
    deficit_high = ka / kd_high        # autocrat's multiplicative advantage
    deficit_low = ka / kd_low

    # fraction of the EXCESS multiplicative gap removed by cutting chi alone
    gap_removed = (deficit_high - deficit_low) / (deficit_high - 1.0)

    # Monte-Carlo confirmation of the analytic mean + the volatility result.
    mc = {}
    for n, r in regimes.items():
        term = _simulate_pdmp(r["lam"], r["chi"], n_paths=20000, horizon=400.0,
                              rng=rng)
        mc[n] = dict(mean=float(term.mean()), sd=float(term.std()),
                     cv=float(term.std() / term.mean()), analytic=ks[n])

    return dict(
        regimes={n: dict(lam=r["lam"], chi=r["chi"], reset_tax=r["lam"] * r["chi"],
                         eff_decay=gd[n], kstar=ks[n]) for n, r in regimes.items()},
        ratio_high=ratio_high, ratio_low=ratio_low,
        deficit_high=deficit_high, deficit_low=deficit_low,
        gap_removed=gap_removed,
        reset_tax_high=DEM_HIGH["lam"] * DEM_HIGH["chi"],
        reset_tax_low=DEM_LOW["lam"] * DEM_LOW["chi"],
        reset_tax_auto=AUTOCRACY["lam"] * AUTOCRACY["chi"],
        cv_high=mc["high-reset democracy"]["cv"],
        cv_low=mc["low-reset democracy"]["cv"],
        mc=mc,
        # rounded keys so prose decimals reconcile against this file
        r_ratio_high=round(ratio_high, 2), r_ratio_low=round(ratio_low, 2),
        r_deficit_high=round(deficit_high, 1), r_deficit_low=round(deficit_low, 2),
        r_gap_removed_pct=round(100 * gap_removed),
        r_cv_high=round(mc["high-reset democracy"]["cv"], 2),
        r_cv_low=round(mc["low-reset democracy"]["cv"], 2),
    )


# --------------------------------------------------------------------------- #
# Study 2 — the horizon a democracy can finance                               #
# --------------------------------------------------------------------------- #
def horizon() -> dict:
    """A reform costs C now, returns B at tau years, is cancelled at hazard
    lambda*chi, ordinary discount rho. Net present value

        V(tau) = B*exp(-(rho+lambda*chi)*tau) - C

    is positive iff tau < tau* = ln(B/C) / (rho + lambda*chi). So the maximum
    horizon a regime can finance falls as the reset tax rises.
    """
    bc = 4.0                       # a reform whose eventual benefit is 4x its cost
    ln_bc = np.log(bc)
    fixed_tau = 15.0               # an education / infrastructure mission

    out = {}
    for r in (DEM_HIGH, DEM_LOW, AUTOCRACY):
        h = RHO + r["lam"] * r["chi"]
        tau_star = ln_bc / h                       # longest financeable horizon
        req_mult = float(np.exp(h * fixed_tau))    # B/C needed for a 15-yr reform
        out[r["name"]] = dict(hazard=h, tau_star=tau_star,
                              req_multiple_15yr=req_mult)

    th, tl, ta = (out["high-reset democracy"]["tau_star"],
                  out["low-reset democracy"]["tau_star"],
                  out["autocracy"]["tau_star"])
    return dict(
        benefit_cost=bc, fixed_tau=fixed_tau, detail=out,
        tau_high=th, tau_low=tl, tau_auto=ta,
        horizon_gain=tl / th,                       # how much cutting chi buys
        req_mult_high=out["high-reset democracy"]["req_multiple_15yr"],
        req_mult_low=out["low-reset democracy"]["req_multiple_15yr"],
        req_mult_auto=out["autocracy"]["req_multiple_15yr"],
        r_tau_high=round(th, 1), r_tau_low=round(tl, 1), r_tau_auto=round(ta, 1),
        r_horizon_gain=round(tl / th, 1),
        r_req_mult_high=round(out["high-reset democracy"]["req_multiple_15yr"], 1),
        r_req_mult_low=round(out["low-reset democracy"]["req_multiple_15yr"], 1),
        r_req_mult_auto=round(out["autocracy"]["req_multiple_15yr"], 2),
    )


# --------------------------------------------------------------------------- #
# Study 3 — the drift: alternation is not self-correcting                      #
# --------------------------------------------------------------------------- #
def drift(rng: np.random.Generator) -> dict:
    """Institutional integrity I in [0,1] alternates between capture episodes
    (I falls at rate d_A) and repair (I rises at rate r_D). Building capacity
    needs coordinated entry across cohorts and is slow; destroying it needs only
    decentralised exit and is fast (Besley & Persson; Guedes-Neto & Peters). Over
    one cycle with capture time-share phi,

        Delta I per unit time = -d_A*phi + r_D*(1-phi),

    so integrity is sustained iff d_A/r_D <= (1-phi)/phi. The critical
    destroy/build ratio is (1-phi)/phi: even perfect alternation (phi=1/2) needs
    destruction no faster than construction, which the asymmetry violates.
    """
    phi = 0.35                              # capture is the minority of the timeline
    crit_ratio = (1 - phi) / phi            # sustain threshold on d_A/r_D

    # Heterogeneous episodes: draw destroy/build ratios across a population of
    # autocratization attempts and integrate integrity to the absorbing floor.
    n = 40000
    median_ratio = 3.0                      # destruction ~3x faster than repair
    ratios = median_ratio * np.exp(0.5 * rng.standard_normal(n))  # lognormal
    # net drift per unit time for each episode at the same phi, r_D normalised to 1
    r_D = 1.0
    d_A = ratios * r_D
    net = -d_A * phi + r_D * (1 - phi)
    breakdown_frac = float((net < 0).mean())  # share whose integrity drifts to 0

    # the lever: protect capacity so repair is faster / episodes shorter
    def bf(med, ph):
        rr = med * np.exp(0.5 * rng.standard_normal(n))
        return float((-rr * ph + (1 - ph) < 0).mean())

    bf_protected = bf(1.5, phi)             # halve the asymmetry (repair twice as fast)
    bf_early = bf(median_ratio, 1.0 / 6)    # resist early: capture share -> 1/6

    return dict(
        phi=phi, crit_ratio=crit_ratio, median_ratio=median_ratio,
        breakdown_frac=breakdown_frac,
        breakdown_protected=bf_protected, breakdown_early=bf_early,
        r_crit_ratio=round(crit_ratio, 2),
        r_breakdown_pct=round(100 * breakdown_frac),
        r_breakdown_protected_pct=round(100 * bf_protected),
        r_breakdown_early_pct=round(100 * bf_early),
    )


# --------------------------------------------------------------------------- #
# Study 4 — the two clocks: reset route dominates tenure route                 #
# --------------------------------------------------------------------------- #
def two_clocks() -> dict:
    """To match a low-reset democracy's continuity, how long must a high-reset
    democracy keep its leaders? Hold chi at the high value 0.80 and solve for the
    lambda that reproduces the low-reset effective decay; invert to a tenure.
    """
    target_decay = eff_decay(DEM_LOW["lam"], DEM_LOW["chi"])   # 0.075
    # tenure route: same target via lambda at fixed high chi
    lam_needed = (target_decay - DELTA) / DEM_HIGH["chi"]
    tenure_needed = 1.0 / lam_needed                            # years per leader
    autocrat_tenure = 1.0 / AUTOCRACY["lam"]                    # 20 years
    dem_tenure = 1.0 / DEM_LOW["lam"]                           # 4 years

    # what the reset route delivers: capacity vs autocracy, removability gain
    cap_ratio = kstar(DEM_LOW["lam"], DEM_LOW["chi"]) / kstar(*[AUTOCRACY[k] for k in ("lam", "chi")])
    removability_gain = DEM_LOW["lam"] / AUTOCRACY["lam"]       # 5x

    return dict(
        target_decay=target_decay, lam_needed=lam_needed,
        tenure_needed=tenure_needed, autocrat_tenure=autocrat_tenure,
        dem_tenure=dem_tenure, cap_ratio=cap_ratio,
        removability_gain=removability_gain,
        r_tenure_needed=round(tenure_needed),
        r_cap_ratio=round(cap_ratio, 2),
        r_removability_gain=round(removability_gain),
    )


def run() -> dict:
    rng = np.random.default_rng(SEED)
    return dict(
        seed=SEED,
        params=dict(u=U, delta=DELTA, rho=RHO),
        reset_tax=reset_tax(rng),
        horizon=horizon(),
        drift=drift(rng),
        two_clocks=two_clocks(),
    )
