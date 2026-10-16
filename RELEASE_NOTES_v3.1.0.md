# v3.1.0 — Scientific Research Lifecycle

## Purpose
Move from **topic -> literature -> scoped objective -> valid proof -> auditable paper**, without assuming topic equals hypothesis or LaTeX is the source of mathematical truth.

## Added
- RESEARCH_INTAKE: progressive property/domain selection, verified seed, staged objective approval.
- PUBLISHED_LITERATURE_DISCOVERY: only verified publications counted as published; separate preprint/unknown watchlist; source and full-text checks.
- RESEARCH_ROUTE_SELECTION: up to four justified routes with countersearch, user/lead approval and controlled revision.
- THEOREM_APPLICABILITY_LOOP: source, theorem hypotheses, target compatibility, bridge, alternate routes and refutation firewall.
- RESEARCH_GRAPH: project-local connected literature/inquiry/proof graphs; canonical IDs, namespaces and evidence-based checklists.
- THESIS_TO_PAPER: thesis-depth research dossier -> journal manuscript with section/claim mapping, LaTeX and semantic gates.
- Executable structural validator, empty graph template and stdlib regression tests.

## Corrected
- REFUTED essential proof obligation is no longer accepted as a *satisfied* obligation when checking a CERTIFIED claim.
- The legacy v3 blackboard checker now handles non-object node entries gracefully.
- v3.0 and v3.1 blackboard version tags can be read by the runtime state validator; skill template is v3.1.
- CI also runs lifecycle template validation and unit tests.

## Scientific boundaries
- No native vector indexing, scholarly API client, full-text downloader, LaTeX compiler or autonomous runtime has been silently added; the surrounding agent must supply supported capabilities. Publication/metadata verification and scientific second review are external evidence tasks.
- Structural PASS does not prove theorem truth, guarantee novelty or certify manuscript quality.
- No arbitrary quota of 30-40 references: prioritize relevant, verifiable works.

## Compatibility
Additive on v3.0/v2.12. Existing project ledgers, certificates, labels and historical states remain valid; old >=3.0 prompts remain compatible. No auto-migration of active projects.
