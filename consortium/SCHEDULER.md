# Proof-Obligation Scheduler

## Purpose

Choose the next scientifically valuable action without forcing one methodology on the whole objective.

## Scheduling unit

The atomic unit is a `Proof_Obligation_ID`, not the whole manuscript/problem.

## Priority order

For an open essential obligation prefer, when applicable:

1. compatible certified internal result;
2. direct external theorem with verified applicability;
3. short direct analytic proof;
4. symbolic exact computation;
5. exhaustive finite computation;
6. validated numerics / rigorous computer-assisted proof;
7. longer interdisciplinary derivation;
8. numerical scout/falsification when it can reduce uncertainty.

This ordering is defeasible; record why a lower route is chosen.

## Tactic record

```text
Obligation_ID
Candidate_tactics
Selected_tactic
Expected_closure_strength
Critical_hypotheses
Cost_context_class
Fallback_tactic
Why_selected
```

No numerical score is required.

## Dynamic branching

If a tactic fails:
- classify the failure using `protocols/RESEARCH_LOOP.md`;
- extract reusable knowledge;
- preserve the same Obligation_ID when only the tactic changes;
- create a new sub-obligation only when the logical statement changes.

## Computational decision

Before writing code ask:
- can analysis decide this exactly?
- can an external theorem decide it?
- is symbolic exact natural?
- is ordinary numerics only scout/corroboration?
- can validated numerics close the quantified domain?

## Parallelism

Independent obligations may be delegated in parallel.
State-changing integration is serialized through the lead/gates.

## Stop rule

Do not keep generating routes after the Research Loop stop budget is reached.
