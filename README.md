# Scientific Research RAG Council

Skill de investigación científica/matemática RAG-first con:

- selección dinámica de especialistas;
- regla absoluta de no inventar;
- literatura recuperada antes de usar resultados externos;
- Evidence Cards y matrices de aplicabilidad;
- demostración + red team;
- Proof Certificates reutilizables;
- memoria científica indexada;
- auditoría de manuscritos;
- protocolos estrictos de numeración, optimización, ML y caos;
- Context7 opcional para documentación actual de software;
- cumplimiento dinámico de políticas de revista;
- registro de búsquedas RAG reutilizable;
- presupuesto explícito de contexto;
- Research Loop orientado a objetivos con rutas sucesivas de prueba/refutación;
- Answer Interpreter para responder desde memoria/grafos sin rehacer investigación;
- recuperación jerárquica con Sufficiency Gate;
- modos de explicación simple, technical, rigorous y paper;
- Certification Gate con propagación de dependencias, second review, cómputo reproducible y coverage de novedad;
- Manuscript Rendering Gate con tipado de objetos, Claim Signatures, Minimal Patch Policy y Semantic Diff;
- Objective Closure Gate para comprobar que el resultado final responde realmente al objetivo y no sólo a una subfamilia más fácil;
- Claim Strength Firewall para genericidad, maximalidad, minimalidad e imposibilidad;
- Exact Witness Gate para separar no-anulación exacta de evidencia float/high-precision;
- Artifact Consistency Gate para sincronizar certificados, proof obligations, computation certificates, second reviews, ledgers y manuscrito;
- Memory Lifecycle & GC para mantener un working set acotado aunque el proyecto acumule años de investigación;
- Multi-Agent Scientific Handoff para delegar escritura, código y numerics sin transferir autoridad epistemológica;
- Proof-Obligation Tactic Routing para seleccionar una táctica distinta por subclaim;
- Contract Preservation Check entre `TASK_PACKET` y `WORKER_MISSION`;
- validación estática automática de rutas, enums, señales y versionado.

## Idea central

```text
Pregunta
  -> Interpreter
     -> ¿ya está resuelta?
        -> sí: memoria/certificado/subgrafo -> respuesta adaptada
        -> no: Router
     -> mínimo panel necesario
        -> Module Selection
           -> TASK_PACKET
              -> WORKER_MISSION
                 -> Research / Proof / Numerics / Literature
                    -> WORKER_RESULT + certificates
                       -> deterministic gate
                          -> scientific audit
                             -> certification / revision / reopen
                                -> objective closure
                                   -> canonical memory
```

## Estructura

```text
SKILL.md
agents/
protocols/
config/
memory/
modules/
templates/
prompts/
scripts/
.github/workflows/
```

La skill principal es deliberadamente más corta que todos los protocolos juntos. Los archivos auxiliares deben cargarse sólo cuando la tarea los requiere.

## Context7

Context7 no sustituye la literatura científica. Se integra únicamente como proveedor de documentación actual de librerías/APIs.

Repositorio: https://github.com/upstash/context7

Si el cliente lo soporta, puede instalarse con el procedimiento oficial de Context7. Si no está disponible, usar documentación oficial actual.

## Uso recomendado

### Demostración

1. cargar `SKILL.md`;
2. cargar `MEMORY_CORE.md`;
3. resolver tags en `MEMORY_INDEX.md`;
4. abrir Proof Certificates relevantes;
5. recuperar literatura faltante;
6. aplicar `protocols/PROOF.md` y, para subclaims nuevos, `protocols/PROOF_TACTICS.md`.

### Auditoría

Cargar:

- `protocols/AUDIT.md`;
- protocolos del dominio;
- sólo las secciones del manuscrito necesarias.

### Programación/numeración

Cargar:

- `protocols/NUMERICS.md`;
- `config/CONTEXT7.md`;
- specialist panel necesario.

Si la computación pretende cerrar una obligación matemática, debe recibir un `Proof_Obligation_ID`, `Computation_semantics`, `Closure_standard` y producir el certificado correspondiente.

## Inicialización de un proyecto nuevo

