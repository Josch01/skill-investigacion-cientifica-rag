# Module: NOVELTY_ASSESSMENT

## Activar cuando

El usuario pregunte por novedad, contribución, prior art, prioridad o nivel de diferenciación respecto de la literatura.

## Requiere

- `modules/LITERATURE_REVIEW.md`
- `protocols/NOVELTY.md`
- `protocols/CERTIFICATION.md` para el Novelty Coverage Gate.

Memoria:
- `memory/LITERATURE_LEDGER.md`
- `memory/SEARCH_LEDGER.md`

Templates:
- `templates/EVIDENCE_CARD.md`
- `templates/NOVELTY_COVERAGE.md`

## Obligaciones

1. Descomponer la contribución: objeto, hipótesis, conclusión, generalización, método, combinación, algoritmo, benchmark/aplicación.
2. Buscar por múltiples familias de consultas y terminología histórica/sinónimos.
3. Identificar prior art más cercano y comparar hipótesis/objeto/conclusión/método.
4. Hacer backward/forward chaining cuando sea material y disponible.
5. Declarar fecha, cobertura y límites de la búsqueda.

## Estados permitidos

`PRIOR_ART_FOUND | KNOWN_COMPONENTS_NEW_COMBINATION | APPARENTLY_NEW_WITHIN_SEARCH_SCOPE | STRONG_NOVELTY_SUPPORT | NOVELTY_UNRESOLVED`

## Prohibido

No emitir `FIRST`, `UNIQUE`, `CERTIFIED NEW` o equivalentes sin evidencia extraordinaria.