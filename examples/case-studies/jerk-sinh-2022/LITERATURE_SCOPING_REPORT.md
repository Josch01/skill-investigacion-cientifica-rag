# Case study: 2022 Jerk sinh model — v3.1 scientific lifecycle smoke test

> **Status**: research scoping only, ROUTES_PENDING. No mathematical novelty, numerical UPO, certified chaos or manuscript claimed. Published source and model were verified but the user's exact intended paper remains unconfirmed.

## Seed publication
REF-001: X. Hu, B. Sang, N. Wang, *The chaotic mechanisms in some jerk systems*, AIMS Mathematics **7**(9) (2022), pp. 15714–15740. DOI: [10.3934/math.2022861](https://doi.org/10.3934/math.2022861). Publisher full text: https://www.aimspress.com/aimspress-data/math/2022/9/PDF/math-07-09-861.pdf

From Eq. (2.2), with the paper's assumptions:
~~~tex
\dot{x}=y,\quad \dot{y}=z,\quad
\dot{z}=\varepsilon-ax-b^2 y-cz+d\sinh(x),
\qquad b>0,\ c>0,\ d\ne 0,\ 0\le\varepsilon\ll1.
~~~

Paper's Case A: epsilon=0, b=1, c=1/5, d=+1. The source studies pitchfork/Hopf bifurcations analytically and periodic/chaotic behavior through bifurcation diagrams, Poincare sections, Lyapunov exponents and circuit simulations.

### Scientific background and provisional literature
- REF-002, Symmetry 2023 DOI 10.3390/sym15111991: numerical methods for a related symmetric sinh Jerk; editorial abstract only, mathematical equivalence **not yet verified**.
- REF-003, Computer Physics Communications 2012 DOI 10.1016/j.cpc.2011.09.001: validated periodic orbits via interval analysis, unrelated physical system; possible method, source theorem not fully audited.
- REF-004, SIADS 2023 DOI 10.1137/22M1499418: validated persistence of periodic orbits under state-dependent delay (different object). Not automatically applicable to this ordinary Jerk.
- REF-005, Chaos Solitons Fractals 2018 DOI 10.1016/j.chaos.2017.12.008: fourth-order hyperjerk sinh system; **not the same 3D model**.
- REF-006, Chaos Solitons Fractals 2025 DOI 10.1016/j.chaos.2025.116061: fourth-order snap / hyperjerk; **not equivalent** merely by both including sinh.

This is **NOT** a full or exhaustive forward/backward citation chaining review. Six published works confirmed via publishers; full mathematical source analyzed only for REF-001. All route novelty remains unresolved.

## Verification 1 — Z2 symmetry [analytic]
Let u=(x,y,z). For epsilon=0 the vector field is odd:
F(-x,-y,-z) = -F(x,y,z) because sinh(-x)=-sinh(x).
Therefore if u(t) solves the ODE then -u(t) solves it on the same existence interval. This proves *equivariance*, **not** the existence of two different attractors or UPOs.

## Verification 2 — source Theorem 5.1: check conditions before invoking
REF-001 p.15732: under b>0,c>0,d!=0 and epsilon=0, the origin is asymptotically stable when
d < a < d + c b^2. The source proves the statement using Routh-Hurwitz.

At u=0, the Jacobian characteristic polynomial is
p(lambda)=lambda^3+c lambda^2+b^2 lambda+(a-d).

Routh-Hurwitz for this cubic requires c>0, b²>0, a-d>0 and c b²>a-d.
Case A: b=1,c=1/5,d=1 -> 1<a<6/5.
* a=11/10: 1<11/10<6/5, every relevant hypothesis holds; T5.1 APPLICABLE and its conclusion directly matches local stability target.
* a=167/100: 167/100>6/5; T5.1 NOT_APPLICABLE. Not applying a theorem does **not** by itself refute stability or prove chaos. An independent Routh check in this case gives p(lambda)=lambda³+(1/5)lambda²+lambda+(67/100) and two sign changes in Routh's first column, thus 2 unstable eigenvalues. This follows from a separate verified criterion, not from invalid application of T5.1.

## Verification 3 — critical missing inference in the seed paper
From the vector field, div F=-c. Liouville's formula yields local volume contraction:
det D Phi_t = exp(-ct) for flow maps defined up to time t.
The paper (p.15719) further asserts all orbits eventually confined to a bounded set of zero volume. **Negative divergence alone does not establish global existence or eventual boundedness.**

Generic rigorous counterexample to that inference (NOT a counterexample specific to Eq. 2.2):
x'=x²,
y'=-(2x+c)y,
c>0.
Then div F=2x-(2x+c)=-c, yet the trajectory x(0)=x0>0,y(0)=0 obeys x(t)=x0/(1-x0 t) and blows up at t=1/x0.
Thus uniform volume contraction does not imply an absorbing compact set. Whether the specific 2022 sinh Jerk admits unbounded or finite-time-escape trajectories requires its own analysis; this case does not yet decide that question.

## Up to four bounded research routes
1. **ROUTE-UPO**: rigorously validate candidate unstable periodic orbits, Floquet multipliers and parameter regions; external validated numerical methods are *candidates*, not automatically applicable.
2. **ROUTE-SYM**: examine relations/continuation of Z2-symmetric periodic orbits upon epsilon symmetry breaking; equivariance does not guarantee pairs of distinct orbits.
3. **ROUTE-GLOBAL**: rigorously establish existence/absorbing sets or escape regimes, rather than infer globality from negative divergence.
4. **ROUTE-BIF**: rigorous continuation/parameter-domain claims beyond local Hopf and pitchfork proven in 2022, avoiding reproduction of already known results.

No route currently justifies a claim of priority or novelty. The next step is a researcher selection **and** deeper countersearch of the chosen route.

## Source provenance
Publisher PDF: https://www.aimspress.com/aimspress-data/math/2022/9/PDF/math-07-09-861.pdf
Related publisher records:
- https://www.mdpi.com/2073-8994/15/11/1991
- https://www.sciencedirect.com/science/article/pii/S0010465511003031
- https://epubs.siam.org/doi/abs/10.1137/22M1499418
- https://www.sciencedirect.com/science/article/abs/pii/S0960077917305106
- https://www.sciencedirect.com/science/article/abs/pii/S0960077925000748

### Limits and next step
No code simulations, numerical convergence or interval arithmetic were executed in this test. No independent second review. The demonstration exhibits a *local* theorem that applies and a case where it does not, plus a generic counterexample to a faulty inference. This is scoping evidence, not a new article.

State: ROUTES_PENDING; selected_route_id empty; objective not approved; manuscript NOT_STARTED.
