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
- Manuscript Rendering Gate con tipado de objetos, Claim Signatures, Minimal Patch Policy y Semantic Diff.

## Idea central

```text
Pregunta
  -> Interpreter
     -> ¿ya está resuelta?
        -> sí: memoria/certificado/subgrafo -> respuesta adaptada
        -> no: Router
     -> mínimo panel necesario
        -> MEMORY_CORE + INDEX
           -> certificados relevantes
              -> RAG externo sólo para huecos
                 -> RESEARCH LOOP
                    -> mejor ruta
                       -> RAG + prueba + red team
                          -> éxito / siguiente ruta
                             -> certificado + memoria
```

## Estructura

```text
SKILL.md
agents/
protocols/
config/
memory/
templates/
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
6. aplicar `protocols/PROOF.md`.

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

## Inicialización de un proyecto nuevo

Copiar los archivos de `memory/` a la carpeta del proyecto y rellenar sólo `MEMORY_CORE.md`. Los demás crecen conforme se certifican resultados.

## Seguridad epistemológica

La memoria nunca sustituye la fuente. Un certificado interno nunca se reutiliza si cambió su contexto de validez.


## Research Loop v2.2

Cuando el usuario plantea un objetivo científico, la skill no se limita a intentar una sola demostración.

```text
OBJECTIVE
  -> THEORY SCAN
  -> ROUTE GENERATION
  -> BEST ROUTE
  -> RAG + APPLICABILITY + PROOF + RED TEAM
  -> if fail: diagnose + learn + next route
  -> falsification track
  -> PROVED | REFUTED | CONDITIONAL | PARTIAL | UNRESOLVED
```

Una ruta fallida no se interpreta como refutación. Sólo se refuta mediante contraejemplo, contradicción o teoría plenamente aplicable.

Los archivos clave son:

- `protocols/RESEARCH_LOOP.md`
- `memory/ROUTE_LEDGER.md`
- `templates/RESEARCH_OBJECTIVE.md`


## Answer Interpreter v2.3

Antes del router científico, la skill decide si la pregunta realmente necesita nueva investigación.

Ruta de recuperación:

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

La misma conclusión puede explicarse como:

- `simple`: conceptual y accesible;
- `technical`: científica compacta;
- `rigorous`: hipótesis, cuantificadores, dependencias y fuentes;
- `paper`: redacción para manuscrito.

Archivos clave:

- `protocols/INTERPRETER.md`
- `config/RETRIEVAL_POLICY.md`
- `templates/ANSWER_REQUEST.md`


## Certification Gate v2.4

Un resultado central ya no llega a `CERTIFIED` sólo porque una primera auditoría no encuentre errores.

```text
PROOF
 -> RED TEAM
 -> DEPENDENCY STATUS PROPAGATION
 -> INDEPENDENT SECOND REVIEW
 -> COMPUTATION GATE (si aplica)
 -> NOVELTY COVERAGE GATE (si se afirma novedad)
 -> CERTIFIED / CONDITIONAL / PARTIAL / NEEDS_REVALIDATION
```

La regla clave es:

```text
effective_status(child) <= weakest_required_dependency
```

salvo que se pruebe explícitamente que el hijo no necesita esa dependencia o que sus condiciones fueron descargadas.

Archivos clave:

- `protocols/CERTIFICATION.md`
- `templates/COMPUTATION_CERTIFICATE.md`
- `templates/NOVELTY_COVERAGE.md`


## Scientific Rendering Gate v2.5

La skill separa ahora la verdad científica de su representación escrita:

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

Es deliberadamente general:
- matemática: espacios, mapas, símbolos y cuantificadores;
- estadística/epidemiología: población, muestra, outcome, estimando y escala;
- ML: dataset, split, métrica, checkpoint y preprocesamiento;
- software: API, firma, versión y contrato;
- física/ingeniería: variables, unidades y condiciones;
- experimentos: instrumento, calibración, réplicas y condiciones.

Regla central: el editor puede cambiar palabras, pero no la identidad científica del claim.

Archivos clave:
- `protocols/MANUSCRIPT_EDIT.md`
- `protocols/TYPE_NOTATION_GATE.md`
- `memory/SYMBOL_TABLE.md`
- `templates/CLAIM_SIGNATURE.md`
- `templates/SEMANTIC_DIFF.md`