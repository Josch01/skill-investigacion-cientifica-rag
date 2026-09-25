# Worker Result

```text
Task_ID:
Revision:
Mission_ID:
Contract_hash:
Mission_hash_if_available:
Framework_version:
Framework_commit:
Worker_role:
Provider_if_recorded:

Status: COMPLETED|PARTIAL|SCIENTIFIC_OBJECTION|TECHNICAL_BLOCK|FAILED

Contract_understood: yes|no
Contract_preserved: yes|no

Actions_performed:
Files_created:
Files_modified:
Commands_executed:
Tests_or_checks_run:

Proof_obligations_addressed:
  - Obligation_ID:
    statement:
    tactic_attempted:
    closure_standard:
    computation_semantics_if_any:
    closure_class_observed: OPEN|EVIDENCE_ONLY|CONDITIONAL|RIGOROUSLY_CLOSED|REFUTED
    evidence_or_artifact:
    computation_certificate_if_any:
    limitation_or_failure_reason:

Machine_readable_results:
Computation_semantics_used:
Numerical_precision_and_tolerances:
Computation_certificates_produced:
Exact_witness_records_produced:

Claims_demonstrated_or_refuted:
Claims_not_demonstrated:
Open_questions:

Acceptance_criteria_self_check:
  criterion:
  result: PASS|FAIL|UNKNOWN
  evidence:

Deviations_from_packet:
Unexpected_findings:
Scientific_objection_if_any:
Limitations:

Output_hashes:
Reproducibility_notes:

I_DO_NOT_AUTHORIZE_SCIENTIFIC_STATUS_CHANGE: true
Suggested_next_state: READY_FOR_DETERMINISTIC_CHECK|READY_FOR_AUDIT|REVISION_REQUIRED|SCIENTIFIC_REOPEN
```

## Regla

El worker informa el resultado observado de cada obligación, pero no promueve por autoridad propia una obligación ni un claim a estado científico canónico. `RIGOROUSLY_CLOSED` en este reporte significa "el worker produjo evidencia que pretende satisfacer ese estándar"; el Scientific Auditor debe verificarlo antes de integración/certificación.
