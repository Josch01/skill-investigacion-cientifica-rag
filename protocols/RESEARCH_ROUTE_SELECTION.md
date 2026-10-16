# Research Route Selection and Objective Approval — v3.1

## Input
A scoped property, verified prior art with countersearch coverage, explicit unknowns and source limitations. Preserve existing Objective Closure / Novelty gates.

## Candidate route packet
For each route record:
- id; scientific question / candidate claim and its negation;
- published closest prior art and direct comparison of assumptions/object/method/conclusion;
- the observed coverage gap (not a claim of global absence);
- hypothesized mathematical or numerical contribution;
- evidence availability, assumptions, possible obstructions and proposed falsification;
- initial proof obligations and alternative tactics;
- feasibility and scientific value (qualitative, no fake precise score);
- status: PROPOSED | REVIEW_REQUIRED | APPROVED | BLOCKED | SUPERSEDED.

Return **up to four**, not exactly four: do not invent novelty to fill a quota. Search explicitly for papers contradicting each proposed gap. Distinguish a new proof from a new theorem and an exploratory case study from a theorem about a family.

## Objective approval
An approved route permits a Research Objective:
Exact statement P, mathematical domain/regularity/parameters, quantifiers, claimed local/global or generic/universal strength, hypotheses, delimitations, expected contribution, success criterion and rigorous disproof criterion.

Scientific Lead checks consistency and user confirms/selects the scientific direction; record route ID, date and approval. If user already supplied a precise objective, assess it against literature first and offer targeted scope repairs without forcing four routes.

## Reopen conditions
New decisive literature, counterexample, unrealizable hypothesis, non-applicable theorem, or a mathematically different target must open a revision decision; do not silently replace the original. Route FAILED != target REFUTED.

## Handoff
Persist route decision in project-local research graph / ROUTE_LEDGER; hand off to Research Loop and protocols/THEOREM_APPLICABILITY_LOOP.md.
