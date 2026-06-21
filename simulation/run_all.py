"""Orchestrator: reproduces every modelled number in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. The Monte-Carlo confirmation of
the analytic steady state is seeded (analyses.SEED), so the run is reproducible.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_reset_tax, plot_horizon, plot_drift

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_reset_tax(results, str(OUT / "figures" / "reset_tax.png"))
    plot_horizon(results, str(OUT / "figures" / "horizon.png"))
    plot_drift(results, str(OUT / "figures" / "drift.png"))

    rt, h, d, tc = (results["reset_tax"], results["horizon"],
                    results["drift"], results["two_clocks"])
    print("RESET TAX")
    print(f"  capacity ratio  dem/auto  (high-reset): {rt['ratio_high']:.3f} "
          f"(autocrat {rt['deficit_high']:.1f}x ahead)")
    print(f"  capacity ratio  dem/auto  (low-reset) : {rt['ratio_low']:.3f} "
          f"(autocrat {rt['deficit_low']:.2f}x ahead)")
    print(f"  excess gap removed by cutting chi      : {100*rt['gap_removed']:.0f}%")
    print(f"  Monte-Carlo mean vs analytic (low)     : "
          f"{rt['mc']['low-reset democracy']['mean']:.3f} vs "
          f"{rt['mc']['low-reset democracy']['analytic']:.3f}")
    print(f"  relative volatility CV  high -> low    : "
          f"{rt['cv_high']:.2f} -> {rt['cv_low']:.2f}")
    print("HORIZON")
    print(f"  longest financeable reform (yr)        : "
          f"high {h['tau_high']:.1f} | low {h['tau_low']:.1f} | auto {h['tau_auto']:.1f}")
    print(f"  benefit/cost a 15-yr reform must clear : "
          f"high {h['req_mult_high']:.1f}x | low {h['req_mult_low']:.1f}x | auto {h['req_mult_auto']:.2f}x")
    print("DRIFT")
    print(f"  sustain threshold (d/b) at phi={d['phi']:.2f}   : {d['crit_ratio']:.2f}")
    print(f"  breakdown share  baseline              : {100*d['breakdown_frac']:.0f}%")
    print(f"  breakdown share  faster repair / early : "
          f"{100*d['breakdown_protected']:.0f}% / {100*d['breakdown_early']:.0f}%")
    print("TWO CLOCKS")
    print(f"  tenure route needs leaders kept        : {tc['tenure_needed']:.0f} years")
    print(f"  reset route: capacity vs autocracy     : {tc['cap_ratio']:.2f}")
    print(f"  reset route: removability gain         : {tc['removability_gain']:.0f}x")


if __name__ == "__main__":
    main()
