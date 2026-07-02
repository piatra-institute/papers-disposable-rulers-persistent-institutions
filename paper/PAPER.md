---
title: |
  Disposable Rulers, Persistent Institutions:\
  The Reset Tax and the Continuity a Democracy Can Buy Without a Strongman
author: PIATRA . INSTITUTE
date: June 2026
---

## Abstract

A democracy and a dictatorship are not racing on the same clock. A new prime minister inherits a damaged system, needs years for a reform to mature, and is often removed before any of it shows, while an entrenched ruler holds position through fear and accumulates across decades. The intuitive fix, a strong leader who stays long enough to finish the job, is the wrong one, because it builds the vehicle the next illiberal government will drive. This paper prices the right one. It treats a democracy's strategic capacity, the expertise and institutional memory and half-built reforms that let a state act on a long horizon, as a stock that accumulates continuously and is knocked down at each change of government, which is a piecewise-deterministic Markov process with a closed-form long-run mean, $K^* = u/(\delta + \lambda\chi)$. The disadvantage the model isolates is not the turnover rate $\lambda$ but the product $\lambda\chi$, turnover multiplied by the fraction $\chi$ of capacity lost per turnover, a quantity the paper calls the reset tax. Four results follow from the one process. At fixed democratic turnover, cutting reset severity from $\chi = 0.8$ to $\chi = 0.1$ lifts a democracy from 0.22 to 0.73 of an autocracy's long-run capacity, closing about 90 percent of the excess gap and removing most of its volatility, with no change to how often leaders are replaced. The same cut more than triples the reform horizon a government can finance, from 5.5 to 18.5 years, so a 15-year mission that would need a 42.5-fold payoff to survive a high-reset democracy needs only a 3.1-fold payoff under a low-reset one. Because institutions build slowly through coordinated entry and break fast through decentralized exit, electoral alternation is not self-correcting: when destruction outpaces repair, even perfect alternation drifts to breakdown, a model echo of the finding that four in five democracies that begin to autocratize do not recover, and the two cures, faster repair and earlier resistance, are both ways of lowering the reset tax. And to match an autocrat's continuity by entrenchment a democracy would have to keep its leaders for 32 years, longer than the dictator it fears, whereas the reset route keeps 4-year leaders and still buys 73 percent of autocratic continuity at 5 times the removability. The construct prices an incentive structure; it measures no country, it predicts no collapse, and it holds throughout that leaders must stay genuinely removable. Continuity belongs in the architecture of the state, not in the body of a ruler.
## 1. The Football-Manager Problem

Picture a newly elected government in a country whose institutions have been hollowed out. It takes office, replaces the senior staff, reconstructs what the last government knew, renegotiates the coalition, rebrands the inherited projects, and starts the reforms it promised. Education, infrastructure, an honest tax administration, a working court system: these mature over 10 or 15 years, and the voters who elected the government will judge it on how things feel in 4. When the reforms have not yet bloomed, the government is removed, and the next one begins the same cold start. Across the border, a ruler who took power through a coup or a captured election simply stays, holds the army and the broadcaster and the prosecutor, and adds another layer to the apparatus each year that the democracy spends restarting.

This is the asymmetry that makes a certain kind of slow authoritarian advance so hard to answer. The democrat is treated as a temporary player and behaves like one. The autocrat is a persistent player and invests like one, in cadres and media and intelligence and the long relationships that outlast any single election abroad. The true scale of the problem is not rhetorical. The V-Dem Institute's 2026 report counts 44 countries, holding about 41 percent of the world's population, in some phase of autocratization, and earlier work on the same data found that once autocratization begins inside a democracy, only about one in five democracies recover (V-Dem Institute, 2026; Boese et al., 2021). The mode of attack is rarely the tank. It is executive aggrandizement, the incremental and legalistic capture of the referees, the salami slicing that never quite triggers a response (Bermeo, 2016; Levitsky and Ziblatt, 2018; Ginsburg and Huq, 2018).

