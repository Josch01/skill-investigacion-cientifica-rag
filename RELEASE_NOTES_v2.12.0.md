# Release Notes v2.12.0 — Audit Hard Gates

## Motivo

v2.12 endurece la auditoría de manuscritos después de observar fallos de ejecución donde un modelo podía producir los artefactos nominales correctos sin realizar una revisión científica claim-by-claim suficientemente específica.

## Nuevos protocolos

- `protocols/MANUSCRIPT_AUDIT_COVERAGE.md`
- `protocols/CLAIM_EVIDENCE_ARTIFACT_SEPARATION.md`
- `protocols/ADVERSARIAL_OBJECTION_GATE.md`
- `protocols/SECOND_REVIEW_COVERAGE.md`
- `protocols/SEMANTIC_ARTIFACT_COMPLETENESS.md`
- `protocols/AUDIT_BATCHING.md`

## Invariantes nuevos

```text
ARTIFACT_EXISTS != ARTIFACT_SEMANTICALLY_COMPLETE
CLAIM_STATUS != EVIDENCE_STATUS != ARTIFACT_STATUS
PROPOSED_OBJECTION != VERIFIED_OBJECTION
SECOND_REVIEW_FILE_EXISTS != SECOND_REVIEW_COVERAGE
AUDIT_INVENTORY_EXISTS != AUDIT_COVERAGE
```

## Cambios de comportamiento

### Coverage

Una auditoría completa debe contar el inventario canónico y cerrar la correspondencia entre objetos en scope y registros auditados.

### Semántica por tipo

- assumptions se tratan como hipótesis explícitas, no como teoremas no demostrados;
- definitions se auditan por tipado/no circularidad/consistencia, no por proof status;
- theorem-like claims requieren obligaciones y dependencias específicas.

### Evidence separation

Invalidar un cálculo corroborativo ya no puede refutar automáticamente un theorem cuya prueba analítica sobreviva.

### Red Team

Las objeciones adversariales tienen su propio status:
`PROPOSED | VERIFIED | REFUTED | UNRESOLVED`.
Una objeción plausible pero no verificada no autoriza `REFUTED`.

### Second Review

La existencia de `SECOND_REVIEW.md` ya no basta. Se exige cobertura específica por claim relevante.

### Semantic completeness

Archivos vacíos o boilerplate no satisfacen el protocolo por existir.

### Batching

Con más de 6 claims matemáticos centrales, la auditoría se divide por defecto en bloques de 4–6 y se reconcilia globalmente antes de certificar.

## Plantillas nuevas

- `templates/MANUSCRIPT_AUDIT_COVERAGE_REPORT.md`
- `templates/ADVERSARIAL_OBJECTION.md`
- `templates/SECOND_REVIEW_RECORD.md`
- `templates/ARTIFACT_COMPLETENESS_REPORT.md`

## Compatibilidad

No cambia la taxonomía canónica de `Computation_semantics` ni los veredictos de handoff de v2.11. La versión mínima de los prompts canónicos pasa a v2.12.0.
