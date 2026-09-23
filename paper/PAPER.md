---
title: |
  Disposable Rulers, Persistent Institutions:\
  The Reset Tax and the Continuity a Democracy Can Buy Without a Strongman
author: PIATRA . INSTITUTE
date: June 2026
---

## Abstract

Democracies and entrenched autocracies accumulate state capacity on different clocks: a democratic government is often removed before a long reform matures, while an autocrat holds office for decades. Extending a good leader's tenure answers the asymmetry by building the apparatus that the next illiberal government inherits. We model a state's strategic capacity (expertise, institutional memory, live alliances and unfinished reforms) as a stock that accumulates continuously and loses a fraction $\chi$ at each change of government, a piecewise-deterministic Markov process with expected long-run level $K^* = u/(\delta + \lambda\chi)$. The democratic disadvantage depends on the product $\lambda\chi$ of turnover rate and reset severity, which we call the reset tax. In an illustrative calibration with 4-year governments, cutting $\chi$ from 0.8 to 0.1 raises a democracy's long-run capacity from 0.22 to 0.73 of an autocracy's, removes about 90 percent of the excess gap, and lowers the coefficient of variation from 0.69 to 0.13, with turnover unchanged. The longest financeable reform horizon rises from 5.5 to 18.5 years, and the benefit-to-cost ratio a 15-year reform must clear falls from 42.5 to 3.1. Because institutions are built slowly and destroyed quickly, alternation between capturing and repairing governments drifts to breakdown when destruction outpaces repair; with a median threefold asymmetry, 83 percent of simulated episodes break down, and faster repair or earlier resistance lowers this to 33 or 15 percent. Matching the low-reset continuity by longer tenure would require 32-year leaders. The model calibrates no country and assumes throughout that leaders remain removable.

## 1. Introduction

A newly elected government in a country with hollowed-out institutions replaces the senior staff, reconstructs what its predecessor knew, renegotiates the coalition, rebrands inherited projects and starts the reforms it promised. Education, infrastructure, an honest tax administration and a working court system mature over 10 or 15 years, and voters judge the government on the conditions they see within 4. If the reforms have not yet produced results, the government is removed, and its successor begins from the same low base. In a neighbouring state, a ruler who took power through a coup or a captured election stays in office, controls the army, the broadcaster and the prosecutor, and adds to the apparatus in each year that the democracy spends restarting.

This asymmetry makes a slow authoritarian advance hard to counter. A democratic government is a temporary player and invests like one. An autocrat is a persistent player and invests in cadres, media, intelligence and long relationships that outlast elections abroad. The scale of the problem is large. The V-Dem Institute's 2026 report counts 44 countries, holding about 41 percent of the world's population, in some phase of autocratization, and earlier work on the same data found that once autocratization begins inside a democracy, only about one in five democracies recover [@vdem2026; @boese2021]. The usual mode of attack is executive aggrandizement, the incremental and legalistic capture of the referees, proceeding in steps each too small to trigger a response [@bermeo2016; @levitsky2018; @ginsburg2018].

The obvious response is symmetry: if the autocrat gains by lasting, the reforming government should last as well, through weaker term limits, longer emergency powers and competent officials kept in place. The objection is structural. A state designed to retain a good leader will retain the next leader too, who may be the person the design was meant to stop. A democracy facing a 20-year autocrat therefore needs a 20-year project that survives 5 different governments: continuity moved from the ruler into the institutions, with the ruler as removable as before.

The model below gives this proposal an arithmetic, so that its trade-offs are visible and continuity has a numerical measure. It is a single stochastic process examined in four ways: the long-run stock, the financeable reform horizon, the drift of institutional integrity under alternation, and the comparison between longer tenure and lower reset severity.

## 2. Model

Let $K_t$ be a state's strategic capacity at time $t$: its working stock of expertise, institutional memory, live alliances, administrative routine and reform progress, the resources that let it pursue goals longer than one term. The written constitution is excluded. Two forces act on the stock continuously. The state invests at rate $u$ per year, and capacity depreciates at rate $\delta$, the ordinary forgetting and obsolescence that would occur even under a single uninterrupted government. Between changes of government the stock follows

$$\dot K_t = u - \delta K_t,$$

relaxing toward the level $u/\delta$ that investment alone would sustain.

A change of government is a discrete event at which a fraction $\chi$ of the accumulated stock is lost: staff are replaced, unfinished projects are shelved or rebranded, relationships are reset and records are mislaid. If turnovers arrive as a Poisson process $N_t$ with rate $\lambda$, the dynamics are

