# Protocol: Scientific Mailbox

## Propósito

Permitir consultas puntuales entre worker y Scientific Lead/Auditor sin convertir la coordinación en una conversación permanente ni reenviar todo el contexto.

## Tipos de consulta permitidos

- `SCIENTIFIC_CLARIFICATION`
- `SCOPE_CONFLICT`
- `HYPOTHESIS_CONFLICT`
- `NOTATION_CONFLICT`
- `MISSING_REQUIRED_INPUT`
- `SCIENTIFIC_OBJECTION`

Preguntas operativas menores que no alteran el contrato deben resolverse localmente por el worker y no abrir mailbox.

## Formato mínimo de pregunta

- `id`
- `task_id`
- `revision`
- `from`
- `to`
- `type`
- `status`
- `question`
- `blocks_work: true|false`
- `affected_claims/files`

## Formato mínimo de respuesta

- `id`
- `reply_to`
- `task_id`
- `revision`
- `from`
- `to`
- `decision`
- `answer`
- `changes_scientific_contract: true|false`

## Regla crítica

Una respuesta de mailbox no puede modificar silenciosamente:
- claim;
- hipótesis;
- scope;
- definiciones;
- cuantificadores;
- criterios de éxito/refutación;
- estatus epistemológico.

Si cualquiera de éstos cambia, marcar `changes_scientific_contract=true` y exigir nueva revisión/contrato antes de continuar.

## Bloqueo

- `blocks_work=false`: el worker continúa por rutas independientes.
- `blocks_work=true`: el runtime puede pasar a `WAITING_FOR_LEAD_CLARIFICATION`.

## Economía

Cada mensaje debe ser autocontenido pero corto. Referenciar paths/IDs en vez de copiar informes completos. El destinatario lee sólo la pregunta y los fragmentos mínimos afectados.

## Trazabilidad

Preguntas y respuestas son artefactos de coordinación, no evidencia científica por sí mismas. Toda decisión material debe reflejarse después en el contrato, ledger o artefacto científico correspondiente.