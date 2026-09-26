# Runtime Profile: AUTO

## Purpose

Choose the least complex topology that preserves required scientific independence and tooling.

## Decision

1. Read `config/EXECUTION_MODES.md`.
2. Record runtime capabilities.
3. If an active v2.12 coordination task exists, preserve it unless the user requests migration.
4. For R3/high-risk objectives prefer the strongest available separation:
   `MULTI_PROVIDER_COUNCIL > SINGLE_PROVIDER_MULTI_CONTEXT > SINGLE_PROVIDER_SEQUENTIAL`.
5. For simple tasks use `LIGHTWEIGHT`.
6. Never upgrade a task's scientific status merely because the runtime is richer.

## Output

Record selected:
`EXECUTION_MODE | PROVIDER_PROFILE | INDEPENDENCE_LEVEL | WHY`.