Sincronizar la skill canónica y copiar/crear los archivos de memoria/coordinación requeridos. Rellenar `MEMORY_CORE.md` sólo con estado HOT; los demás registros crecen conforme se verifican resultados.

## Seguridad epistemológica

La memoria nunca sustituye la fuente. Un certificado interno nunca se reutiliza si cambió su contexto de validez.

## Research Loop v2.2+

Cuando el usuario plantea un objetivo científico, la skill no se limita a intentar una sola demostración.

```text
OBJECTIVE
  -> THEORY SCAN
  -> ROUTE GENERATION
  -> BEST ROUTE
  -> RAG + APPLICABILITY + PROOF + RED TEAM
  -> if fail: diagnose + learn + next tactic/route
  -> falsification track
  -> PROVED | REFUTED | CONDITIONAL | PARTIAL | UNRESOLVED
```

Una ruta fallida no se interpreta como refutación. Sólo se refuta mediante contraejemplo, contradicción o teoría plenamente aplicable.

Archivos clave:
- `protocols/RESEARCH_LOOP.md`
- `memory/ROUTE_LEDGER.md`
- `templates/RESEARCH_OBJECTIVE.md`

## Answer Interpreter v2.3

Antes del router científico, la skill decide si la pregunta realmente necesita nueva investigación.

```text
MEMORY_CORE
  -> MEMORY_INDEX
  -> CERTIFICATE
  -> DEPENDENCY SUBGRAPH
  -> INTERNAL ORIGINAL
  -> EXTERNAL RAG
  -> RESEARCH LOOP
```

La recuperación se detiene tan pronto como exista evidencia suficiente para responder fielmente.

Archivos clave:
- `protocols/INTERPRETER.md`
- `config/RETRIEVAL_POLICY.md`
- `templates/ANSWER_REQUEST.md`

## Certification Gate v2.4+

Un resultado central no llega a `CERTIFIED` sólo porque una primera auditoría no encuentre errores.

```text
PROOF
 -> RED TEAM
 -> DEPENDENCY STATUS PROPAGATION
 -> PROOF-OBLIGATION CLOSURE AUDIT
 -> INDEPENDENT SECOND REVIEW
 -> COMPUTATION GATE (si aplica)
 -> OBJECTIVE/CLAIM STRENGTH GATES
 -> CERTIFIED / CONDITIONAL / PARTIAL / NEEDS_REVALIDATION
```

Regla:

```text
effective_status(child) <= weakest_required_dependency
```

salvo independencia o descarga explícita de condiciones.

## Scientific Rendering Gate v2.5

Separa conocimiento científico de representación escrita:

```text
SCIENTIFIC TRUTH
      ↓
CERTIFICATE / EVIDENCE
      ↓
CLAIM SIGNATURE + OBJECT REGISTRY
      ↓
MINIMAL MANUSCRIPT PATCH
      ↓
TYPE / NOTATION / ENTITY GATE
      ↓
SEMANTIC DIFF
      ↓
COMPILE / VALIDATE
      ↓
MANUSCRIPT CONSISTENCY REVIEW
      ↓
MANUSCRIPT_READY
```

El editor puede cambiar palabras, no la identidad científica del claim.

## Objective Closure Gate v2.6+

Un teorema correcto no implica que el objetivo original esté cerrado.

```text
RESEARCH OBJECTIVE
      ↓
ACHIEVED CLAIM
      ↓
OBJECTIVE ↔ CLAIM ALIGNMENT
      ↓
FIRST-SUCCESS CHECK
      ↓
GENERIC / MAXIMAL / MINIMAL STRENGTH GATES
      ↓
CLOSED_EXACTLY | CLOSED_STRONGER | PARTIAL_USEFUL | OPEN_SCOPE_GAP | REFUTED | UNRESOLVED
```

Un puente exacto puede ser analítico, simbólico exacto o computacional riguroso certificado según la obligación. Un sweep ordinario nunca sustituye cuantificadores.

## Exact Witness & Global State Gate v2.7

```text
EXACT CLAIM
   ↓
NONZERO / WITNESS NEEDED?
   ↓
EXACT_NONZERO or RIGOROUS_NUMERIC_NONZERO
   ↓
CERTIFICATION
   ↓
ARTIFACT CONSISTENCY
   ↓
FINAL STATE
```