The tempting response is symmetry: if the dictator wins by lasting, let the good government last too. Weaken the term limits for the reformers, give the emergency a longer leash, keep the competent hands in place. The objection is not moral but structural, and it is decisive. A state built to keep a good leader is a state built to keep the next one, and the next one may be the person the design was meant to stop. So the question has to be posed more carefully. The democratic answer to a 20-year dictator cannot be a 20-year democrat. It has to be a 20-year project that survives 5 different governments, a way to move continuity out of the ruler and into the institutions, while leaving the ruler as removable as ever.

That sentence is easy to write and easy to mean nothing by. The rest of this paper is an attempt to give it an arithmetic, so that the trade-offs it implies are visible and the word continuity has a number attached. The instrument is deliberately small. It is one stochastic process, looked at four ways.

## 2. What Resets When a Government Falls

Let $K_t$ be a state's strategic capacity at time $t$: not its constitution on paper but its working stock of expertise, institutional memory, live alliances, administrative routine, and reform progress, the things that let it pursue a goal that takes longer than one term. Two forces act on this stock continuously. The state invests in it at some rate $u$ per year, and it depreciates at a rate $\delta$, the ordinary forgetting and obsolescence that would erode capacity even under a single unbroken government. Between changes of government the stock therefore follows

$$\dot K_t = u - \delta K_t,$$

drifting toward the level $u/\delta$ that investment alone would sustain.

A change of government is the discrete event. When the government turns over, a fraction $\chi$ of the accumulated stock is lost: the new minister's staff are replaced, the half-finished project is shelved or rebranded, the relationships are reset, the files are not where the last team left them. If turnovers arrive as a Poisson process $N_t$ with rate $\lambda$, the whole dynamics are

$$dK_t = (u - \delta K_t)\,dt - \chi K_{t^-}\,dN_t,$$

a piecewise-deterministic Markov process: smooth accumulation between shocks, multiplicative knockdowns at random times. Taking expectations turns the jump term into a steady drain at rate $\lambda\chi$,

$$\frac{d\,\mathbb{E}[K_t]}{dt} = u - (\delta + \lambda\chi)\,\mathbb{E}[K_t],$$

so the expected long-run stock has a closed form,

$$\boxed{\,K^* = \frac{u}{\delta + \lambda\chi}\,.}$$

The whole argument is already visible in the denominator. A democracy's strategic disadvantage is not its turnover rate $\lambda$. It is the product $\lambda\chi$, the frequency of turnover multiplied by the severity of the reset, and the two factors are not the same kind of thing. The rate $\lambda$ is the price of accountability, the rate at which voters can replace a government they dislike, and lowering it means keeping bad leaders longer. The fraction $\chi$ is pure waste, the share of accumulated public capacity that a transition destroys for no democratic purpose at all. The state-capacity tradition has long treated capacity as a forward-looking investment whose value depends on who will hold power next (Besley and Persson, 2009; Besley and Persson, 2011). The reset tax is what that investment looks like when the holder changes on a schedule and the handover is lossy. The design target writes itself: leave $\lambda$ high and drive $\chi$ down.

## 3. The Reset Tax

Put numbers on it with the seed's own worked example. A democracy changes government on average every 4 years, so $\lambda = 0.25$, and an autocracy every 20, so $\lambda = 0.05$; ordinary depreciation $\delta = 0.05$ is common to both; and a poorly designed democratic transition loses most of what it inherited, $\chi = 0.8$, against an autocrat's smooth $\chi = 0.1$. The effective decay rates are then $0.25$ for the democracy and $0.055$ for the autocracy, and with equal annual investment the democracy holds only $0.22$ of the autocracy's long-run capacity. The autocrat is roughly 4.5 times ahead. This is the football-manager problem stated as a ratio, and nothing in it yet mentions a remedy.

