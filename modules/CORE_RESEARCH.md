# Module: CORE_RESEARCH

## Activar cuando

Toda tarea científica sustantiva requiera nueva investigación, deducción, refutación, evaluación de evidencia o extensión de un resultado existente.

## Composición mínima

Protocolos:
- `protocols/INTERPRETER.md`
- `protocols/RESEARCH_LOOP.md`
- `protocols/RAG.md`
- `protocols/TYPE_NOTATION_GATE.md`
- `protocols/CONSORTIUM_RESEARCH.md` cuando `CONSORTIUM_MODE=yes`

Memoria inicial:
- `memory/MEMORY_CORE.md`
- tags pertinentes de `memory/MEMORY_INDEX.md`
- sólo el subgrafo necesario después del Sufficiency Gate.

Templates típicos:
- `templates/RESEARCH_OBJECTIVE.md`
- `templates/CLAIM_SIGNATURE.md` cuando el claim sea material.

## Obligaciones

1. Formalizar objetivo, éxito, refutación, dominio, cuantificadores, hipótesis y scope.
2. Intentar primero memoria/certificados antes de RAG externo.
3. Mantener separados `[L] [D] [C] [N] [H] [X] [U] [DEC]`.
4. Conservar track de prueba y track de falsificación cuando corresponda.
5. No confundir éxito de una ruta con cierre del objetivo.
6. Ejecutar gates especializados activados por módulos adicionales.
7. Terminar con el strongest sustainable result, no con el resultado deseado.

## No duplica

Este módulo no redefine RAG, Proof, Numerics, Novelty ni Certification. Sólo los compone cuando otros módulos los requieren.

## v3.0 Consortium compatibility

El módulo conserva el Research Loop existente como semántica científica.
El consorcio sólo añade scheduling/roles/blackboard para ejecutar el mismo objetivo por obligaciones.