$$dK_t = (u - \delta K_t)\,dt - \chi K_{t^-}\,dN_t,$$

a piecewise-deterministic Markov process with smooth accumulation between shocks and multiplicative losses at random times. Taking expectations converts the jump term into a continuous drain at rate $\lambda\chi$,

$$\frac{d\,\mathbb{E}[K_t]}{dt} = u - (\delta + \lambda\chi)\,\mathbb{E}[K_t],$$

so the expected long-run stock is

$$\boxed{\,K^* = \frac{u}{\delta + \lambda\chi}\,.}$$

The denominator contains the main result. A democracy's strategic disadvantage depends on the product $\lambda\chi$ of turnover frequency and reset severity, and the two factors differ in kind. The rate $\lambda$ is the price of accountability, the rate at which voters can replace a government, and lowering it keeps bad leaders in office longer. The fraction $\chi$ is a loss with no democratic function: the share of accumulated public capacity that a transition destroys. The state-capacity literature treats capacity as a forward-looking investment whose value depends on who will hold power next [@besley2009; @besley2011]; the reset tax describes that investment when the holder changes on a schedule and the handover loses part of it. The design target follows: keep $\lambda$ high and reduce $\chi$.

## 3. Results

### 3.1 Long-run capacity and volatility

The calibration is illustrative. A democracy changes government on average every 4 years ($\lambda = 0.25$) and an autocracy every 20 ($\lambda = 0.05$); ordinary depreciation $\delta = 0.05$ is common to both; a poorly designed democratic transition loses most of what it inherited ($\chi = 0.8$), and an autocratic succession loses little ($\chi = 0.1$). The effective decay rates are 0.25 for the democracy and 0.055 for the autocracy, and with equal annual investment the democracy holds 0.22 of the autocracy's long-run capacity. The autocracy is about 4.5 times ahead.

Holding elections equally frequent ($\lambda = 0.25$) and lowering the reset from $\chi = 0.8$ to $\chi = 0.1$, by the administrative means listed in Section 4, reduces the democratic effective decay to 0.075. The capacity ratio rises from 0.22 to 0.73, and the autocracy's advantage falls from 4.5-fold to 1.36-fold. About 90 percent of the excess gap above parity is removed, and no politician has become harder to remove.

The same change reduces variance. $K^*$ is the mean of a stationary distribution, and a high-reset democracy both sits lower and fluctuates more, falling at each turnover and recovering between them. Direct simulation of 20,000 sample paths over 400 years reproduces the analytic means to within 0.4 percent and measures the spread. The coefficient of variation falls from 0.69 at $\chi = 0.8$ to 0.13 at $\chi = 0.1$, so a low-reset democracy is about 5 times steadier. The troughs after a bad transition, more than the average level, are what an opportunistic rival exploits.

Because $K^*$ depends on $\lambda$ and $\chi$ only through their product, the combinations yielding a given capacity lie on hyperbolae $\lambda\chi = \text{const}$. The high-reset democracy lies at $\lambda\chi = 0.2$ and the autocracy at $\lambda\chi = 0.005$. A state can move to a lower hyperbola by reducing $\chi$ or by reducing $\lambda$, and the costs differ: reducing $\chi$ requires administrative effort, while reducing $\lambda$ reduces accountability. The arithmetic treats the two as equivalent; constitutional design must distinguish them.

### 3.2 Financeable reform horizon

The reset tax also shortens the horizon over which a government can rationally plan. Consider a reform that costs $C$ now and returns a benefit $B$ after $\tau$ years, such as a rebuilt education system, coastal defence or a reformed tax authority. If the project faces the same effective termination hazard as the capacity stock, its expected present value is approximately

$$V(\tau) = B\,e^{-(\rho + \lambda\chi)\tau} - C,$$

where $\rho$ is the ordinary discount rate. The project has positive value only when

$$\tau < \tau^* = \frac{\ln(B/C)}{\rho + \lambda\chi}.$$

The reset tax appears in the denominator of the horizon, so raising it excludes long reforms entirely.

For a reform whose eventual benefit is 4 times its cost, with $\rho = 0.05$, the high-reset democracy can finance projects out to $\tau^* = 5.5$ years. Reforms that take a decade or more are irrational for it to begin, because they will be reset before they pay. With $\chi = 0.1$ the financeable horizon extends to 18.5 years, a factor of 3.3, and the autocracy can plan 25.2 years ahead. For a fixed 15-year mission, the high-reset democracy requires the benefit to exceed the cost 42.5-fold, a threshold few real projects clear. The low-reset democracy requires a 3.1-fold payoff and the autocracy a 2.28-fold one.

