# Published Literature Discovery — v3.1

## Purpose
Create an evidence-backed map of **published** prior art before proposing novelty. This orchestrates protocols/RAG.md, protocols/NOVELTY.md and existing literature/search ledgers; it does not replace them or claim a built-in search engine.

## Corpus and status
Every record must distinguish:
- PUBLISHED_VERIFIED: publisher or authoritative index confirms published bibliographic object (journal article, edited book, proceedings; mark peer-review status separately if verified).
- PREPRINT_VERIFIED: publicly available preprint but publication not confirmed.
- UNVERIFIED: snippet/citation/user recollection/metadata incomplete.
- WITHDRAWN: publication or repository documents withdrawal.

For the **published-publications count**, include only PUBLISHED_VERIFIED. Preprints and withdrawn work remain in a separate watchlist if relevant to priority or overlap; do not call them accepted journal research.

## Discovery process
1. Seed retrieval: identify user-specified article from exact title, DOI, journal or author; if ambiguous produce candidates and provenance, never choose by guess.
2. Query expansion: exact model terms + mathematical synonyms + classical variants and rival terminology + direct counterexamples.
3. Search multiple independent sources when available (publisher, Crossref, OpenAlex, Semantic Scholar, arXiv, discipline-specific indexes); state exactly what sources/tools were reached. Do not claim any database queried without access.
4. Deduplicate by canonical DOI/publisher ID, arXiv ID+version for preprints, or verified title/authors/year combinations. A publication and its preprint version map to a canonical work with separate manifestations.
5. Build ARTICLE_RECORD for each important work; abstract and metadata are leads, not verification of the theorem. Try full text via legal publisher / author repository / open-access links. Mark FULL | PARTIAL | UNAVAILABLE and theorem location.
6. Backward chaining: extract references supporting central statements and query their exact source. Forward chaining: search subsequent works citing the central paper when available. Track depth, stop criteria, author disambiguation (ORCID if verified) and date.
7. Construct a comparison table: objects, hypotheses, claims, method, numerical rigor, exceptions, exact source location. Distinguish proved theorem from numerical conjecture.
8. Identify candidate gaps only inside the searched corpus, then search *against* each gap (countersearch) before recommending a route.
9. Produce coverage report with search strings, databases, query date, included/excluded counts, missing full texts, nearest prior art, countersearches and uncertainty.

## Evidence and bibliographic provenance
Paper evidence needs exact journal/publisher identifier + bibliographic status and reliable location. Theorem applicability needs original formulation or a verifiable full-text equivalent with all hypotheses. Snippet alone => VERIFICATION=partial; no theorem certified.

Bibliography quantity is not a target: 30–40 references may be appropriate to a thorough article, but quality, primary relevance, verification and venue policy control the final count.

## Nonexistence firewall
"No published paper was found in the documented search" is a bounded search outcome, not proof of world-wide novelty. Novelty status uses the existing Novelty Coverage Gate, never "CERTIFIED NEW".

## Outputs
ARTICLE_RECORDs; Evidence Cards; SEARCH_LEDGER and LITERATURE_LEDGER pointers; a research-gap matrix; optional discovered author/citation graph; verification status and remaining retrieval limitations.
