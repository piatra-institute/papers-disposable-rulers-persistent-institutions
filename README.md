# Disposable Rulers, Persistent Institutions

The Reset Tax and the Continuity a Democracy Can Buy Without a Strongman.

Democracies and entrenched autocracies accumulate state capacity on different clocks: a democratic government is often removed before a long reform matures, while an autocrat holds office for decades. Extending a good leader's tenure answers the asymmetry by building the apparatus that the next illiberal government inherits. We model a state's strategic capacity (expertise, institutional memory, live alliances and unfinished reforms) as a stock that accumulates continuously and loses a fraction $\chi$ at each change of government, a piecewise-deterministic Markov process with expected long-run level $K^* = u/(\delta + \lambda\chi)$. The democratic disadvantage depends on the product $\lambda\chi$ of turnover rate and reset severity, which we call the reset tax. In an illustrative calibration with 4-year governments, cutting $\chi$ from 0.8 to 0.1 raises a democracy's long-run capacity from 0.22 to 0.73 of an autocracy's, removes about 90 percent of the excess gap, and lowers the coefficient of variation from 0.69 to 0.13, with turnover unchanged. The longest financeable reform horizon rises from 5.5 to 18.5 years, and the benefit-to-cost ratio a 15-year reform must clear falls from 42.5 to 3.1. Because institutions are built slowly and destroyed quickly, alternation between capturing and repairing governments drifts to breakdown when destruction outpaces repair; with a median threefold asymmetry, 83 percent of simulated episodes break down, and faster repair or earlier resistance lowers this to 33 or 15 percent. Matching the low-reset continuity by longer tenure would require 32-year leaders. The model calibrates no country and assumes throughout that leaders remain removable.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build disposable-rulers-persistent-institutions`.

## Simulation

```bash
cd simulation && uv run run_all.py   # -> output/results.json, output/figures/
```

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
