# Thesis-depth Research -> Journal Paper — v3.1

## Rule
Investigate with thesis-like depth; publish with article-specific economy. A paper is **rendered from scientific artifacts**, not a place for the language model to invent missing arguments.

## Project dossier (research source of truth)
Keep:
- topic, verified seed source, broad motivation, problem statement, delimitations and selected objective;
- explicit hypotheses (mathematical assumptions vs scientific conjectures), scope, parameters and versioned notations;
- state-of-the-art map and closest prior art; documented countersearch and references;
- argument graph with Proof Obligations, exact theorem applications and application matrices;
- certified analytic results and separately classified exploratory/corroborative/validated numerical outcomes;
- unresolved objections, limitation record, open questions, negative results and route history.

Use templates/RESEARCH_DOSSIER.md; do not require final manuscript to include all of this internal material.

## Planning
1. Choose journal/format, retrieve latest publisher instructions under JOURNAL_COMPLIANCE.
2. Create a section-to-claim manifest: which objective/claim/support is displayed, source ID and proof skeleton.
3. Abstract: write *after* conclusions are grounded, no unsupported novelty.
4. Introduction: motivated problem, closest published prior art and precisely bounded contribution.
5. Definitions/setup: single authoritative notation, spaces, domains, units, regularity, hypotheses.
6. Results: theorem/lemma/proposition statements and proof arguments constructed **before prose**. Every nontrivial inferential arrow must match its certificate, applicability record, source or new explicitly proved step.
7. Numerical studies: methods, datasets/parameters/code, diagnostics, error and limitations, and taxonomy from NUMERICS; do not render ordinary simulation as proof.
8. Discussion/conclusion: answer original objective vs achieved claim, limitations and legitimate future directions. No unexplored family silently becomes a theorem.
9. References: generate bib entries only from verified bibliographic records; target relevance, not an arbitrary 30–40 quota; in-review papers do not masquerade as published.
10. Supplements: full proofs or computational artifacts if journal format benefits, with pointers and hashes.

## Two independent render gates
A. Mechanical gate: LaTeX syntax/compile, citations/labels, bibliography metadata, symbols/undefined macros, environments and reproducibility links.
B. Semantic gate: for each manuscript claim compare certified Exact_statement, hypotheses, domain, quantifiers, scope, exceptions, numerical epistemic class and dependencies via SEMANTIC_DIFF. A changed claim reopens scientific work instead of being quietly rewritten.
LaTeX compilation succeeds != mathematical truth. Missing source material => explicit placeholder / DRAFT_RENDER, never manufacture theorem proof.

## MANUSCRIPT_READY
Requires approved objective, complete claim-to-section traceability, successful notation and semantic checks, successful compile when tooling allows, verified bibliography, and no unsupported central theorem. A not-yet-certified proposition may be presented honestly as a conjecture/discussion, **not** as an established central result.

## Outputs
templates/RESEARCH_DOSSIER.md, section-claim manifest, manuscript LaTeX and BibTeX (only if requested), semantic diff report, proof obligations outstanding, journal compliance checklist.