Now change one number. Hold the elections just as frequent, $\lambda = 0.25$, and lower the reset from $\chi = 0.8$ to $\chi = 0.1$ by the unglamorous means a later section will name. The democratic effective decay falls to $0.075$, the capacity ratio rises from $0.22$ to $0.73$, and the autocrat's advantage shrinks from 4.5-fold to 1.36-fold. In terms of the excess gap, the part above parity, about 90 percent of it is gone, and not one politician has been made harder to remove. The lever was never tenure. It was the handover.

There is a second gain in the same move, and it is about variance rather than mean. The model is stochastic, so $K^*$ is the center of a distribution, not a guarantee, and a high-reset democracy does not merely sit lower, it swings harder, lurching down at each turnover and clawing back between. Simulating the process directly, with 20,000 sample paths run long enough to forget their start, confirms the analytic mean to three significant figures and measures the spread. The coefficient of variation, the standard deviation as a fraction of the mean, falls from 0.69 at $\chi = 0.8$ to 0.13 at $\chi = 0.1$. A low-reset democracy is not only higher on average; it is about 5 times steadier, which matters because it is the deep troughs after a bad transition, not the average, that an opportunistic rival exploits.

It helps to see why $\lambda$ and $\chi$ are not interchangeable even though they enter as a product. Because $K^*$ depends on the pair only through $\lambda\chi$, the combinations that yield a given capacity trace a hyperbola, $\lambda\chi = \text{const}$, and the design question is which point on which hyperbola a state occupies. The high-reset democracy sits at $\lambda\chi = 0.2$. The autocracy sits at $\lambda\chi = 0.005$. Moving between hyperbolae can be done two ways, by sliding down in $\chi$ or down in $\lambda$, and the two slides cost utterly different things. Sliding down $\chi$ spends administrative effort. Sliding down $\lambda$ spends democracy. The arithmetic treats them as equivalent; the constitution must not.

## 4. How Far Ahead a Government Can See

The reset tax does more than lower a stock. It shortens the horizon over which a government can rationally plan, and that is where citizens feel it. Consider a reform that costs $C$ now and returns a benefit $B$ after $\tau$ years, an education system rebuilt, a coastline defended, a tax authority made honest. If the project is exposed to the same effective termination hazard as everything else, its expected present value is approximately

$$V(\tau) = B\,e^{-(\rho + \lambda\chi)\tau} - C,$$

where $\rho$ is the ordinary discount rate. The project is worth starting only while $\tau$ is short enough that the exponential has not eaten the benefit, that is, while

$$\tau < \tau^* = \frac{\ln(B/C)}{\rho + \lambda\chi}.$$

The reset tax sits in the denominator of the horizon too, so raising it does not just shrink reforms, it forbids the long ones outright.

Take a reform whose eventual benefit is 4 times its cost, with $\rho = 0.05$. The high-reset democracy can finance projects out to $\tau^* = 5.5$ years and no further; the cathedral-building reforms, the ones that take a decade or more, are simply irrational for it to begin, because they will be reset before they pay. Cut $\chi$ to $0.1$ and the financeable horizon stretches to 18.5 years, more than triple, by a factor of 3.4. The autocracy, for comparison, can see 25.2 years out. Read the other way, around a fixed 15-year mission, the numbers are starker. To be worth starting under a high-reset democracy, a 15-year reform would need its benefit to exceed its cost 42.5-fold, a threshold almost no real project clears, which is why such democracies do not attempt them. Under a low-reset democracy the same mission needs only a 3.1-fold payoff, and under the autocracy a 2.28-fold one. The long reform does not become easy. It becomes thinkable.

This is the quantitative content of the multi-clock idea, the recognition that not everything in a state should run on the 4-year electoral clock. A reform framed as one government's promise inherits that government's hazard and cannot outlast it. A reform framed as a chartered mission, with staged milestones and protected multi-year funding and a published rule for when it may be cancelled, is detached from the electoral clock and inherits a much lower hazard, which raises the survival probability of the program without raising the survival probability of the politician. The model does not prove any particular charter works. It shows what a charter is for: it is a device for lowering $\lambda\chi$ on the projects that need a long horizon, while leaving $\lambda$ on the leaders untouched.

## 5. Why Throwing the Bums Out Is Not Enough

