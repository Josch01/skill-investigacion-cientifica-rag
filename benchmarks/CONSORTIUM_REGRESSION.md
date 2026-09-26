# Consortium Regression Cases

## B01 — Exact witness trap

Given an exact claim `det A != 0` supported only by `det A = 3.7e-15` in float64.

Expected:
- evidence = corroborative/insufficient for exact nonzero;
- exact claim not certified from that evidence.

## B02 — Local/global drift

A theorem proves local identifiability; manuscript claims global identifiability.

Expected:
- global claim blocked or weakened;
- no silent local -> global bridge.

## B03 — Failed route != refutation

Three proof tactics fail to establish P.

Expected:
- P = UNRESOLVED unless rigorous refutation exists.

## B04 — Invalid Red-Team objection

Hypotheses include finite-order linear operator over C:
`R^m=I`.
Red Team claims "R may be non-diagonalizable" without further argument.

Expected:
- objection must be verified;
- direct minimal-polynomial argument refutes objection;
- objection cannot downgrade target.

## B05 — Definition is not theorem

A definition appears in a manuscript inventory.

Expected:
- type/non-circularity audit;
- no proof status such as REFUTED/UNRESOLVED merely because it is not proved.

## B06 — Corroborative computation fails but analytic proof survives

An analytic rank theorem is valid.
A float64 SVD was incorrectly labeled "exact rank collapse".

Expected:
- evidence artifact downgraded/repaired;
- theorem status recomputed from analytic proof, not automatically refuted.

## B07 — Genericity from samples

10,000 samples show nonzero determinant.

Expected:
- cannot conclude generic/open dense without exact non-identity bridge or rigorous equivalent.

## B08 — Sharp minimum without attainment

A lower bound `N >= 3` is proved but no construction with N=3 is proved.

Expected:
- lower bound may survive;
- "sharp minimum = 3" blocked.

## B09 — External theorem missing hypothesis

Theorem T requires H1,H2,H3.
Current problem verifies H1,H2; H3 is unresolved.

Expected:
- T = CONDITIONALLY_APPLICABLE or UNRESOLVED;
- create obligation for H3;
- do not use T unconditionally.

## B10 — Analytic/computational strategy

Target is a simple algebraic identity that can be proved directly, but code execution is available.

Expected:
- scheduler prefers direct analytic/symbolic exact route;
- ordinary numerical simulation is not the default.

## B11 — Disagreement is not voting

Two workers support P; one verified counterexample supports not-P.

Expected:
- open Dispute_ID;
- resolve exact conflict;
- majority cannot override counterexample.

## B12 — Boilerplate breadth collapse

Twenty unrelated claims receive nearly identical proof-state text.

Expected:
- semantic completeness/anti-boilerplate warning;
- reduce batch size;
- reopen affected records.
