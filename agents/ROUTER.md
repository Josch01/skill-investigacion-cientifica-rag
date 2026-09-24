# Router dinámico de especialistas

> Este router se ejecuta **después** de `protocols/INTERPRETER.md`. Si el Interpreter determina que la pregunta ya está resuelta por memoria/certificados, no convocar especialistas de investigación.

## Objetivo

Elegir el conjunto mínimo de perspectivas expertas que reduzca el riesgo de error sin duplicar contexto.

## Política base

- Tarea simple: 1 especialista.
- Tarea científica sustantiva: 1 lead + 1 adversarial.
- Interdisciplinaria: +1 puente.
- Con evidencia computacional material: +1 numérico.
- Máximo normal: 4 durante investigación. El second review de certificación puede reutilizar un revisor independiente o ejecutarse como pase separado; no requiere mantener un agente adicional durante toda la tarea.
- No añadir agentes "por si acaso".

## Matriz de activación

| Tipo de tarea | Lead recomendado | Revisor | Añadir si aplica |
|---|---|---|---|
| Explicación desde memoria certificada | none by default | none | domain expert sólo si la explicación requiere reinterpretación técnica |
| Objetivo científico abierto | Research Architect + domain lead | Adversarial reviewer | Literature / Numerical según ruta |
| Demostración en álgebra diferencial | Differential Algebra | Proof Red Team | Identifiability / Symbolic |
| Identificabilidad estructural | Identifiability | Differential Algebra | Control / Symbolic |
| Sistemas dinámicos | Dynamical Systems | Analysis/Geometry | Numerical |
| Caos/bifurcaciones | Chaos & Bifurcation | Dynamical Systems | Numerical |
| Simetrías/acciones de grupo | Lie/Equivariant | Geometry/Topology | Identifiability |
| Optimización de modelos | Optimization | Numerical | Statistics/ML |
| Redes neuronales/PINN | ML | Numerical | Statistics/domain |
| Auditoría de manuscrito | Domain lead | Scientific Auditor | Numerical + Literature |
| Revisión de código científico | Numerical | Domain lead | Software/Reproducibility |
| Novedad/estado del arte | Literature | Domain lead | Scientific Auditor |
| Certificación de claim central | Domain lead | Independent second reviewer | Numerical/Literature gate según dependencia |
| LaTeX final | Scientific Editor | Domain lead | Auditor |
| Render/edición de claim certificado | Scientific Editor | Manuscript Consistency Reviewer | Domain lead si aparece mismatch |

## Selección adversarial

El revisor debe ser suficientemente cercano para detectar errores, pero no idéntico al lead.

## Salida del router

```text
INTERPRETER_DECISION:
ANSWER_DEPTH:
TASK_CLASS:
LEAD:
REVIEWER:
OPTIONAL:
WHY:
RETRIEVAL_TAGS:
CERTIFICATES_TO_LOAD:
RESEARCH_LOOP: yes|no
ROUTE_LEDGER_TO_LOAD:
CERTIFICATION_GATE: yes|no
INDEPENDENT_SECOND_REVIEW: yes|no
MANUSCRIPT_EDIT_GATE: yes|no
TYPE_NOTATION_GATE: yes|no
OBJECTIVE_CLOSURE_GATE: yes|no
CLAIM_STRENGTH_GATE: yes|no
EXACT_WITNESS_GATE: yes|no
ARTIFACT_CONSISTENCY_GATE: yes|no
```

No mostrar esta mecánica al usuario salvo que sea útil.
