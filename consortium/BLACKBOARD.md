# Scientific Blackboard

## Purpose

Provide a small runtime view of the active research graph without replacing canonical memory/certificates.

## Node types

`OBJECTIVE`
`CLAIM`
`OBLIGATION`
`ROUTE`
`EVIDENCE`
`OBJECTION`
`DISPUTE`
`COMPUTATION`
`CERTIFICATE`

## Required node identity

Every node has:
- stable ID;
- type;
- status;
- provenance;
- parent IDs where applicable;
- canonical artifact pointer when one exists.

## Event types

`NODE_CREATED`
`DEPENDENCY_ADDED`
`ROUTE_ACTIVATED`
`ROUTE_BLOCKED`
`EVIDENCE_ADDED`
`OBJECTION_RAISED`
`DISPUTE_OPENED`
`OBLIGATION_CLOSED`
`CERTIFICATE_ACCEPTED`
`NODE_SUPERSEDED`

## Authority

Workers may propose events.

Only the authorized Scientific Lead/Auditor + gates may integrate status-changing events into canonical state.

## Invariants

- no `CERTIFIED` claim with an essential `OPEN|EVIDENCE_ONLY` obligation;
- no `REFUTED` claim solely because a route failed;
- no exact closure from ordinary float/high precision;
- no resolved dispute without a resolution artifact;
- no status-changing evidence propagation without essentiality analysis;
- no hidden hypothesis injection.

## Context budget

The blackboard contains only active/HOT nodes.

Historical detail remains in ledgers/artifacts by pointer.

## Canonical status

The blackboard mirrors scientific status; it does not originate certification.
