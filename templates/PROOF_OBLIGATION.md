# Proof Obligation

```text
Obligation_ID: PO-###
Parent_claim:
Statement:
Role: essential | auxiliary
Local_hypotheses:
Domain_and_quantifiers:
Desired_strength:

Candidate_tactics:
Active_tactic:
Closure_standard:
Computation_semantics_if_any:

Inputs:
Dependencies:
Evidence_or_artifacts:
Computation_certificate_if_any:
Exact_witness_if_any:

Epistemic_label: [L]|[D]|[N]|[C]|[H]|[X]|[U]|[DEC]
Closure_class: OPEN | EVIDENCE_ONLY | CONDITIONAL | RIGOROUSLY_CLOSED | REFUTED
Conditions_or_exceptions:
Failure_reason_if_any:
Fallback_tactic_or_subclaim:

Auditor_notes:
Date:
```

## Regla

Una obligación esencial sólo cuenta como cerrada para un claim exacto cuando `Closure_class = RIGOROUSLY_CLOSED` o cuando una refutación rigurosa decide el target.

`NUMERICAL_SCOUT` y evidencia muestral ordinaria no pueden producir por sí solos `RIGOROUSLY_CLOSED`.
