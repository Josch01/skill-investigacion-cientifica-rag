# Execution Modes — v3.0

## Purpose

Separate scientific protocol from runtime topology.

The same scientific rules apply regardless of provider.

## Canonical modes

`AUTO`
`LEGACY_V2_12`
`MULTI_PROVIDER_COUNCIL`
`SINGLE_PROVIDER_MULTI_CONTEXT`
`SINGLE_PROVIDER_SEQUENTIAL`
`LIGHTWEIGHT`

## Runtime capability record

Before choosing a non-legacy consortium mode, record:

```text
real_subagents:
separate_contexts:
external_worker:
web_access:
code_execution:
filesystem_write:
persistent_state:
provider_name:
model_name_if_known:
```

## AUTO selection

Prefer:

1. `MULTI_PROVIDER_COUNCIL` when distinct providers/contexts are available and the task is R3/high risk.
2. `SINGLE_PROVIDER_MULTI_CONTEXT` when independent contexts/subagents exist under one provider.
3. `SINGLE_PROVIDER_SEQUENTIAL` when only one context is available.
4. `LIGHTWEIGHT` for simple/non-research tasks.
5. `LEGACY_V2_12` for active legacy projects or explicit user request.

## Independence labels

`CROSS_PROVIDER_SEPARATE_CONTEXT`
`SAME_PROVIDER_SEPARATE_CONTEXT`
`SAME_PROVIDER_SEQUENTIAL`
`NONE`

Never label same-provider sequential review as independent.

## Scientific invariant

Changing execution mode never changes:
- claim meaning;
- proof standards;
- numerical semantics;
- certification gates;
- novelty standards.

## Coordination invariant

Distributed coordination artifacts are required only when there is a real handoff.

Scientific rigor is mandatory in every mode; distributed orchestration is not.