There is a comforting belief that democracy is self-correcting, that an illiberal government will be voted out and the damage undone at the next election. The belief assumes that repair and destruction run at the same speed. They do not, and the asymmetry is the heart of why backsliding is dangerous.

Building institutional capacity is slow because it is team production across overlapping cohorts: an agency works when enough trained people with tenure and mutual trust choose to enter and stay, and that competence is reconstructed only over years (Besley and Persson, 2011; Guedes-Neto and Peters, 2025). Destroying it is fast because it requires only decentralized exit, which a single hostile administration can trigger in months by firing, threatening, defunding, or simply making the honest official's job unbearable. One leader can empty a building faster than five can fill it. Represent institutional integrity as a quantity $I$ that falls at rate $d_A$ while a capturing government is in office and rises at rate $r_D$ while a repairing one governs. Over a long run that spends a fraction $\phi$ of its time under capture, the net drift per unit time is

$$-\,d_A\,\phi + r_D\,(1-\phi),$$

so integrity is sustained only when $d_A/r_D \le (1-\phi)/\phi$.

Read that threshold slowly. Under perfectly even alternation, $\phi = \tfrac12$, it demands $d_A \le r_D$: destruction no faster than repair. The asymmetry violates exactly this. Even when capture holds office only a minority of the time, $\phi = 0.35$, the system tolerates a destroy-to-build ratio of just 1.86 before it drifts down, and the empirically plausible asymmetry is larger than that. Drawing a population of autocratization episodes with destruction a median 3 times faster than repair, and integrating each to the absorbing floor, 83 percent of them reach breakdown. This is an output of a stipulated asymmetry, not a measurement of one: the median three-fold ratio is chosen to display the mechanism, and a different choice would move the breakdown share with it. That the figure happens to fall near the empirical four-in-five is therefore a coincidence of the chosen input rather than a derivation of the historical rate, and the number carries no more weight than its direction, that a plausible destroy-faster-than-repair asymmetry sends most episodes to breakdown, which is the direction the one-in-five survival rate records (Boese et al., 2021; Maeda, 2010). Alternation alone does not save a democracy whose institutions break faster than elections can rebuild them.

The same threshold names the two ways out, and both are forms of lowering the reset tax. Make repair faster, so that the destroy-to-build ratio falls: a government that inherits preserved records, an intact civil service, and a running project registry repairs from a high baseline rather than from zero, which is precisely what a low $\chi$ means, and halving the asymmetry drops the breakdown share from 83 to 34 percent. Or shorten the capture episodes, cutting $\phi$, which is the case for resisting in the first electoral cycle rather than waiting for the courts that have not yet been packed; pushing the capture share down to a sixth of the timeline drops the breakdown share to 15 percent. Faster repair and earlier resistance are the same medicine in two doses. Both buy back the time the build-destroy asymmetry steals.

## 6. The Two Clocks

The four-year clock that removes leaders and the long clock that accumulates capacity have been tangled together throughout, and the design problem is to separate them. Write $\lambda_{\text{leader}}$ for the rate at which a state replaces its governments and $\lambda\chi$ for the rate at which it resets its strategy. The autocrat's formula is to make both small: leaders are irremovable and, because they rarely change, strategy is rarely reset. The democratic formula has to be the opposite pairing, a high $\lambda_{\text{leader}}$ for accountability and a low $\lambda\chi$ for continuity, and the question is whether that pairing is actually available or merely a wish.

It is available, and the way to see it is to ask what the tempting alternative would cost. Suppose a high-reset democracy refuses to fix its handovers and tries instead to win continuity the autocrat's way, by keeping its leaders longer. Holding $\chi$ at the wasteful $0.8$, the turnover rate it would need to reach the same effective decay as a well-run low-reset democracy corresponds to keeping each leader for 32 years. To match the continuity that good transitions would supply, a democracy that will not reform its transitions must out-sit the very dictator it was afraid of. The tenure route is not merely distasteful; it is quantitatively worse than the disease.

