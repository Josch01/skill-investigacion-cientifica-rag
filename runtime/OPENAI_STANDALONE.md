# Runtime Profile: OPENAI_STANDALONE

## Purpose

Run the consortium with one OpenAI context or available subagents while preserving the same scientific core.

## Mode selection

- use `SINGLE_PROVIDER_MULTI_CONTEXT` when true separate contexts/subagents are available;
- otherwise use `SINGLE_PROVIDER_SEQUENTIAL`;
- existing v2.12 project coordination remains supported.

## Rules

- use the consortium only for substantive new research/audit;
- keep active blackboard small;
- apply Context Firewall to adversarial and second-review passes;
- do not conflate model reasoning strength with certification;
- all v2.12 gates remain mandatory.
