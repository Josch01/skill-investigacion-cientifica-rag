# Consortium Research Orchestration Protocol

## 1. Scope

Activates for substantive new research when consortium mode is enabled.

It composes, not replaces:
`RESEARCH_LOOP.md`, `RAG.md`, `PROOF.md`, `PROOF_TACTICS.md`, `NUMERICS.md`, `CERTIFICATION.md`.

## 2. Bootstrap

1. preserve the user's original objective;
2. create/refresh Research Objective;
3. build active blackboard projection;
4. choose execution mode from `config/EXECUTION_MODES.md`;
5. select minimum functional roles from `consortium/ROLE_REGISTRY.md`.

## 3. Architecture pass

Research Architect must produce:
- exact target;
- success/refutation criteria;
- object/type registry;
- initial claim graph;
- essential proof obligations;
- initial routes;
- uncertainty/blockers.

No proof verdict is allowed in this pass unless inherited from a compatible certificate.

## 4. Theory-first pass

Theory Scout + Applicability Judge:
- recover certified internal results first;
- search primary literature when needed;
- create Evidence Cards;
- verify theorem hypotheses one by one;
- create missing-hypothesis obligations instead of assuming applicability.

## 5. Obligation loop

For each essential open obligation:
- run scheduler;
- execute selected tactic;
- record evidence;
- run falsification track when material;
- open dispute if outputs conflict;
- update route state.

## 6. Computation escalation

Ordinary code is never the default merely because it is available.

Use `Computational Strategist` logic:
`none | symbolic_exact | exploratory_numeric | falsification_search | corroborative_numeric | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`.

Any exact closure must still satisfy existing numerical and certificate gates.

## 7. Adversarial pass

Material claims must survive:
- objection verification;
- counterexample search appropriate to scope;
- dependency/status propagation;
- exact-witness checks when required.

## 8. Second review

Apply `SECOND_REVIEW_COVERAGE.md` with the strongest independence available in the selected runtime.

## 9. Certification and closure

Certification remains governed exclusively by existing gates.

The consortium may propose `candidate_for_certification`; it cannot bypass gates.

## 10. Learning from failure

Every failed route must contribute one of:
- eliminated hypothesis;
- missing lemma;
- obstruction;
- counterexample;
- useful source;
- local/conditional result;
- next tactic.

## 11. Final output

Return:
`OBJECTIVE | STRONGEST_SUSTAINABLE_RESULT | SUCCESSFUL_ROUTE | FAILED_ROUTES | OPEN_OBLIGATIONS | DISPUTES | EVIDENCE_CLASSES | NEW_CERTIFICATES | NEXT_HIGHEST_VALUE_STEP`.