These figures quantify the case for separating clocks within the state. A reform framed as one government's promise inherits that government's hazard. A reform framed as a chartered mission, with staged milestones, protected multi-year funding and a published rule for cancellation, is detached from the electoral clock and faces a lower hazard, which raises the survival probability of the programme without changing that of the politician. The model does not show that any particular charter works; it identifies the function of a charter, which is to lower $\lambda\chi$ on projects that need a long horizon while leaving the turnover of leaders unchanged.

### 3.3 Drift of institutional integrity under alternation

A common belief holds that democracy corrects itself: an illiberal government is voted out and its damage undone. The belief assumes that repair and destruction proceed at similar speeds, and they do not.

Building institutional capacity is slow because it is team production across overlapping cohorts: an agency functions when enough trained people with tenure and mutual trust choose to enter and stay, and that competence takes years to rebuild [@besley2011; @guedesneto2025]. Destroying it is fast because it requires only decentralized exit, which a hostile administration can trigger within months through dismissals, threats, defunding or intolerable working conditions. Let institutional integrity $I$ fall at rate $d_A$ while a capturing government holds office and rise at rate $r_D$ while a repairing government holds office. Over a long run with a fraction $\phi$ of time under capture, the net drift per unit time is

$$-\,d_A\,\phi + r_D\,(1-\phi),$$

and integrity is sustained only when $d_A/r_D \le (1-\phi)/\phi$.

Under even alternation, $\phi = \tfrac12$, the condition is $d_A \le r_D$: destruction no faster than repair, which the asymmetry violates. With capture in office for a minority share $\phi = 0.35$ of the time, the system tolerates a destroy-to-build ratio of at most 1.86, and plausible empirical asymmetries exceed that. For a population of episodes with log-normally distributed destroy-to-build ratios (median 3, log-standard deviation 0.5), classified by the sign of their net drift, 83 percent drift to breakdown (closed form 83.1 percent; Monte Carlo over 40,000 draws 83.3 percent). The median ratio of 3 is stipulated to display the mechanism, and a different choice would move the breakdown share. Its proximity to the empirical four in five is a consequence of that input and does not reproduce the historical rate. The result supports only the direction: a plausible destroy-faster-than-repair asymmetry sends most episodes to breakdown, consistent with the low recovery rate in the record [@boese2021; @maeda2010]. Alternation alone does not preserve a democracy whose institutions are destroyed faster than they are rebuilt.

The same condition identifies two remedies, and both lower the reset tax. Faster repair reduces the destroy-to-build ratio: a government that inherits preserved records, an intact civil service and a running project registry repairs from a high baseline, which is what a low $\chi$ means. Halving the median asymmetry to 1.5 lowers the breakdown share from 83 to 33 percent. Shorter capture episodes reduce $\phi$, which supports resistance in the first electoral cycle, before the courts are packed; reducing the capture share to one sixth lowers the breakdown share to 15 percent.

### 3.4 Tenure and reset as routes to continuity

Write $\lambda_{\text{leader}}$ for the rate at which a state replaces its governments and $\lambda\chi$ for the rate at which it resets its strategy. The autocratic arrangement makes both small: leaders cannot be removed and, because they rarely change, strategy is rarely reset. A democracy needs the opposite pairing, a high $\lambda_{\text{leader}}$ for accountability and a low $\lambda\chi$ for continuity.

The alternative has a calculable cost. Suppose a high-reset democracy keeps $\chi = 0.8$ and seeks continuity by retaining leaders longer. Reaching the effective decay of the low-reset democracy then requires each leader to serve 32 years, longer than the 20-year autocratic tenure in the calibration. Entrenchment is therefore quantitatively worse than the problem it addresses.

A democracy that keeps 4-year leaders and cuts $\chi$ to 0.1 reaches 73 percent of an autocracy's long-run capacity while replacing its governments 5 times as often. Most of the strategic continuity is obtained with five times the accountability and without entrenching anyone: high personnel turnover combined with low institutional reset. The state becomes the persistent player, and governments remain temporary and removable.

## 4. Institutional instruments

The parameters $\chi$, $r_D$ and $u$ correspond to known institutional machinery. The model places otherwise incommensurable reforms on common axes: whether they lower the reset tax, speed repair or raise the cost of capture, in each case without lowering $\lambda$.