Reglas:
- float64 != exact witness;
- exact-looking formula with approximate factors != exact proof;
- CLOSED_EXACTLY exige scope completion;
- CERTIFIED exige second review;
- artefactos activos deben concordar o quedar historical/superseded.

## Memory Lifecycle & GC v2.8

```text
CURRENT OBJECTIVE
      ↓
HOT MEMORY
      ↓
CERTIFY / CLOSE
      ↓
COMPACT
      ↓
WARM CERTIFICATES + CANONICAL NODES
      ↓
ARCHIVE HISTORICAL DETAIL
```

`compact != delete`; un único resultado canónico activo por concepto cuando sea posible.

## Multi-Agent Scientific Handoff v2.9+

```text
SCIENTIFIC LEAD
      ↓
TASK_PACKET
      ↓
CONTRACT PRESERVATION CHECK
      ↓
WORKER_MISSION
      ↓
WORKER
      ↓
WORKER_RESULT
      ↓
DETERMINISTIC GATE
      ↓
AUDIT_PACKET
      ↓
SCIENTIFIC AUDITOR
      ↓
ACCEPT | REVISION_REQUIRED | SCIENTIFIC_REOPEN | BLOCKED
```

Principios:
- autoridad por rol, no provider;
- worker produce candidatos, no certifica;
- deterministic success != scientific acceptance;
- revisión local no cambia contrato;
- cambios de claim/scope/hypotheses/quantifiers requieren `SCIENTIFIC_REOPEN`.

## Proof-Obligation Tactic Routing v2.11

Principio:

> Las tácticas son opcionales; las obligaciones lógicas esenciales no.

Cada subclaim material se representa como:

```text
Proof obligation
  -> candidate tactics
  -> active tactic
  -> closure standard
  -> artifact/certificate
  -> closure class
```

Tácticas principales:

```text
CERTIFIED_INTERNAL_RESULT
EXTERNAL_THEOREM
DIRECT_ANALYTIC
SYMBOLIC_EXACT
EXHAUSTIVE_FINITE_COMPUTATION
VALIDATED_NUMERICS
RIGOROUS_COMPUTER_ASSISTED_PROOF
NUMERICAL_SCOUT
COUNTEREXAMPLE_SEARCH
```

Clases de cierre:

```text
OPEN | EVIDENCE_ONLY | CONDITIONAL | RIGOROUSLY_CLOSED | REFUTED
```

El routing es idempotente: una misma obligación activa conserva su `Obligation_ID`; cambiar de táctica no crea un subclaim duplicado.

La dirección computacional canónica es:

```text
PROOF
 -> PROOF_TACTICS
 -> NUMERICS
 -> artifact / computation certificate
 -> obligation audit
 -> certification
```

`NUMERICS` no vuelve a enrutar la obligación.

## Computation semantics v2.11

Taxonomía canónica única:

```text
exploratory_numeric
falsification_search
corroborative_numeric
symbolic_exact
exhaustive_finite
validated_numeric
rigorous_computer_assisted_proof
```

Sólo los cuatro últimos tipos exactos/rigurosos pueden aspirar a cerrar un subclaim exacto, y únicamente si satisfacen el `Closure_standard` específico.

Reproducibility != proof sufficiency.

## Coordinación determinista v2.11

Signals canónicos:

- `templates/CODEX_PLAN_DONE.json`
- `templates/WORKER_DONE.json`
- `templates/CODEX_AUDIT_DONE.json`

`WORKER_DONE` confirma ejecución, nunca cierre científico del objetivo. Los hashes de contrato y misión permiten detectar resultados stale o asociados a otra revisión.

## Static validation / CI v2.11

`scripts/validate_skill.py` comprueba, entre otros:

- versión mínima canónica;
- archivos obligatorios;
- referencias internas rotas;
- JSON de coordinación;
- taxonomía `Computation_semantics`;
- veredictos de auditoría;
- campos materiales de `WORKER_MISSION`;
- dirección acíclica Proof Tactics → Numerics;
- reglas de Objective Closure.

`.github/workflows/validate-skill.yml` ejecuta el validador en push y pull request.
