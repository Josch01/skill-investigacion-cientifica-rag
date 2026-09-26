# Scientific Research Consortium — v3.0

## Mission

Turn a scientific objective into a dynamically maintained graph of claims, dependencies, proof obligations, evidence, routes, objections and certificates.

The consortium does not try to answer the objective in one pass.

It repeatedly asks:

1. What exactly must be established?
2. Is there already a certified/internal/external theorem?
3. Do its hypotheses apply?
4. If not, can missing hypotheses be proved?
5. Which tactic has the best expected closure strength for the current obligation?
6. Should computation be analytic support, scout, falsifier or rigorous closure?
7. What does the falsification track say?
8. Are disputes resolved?
9. What is the strongest sustainable result?

## Core loop

```text
OBJECTIVE
  -> ARCHITECT
  -> THEORY SCAN
  -> APPLICABILITY
  -> OBLIGATION SCHEDULER
  -> ANALYTIC / EXTERNAL / SYMBOLIC / COMPUTATIONAL ROUTE
  -> FALSIFICATION
  -> ADJUDICATION IF NEEDED
  -> SECOND REVIEW
  -> CERTIFICATION
  -> CLOSE or REOPEN GRAPH
```

## Non-majority principle

Scientific disagreement is not resolved by voting.

A conflict becomes a `Dispute_ID` with an explicit resolution obligation.

## Minimal council principle

Do not activate every role by default.

Instantiate only roles required by the active subgraph.

## Canonical authority

Functional consortium roles map to existing authority roles in `config/AGENT_AUTHORITY.md`.

No consortium role bypasses Certification, Exact Witness, Objective Closure, Artifact Consistency, or v2.12 Audit Hard Gates.

## Compatibility

See `config/COMPATIBILITY.md`.

The consortium is optional orchestration. Existing v2.12 workflows remain valid.
