# Theorem Applicability & Proof Repair Loop — v3.1

## Rule
An external theorem is usable only after checking its **exact source, statement, universe, hypotheses, conclusion and relation to our target**. Mentioning or citing a named theorem is never proof of applicability.

### Loop for obligation PO
1. Retrieve strongest suitable *verified* primary theorem and record source ID, DOI/venue, section/page/theorem number (when available), textual coverage FULL/PARTIAL and version.
2. Type-check map domains, time regularity, parameters, invariance and required spaces; add theorem statement T: (H1 and ... and Hn) => Q.
3. For each Hi, make an applicability row with Hi, its exact interpretation in our model, evidence (proved lemma / source / certified computation) and status VERIFIED | REFUTED | UNVERIFIED.
4. If any essential Hi is UNVERIFIED, open a NEW sub-obligation for Hi; do not invoke T yet. If Hi is false for the target system, mark theorem NOT_APPLICABLE **not** target REFUTED.
5. Even when all Hi hold, verify any bridge Q => P and record its proof separately; otherwise theorem is at most CONDITIONALLY_APPLICABLE.
6. Apply the theorem only after the hypotheses, source and bridge close under the required rigorous standard; persist THEOREM_APPLICATION with source and evidence.
7. Attempt adversarial objections: hidden differentiability, noncompactness, transversality, parameter boundaries, local/global switches, exceptional sets, loss of positivity.
8. If route fails: choose a nearby theorem, strengthen/alter transparent assumptions, prove auxiliary lemma, use suitable symbolic/validated computation, or weaken target with user-approved revision. Reuse route knowledge, do not fabricate assumptions.
9. When an exact counterexample to P is independently verified, the target may become REFUTED under the existing adversarial and certification rules. A failed theorem hypothesis or failed tactic alone **cannot** refute P.

## Status
UNVERIFIED | CONDITIONALLY_APPLICABLE | NOT_APPLICABLE | APPLICABLE.
APPLICABLE requires source text inspected, all essential hypotheses individually verified, and theorem conclusion-to-target bridge verified. Applicability != completed theorem proof if PO contains more steps.

## Artifacts
templates/THEOREM_APPLICATION.md, Evidence Card, applicability matrix, Proof Obligation ID, route outcome. Preserve existing PROOF, PROOF_TACTICS, RAG, NUMERICS, EXACT_WITNESS and CERTIFICATION as normative.
