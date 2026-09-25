# Module: WORKER_COMPLETION

## Activar cuando

Toda tarea sea delegada a un worker externo o subagente.

## Composición

- `config/AGENT_AUTHORITY.md`
- `protocols/MULTI_AGENT_HANDOFF.md`
- `protocols/TASK_COORDINATION.md`
- `protocols/SCIENTIFIC_MAILBOX.md`
- `templates/WORKER_RESULT.md`
- `templates/WORKER_DONE.json`

## Obligaciones del worker

1. Trabajar sólo dentro del task/revision autorizado.
2. No cambiar claim, hipótesis, scope, definiciones, cuantificadores o estatus científico.
3. Producir todos los artefactos exigidos por `WORKER_MISSION.md`.
4. Crear `WORKER_RESULT.md` con resultados, limitaciones, archivos consultados/producidos y claims no demostrados.
5. Emitir `WORKER_DONE.json` **al final**, después de escribir todos los demás outputs.
6. Si hay bloqueo científico material, usar el mailbox; si hay bloqueo técnico, declararlo.

## Regla atómica

El runtime debería escribir/renombrar señales de completion de forma atómica cuando sea posible. Un archivo `WORKER_DONE.json` incompleto o con task/revision/hash incorrecto no activa auditoría.

## Completion no es certificación

`COMPLETE` significa que el worker terminó el encargo; no significa `ACCEPTED`, `PROVED`, `CERTIFIED` ni `NOVEL`.