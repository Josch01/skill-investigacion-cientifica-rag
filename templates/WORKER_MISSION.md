# WORKER_MISSION

## Identity
- Task_ID:
- Revision:
- Mission_ID:
- Contract_hash:
- Mission_hash_if_available:
- Framework_version:
- Framework_commit:
- Assigned_role:

## Scientific contract
- Objective:
- Immutable_claim_statement:
- Current_epistemic_status:
- Objects_and_types:
- Hypotheses:
- Scope:
- Definitions:
- Quantifiers:
- Success_criterion:
- Refutation_criterion_if_applicable:
- Forbidden_strengthenings:

## Proof/computation contract if applicable
- Proof_tactic_routing: yes|no|not_applicable
- Proof_obligations_to_address:
- Candidate_tactic_families:
- Permitted_closure_methods:
- Computation_semantics_if_any: none|exploratory_numeric|falsification_search|corroborative_numeric|symbolic_exact|exhaustive_finite|validated_numeric|rigorous_computer_assisted_proof
- Rigorous_computation_standard_if_any:
- Exactness_required: yes|no|conditional
- Required_proof_obligation_records:
- Required_computation_certificates:

## Composition
- Modules_to_apply:
- Protocols_to_apply:
- Memory/certificates_to_load:
- Local_files_to_read:
- External_search_required: yes|no

## Authority and file ownership
- Allowed_actions:
- Forbidden_actions:
- Canonical_files_read_only:
- Worker_writable_paths:

## Required work
- Research_routes:
- Falsification_routes:
- Numerical/code work:
- Literature/novelty work:
- Notation/type constraints:

## Deliverables
- Required_outputs:
- Required_machine_readable_outputs:
- Deterministic_checks:
- Acceptance_criteria:

## Failure / objection protocol
- Scientific inconsistency: SCIENTIFIC_OBJECTION
- Missing required input: TECHNICAL_BLOCK
- Required closure method insufficient: SCIENTIFIC_OBJECTION
- Do not silently modify claim, hypotheses, scope, definitions, quantifiers, success/refutation criteria or epistemic status.

## Mailbox policy
Open a mailbox question only for scientific clarification, scope/hypothesis/notation conflict, missing required input, or scientific objection. Operational details that do not alter the contract are resolved locally.

## Completion contract
1. Validate the mission against `TASK_PACKET.md` before starting material work.
2. Produce all required outputs first.
3. For each material proof obligation report its status, tactic attempted, closure standard and supporting artifact/certificate.
4. Produce `WORKER_RESULT.md` with work done, evidence, limitations, claims not demonstrated, open questions and artifact inventory.
5. Emit `WORKER_DONE.json` last.
6. `COMPLETE` means execution completed. It is not scientific acceptance, proof, novelty or certification.