Lowering $\chi$ is mainly a matter of memory and personnel. A merit-based permanent civil service protected from politically motivated dismissal keeps agencies staffed through a change of minister. A standing transition office, mandatory handover documents and a public register of every major project, contract, deadline and responsible official let an incoming government start from the state's accumulated knowledge. Append-only records that cannot be quietly deleted preserve evidence and routine across the handover. None of these measures affects who governs; all of them reduce what a handover destroys.

Speeding repair and resisting capture depend on distributing control over time and across bodies. Staggered, preferably non-renewable terms for courts, auditors and electoral commissions prevent any single election from replacing a guardian institution wholesale, so that each such body reflects several electoral majorities [@bisarya2023]. Appointment powers split among government, opposition, courts and professional bodies, together with protected direct appropriations that an executive cannot impound, prevent an institution's independence from resting on a single dependency. A successor-only rule, under which a majority that changes the rules of competition cannot itself benefit from the change, removes the immediate payoff from constitutional self-dealing, the means by which a strategic incumbent binds its successors [@alesina1990; @venice2002]. Coercive power requires separate safeguards: armed forces under constitutional command, and multiple authenticated signatures for high-risk orders, raise the number of independent actors an aspiring autocrat must capture [@osce1994]. Germany's constructive vote of no confidence illustrates the principle: parliament may remove a chancellor only by simultaneously electing a successor, which blocks purely destructive majorities while keeping the government removable [@basiclaw1949, art. 67].

Two qualifications apply. Distribution helps only when the distributed nodes are independent; three guardians appointed at once by the same leader amount to a single gate, and polycentric redundancy raises the cost of capture only to the extent that the centres answer to different principals on different schedules [@ostrom1961; @ostrom1990]. Every gate that resists capture also slows ordinary government, so the staggering that protects a court can also entrench a policy, and beyond some point additional veto points add little resilience and substantial delay. The design target is the greatest capture resistance compatible with a state that can still act.

## 5. Limitations

The model measures no country. The numbers form an illustrative calibration chosen to expose a mechanism and are not estimates of any state's $\chi$ or $\lambda$; the model forecasts no collapse and certifies no reform. It decomposes a democracy's strategic disadvantage into a turnover rate that must remain high and a reset severity that need not, and shows that the second is the effective lever. The empirical regularities it mentions, the share of autocratization episodes that end in breakdown and the scale of the current wave, locate the mechanism against the record; the model does not generate them.

The argument is conditional on $\lambda$ remaining high and on leaders remaining removable. A design that buys continuity by making governments hard to replace reconstructs the autocratic arrangement, and this condition is the reason for placing continuity in $\chi$ instead of tenure. Democracy is self-enforcing only while the losers of an election expect to compete again, and the public, common-knowledge signal an election provides lets citizens coordinate to defend it [@fearon2011; @przeworski2010]. Lowering $\lambda$ weakens that signal regardless of the capacity stock. The same condition addresses the strongest objection to the proposal, that a state hardened against its own government shifts power from elected officials to unelected guardians: liberty survives in a narrow corridor that both an overweening state and an overweening executive can leave [@acemoglu2019]. The model assumes the state remains inside that corridor and does not defend it.

The model also treats $\chi$ as a parameter set by the constitution, whereas a determined capturer will attack the institutions that keep $\chi$ low, the civil service, the registry and the audit office, because they supply the continuity. The analysis is a viability argument: it describes how to keep a state inside the region where ordinary electoral correction still works, and viability problems favour early intervention while the system is well inside the viability kernel [@aubin1991]. Once $\chi$ is rising because the record-keeping institutions are themselves being dismantled, the inexpensive interventions are no longer available. The steady-state formula does not capture this dynamic.

## 6. Conclusion

An autocracy's advantage is that continuity resides in a ruler who does not leave. A democracy cannot answer by retaining a ruler of its own, because that ruler's position passes to the next autocrat. It can move continuity into records, routines and staggered guardian bodies that no single government installs or removes, keeping leaders replaceable and the state persistent. In the calibration, this route recovers 73 percent of autocratic capacity while replacing governments five times as often.

## Reproducibility

The simulation is in `simulation/` (`analyses.py`, `figures.py`, `run_all.py`) and runs with `uv run python run_all.py`, seeded with 20260621; it writes every modelled number to `simulation/output/results.json` and the figures to `simulation/output/figures/`. The run checks that the Monte Carlo means lie within 1 percent of $K^*$, that the simulated breakdown shares match the log-normal closed form, and that the tenure route requires 32-year leaders.

## References
