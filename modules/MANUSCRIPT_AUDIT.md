# Module: MANUSCRIPT_AUDIT

## Activar cuando

El usuario solicite auditar un manuscrito, sección, preprint, tesis o paper respecto de rigor, consistencia, literatura, notación, claims y evidencia.

## Composición

- `modules/CORE_RESEARCH.md`
- `modules/LITERATURE_REVIEW.md` si el estado del arte o citas son materiales.
- `modules/THEOREM_RESEARCH.md` para claims analíticos centrales.
- `modules/NUMERICAL_STUDY.md` para resultados computacionales centrales.
- `protocols/AUDIT.md`
- `protocols/TYPE_NOTATION_GATE.md`
- `protocols/ARTIFACT_CONSISTENCY.md`
- `protocols/MANUSCRIPT_AUDIT_COVERAGE.md`
- `protocols/CLAIM_EVIDENCE_ARTIFACT_SEPARATION.md`
- `protocols/ADVERSARIAL_OBJECTION_GATE.md`
- `protocols/SECOND_REVIEW_COVERAGE.md`
- `protocols/SEMANTIC_ARTIFACT_COMPLETENESS.md`
- `protocols/AUDIT_BATCHING.md`

## Obligaciones

Distinguir errores fatales, gaps reparables, claims sobredimensionados, notación inconsistente, citas no verificadas, evidencia insuficiente y mejoras editoriales. No reescribir silenciosamente una afirmación para hacerla verdadera: registrar el delta.

Antes de revisar pruebas, construir inventario canónico y dependency skeleton.

Definitions y assumptions se auditan con semántica propia; no reciben automáticamente proof status.

Toda objeción material del Red Team debe tener `Objection_ID` y status verificable.

Si `N_CENTRAL_CLAIMS > 6`, usar bloques de 4–6 claims relacionados por dependencia salvo justificación explícita.

## Hard completion criteria

Una auditoría completa requiere simultáneamente:

- `AUDIT_COVERAGE_STATUS=PASS`;
- proof state específico, sin boilerplate, para todos los theorem-like claims del scope;
- dependency graph materialmente completo o `DEPENDENCIES=NONE` justificado;
- claim/evidence/artifact statuses separados;
- objeciones materiales verificadas o registradas como unresolved;
- second-review coverage completo para claims que lo requieren;
- semantic artifact completeness;
- artifact consistency sin contradicciones activas.

## Salida

`claim-by-claim audit | severity | evidence | required repair | affected files/sections | acceptance criteria | unresolved scientific risks | coverage metrics | batch plan | objection status`.
