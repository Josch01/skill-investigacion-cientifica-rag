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
- Research Loop orientado a objetivos con rutas sucesivas de prueba/refutación.

## Idea central

```text
Pregunta
  -> Router
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
