"""Figures for Disposable Rulers, Persistent Institutions.

Three figures, one per substantive result. Imported by run_all.py; each takes
the results dict and a path.
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from analyses import kstar, eff_decay, U, DELTA, RHO, DEM_HIGH, DEM_LOW, AUTOCRACY


def plot_reset_tax(results: dict, path: str) -> None:
    rt = results["reset_tax"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))

    # Panel A: K* as a function of reset severity chi, at democratic turnover.
    chi = np.linspace(0.0, 1.0, 300)
    ax1.plot(chi, [kstar(DEM_HIGH["lam"], c) for c in chi], color="#1b3a5b", lw=2)
    for r, col, lab in ((DEM_HIGH, "#c0392b", "high-reset\n(chi=0.80)"),
                        (DEM_LOW, "#27ae60", "low-reset\n(chi=0.10)")):
        ax1.scatter([r["chi"]], [kstar(r["lam"], r["chi"])], color=col, zorder=5, s=55)
        ax1.annotate(lab, (r["chi"], kstar(r["lam"], r["chi"])),
                     textcoords="offset points", xytext=(8, 6), fontsize=8.5, color=col)
    ax1.set_xlabel("reset severity  chi  (fraction of capacity lost per turnover)")
    ax1.set_ylabel("long-run strategic stock  K*")
    ax1.set_title("Same elections, same removability: the stock is set by chi", fontsize=10)
    ax1.grid(alpha=0.25)

    # Panel B: the (lambda, chi) plane; iso-capacity hyperbolae lambda*chi=const;
    # the two routes out of the high-reset democracy.
    lam = np.linspace(0.02, 0.30, 200)
    for tax, ls in ((0.20, ":"), (0.025, "--"), (0.005, "-")):
        ax2.plot(lam, tax / lam, color="#7f8c8d", ls=ls, lw=1.2,
                 label=f"reset tax lambda*chi = {tax:g}")
    ax2.scatter([DEM_HIGH["lam"]], [DEM_HIGH["chi"]], color="#c0392b", s=55, zorder=5)
    ax2.scatter([DEM_LOW["lam"]], [DEM_LOW["chi"]], color="#27ae60", s=55, zorder=5)
    ax2.scatter([AUTOCRACY["lam"]], [AUTOCRACY["chi"]], color="#2c3e50", s=55, zorder=5)
    # reset route (cut chi, hold lambda) and tenure route (cut lambda, hold chi)
    ax2.annotate("", xy=(DEM_LOW["lam"], DEM_LOW["chi"]),
                 xytext=(DEM_HIGH["lam"], DEM_HIGH["chi"]),
                 arrowprops=dict(arrowstyle="->", color="#27ae60", lw=2))
    tc = results["two_clocks"]
    ax2.annotate("", xy=(tc["lam_needed"], DEM_HIGH["chi"]),
                 xytext=(DEM_HIGH["lam"], DEM_HIGH["chi"]),
                 arrowprops=dict(arrowstyle="->", color="#8e44ad", lw=2))
    ax2.text(DEM_LOW["lam"] + 0.005, DEM_LOW["chi"] - 0.07, "reset route\n(keep leaders\ndisposable)",
             fontsize=8, color="#27ae60")
    ax2.text(tc["lam_needed"] - 0.005, DEM_HIGH["chi"] - 0.16,
             f"tenure route\n(entrench:\n{tc['r_tenure_needed']}-yr leaders)",
             fontsize=8, color="#8e44ad", ha="left")
    ax2.set_xlabel("leader turnover  lambda  (per year)")
    ax2.set_ylabel("reset severity  chi")
    ax2.set_ylim(0, 1.02)
    ax2.set_title("Two routes to continuity", fontsize=10)
    ax2.legend(fontsize=7.5, loc="upper right")
    ax2.grid(alpha=0.25)

    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def plot_horizon(results: dict, path: str) -> None:
    h = results["horizon"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))

    # Panel A: longest financeable horizon tau* vs the reform hazard.
    haz = np.linspace(0.05, 0.30, 200)
    ax1.plot(haz, np.log(h["benefit_cost"]) / haz, color="#1b3a5b", lw=2)
    for key, col, lab in (("high-reset democracy", "#c0392b", "high-reset"),
                          ("low-reset democracy", "#27ae60", "low-reset"),
                          ("autocracy", "#2c3e50", "autocracy")):
        d = h["detail"][key]
        ax1.scatter([d["hazard"]], [d["tau_star"]], color=col, s=55, zorder=5)
        ax1.annotate(f"{lab}\n{d['tau_star']:.1f} yr", (d["hazard"], d["tau_star"]),
                     textcoords="offset points", xytext=(8, 2), fontsize=8.5, color=col)
    ax1.set_xlabel("reform hazard  rho + lambda*chi")
    ax1.set_ylabel("longest financeable horizon  tau*  (years)")
    ax1.set_title("How far ahead a regime can see (benefit/cost = 4)", fontsize=10)
    ax1.grid(alpha=0.25)

    # Panel B: benefit multiple a 15-year reform must clear to survive.
    keys = ["high-reset democracy", "low-reset democracy", "autocracy"]
    labs = ["high-reset\ndemocracy", "low-reset\ndemocracy", "autocracy"]
    vals = [h["detail"][k]["req_multiple_15yr"] for k in keys]
    cols = ["#c0392b", "#27ae60", "#2c3e50"]
    bars = ax2.bar(labs, vals, color=cols)
    for b, v in zip(bars, vals):
        ax2.annotate(f"{v:.1f}x", (b.get_x() + b.get_width() / 2, v),
                     textcoords="offset points", xytext=(0, 3), ha="center", fontsize=9)
    ax2.set_ylabel("benefit/cost a 15-year reform must exceed")
    ax2.set_title("A 15-year mission: thinkable only at low reset", fontsize=10)
    ax2.grid(alpha=0.25, axis="y")

    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def plot_drift(results: dict, path: str) -> None:
    d = results["drift"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))

    # Panel A: the sustain threshold. Net drift sign vs destroy/build ratio,
    # for several capture time-shares phi.
    ratio = np.linspace(0.5, 8.0, 200)
    for phi, col in ((0.5, "#c0392b"), (0.35, "#e67e22"), (1 / 6, "#27ae60")):
        net = -ratio * phi + (1 - phi)        # r_D normalised to 1
        ax1.plot(ratio, net, color=col, lw=2, label=f"capture share phi = {phi:.2f}")
    ax1.axhline(0, color="#2c3e50", lw=1)
    ax1.scatter([d["median_ratio"]], [-d["median_ratio"] * d["phi"] + (1 - d["phi"])],
                color="#e67e22", s=55, zorder=5)
    ax1.set_xlabel("destroy / build ratio  d_A / r_D")
    ax1.set_ylabel("net drift of institutional integrity")
    ax1.set_title("Below the line, integrity drifts to breakdown", fontsize=10)
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.25)

    # Panel B: breakdown share and the two levers.
    labs = ["baseline\n(d/b~3,\nphi=0.35)", "faster repair\n(d/b~1.5)", "early resist\n(phi=1/6)"]
    vals = [100 * d["breakdown_frac"], 100 * d["breakdown_protected"],
            100 * d["breakdown_early"]]
    cols = ["#c0392b", "#27ae60", "#27ae60"]
    bars = ax2.bar(labs, vals, color=cols)
    for b, v in zip(bars, vals):
        ax2.annotate(f"{v:.0f}%", (b.get_x() + b.get_width() / 2, v),
                     textcoords="offset points", xytext=(0, 3), ha="center", fontsize=9)
    ax2.axhline(80, color="#7f8c8d", ls="--", lw=1)
    ax2.text(2.4, 81.5, "~80% empirical\n(Boese et al. 2021)", fontsize=7.5,
             color="#7f8c8d", ha="right")
    ax2.set_ylabel("share of capture episodes reaching breakdown (%)")
    ax2.set_ylim(0, 100)
    ax2.set_title("The same asymmetry, two ways to fix it", fontsize=10)
    ax2.grid(alpha=0.25, axis="y")

    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
