# Router dinámico de especialistas

> Este router se ejecuta **después** de `protocols/INTERPRETER.md`. Si el Interpreter determina que la pregunta ya está resuelta por memoria/certificados, no convocar especialistas de investigación.

## Objetivo

Elegir el conjunto mínimo de perspectivas expertas y módulos que reduzca el riesgo de error sin duplicar contexto.

## Política base

- Tarea simple: 1 especialista.
- Tarea científica sustantiva: 1 lead + 1 adversarial.
- Interdisciplinaria: +1 puente.
- Con evidencia computacional material: +1 numérico.
- Máximo normal: 4 durante investigación. El second review de certificación puede reutilizar un revisor independiente o ejecutarse como pase separado; no requiere mantener un agente adicional durante toda la tarea.
- No añadir agentes ni módulos "por si acaso".

## Matriz de activación

| Tipo de tarea | Lead recomendado | Revisor | Añadir si aplica |
|---|---|---|---|
| Explicación desde memoria certificada | none by default | none | domain expert sólo si la explicación requiere reinterpretación técnica |
| Objetivo científico abierto | Research Architect + domain lead | Adversarial reviewer | Literature / Numerical según ruta |
| Demostración en álgebra diferencial | Differential Algebra | Proof Red Team | Identifiability / Symbolic |
| Identificabilidad estructural | Identifiability | Differential Algebra | Control / Symbolic |
| Sistemas dinámicos | Dynamical Systems | Analysis/Geometry | Numerical |
| Caos/bifurcaciones | Chaos & Bifurcation | Dynamical Systems | Numerical |
| Simetrías/acciones de grupo | Lie/Equivariant | Geometry/Topology | Identifiability / Symbolic / finite computation según claim |
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

## Module Selection v2.11

Después de clasificar la tarea, consultar `modules/MODULE_INDEX.md` y seleccionar el conjunto mínimo de módulos que cubra el objetivo y sus dependencias materiales.

Reglas:
- investigación sustantiva -> `CORE_RESEARCH`;
- estado del arte -> `LITERATURE_REVIEW`;
- novedad/prior art -> `NOVELTY_ASSESSMENT`;
- teorema/prueba/refutación -> `THEOREM_RESEARCH`;
- evidencia computacional o cierre computacional material -> `NUMERICAL_STUDY`;
- identificabilidad -> `IDENTIFIABILITY_STUDY`;
- sistemas dinámicos/caos -> `DYNAMICAL_SYSTEMS_STUDY`;
- optimización -> `OPTIMIZATION_STUDY`;
- ML/PINN -> `ML_PINN_STUDY`;
- maximalidad/genericidad/frontera -> `OBJECTIVE_EXPANSION`;
- código científico material -> `CODE_VERIFICATION`;
- auditoría de paper -> `MANUSCRIPT_AUDIT`;
- redacción/render -> `SCIENTIFIC_WRITING`;
- corrección localizada -> `REVISION_ONLY`;
- delegación -> `WORKER_COMPLETION`.

Para tareas `PROVE|REFUTE` con subclaims nuevos o puentes no certificados, cargar `protocols/PROOF_TACTICS.md` mediante `THEOREM_RESEARCH`.

No cargar todos los módulos. Resolver dependencias referenciando protocolos existentes; no duplicarlos en el prompt.

## Proof tactic routing

Cuando una tarea matemática exacta requiera construir o auditar una prueba, el router no debe imponer una sola metodología a toda la tarea. Debe permitir que `protocols/PROOF.md` descomponga el target en obligaciones y que `protocols/PROOF_TACTICS.md` seleccione una táctica apropiada por obligación.

El router debe distinguir, cuando haya computación:

```text
NUMERICAL_ROLE:
  none
  exploratory_numeric
  falsification_search
  corroborative_numeric
  symbolic_exact
  exhaustive_finite
  validated_numeric
  rigorous_computer_assisted_proof
```

Si `NUMERICAL_ROLE` puede ser esencial para cerrar un subclaim exacto, activar `NUMERICAL_STUDY`, `COMPUTATION_CERTIFICATE` y los gates de certificación aplicables.

No confundir que una tarea sea `NUMERICAL` con que la computación tenga fuerza de prueba.

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
PROOF_TACTIC_ROUTING: yes|no
NUMERICAL_ROLE:
RIGOROUS_COMPUTATIONAL_CLOSURE_ALLOWED: yes|no|not_applicable
CERTIFICATION_GATE: yes|no
INDEPENDENT_SECOND_REVIEW: yes|no
MANUSCRIPT_EDIT_GATE: yes|no
TYPE_NOTATION_GATE: yes|no
OBJECTIVE_CLOSURE_GATE: yes|no
CLAIM_STRENGTH_GATE: yes|no
EXACT_WITNESS_GATE: yes|no
ARTIFACT_CONSISTENCY_GATE: yes|no
MEMORY_GC_GATE: yes|no
MULTI_AGENT_HANDOFF: yes|no
RISK_CLASS: R0|R1|R2|R3
DELEGATED_ROLE:
SCIENTIFIC_AUTHORITY_ROLE:
MODULES_TO_LOAD:
PROTOCOLS_TO_LOAD:
MEMORY_TAGS:
TEMPLATES_TO_USE:
TASK_COMPILATION: yes|no
COORDINATION_REQUIRED: yes|no
WORKER_ROLE:
AUDIT_REQUIRED: yes|no
```

No mostrar esta mecánica al usuario salvo que sea útil.

## Delegation routing v2.11

Si `MULTI_AGENT_HANDOFF=yes`, cargar `config/AGENT_AUTHORITY.md`, `protocols/MULTI_AGENT_HANDOFF.md` y `protocols/TASK_COORDINATION.md`.

Si hay worker externo, el Scientific Lead compila `templates/WORKER_MISSION.md` usando `protocols/TASK_COMPILATION.md`.

Routing mínimo:
- R0: deterministic checker; model optional.
- R1: worker + deterministic check; auditor si representa claims.
- R2: worker + deterministic check + scientific auditor.
- R3: Scientific Lead; workers sólo para subtareas acotadas; independent review para certification.

Si una misión delegada contiene una obligación computacional esencial, el contrato debe fijar su `Computation_semantics`, `Closure_standard` y outputs de certificación; el worker no puede decidir unilateralmente que una simulación ordinaria se convirtió en prueba.

El router selecciona roles científicos y módulos. El runtime externo decide qué provider implementa cada rol y es dueño del estado canónico.