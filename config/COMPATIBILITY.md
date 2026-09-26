# Backward Compatibility Policy — v3.0

## 1. Principle

v3.0 is an additive orchestration layer over the certified v2.12 scientific core.

No v2.12 protocol, template, memory ledger, handoff flow, Claim_ID, Obligation_ID, Route_ID, or certificate is invalidated merely by upgrading to v3.0.

## 2. Compatibility invariants

- Existing paths are not renamed or deleted.
- Existing `TASK_PACKET -> WORKER_MISSION -> WORKER_RESULT -> AUDIT_PACKET` flows remain valid.
- Existing v2.12 audit hard gates remain normative.
- Existing proof certificates remain reusable under their original compatibility rules.
- Existing projects are not required to create consortium state files.
- Legacy prompts requiring `>= 2.12.0` remain valid with v3.0.
- New v3.0 prompts may require `>= 3.0.0`.

## 3. Blackboard compatibility

The consortium blackboard is a runtime projection/index, not a second source of scientific truth.

Canonical scientific status remains in the existing ledgers/certificates governed by the skill.

Blackboard nodes reference existing IDs where possible:
`Claim_ID | Obligation_ID | Route_ID | Evidence_ID | Certificate_ID | Objection_ID`.

A blackboard transition does not certify knowledge by itself.

## 4. Legacy mode

`EXECUTION_MODE=LEGACY_V2_12` runs the previous orchestration unchanged.

AUTO may fall back to LEGACY_V2_12 when:
- the project already has an active v2.12 coordination task;
- consortium state is absent and migration adds no value;
- the user explicitly requests legacy behavior.

## 5. Migration

Migration is opt-in per active objective.

Do not rewrite historical ledgers. Build a consortium view by linking existing IDs and marking provenance.

## 6. Rule

> v3.0 may orchestrate v2.12 artifacts; it may not silently reinterpret them.