The reset route, by contrast, delivers. A democracy that keeps 4-year leaders but cuts $\chi$ to $0.1$ reaches 73 percent of an autocracy's long-run capacity while replacing its governments 5 times as often. That is the thesis in one comparison: almost all of the strategic continuity, at 5 times the accountability, bought without entrenching anyone. High personnel turnover, low institutional reset. The state becomes the persistent player in the long game, and the governments remain temporary, corrigible, and removable, which is the only arrangement that is both effective against a patient adversary and safe against its own winners.

## 7. What Lowers Chi

The argument has treated $\chi$, $r_D$, and $u$ as dials. They are not abstract. Each corresponds to institutional machinery that is well understood, and the model's contribution is to say what that machinery is for and to put the otherwise incommensurable reforms on one axis: do they lower the reset tax, speed repair, or raise the cost of capture, without lowering $\lambda$.

Lowering $\chi$, the reset itself, is mostly about memory and personnel. A merit-based permanent civil service protected from politically motivated dismissal means a change of minister does not empty the building. A standing transition office, mandatory handover documents, and a public register of every major project, contract, deadline, and responsible official mean the incoming government starts from the state's accumulated knowledge rather than from rumor. Append-only records that cannot be quietly deleted mean the evidence and the routine survive the handover. None of this touches who governs; all of it shrinks what a handover destroys.

Speeding repair and resisting capture is mostly about distributing control over time and across bodies. Staggered, preferably non-renewable terms for courts, auditors, and electoral commissions mean no single election can replace a guardian institution wholesale, so that such a body embodies several electoral majorities at once rather than the last winner's (International IDEA, 2023). Appointment powers split among government, opposition, courts, and professional bodies, and protected direct appropriations an executive cannot impound, keep an institution's independence from resting on a single dependency. A successor-only rule, under which a majority that changes the rules of competition cannot itself benefit from the change, removes the immediate payoff from constitutional self-dealing, the move a strategic incumbent makes to bind its successors (Alesina and Tabellini, 1990; Venice Commission, 2002). Coercion deserves its own interlock: armed forces kept under constitutional rather than personal command, and high-risk orders requiring authenticated multiple signatures, raise the number of independent actors an aspiring autocrat must capture (OSCE, 1994). Germany's constructive vote of no confidence is the clean illustration of the spirit, since parliament may remove a chancellor only by simultaneously electing a successor, which blocks purely destructive majorities while keeping the government removable (Basic Law, 1949, Article 67).

Two cautions keep this from becoming a wish list. Distribution helps only when the distributed nodes are genuinely independent; three guardians appointed at once by the same leader are one gate with three pens, and polycentric redundancy raises the cost of capture only to the extent that the centers answer to different masters and different clocks (Ostrom, Tiebout, and Warren, 1961; Ostrom, 1990). And every gate that resists capture also slows ordinary government, so the same staggering that protects a court can ossify a policy, and beyond some point added veto points buy little resilience while imposing real latency. The design target is not maximum obstruction. It is the most capture resistance compatible with a state that can still act.

## 8. Continuity Off the Body

A construct this spare is most useful when its limits are stated as plainly as its results, because the temptation to over-read it is strong.

It measures no country. The numbers are an illustrative calibration chosen to expose a mechanism, not estimates of any real state's $\chi$ or $\lambda$, and the model forecasts no collapse and certifies no reform. What it offers is an accounting identity with teeth, the decomposition of a democracy's strategic disadvantage into a turnover rate that must stay high and a reset severity that need not, and the demonstration that the second is the lever. The empirical regularities it touches, the share of autocratization episodes that end in breakdown, the scale of the current wave, are cited to locate the mechanism against the record, not to claim the model generated them.

