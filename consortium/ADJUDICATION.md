# Scientific Adjudication

## Principle

No majority vote.

If agents disagree about a scientific statement, open a dispute.

## Dispute record

```text
Dispute_ID:
Target_ID:
Position_A:
Evidence_A:
Position_B:
Evidence_B:
Exact_conflict:
Resolution_obligation:
Permitted_tactics:
Status: OPEN | RESOLVED_A | RESOLVED_B | RESOLVED_REFORMULATED | UNRESOLVED
Resolution_artifact:
Downstream_effects:
```

## Procedure

1. normalize both positions into exact statements;
2. check whether the apparent disagreement is only scope/notation;
3. identify the smallest proposition that decides the conflict;
4. create a proof obligation for that proposition;
5. route it through Proof/Proof Tactics/Numerics as needed;
6. apply `protocols/ADVERSARIAL_OBJECTION_GATE.md` when one side is an objection;
7. update descendants only after resolution.

## Unresolved disputes

A material unresolved dispute blocks certification of affected claims.

## Rule

> Disagreement generates a new scientific obligation, not a vote.
