# Research Intake & Scientific Delimitation — v3.1

## Mission
Convert a broad topic into a scoped, falsifiable research question without manufacturing novelty or proof. Activate before Research Loop whenever the user supplies a system, article, phenomenon or area but not an exact target.

**Topic is not objective.** A system has many legitimate research questions. A broad topic must never silently become a claim about chaos, stability or identifiability.

## Progressive dialogue
1. Identify the model/source exactly; when only year/title fragments are known, mark SOURCE_VERIFICATION_PENDING. Never invent paper metadata or equations.
2. Offer a small domain-appropriate menu of properties (e.g. chaos/UPOs, bifurcations, symmetry, stability, control) with an open answer option. Ask at most one central choice per turn unless the task clearly warrants more.
3. Refine one property into mathematical object, parameter class, target strength, quantifiers, observable, constraints and potential disproof.
4. Record boundaries: family/model, physical admissibility, interval/domain, known assumptions, excluded cases, theory/numerics level.
5. Trigger Published Literature Discovery, then Research Route Selection; the goal stays provisional until that review is integrated.
6. Present 1–4 defensible route candidates and obtain a scientific choice. Only then formulate and approve a formal objective.
7. If the user already supplies a precise viable objective, verify sufficiency and bypass repetitive questioning. Do not restart approved projects.
8. If information is missing, record it explicitly as UNKNOWN; work can advance provisionally but no implied certification.

## State machine
States:
TOPIC_UNDELIMITED -> SOURCE_VERIFICATION_PENDING or PROPERTY_SELECTED;
SOURCE_VERIFICATION_PENDING -> PROPERTY_SELECTED or SCOPE_PROVISIONAL;
PROPERTY_SELECTED -> SOURCE_VERIFICATION_PENDING or SCOPE_PROVISIONAL;
SCOPE_PROVISIONAL -> LITERATURE_REVIEW_PENDING -> ROUTES_PENDING -> OBJECTIVE_PROPOSED -> OBJECTIVE_APPROVED.

Revisions: ROUTES_PENDING -> LITERATURE_REVIEW_PENDING; OBJECTIVE_PROPOSED -> ROUTES_PENDING; OBJECTIVE_APPROVED -> ROUTES_PENDING or OBJECTIVE_PROPOSED, preserving prior IDs/versions and explaining why.

Each transition records from, to, reason, time and evidence/pointer when applicable. No implicit state skipping. If source identification is irrelevant (self-defined model), PROPERTY_SELECTED -> SCOPE_PROVISIONAL is valid.

Approved objective must specify claim, domain, quantifiers, hypotheses, delimitations, success and refutation criteria, and selected approved research route. Approval is a **research scope decision**, not proof or novelty certification.

## Output
Project-local templates/RESEARCH_GRAPH.json and the intake record; link to Research Objective in templates/RESEARCH_OBJECTIVE.md. Never write user-specific HOT state into the skill's repository-wide template.

## Scientific gates
- User's preference may choose a topic; literature cannot be reverse-engineered to assert fabricated novelty.
- Unpublished and unpublished-in-review works are not counted among published studies.
- An unverified article cannot contribute its purported theorem to proof.
- Objective choice is not a proof result and cannot bypass Research Loop.
- Hand off to protocols/PUBLISHED_LITERATURE_DISCOVERY.md, protocols/RESEARCH_ROUTE_SELECTION.md and then protocols/THEOREM_APPLICABILITY_LOOP.md.
