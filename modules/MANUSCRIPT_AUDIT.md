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

## Obligaciones

Distinguir errores fatales, gaps reparables, claims sobredimensionados, notación inconsistente, citas no verificadas, evidencia insuficiente y mejoras editoriales. No reescribir silenciosamente una afirmación para hacerla verdadera: registrar el delta.

## Salida

`claim-by-claim audit | severity | evidence | required repair | affected files/sections | acceptance criteria | unresolved scientific risks`.