It depends, throughout, on a floor it does not get to lower. The entire argument is conditional on $\lambda$ staying high, on leaders remaining genuinely removable, because the moment a design buys continuity by making governments hard to replace it has rebuilt the autocrat's machine for him. This is not a side constraint; it is the reason for insisting that continuity live in $\chi$ and not in tenure. A democracy is self-enforcing only while the losers of an election expect to compete again, and the public, common-knowledge signal an election provides is what lets them coordinate to defend it (Fearon, 2011; Przeworski, 2010). Drop $\lambda$ and that signal weakens, whatever the model's stock does. The same warning answers the deepest objection to the whole project, that a state hardened against its own government has shifted power from elected officials to unelected guardians: the corridor in which liberty survives is narrow precisely because both an overweening state and an overweening executive can leave it (Acemoglu and Robinson, 2019). The model lives inside that corridor and assumes it; it cannot defend it.

It assumes $\chi$ is a parameter the constitution sets, when a determined capturer will attack the very institutions that keep $\chi$ low, the civil service and the registry and the audit office, precisely because they are the continuity. The model is a viability argument and should be read as one: it describes how to keep a state inside the safe region where ordinary electoral correction still works, and the discipline of a viability problem is to intervene early, while the system is well inside the kernel, rather than at the boundary where correction may no longer be enough (Aubin, 1991). By the time $\chi$ is rising because the memory-keeping institutions are themselves falling, the cheap interventions are behind you. None of this is in the steady-state formula. It is why the formula is not the last word.

What the model does say, and says cleanly, is the thing the football-manager problem made it hard to see. The dictator's advantage is that continuity sits in a body that does not leave. A democracy cannot answer that by keeping a body of its own, because the body it keeps becomes the next dictator's inheritance. It answers by moving continuity off the body entirely, into records and routines and staggered guardians that no single government installs or removes, so that the leaders stay disposable and the state does not. The arithmetic of the reset tax is the price of doing that, and the surprising part of the price is how low it is: most of the way to a dictator's patience, at none of the cost to a citizen's power to throw the government out.

## References

Acemoglu, D., and Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Alesina, A., and Tabellini, G. (1990). A positive theory of fiscal deficits and government debt. *Review of Economic Studies*, 57(3), 403–414.

Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser.

Basic Law for the Federal Republic of Germany (1949). Article 67 (constructive vote of no confidence).

Bermeo, N. (2016). On democratic backsliding. *Journal of Democracy*, 27(1), 5–19.

Besley, T., and Persson, T. (2009). The origins of state capacity: property rights, taxation, and politics. *American Economic Review*, 99(4), 1218–1244.

Besley, T., and Persson, T. (2011). *Pillars of Prosperity: The Political Economics of Development Clusters*. Princeton University Press.

Boese, V. A., Edgell, A. B., Hellmeier, S., Maerz, S. F., and Lindberg, S. I. (2021). How democracies prevail: democratic resilience as a two-stage process. *Democratization*, 28(5), 885–907.

Fearon, J. D. (2011). Self-enforcing democracy. *Quarterly Journal of Economics*, 126(4), 1661–1708.

Ginsburg, T., and Huq, A. Z. (2018). *How to Save a Constitutional Democracy*. University of Chicago Press.

Guedes-Neto, J. V., and Peters, B. G. (2025). *Bureaucratic Resistance in Times of Democratic Backsliding*. Cambridge University Press.

International IDEA. (2023). *Designing Resistance: Democratic Institutions and the Threat of Backsliding*. International Institute for Democracy and Electoral Assistance.

Levitsky, S., and Ziblatt, D. (2018). *How Democracies Die*. Crown.

Maeda, K. (2010). Two modes of democratic breakdown: a competing risks analysis of democratic durability. *Journal of Politics*, 72(4), 1129–1143.

Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.

Ostrom, V., Tiebout, C. M., and Warren, R. (1961). The organization of government in metropolitan areas: a theoretical inquiry. *American Political Science Review*, 55(4), 831–842.

Przeworski, A. (2010). *Democracy and the Limits of Self-Government*. Cambridge University Press.

V-Dem Institute. (2026). *Democracy Report 2026: Unraveling the Democratic Era?* University of Gothenburg, V-Dem Institute.

Venice Commission. (2002). *Code of Good Practice in Electoral Matters*. Council of Europe.
