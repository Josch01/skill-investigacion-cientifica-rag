# Scientific Audit Packet

```text
Audit_ID:
Task_ID:
Revision:

Auditor_role:
Independent_from_worker: yes|no

Inputs_reviewed:
  task_packet:
  worker_result:
  artifacts:
  deterministic_check_result:

Contract_compliance:
  exact_task:
  required_outputs:
  acceptance_criteria:

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

Skill_gates_applied:

Findings:
  severity:
  issue:
  required_repair:

Verdict: ACCEPT|ACCEPT_WITH_NONSCIENTIFIC_PATCH|REVISION_REQUIRED|SCIENTIFIC_REOPEN|BLOCKED

Authorized_integration_scope:
Scientific_status_change_authorized: yes|no
If_yes_basis:

Next_state:
```

## Regla

`ACCEPT` significa conformidad con el TASK_PACKET. Cambiar un status científico exige además los gates de certificación pertinentes.