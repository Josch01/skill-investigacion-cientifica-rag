# Protocol: Scientific Task Compilation

## Propósito

Transformar un objetivo amplio del usuario en una misión científica delegable, autocontenida y económicamente contextualizada, sin delegar autoridad epistemológica ni perder campos materiales del contrato.

## Autoridad

Sólo el Scientific Lead puede compilar o revisar el contrato científico. El worker ejecuta la misión; no redefine claim, hipótesis, scope, definiciones, cuantificadores, criterios de éxito/refutación ni estatus.

## Entrada

- objetivo del usuario;
- decisión de `protocols/INTERPRETER.md`;
- salida de `agents/ROUTER.md`;
- módulos seleccionados desde `modules/MODULE_INDEX.md`;
- `templates/TASK_PACKET.md` de la revisión activa;
- memoria/certificados recuperados bajo `config/RETRIEVAL_POLICY.md` y `config/CONTEXT_BUDGET.md`.

## Invariante de compilación

`WORKER_MISSION.md` es una representación ejecutable del `TASK_PACKET.md`, no una reinterpretación resumida del contrato.

Todo campo material para corrección científica debe preservarse explícitamente o mediante un puntero inequívoco al packet. En particular no pueden perderse:

- claim/objetivo;
- objetos y tipos;
- hipótesis;
- scope;
- definiciones;
- cuantificadores;
- criterios de éxito/refutación;
- acciones permitidas/prohibidas;
- forbidden strengthenings;
- file ownership;
- acceptance criteria;
- deterministic checks;
- proof obligations materiales;
- `Proof_tactic_routing`;
- `Permitted_closure_methods`;
- `Computation_semantics`;
- `Closure_standard` o estándar de cómputo riguroso cuando aplique;
- certificados/records exigidos.

## Algoritmo de compilación

1. Formalizar `TASK_PACKET` y preservar literalmente los campos suministrados por el usuario.
2. Seleccionar el conjunto mínimo de módulos suficiente para el objetivo.
3. Resolver dependencias de cada módulo: protocolos, memoria, templates y gates.
4. Recuperar primero memoria/certificados; cargar sólo fragmentos pertinentes.
5. Determinar qué contexto debe incluirse en la misión y qué contexto debe referenciarse por path.
6. Si existe proof-tactic routing, transferir al worker sólo las obligaciones que deba ejecutar, junto con táctica permitida/candidata, estándar de cierre y outputs requeridos.
7. Si existe computación material, copiar exactamente la taxonomía canónica `Computation_semantics` y fijar si puede o no cerrar una obligación exacta.
8. Definir fases de trabajo sólo cuando añadan estructura real; no imponer fases vacías.
9. Definir outputs obligatorios, checks deterministas, acceptance criteria y forbidden strengthenings.
10. Incluir criterios explícitos de éxito, refutación, parcialidad y bloqueo.
11. Generar `WORKER_MISSION.md` con `contract_hash` y, cuando el runtime lo soporte, `mission_hash`.
12. Ejecutar un **Contract Preservation Check** antes de emitir la señal de plan completo.
13. Emitir la señal de plan completo sólo después de que packet y misión sean consistentes.

## Contract Preservation Check

Comparar:

```text
TASK_PACKET <-> WORKER_MISSION
```

Debe resultar `PASS` para:

- immutable claim;
- objects/types;
- hypotheses;
- scope;
- definitions;
- quantifiers;
- success/refutation criteria;
- allowed/forbidden actions;
- forbidden strengthenings;
- file ownership;
- proof/computation semantics;
- required outputs;
- acceptance criteria.

Una pérdida material produce `COMPILATION_BLOCKED` y no se emite `CODEX_PLAN_DONE.json`.

## Economía de contexto

No copiar la skill completa al worker. Preferir:

`objetivo + contrato + módulos seleccionados + fragments relevantes + paths de protocolos + outputs + acceptance criteria`.

Evitar transcripts, archivos no relacionados, memoria WARM/ARCHIVE no necesaria y protocolos redundantes.

## WORKER_MISSION debe contener

- Task/revision/mission IDs y hashes;
- framework version/commit;
- objetivo científico;
- immutable claim/hypotheses/scope/definitions/quantifiers;
- objects/types;
- success/refutation criteria;
- módulos/protocolos aplicables;
- proof/computation contract si aplica;
- contexto local autorizado y archivos a leer;
- literatura/búsqueda requerida si aplica;
- rutas de prueba/falsificación o experimentales requeridas;
- disciplina de notación y estatus epistemológico;
- allowed/forbidden actions y file ownership;
- deliverables exactos;
- deterministic checks;
- forbidden strengthenings;
- mailbox policy;
- completion contract;
- acceptance criteria.

## Prohibido

- copiar toda la skill por defecto;
- inventar dependencias inexistentes;
- pedir al worker que certifique su propio resultado;
- ocultar una hipótesis añadida dentro del prompt;
- degradar un estándar de cierre al resumir;
- cambiar una `Computation_semantics` durante compilación;
- tratar una misión compilada como aprobación científica.
