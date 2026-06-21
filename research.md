# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2.
T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only).
A claim that reaches the paper rests on a T1 or T2 source.

## Findings

- [T1] The reset-tax steady state K* = u/(delta + lambda·chi) follows from taking expectations of the PDMP dK = (u - delta·K)dt - chi·K·dN, N~Poisson(lambda). — derived in simulation/analyses.py — the analytical core; the disadvantage is the product lambda·chi.
- [T1] Worked example (seed): democracy lambda=0.25, autocracy lambda=0.05, delta=0.05, chi 0.8 vs 0.1 → capacity ratio 0.22 (autocrat 4.5x) rising to 0.73 (1.36x) on cutting chi alone; 90% of the excess gap removed; Monte-Carlo (20k paths) confirms the analytic mean to 3 sig figs; coefficient of variation 0.69 → 0.13. — results.json/reset_tax — Study 1.
- [T1] Reform horizon tau* = ln(B/C)/(rho+lambda·chi); at B/C=4, rho=0.05: 5.5 / 18.5 / 25.2 years (high-reset dem / low-reset dem / autocracy); a 15-year mission needs benefit/cost 42.5 / 3.1 / 2.28. — results.json/horizon — Study 2.
- [T1] Drift: integrity sustained iff d_A/r_D <= (1-phi)/phi; at phi=0.35 the threshold is 1.86; with destruction a median 3x faster than repair, 83% of episodes break down; faster repair (halve the ratio) → 34%, earlier resistance (phi→1/6) → 15%. — results.json/drift — Study 3.
- [T1] Two clocks: matching the low-reset effective decay by tenure (chi held at 0.8) needs leaders kept 32 years; the reset route keeps 4-year leaders, delivers 0.73 of autocratic capacity at 5x removability. — results.json/two_clocks — Study 4.
- [T2] Besley and Persson (2009, AER 99(4):1218–1244; 2011, Princeton): state/fiscal/legal capacity is forward-looking investment whose value depends on who governs next. — frames K as accumulated investment; the build-slow side.
- [T2] Boese et al. (2021, Democratization 28(5):885–907): once autocratization begins, only ~1 in 5 democracies avert breakdown. — verified via Taylor & Francis; the empirical anchor for Study 3's ~80%.
- [T2] V-Dem Institute (2026): ~44 countries / ~41% of world population autocratizing (current-wave breakdown ~70% in the report itself; the 80% historical figure belongs to Boese et al.). — the scale of the problem; correction logged in sources.md.
- [T2] Fearon (2011, QJE 126(4):1661–1708) and Przeworski (2010, CUP): democracy is self-enforcing via common-knowledge electoral signals and the losers' expectation of future competition. — the lambda-floor: leaders must stay removable.
- [T2] Alesina and Tabellini (1990, REStud 57(3):403–414): incumbents strategically constrain successors. — the basis for successor-only rules.
- [T2] Guedes-Neto and Peters (2025, Cambridge Elements): 942-official survey experiment; bureaucratic fidelity varies and is not reducible to formal rules. — the destroy-fast (decentralized exit) mechanism.
- [T2] Bermeo (2016), Levitsky and Ziblatt (2018), Ginsburg and Huq (2018), Maeda (2010): backsliding via executive aggrandizement / salami-slicing; two modes of breakdown. — framing of the attack.
- [T2] Ostrom, Tiebout and Warren (1961); Ostrom (1990); Aubin (1991); Acemoglu and Robinson (2019): polycentric redundancy, viability kernel, the narrow corridor. — the practice/boundary sections.
- [T3] International IDEA (2023), Venice Commission (2002), OSCE (1994), German Basic Law Art. 67: the concrete capture-resistant levers (staggered terms, slow rules, force under constitutional command, constructive vote of no confidence). — §7 mapping of dials to machinery.
