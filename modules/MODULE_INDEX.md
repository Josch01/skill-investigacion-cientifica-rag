# Scientific Task Module Registry

## Propósito

Los módulos son **recetas de composición**, no protocolos científicos nuevos. Indican qué protocolos, memoria, templates, gates y outputs cargar para una clase de tarea sin duplicar las reglas ya normativas de la skill.

Principio:

`protocols = cómo operar rigurosamente`

`modules = qué piezas ensamblar para esta tarea`

`templates = cómo representar contratos, evidencia y resultados`

## Reglas de selección

1. Ejecutar primero `protocols/INTERPRETER.md`.
2. Si basta memoria/certificados, no activar módulos de investigación.
3. Si se requiere nueva investigación, `agents/ROUTER.md` selecciona el conjunto mínimo de módulos.
4. Cargar `CORE_RESEARCH` para toda investigación científica sustantiva.
5. Añadir sólo módulos que cubran dependencias materiales del objetivo.
6. Un módulo nunca autoriza fortalecer claims ni saltarse gates.
7. Los módulos referencian protocolos existentes; no los reescriben.
8. El Scientific Lead compila los módulos seleccionados mediante `protocols/TASK_COMPILATION.md`.

## Registro

| Módulo | Activación típica | Piezas principales |
|---|---|---|
| `CORE_RESEARCH` | investigación científica sustantiva | Research Loop, RAG, notación, cierre |
| `CONSORTIUM_RESEARCH` | objetivo R3 con múltiples obligaciones/rutas/agentes | Blackboard, Scheduler, Context Firewall, Adjudication, runtime profiles |
| `LITERATURE_REVIEW` | teoría existente, estado del arte, fuentes | RAG, Search/Literature ledgers |
| `NOVELTY_ASSESSMENT` | novedad, contribución, prior art | RAG, Novelty, Novelty Coverage |
| `THEOREM_RESEARCH` | demostrar/refutar/teorema/lema | Proof, Proof Tactics, Certification, Red Team |
| `NUMERICAL_STUDY` | ODE/PDE, simulación, optimización, ML, cómputo | Numerics, Computation Certificate |
| `IDENTIFIABILITY_STUDY` | identificabilidad/observabilidad/simetrías | Proof + Numerics + falsificación |
| `DYNAMICAL_SYSTEMS_STUDY` | estabilidad, bifurcaciones, caos | Proof/Proof Tactics/Numerics según claim |
| `OBJECTIVE_EXPANSION` | broadest/maximal/strongest/generic/universal | Objective Closure, Exact Witness |
| `CODE_VERIFICATION` | producir/revisar código científico | Numerics, reproducibilidad, deterministic gate |
| `MANUSCRIPT_AUDIT` | auditar manuscrito científico | Audit, coverage, batching, objection verification, second-review coverage, semantic artifact completeness |
| `SCIENTIFIC_WRITING` | renderizar resultados verificados | Manuscript Edit, Type/Notation, LaTeX si aplica |
| `REVISION_ONLY` | corregir objeciones de auditoría | delta mínimo, misma autoridad y contrato |
| `WORKER_COMPLETION` | toda tarea delegada | handoff, result, signals, completion gate |

## Composición

Ejemplo de novedad:

`CORE_RESEARCH + LITERATURE_REVIEW + NOVELTY_ASSESSMENT + WORKER_COMPLETION`

Ejemplo de teorema con soporte o cierre computacional:

`CORE_RESEARCH + THEOREM_RESEARCH + NUMERICAL_STUDY + WORKER_COMPLETION`

En ese caso `THEOREM_RESEARCH` enruta cada subclaim mediante `protocols/PROOF_TACTICS.md`, y `NUMERICAL_STUDY` sólo adquiere fuerza de cierre cuando satisface el estándar matemático de la obligación correspondiente.

Ejemplo de maximalidad en identificabilidad:

`CORE_RESEARCH + IDENTIFIABILITY_STUDY + OBJECTIVE_EXPANSION + WORKER_COMPLETION`

## Regla de economía

No cargar todos los módulos. Seleccionar el conjunto mínimo que cubra el objetivo, sus dependencias y los gates obligatorios.

La presencia de una táctica en el registro no obliga a usarla: las tácticas son opciones de cierre por obligación, no checklist obligatorio.

## Consortium selection v3.0

Seleccionar `CONSORTIUM_RESEARCH` cuando el objetivo científico requiera varias rutas materiales, composition de resultados conocidos, elección adaptativa analytic/computational, falsificación paralela o resolución de disputas.

No seleccionarlo sólo por complejidad narrativa.

`CONSORTIUM_RESEARCH` orquesta los módulos existentes; no sustituye `THEOREM_RESEARCH`, `NUMERICAL_STUDY`, `LITERATURE_REVIEW` ni los gates v2.12.
