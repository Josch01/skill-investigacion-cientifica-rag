# Agent Authority & Responsibility Matrix

## 1. Principio

La autoridad científica pertenece a roles, no a proveedores/modelos.

Un proveedor puede cambiar sin alterar este contrato.

Roles:
`SCIENTIFIC_LEAD | SCIENTIFIC_AUDITOR | WRITING_WORKER | CODE_WORKER | NUMERICAL_WORKER | DETERMINISTIC_CHECKER | ORCHESTRATOR`.

## 2. Scientific Lead

Puede:
- formalizar objetivos;
- definir/reformular claims;
- fijar hipótesis, objetos, scope y cuantificadores;
- construir proof/argument skeletons;
- decidir qué partes delegar;
- crear TASK_PACKET;
- interpretar resultados de workers;
- proponer estados epistemológicos;
- actualizar proof/dependency graph después de gates;
- autorizar integración científica.

No puede:
- saltarse Certification Gate;
- usar su propia conclusión como independent second review de un claim central;
- convertir evidencia numérica en prueba exacta sin bridge certificado.

## 3. Scientific Auditor

Puede:
- auditar el output del worker contra TASK_PACKET;
- ejecutar semantic/type/scope checks;
- aceptar, pedir revisión o bloquear integración;
- realizar independent second review si cumple independencia;
- recomendar cambio de status.

Para promover a `CERTIFIED` debe aplicar todos los gates vigentes.

## 4. Workers

### WRITING_WORKER
Puede:
- redactar prosa/LaTeX desde un contrato científico exacto;
- reorganizar presentación dentro del scope permitido;
- producir patch/diff y reportes editoriales.

### CODE_WORKER
Puede:
- implementar una especificación;
- escribir tests y documentación técnica;
- corregir bugs dentro del contrato;
- producir patch/diff y artefactos reproducibles.

### NUMERICAL_WORKER
Puede:
- implementar y ejecutar experimentos solicitados;
- generar datos, tablas, plots y certificados computacionales preliminares;
- explorar degeneraciones/counterexamples según spec;
- informar resultados inesperados.

### Todos los workers NO pueden:
- crear o fortalecer silenciosamente un claim científico;
- cambiar hipótesis, dominios, cuantificadores o scope;
- promover `DRAFT/VERIFIED/...` a `CERTIFIED`;
- declarar novedad, genericidad, maximalidad, causalidad o imposibilidad fuera del contrato;
- modificar memoria científica canónica;
- editar directamente certificados vigentes como autoridad;
- resolver una contradicción científica ocultándola mediante redacción/código.

Si el worker detecta que el contrato parece científicamente inconsistente, debe emitir `SCIENTIFIC_OBJECTION` y detener el strengthening.

## 5. Deterministic Checker

Puede verificar únicamente propiedades mecánicas/reproducibles:
- schema JSON;
- existencia/hash de archivos;
- tests;
- lint/type checks;
- compilación LaTeX;
- comandos reproducibles;
- checks simbólicos especificados;
- tolerancias/formato.

No decide verdad científica.

## 6. Orchestrator

Puede:
- leer estado de tareas;
- asignar un rol a un provider configurado;
- lanzar procesos;
- mover estados de workflow;
- aplicar locks/retries/timeouts;
- llamar deterministic checks;
- solicitar audit/revision;
- integrar sólo cuando existe autorización correspondiente.

No puede:
- decidir que un teorema es correcto;
- modificar claims/hypotheses/scope;
- certificar;
- sustituir un audit científico por éxito técnico.

## 7. Risk classes

`R0 DETERMINISTIC`: formato, rename, schema, compilation-only.
`R1 SPEC_IMPLEMENTATION`: escritura o código desde spec exacta.
`R2 SCIENTIFIC_COMPUTATION`: numerics, symbolic computation, manuscript transformation material.
`R3 SCIENTIFIC_REASONING`: nuevo lemma/theorem, refutation, genericity, maximality, identifiability, novelty.

Routing:
- R0 -> deterministic tools; model optional.
- R1 -> worker -> deterministic gate; scientific audit if artifact represents a claim.
- R2 -> worker -> deterministic gate -> scientific auditor.
- R3 -> Scientific Lead; workers sólo reciben sub-tareas acotadas; independent review when certifying.

## 8. Authority invariant

`WORKER_OUTPUT != SCIENTIFIC_ACCEPTANCE`

`DETERMINISTIC_PASS != SCIENTIFIC_PASS`

`SCIENTIFIC_ACCEPTANCE != CERTIFICATION` unless Certification Gate is satisfied.

## 9. Provider mapping

Provider/model selection lives outside this file.

Ejemplo no normativo:
`SCIENTIFIC_LEAD -> Codex/GPT reasoning`
`WRITING/CODE/NUMERICAL_WORKER -> Gemini`.

## 10. Regla final

> Delegar ejecución no delega autoridad epistemológica.

## 11. Consortium functional-role mapping v3.0

Los roles del consorcio son funciones, no nuevas autoridades.

Mapeo canónico:

```text
Research Architect         -> SCIENTIFIC_LEAD
Theory Scout               -> bounded research worker
Applicability Judge        -> SCIENTIFIC_LEAD or SCIENTIFIC_AUDITOR pass
Proof Engineer             -> SCIENTIFIC_LEAD for R3 reasoning
Tactic Selector            -> SCIENTIFIC_LEAD
Computational Strategist   -> SCIENTIFIC_LEAD with numerical input
Numerical/Symbolic Worker  -> NUMERICAL_WORKER / CODE_WORKER
Falsifier                  -> SCIENTIFIC_AUDITOR
Adjudicator                -> SCIENTIFIC_LEAD
Independent Reviewer       -> SCIENTIFIC_AUDITOR with declared independence
Certifier                  -> protocol/gate function, not a provider role
```

Un mismo provider puede ejecutar varias funciones, pero debe registrar el nivel real de separación de contexto.

Ningún functional role puede aumentar autoridad respecto de las secciones 2–8.
