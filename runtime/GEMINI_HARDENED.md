# Runtime Profile: GEMINI_HARDENED

## Purpose

Reduce breadth collapse, boilerplate completion, verdict anchoring and evidence/status conflation in Gemini-style standalone or subagent runtimes.

## Defaults

```text
MAX_CLAIMS_PER_PROOF_BATCH = 4
MAX_CLAIMS_PER_SECOND_REVIEW_BATCH = 3
MAX_ACTIVE_ESSENTIAL_OBLIGATIONS_PER_WORKER = 2
REQUIRE_CONTEXT_FIREWALL = true
REQUIRE_ARTIFACT_WRITE_BEFORE_ROLE_SWITCH = true
REQUIRE_DETERMINISTIC_STATE_VALIDATION = true
```

## Operating pattern

```text
CARTOGRAPHER
 -> batch plan
 -> THEORY/APPLICABILITY
 -> PROOF ENGINEER
 -> FALSIFIER
 -> EVIDENCE AUDITOR
 -> ADJUDICATOR if conflict
 -> STATE SUPERVISOR / deterministic checks
 -> SECOND REVIEW
 -> CERTIFICATION GATES
```

## Hard rules

- Do not ask one context to audit an entire large manuscript proof-by-proof.
- Do not let a worker both propose and canonically certify the same claim.
- Write structured artifacts before changing functional role.
- Do not pass prior verdicts through the Context Firewall.
- Treat a completed file as incomplete until semantic completeness checks pass.
- If subagents/contexts are not real, state `SAME_PROVIDER_SEQUENTIAL`.
- Never pretend provider diversity or independent review.

## Micro-agent mission rule

Each worker receives one bounded question with explicit forbidden actions.

Example:
`Check applicability of REF-12 to PO-7; do not prove PO-7; do not certify the target.`

## Recovery from boilerplate

If repeated generic language appears across unrelated claims:
- stop the batch;
- mark `BREADTH_COLLAPSE_DETECTED`;
- reduce batch size;
- reopen affected records;
- rerun with claim-specific packets.

## Numerical discipline

Gemini numerical output obeys the same `Computation_semantics` taxonomy.
High precision is not an exact witness.
