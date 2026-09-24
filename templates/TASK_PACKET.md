# Scientific Task Packet

```text
Task_ID:
Revision:
Parent_revision:
Risk_class: R0|R1|R2|R3
Task_type: WRITING|CODE|NUMERICAL|SYMBOLIC|DATA|OTHER

Framework_version:
Framework_commit:

Objective_ID:
Claim_ID:

Assigned_role:
Requested_worker_capability:

SCIENTIFIC_CONTRACT:
  Exact_task:
  Scientific_question_if_any:
  Immutable_claim_statement:
  Current_epistemic_status:
  Objects_and_types:
  Hypotheses:
  Scope:
  Definitions:
  Certified_inputs:
  Numerical_evidence_level_if_any:

Inputs:
  source_files_or_refs:
  required_sections:
  input_hashes_if_material:

Allowed_actions:
Forbidden_actions:
Forbidden_strengthenings:

Expected_outputs:
  required_files:
  required_machine_readable_output:
  report:

Acceptance_criteria:
Deterministic_checks:

File_ownership:
  canonical_files_read_only:
  worker_writable_paths:

Failure_or_objection_protocol:
  if_scientific_inconsistency: SCIENTIFIC_OBJECTION
  if_missing_input: TECHNICAL_BLOCK

Next_role_on_success:
Next_role_on_failure:
```

## Regla

El TASK_PACKET es el contrato de una revision concreta. El worker no puede cambiar silenciosamente el contrato que esta ejecutando.