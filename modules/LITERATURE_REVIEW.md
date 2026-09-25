# Module: LITERATURE_REVIEW

## Activar cuando

Se requiera teoría existente, antecedentes, fuente original, estado del arte, cobertura bibliográfica o comparación con literatura.

## Requiere

Protocolos:
- `protocols/RAG.md`
- `config/RETRIEVAL_POLICY.md`

Memoria:
- `memory/LITERATURE_LEDGER.md`
- `memory/SEARCH_LEDGER.md`
- Evidence Cards pertinentes ya verificadas.

Templates:
- `templates/EVIDENCE_CARD.md`
- `templates/APPLICABILITY_MATRIX.md` cuando una fuente sostenga un paso.

## Obligaciones

- Descomponer el objetivo en claims/bridges consultables.
- Priorizar fuentes primarias y detener recuperación cuando la evidencia sea suficiente.
- Registrar fecha, alcance, consultas y limitaciones de búsqueda.
- No usar snippets como sustituto del texto necesario.
- No confundir existencia de referencias relacionadas con aplicabilidad al objeto actual.

## Output mínimo

`verified_sources | claims_supported | applicability | unresolved_gaps | search_scope | limitations`.