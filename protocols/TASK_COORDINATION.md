# Protocol: Task Coordination

## Propósito

Coordinar Scientific Lead, worker y auditor mediante estado mínimo, señales explícitas y revisiones trazables, evitando polling costoso de artefactos grandes.

## Regla de propiedad

**Los modelos no son dueños de `TASK_STATE.json`.** El runtime/orquestador es el único escritor del estado canónico. Los agentes sólo producen artefactos y señales dentro de su task/revision autorizada.

## Estados conceptuales

`READY_FOR_CODEX_PLAN -> CODEX_PLANNING -> READY_FOR_WORKER -> WORKER_RUNNING -> WORKER_DONE -> DETERMINISTIC_CHECK -> READY_FOR_AUDIT -> AUDITING -> ACCEPTED`

Ramas permitidas:

`REVISION_REQUIRED | SCIENTIFIC_REOPEN | WAITING_FOR_LEAD_CLARIFICATION | BLOCKED | FAILED | NEEDS_HUMAN`

El runtime puede mapear estos nombres a una máquina de estados propia siempre que preserve la semántica.

## Polling mínimo

Una tarea programada debe leer primero sólo `TASK_STATE.json` o señal equivalente. Si `next_actor` no corresponde al agente, terminar sin cargar informes, prompts, papers ni artefactos extensos.

Codex/Lead se activa típicamente en:
- `READY_FOR_CODEX_PLAN`;
- `WAITING_FOR_LEAD_CLARIFICATION`;
- `READY_FOR_AUDIT`;
- `SCIENTIFIC_REOPEN`.

Worker se activa típicamente en:
- `READY_FOR_WORKER`;
- `REVISION_REQUIRED` cuando exista `REVISION_DELTA.md` válido.

## Señales

Las señales deben incluir como mínimo:
- `task_id`;
- `revision`;
- `status`;
- referencia/hash de misión o contrato cuando exista;
- outputs requeridos presentes/ausentes;
- blockers;
- timestamp.

Una señal no cambia por sí sola el estado científico. El runtime valida identidad, revisión y precondiciones antes de transicionar.

## Completion Gate

`WORKER_DONE.json` sólo habilita la fase siguiente si:
1. `task_id` y `revision` coinciden;
2. la misión/contrato coincide con la revisión activa;
3. todos los outputs obligatorios declarados existen;
4. no hay bloqueo incompatible con `COMPLETE`;
5. los checks deterministas requeridos pueden ejecutarse o están marcados como pendientes.

## Revisiones

`REVISION_REQUIRED` debe producir un delta localizado. No reiniciar el trabajo completo salvo `SCIENTIFIC_REOPEN`.

Si una aclaración cambia claim, hipótesis, scope, definiciones, cuantificadores, éxito/refutación o estatus epistemológico, crear nueva revisión de contrato; no continuar silenciosamente en la misma revisión.

## Fallos y stale state

- Señal con revision/hash antiguo: ignorar y registrar como stale.
- JSON parcial o inválido: no activar modelo; mantener estado previo y registrar fallo técnico.
- Timeout de worker: no inferir `FAILED` científico; clasificar como bloqueo técnico hasta auditoría/decisión del runtime.

## Economía

El estado canónico debe ser pequeño. Los informes grandes se leen únicamente cuando el estado requiere actuación científica.