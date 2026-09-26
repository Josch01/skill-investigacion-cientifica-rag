# Semantic Artifact Completeness Gate

## 1. Propósito

Distinguir:

`ARTIFACT_EXISTS`
de
`ARTIFACT_SEMANTICALLY_COMPLETE`.

Un archivo vacío, boilerplate o contenido genérico no satisface un protocolo.

## 2. Completitud mínima

Cada artefacto obligatorio debe declarar sus campos materiales y contener valores específicos de la tarea.

Ejemplos:

### PROOF_STATE
Para claims demostrables:
- exact statement;
- concrete hypotheses;
- concrete dependencies;
- specific proof obligations;
- status;
- unresolved gaps.

### DEPENDENCY_GRAPH
Cada claim central debe tener:
- incoming dependencies;
- o `DEPENDENCIES = NONE` con justificación.

### ROUTE_LEDGER
Cada ruta:
- target;
- method;
- dependencies;
- result;
- failure reason/knowledge gained cuando falle.

### LITERATURE_LEDGER
No cuenta como revisión bibliográfica si sólo lista el manuscrito o el nombre del protocolo.

### SECOND_REVIEW
Debe satisfacer `protocols/SECOND_REVIEW_COVERAGE.md`.

## 3. Placeholder detection

Marcar `INCOMPLETE` si predominan frases no específicas como:
- "standard assumptions";
- "previous results";
- "pending rigorous closure";
- "attempted refutation";
- "needs more scrutiny";
- copias idénticas entre claims sin contenido matemático específico.

No se prohíbe lenguaje conciso; se prohíbe usar boilerplate como sustituto del análisis.

## 4. Gate de cierre

Registrar por artefacto:

`Artifact -> required_fields -> populated_specific_fields -> missing_fields -> COMPLETE|PARTIAL|EMPTY`.

`AUDIT_COMPLETE` queda bloqueado si un artefacto obligatorio es `EMPTY` o si uno central es `PARTIAL` sin justificación.
