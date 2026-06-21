# disposable-rulers-persistent-institutions

A democracy and an entrenched dictatorship do not race on the same clock: a new government inherits a damaged state, needs years for reforms to mature, and is removed before they show, while the autocrat simply lasts and accumulates. The intuitive fix, a strong leader who stays long enough to finish, builds the vehicle the next illiberal government will drive. This paper prices the right fix with one instrument: strategic capacity is a stock that accumulates continuously and is knocked down at each change of government, a piecewise-deterministic Markov process with long-run mean K* = u/(delta + lambda·chi). The disadvantage is not the turnover rate lambda but the product lambda·chi, the "reset tax." Cutting reset severity chi from 0.8 to 0.1 at fixed turnover lifts a democracy from 0.22 to 0.73 of an autocracy's capacity (90% of the excess gap) and steadies it 5-fold; it more than triples the reform horizon a government can finance (5.5 to 18.5 years); it answers why alternation is not self-correcting (build-slow, destroy-fast drift, ~80% breakdown) and how to fix it (faster repair, earlier resistance, both low chi); and it shows that matching autocratic continuity by entrenchment needs 32-year leaders, while the reset route keeps 4-year leaders and still buys 73% of the continuity at 5x the removability. High personnel turnover, low institutional reset. Ships a runnable simulation whose output carries every modelled number.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build disposable-rulers-persistent-institutions`.

## Simulation

```bash
cd simulation && uv run run_all.py   # -> output/results.json, output/figures/
```

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
