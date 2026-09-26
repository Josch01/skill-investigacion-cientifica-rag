# Dispute Resolution Protocol

Apply when two accepted task-local outputs make incompatible scientific claims.

1. create `templates/DISPUTE_RECORD.md`;
2. normalize both positions;
3. distinguish scientific contradiction from notation/scope mismatch;
4. identify the minimal deciding proposition;
5. create a new Proof Obligation;
6. route it through the normal tactic system;
7. prohibit majority voting;
8. preserve both positions until resolution;
9. propagate status only after the resolution artifact passes relevant gates.

Allowed final dispute states:
`RESOLVED_A | RESOLVED_B | RESOLVED_REFORMULATED | UNRESOLVED`.

A material `UNRESOLVED` dispute blocks affected certification.
