# Protocol: Scientific Task Compilation

## Propósito

Transformar un objetivo amplio del usuario en una misión científica delegable, autocontenida y económicamente contextualizada, sin delegar autoridad epistemológica.

## Autoridad

Sólo el Scientific Lead puede compilar o revisar el contrato científico. El worker ejecuta la misión; no redefine claim, hipótesis, scope, definiciones, cuantificadores ni estatus.

## Entrada

- objetivo del usuario;
- decisión de `protocols/INTERPRETER.md`;
- salida de `agents/ROUTER.md`;
- módulos seleccionados desde `modules/MODULE_INDEX.md`;
- memoria/certificados recuperados bajo `config/RETRIEVAL_POLICY.md` y `config/CONTEXT_BUDGET.md`.

## Algoritmo de compilación

1. Formalizar `TASK_PACKET` y preservar literalmente los campos suministrados por el usuario.
2. Seleccionar el conjunto mínimo de módulos suficiente para el objetivo.
3. Resolver dependencias de cada módulo: protocolos, memoria, templates y gates.
4. Recuperar primero memoria/certificados; cargar sólo fragmentos pertinentes.
5. Determinar qué contexto debe incluirse en la misión y qué contexto debe referenciarse por path.
6. Definir fases de trabajo sólo cuando añadan estructura real; no imponer fases vacías.
7. Definir outputs obligatorios, checks deterministas, acceptance criteria y forbidden strengthenings.
8. Incluir criterios explícitos de éxito, refutación, parcialidad y bloqueo.
9. Generar `WORKER_MISSION.md` con un `prompt_hash` o identificador equivalente cuando el runtime lo soporte.
10. Emitir la señal de plan completo sólo después de que el contrato y la misión sean consistentes.

## Economía de contexto

No copiar la skill completa al worker. Preferir:

`objetivo + contrato + módulos seleccionados + fragments relevantes + paths de protocolos + outputs + acceptance criteria`.

Evitar transcripts, archivos no relacionados, memoria WARM/ARCHIVE no necesaria y protocolos redundantes.

## WORKER_MISSION debe contener

- Task/revision IDs;
- objetivo científico;
- immutable claim/hypotheses/scope si existen;
- módulos/protocolos aplicables;
- contexto local autorizado y archivos a leer;
- literatura/búsqueda requerida si aplica;
- rutas de prueba/falsificación o experimentales requeridas;
- disciplina de notación y estatus epistemológico;
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
- tratar una misión compilada como aprobación científica.