# Scientific Knowledge Graph and Checklist — v3.1

## Three connected layers, distinct semantics
1. Bibliographic graph: paper, person, citation, theorem source, publication manifestation; citation cycles allowed.
2. Inquiry graph: topic, scope decisions, routes, objective versions, gaps, objections; cycles allowed across revisions, never erase history.
3. Proof DAG: claim, hypothesis, obligation, theorem application, evidence and certificate dependencies. **requires** edges must be acyclic; never equate refutation of a required premise with its satisfaction.

All canonical objects have stable IDs, scoped definitions, typed edges, provenance and artifact locations. New tactic under the same PO preserves ID; changing the logical statement requires an explicit new version.

## Authority
Project-scoped dossier/ledgers and certificates are canonical. Project-local research_graph.json is an index/projection with useful deterministic invariants; a JSON pass is NOT scientific certification. Workers propose graph changes; scientific lead/auditor approves status transitions.

## Essential conditions
- Claim CERTIFIED requires reviewed proof and every essential positive proof obligation RIGOROUSLY_CLOSED with sufficient certificate. REFUTED is **closed as a question**, but NOT satisfied as a prerequisite.
- REFUTED target requires a certified contradiction or valid counterexample, not an inapplicable theorem or failed tactic.
- Changing hypothesis, scope, notation or mathematical object creates version/decision trail and triggers dependent review.
- Literature and source IDs maintain publication vs preprint status and verification depth.
- If a study is already active at v3.0, neither renumber nor silently migrate existing IDs.

## Symbol table and namespaces
Use memory/SYMBOL_TABLE.md as the canonical object registry. Treat object identity (ID), symbol, type, meaning, dimension/domain, scope and alias explicitly.
Same glyph may be reused **only in nonoverlapping local scopes** or when representing the same object as declared alias. Globally theta=angle and theta=function without scope distinction is a collision.
Different glyphs for the same object require an explicit alias/bridge. Bound indices and dummy variables may be locally shadowed with clear scope. Validate against protocols/TYPE_NOTATION_GATE.md, not typographic matching alone.

## Checklist
Checklist items are **derived from evidence/status in the graph**, not editable declarations of scientific truth. Display missing obligation/source/application/second review. Clicking a checklist box never marks a theorem certified.

## Runtime implementation
scripts/validate_research_lifecycle.py checks deterministic structural guards for project JSON. Its schema is documented by templates/RESEARCH_GRAPH.json and tests. It cannot inspect the mathematics. Legacy blackboard stays a HOT projection; no second canonical authority is created.

## Project isolation
Each manuscript/project has its own objects, ARTICLE_RECORDs, graph and dossier. The skill repository keeps **empty templates and normative procedures**, never live thesis memory from unrelated research.
