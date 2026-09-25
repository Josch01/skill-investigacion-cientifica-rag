# Artifact Consistency Report

```text
Run_ID:
Framework_version:
Framework_commit:

Active_artifacts:
Historical_snapshots:
Superseded_artifacts:

Claim_status_matrix:
  Claim_ID | PROOF_STATE | CLAIM_SIGNATURE | ROUTE_LEDGER | PROOF_OBLIGATIONS | COMPUTATION_CERTIFICATES | MANUSCRIPT | SECOND_REVIEW | WITNESS | verdict

Proof_obligation_consistency:
  Obligation_ID | parent_claim | active_tactic | closure_standard | computation_semantics | closure_class | artifact_or_certificate | verdict

Computation_consistency:
  Certificate_ID | obligation_id | semantics | certified_domain | coverage | error_rounding_control | closure_standard | verdict

Version_mismatches:
Missing_second_reviews:
Missing_exact_witnesses:
Missing_computation_certificates:
Open_essential_obligations:
Status_conflicts:
Unresolved_scope_items:

NO_ACTIVE_CONTRADICTIONS: true|false
FINAL_ARTIFACT_GATE: PASS|BLOCKED
Required_repairs:
```

## Regla

Un claim no pasa este gate si su Proof Certificate declara cerrada una obligación esencial pero `PROOF_STATE`, `PROOF_OBLIGATION`, `ROUTE_LEDGER` o el Computation Certificate material discrepan sobre táctica, estándar de cierre, dominio certificado o `closure_class`.
