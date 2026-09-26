# Gemini — Scientific Consortium Standalone Hardened

Use canonical skill `scientific-research-rag-council` version >= 3.0.0.

## First read only

1. `SKILL.md`
2. `config/EXECUTION_MODES.md`
3. `runtime/GEMINI_HARDENED.md`
4. `protocols/INTERPRETER.md`
5. `agents/ROUTER.md`
6. `modules/MODULE_INDEX.md`

Then load only the selected consortium/modules/protocols.

## Runtime truthfulness

Detect whether you actually have:
- real subagents;
- separate contexts;
- code;
- web/RAG;
- filesystem writes.

Do not claim capabilities or independence that are not real.

## For substantive R3 research

Use `protocols/CONSORTIUM_RESEARCH.md`.
Create a small blackboard projection and work obligation-by-obligation.

## Mandatory Gemini hardening

- obey micro-batch limits in `runtime/GEMINI_HARDENED.md`;
- apply `protocols/CONTEXT_FIREWALL.md`;
- persist artifacts before role switches;
- use deterministic validation when available;
- stop and reduce batch size on boilerplate/breadth collapse;
- no worker self-certification.

## Compatibility

If the project has active v2.12 coordination, preserve it under `LEGACY_V2_12` unless the user asks to migrate.
