# Brief

Written before research begins. See the workspace docs (run `papers docs`):
research-pipeline.md §1.

## Question

Entrenched authoritarian rulers exploit a temporal asymmetry: a democratic government inherits a damaged state and is removed before slow reforms mature, while the dictator simply lasts and accumulates. Can democracy be redesigned upstream so that democratic projects outlast individual governments without making leaders irremovable?

## Claim

The democratic disadvantage is not the turnover rate (lambda) but the product of turnover and reset severity (lambda·chi), the "reset tax." A democracy can keep leaders fully disposable (high lambda) while making institutions persistent (low chi), and doing so closes most of the strategic-capacity gap with an autocracy, extends the reform horizon it can finance, and converts a self-destructing alternation into a self-sustaining one — none of which requires entrenching anyone. Continuity belongs in the architecture, not in a ruler's tenure.

## Kind

Formal-model — ships a simulation; `has_simulation: true`, `claims_target: results.json`.

Instrument choice: the seed recommends an attack-graph Monte-Carlo simulator (5 channels, multi-key gates, common-mode capture, minimum cut). That was deliberately declined because it rhymes structurally with the corpus's age-of-impunity (weakest-link accountability chain + adversarial capture). Instead the paper takes the seed's analytic core — stochastic capital accumulation with Poisson jump resets, a piecewise-deterministic Markov process — an instrument the corpus has not used, whose headline is a decomposition-and-lever result rather than another threshold or negative identification.

## Cornerstone literature

Besley and Persson (state capacity as forward-looking investment); Fearon and Przeworski (self-enforcing democracy, the removability floor); Alesina and Tabellini (strategic constraint of successors); Bermeo, Levitsky and Ziblatt, Ginsburg and Huq, Maeda (modes of backsliding); Boese et al. and V-Dem (the empirical scale and the ~80% breakdown rate); Guedes-Neto and Peters (bureaucratic resistance / fragility); Ostrom (polycentric redundancy); Aubin (viability theory); Acemoglu and Robinson (the narrow corridor); International IDEA, Venice Commission, OSCE, and the German Basic Law (the concrete capture-resistant levers).
