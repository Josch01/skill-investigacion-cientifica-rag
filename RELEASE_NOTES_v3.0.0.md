# Release Notes v3.0.0 — Scientific Research Consortium

## Scope

v3.0 adds an optional scientific-consortium orchestration layer while preserving the v2.12 scientific core and legacy coordination flows.

The goal is not "more agents". The goal is to make complex research operate over a verifiable graph of obligations, evidence, routes, objections and disputes.

## Backward compatibility

v3.0 is additive.

- Existing v2.12 paths are preserved.
- Existing TASK_PACKET / WORKER_MISSION / WORKER_RESULT / AUDIT_PACKET flows remain valid.
- Existing proof certificates and memory ledgers remain canonical under their original compatibility rules.
- Existing Codex prompts with floor >=2.12.0 remain valid.
- Active v2.12 projects may continue under EXECUTION_MODE=LEGACY_V2_12.
- Consortium blackboard state is a runtime projection, not a replacement scientific database.

See:
`config/COMPATIBILITY.md`.

## New scientific-consortium layer

New core files:

- `consortium/CONSORTIUM.md`
- `consortium/BLACKBOARD.md`
- `consortium/ROLE_REGISTRY.md`
- `consortium/SCHEDULER.md`
- `consortium/ADJUDICATION.md`
- `protocols/CONSORTIUM_RESEARCH.md`
- `protocols/CONTEXT_FIREWALL.md`
- `protocols/DISPUTE_RESOLUTION.md`

## New execution modes

```text
AUTO
LEGACY_V2_12
MULTI_PROVIDER_COUNCIL
SINGLE_PROVIDER_MULTI_CONTEXT
SINGLE_PROVIDER_SEQUENTIAL
LIGHTWEIGHT
```

The scientific standard is invariant across modes.

## Runtime profiles

- `runtime/GEMINI_HARDENED.md`
- `runtime/OPENAI_STANDALONE.md`
- `runtime/MULTI_PROVIDER.md`
- `runtime/AUTO.md`

Gemini Hardened introduces smaller proof batches, context firewall, artifact persistence between role switches, deterministic validation and breadth-collapse recovery.

## Functional consortium roles

- Research Architect
- Theory Scout
- Applicability Judge
- Proof Engineer
- Tactic Selector
- Computational Strategist
- Numerical/Symbolic Worker
- Falsifier
- Adjudicator
- Independent Reviewer

These do not create new authority. They map to canonical roles in `config/AGENT_AUTHORITY.md`.

## Adaptive research behavior

The scheduler works per Proof Obligation.

Priority favors:
1. compatible certified internal results;
2. directly applicable external theorems;
3. direct analytic proof;
4. symbolic exact computation;
5. exhaustive finite computation;
6. validated numerics / rigorous computer-assisted proof;
7. longer derivations;
8. exploratory numerics when it can reduce uncertainty.

A failed tactic does not create a new claim automatically; the same Obligation_ID is preserved unless the logical statement changes.

## Computation strategy

A Computational Strategist decides whether code is scientifically useful before execution.

Canonical outcomes remain:
`none | exploratory_numeric | falsification_search | corroborative_numeric | symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`.

The v2.12 distinction `numerical evidence != exact proof` remains unchanged.

## Adjudication

Scientific conflicts are not resolved by majority vote.

A conflict creates:
`Dispute_ID -> minimal deciding proposition -> resolution Proof Obligation`.

Material unresolved disputes block affected certification.

## Context firewall

For adversarial and independent review passes, transfer statements, hypotheses and evidence — not prior verdict/confidence language.

Same-provider sequential review must be labeled honestly as:
`SAME_PROVIDER_SEQUENTIAL`.

## Deterministic validation

New scripts:

- `scripts/validate_research_state.py`
- `scripts/validate_audit_run.py`

The existing `scripts/validate_skill.py` now validates v3.0 consortium files while preserving required v2.12 assets.

## New templates

- `templates/BLACKBOARD_STATE.json`
- `templates/CLAIM_NODE.md`
- `templates/OBLIGATION_NODE.md`
- `templates/ROUTE_NODE.md`
- `templates/DISPUTE_RECORD.md`
- `templates/EXECUTION_REPORT.md`

## New entry prompts

- `prompts/GEMINI_STANDALONE_HARDENED.md`
- `prompts/OPENAI_STANDALONE_CONSORTIUM.md`
- `prompts/MULTI_PROVIDER_CONSORTIUM.md`

## Scientific invariants preserved

```text
route failure != refutation
float64 != exact witness
worker output != scientific acceptance
deterministic pass != scientific pass
provider disagreement != majority decision
blackboard event != certification
```

## Upgrade strategy

Existing projects do not need migration.

New complex R3 objectives may use consortium mode immediately.

Migration of an active legacy project is explicit and must preserve existing IDs/provenance.
