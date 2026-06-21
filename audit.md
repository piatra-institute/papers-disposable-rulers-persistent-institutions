# Audit

Dated log of editorial passes and verification runs. Newest first.
See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-06-21 — Initial implementation from seed chat
Scope: full paper built from `chats/chat.md` (a four-turn ChatGPT deep-research thread on countering entrenched autocrats, with a large menu of candidate mathematics) through the PIATRA pipeline.
Decision: ships a simulation in a frame the corpus has not used — a piecewise-deterministic Markov process (stochastic capital accumulation with Poisson jump resets). The seed's own recommendation, an attack-graph Monte-Carlo simulator with multi-key gates / common-mode capture / minimum cut, was DECLINED because it rhymes structurally with age-of-impunity (weakest-link chain + adversarial capture). Taking the seed's analytic core instead keeps the set from sounding like one instrument and yields a decomposition-and-lever result rather than another threshold / negative-identification.
Changes:
  - Lifted the seed's reset model K* = u/(delta + lambda·chi) and made its four faces computable in one process: (1) RESET TAX — the disadvantage is the product lambda·chi, not lambda; cutting chi 0.8→0.1 at fixed lambda lifts capacity 0.22→0.73 (autocrat 4.5x→1.36x ahead), removes 90% of the excess gap, and cuts relative volatility 0.69→0.13 (Monte-Carlo confirms the analytic mean to 3 sig figs). (2) HORIZON — tau* = ln(B/C)/(rho+lambda·chi); financeable horizon 5.5→18.5 yr (autocracy 25.2); a 15-yr mission needs benefit/cost 42.5x (high-reset) vs 3.1x (low-reset). (3) DRIFT — build-slow/destroy-fast asymmetry; sustain threshold (1-phi)/phi = 1.86 at phi=0.35; 83% breakdown at destroy/build~3 (beside Boese et al.'s ~80%), cured to 34% (faster repair) or 15% (earlier resistance). (4) TWO CLOCKS — matching autocratic continuity by tenure needs 32-yr leaders; the reset route keeps 4-yr leaders at 0.73 capacity and 5x removability.
  - Built simulation/ (numpy + matplotlib, uv): analyses.py (4 studies + exact-propagation PDMP Monte-Carlo), figures.py (3 two-panel figures), run_all.py. Seeded (SEED=20260621); reproducible.
  - Wrote PAPER.md (8 sections, argument-driven distinctive titles, no ceremonial intro/lit/conclusion; objections and claim-strength folded into §8 "What the Model Will Not Tell You"); metadata.yaml; brief/research/sources; README.
  - Calibration choice (Study 3): set destroy/build median at 3 (not 4) so the breakdown share lands at 83%, beside the empirical ~80%, rather than an over-tuned exact match; reported the lever values honestly.
  - 19-source bibliography, all engaged in-text, verified in a dedicated pass against publisher pages / CrossRef. Two corrections applied: the ~80% breakdown figure attributed to Boese et al. (2021), not V-Dem 2026 (whose own figure is ~70%); an undateable Gailmard "capacity traps" working paper dropped in favor of published anchors (Besley & Persson; Guedes-Neto & Peters). 0 confabulated (refs MISSING = 0).
Verification:
  - voice: 0 errors, 10 review-candidate warns (negate-pivot / inline-contrastive, intrinsic to the argument). Reworded a "the whole story" pet phrase and thinned "honest".
  - refs: 0 missing, 0 unused (19 in-text keys, 19 bib entries; fixed the Basic Law in-text key to carry its year).
  - claims: 23 prose decimals, 0 without a matching results.json value.
  - build: 10 pages, 0 missing-character warnings.
  - check => PASS
