# Scientific Audit Packet

```text
Audit_ID:
Task_ID:
Revision:
Mission_ID:
Contract_hash:
Mission_hash_if_available:
Framework_version:
Framework_commit:

Auditor_role:
Independent_from_worker: yes|no

Inputs_reviewed:
  task_packet:
  worker_mission:
  worker_result:
  artifacts:
  deterministic_check_result:

Contract_compliance:
  exact_task:
  objects_types:
  hypotheses:
  scope:
  definitions_quantifiers:
  success_refutation_criteria:
  allowed_forbidden_actions:
  file_ownership:
  required_outputs:
  acceptance_criteria:

Proof_obligation_audit:
  - Obligation_ID:
    essential: yes|no
    statement:
    tactic:
    closure_standard:
    computation_semantics_if_any:
    artifact_or_certificate:
    worker_reported_closure_class:
    auditor_verified_closure_class: OPEN|EVIDENCE_ONLY|CONDITIONAL|RIGOROUSLY_CLOSED|REFUTED
    bridge_verified: yes|no|not_applicable
    findings:

Scientific_integrity:
  objects_types_preserved:
  hypotheses_preserved:
  scope_preserved:
  epistemic_status_preserved:
  numerical_vs_exact_preserved:
  forbidden_strengthening_detected:

Reproducibility:
  commands_or_tests_verified:
  hashes_checked:
  computation_certificate_needed:
  computation_certificates_checked:
  domain_coverage_checked:
  rounding_error_checked_if_material:

Skill_gates_applied:

Findings:
  severity:
  issue:
  required_repair:

Verdict: ACCEPT|REVISION_REQUIRED|SCIENTIFIC_REOPEN|BLOCKED

Authorized_integration_scope:
Scientific_status_change_authorized: yes|no
If_yes_basis:

Next_state:
```

## Regla

`ACCEPT` significa conformidad con el TASK_PACKET y la misión compilada. No equivale a `CERTIFIED`.

Cambiar un status científico exige además los gates de certificación pertinentes. Si una obligación esencial no supera su `closure_standard`, el auditor no puede convertir el reporte del worker en cierre canónico.
