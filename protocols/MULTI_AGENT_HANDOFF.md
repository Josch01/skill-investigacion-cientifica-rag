# Multi-Agent Scientific Handoff Protocol

## 1. Propósito

Delegar trabajo científico/technical entre agentes sin perder identidad del claim, trazabilidad, scope, obligaciones de prueba ni control epistemológico.

Flujo:
`LEAD -> TASK_PACKET -> WORKER_MISSION -> WORKER -> WORKER_RESULT -> DETERMINISTIC_GATE -> AUDIT_PACKET -> AUDITOR -> ACCEPT|REVISION_REQUIRED|SCIENTIFIC_REOPEN|BLOCKED`.

## 2. No transferir conversación completa ni razonamiento privado

El handoff debe contener sólo información científica útil y verificable:
- objective/claim;
- objetos y tipos;
- hipótesis;
- scope/definiciones/cuantificadores;
- criterios de éxito/refutación;
- ecuaciones/resultados certificados necesarios;
- proof/argument skeleton si aplica;
- proof obligations materiales, táctica permitida y closure standard si aplica;
- computation semantics cuando aplique;
- inputs exactos;
- acceptance criteria;
- allowed/forbidden operations;
- file ownership;
- provenance/pointers.

No es necesario ni deseable transferir transcript completo o chain-of-thought.

## 3. TASK_PACKET obligatorio

Usar `templates/TASK_PACKET.md`.

Debe fijar un `SCIENTIFIC_CONTRACT` inmutable durante esa revision:
- Claim_ID / Objective_ID;
- exact task;
- scientific inputs;
- objects/types;
- hypotheses/scope/definitions/quantifiers;
- success/refutation criteria;
- evidence level actual;
- proof/computation contract si aplica;
- expected outputs;
- acceptance criteria;
- allowed/forbidden actions;
- forbidden strengthenings;
- file ownership;
- revision number;
- hashes/pointers de inputs materiales.

## 4. WORKER_MISSION compilada

Usar `protocols/TASK_COMPILATION.md` y `templates/WORKER_MISSION.md`.

La misión debe preservar el contrato material del packet. Antes de delegar ejecutar el `Contract Preservation Check`.

Si se pierde un campo material, no emitir señal de plan completo.

## 5. Minimal context

El worker recibe sólo el subgrafo necesario.

Preferir:
`certificate/claim signature + exact source slice + task spec`

sobre:
`entire repository + entire manuscript + historical ledgers`.

Aplicar Memory Lifecycle: HOT packet pequeño; WARM/ARCHIVE sólo bajo necesidad.

## 6. Worker execution

El worker debe:
1. validar que entiende y preserva el contrato;
2. no reinterpretar silenciosamente el claim;
3. producir sólo artefactos autorizados;
4. registrar comandos/código/output material;
5. reportar obligaciones de prueba materiales y evidencia producida;
6. declarar desviaciones;
7. emitir `SCIENTIFIC_OBJECTION` si encuentra un problema conceptual;
8. crear `WORKER_RESULT.md`.

## 7. Worker result statuses

`COMPLETED | PARTIAL | SCIENTIFIC_OBJECTION | TECHNICAL_BLOCK | FAILED`.

`COMPLETED` significa que produjo lo pedido, no que el claim científico sea correcto.

El worker puede reportar que una obligación parece `RIGOROUSLY_CLOSED`, pero sólo el auditor/certification gate puede aceptar ese cierre como estado canónico.

## 8. Deterministic gate

Antes de gastar auditoría científica cuando aplique, verificar mecánicamente:
- required files;
- hashes/schema;
- execution/tests;
- compile;
- specified numerical outputs;
- no unauthorized file edits;
- contract/mission identity.

Resultados:
`PASS | FAIL | NOT_APPLICABLE`.

Un FAIL normalmente vuelve a worker sin convocar auditor científico, salvo que revele un problema conceptual.

## 9. Audit

Usar `templates/AUDIT_PACKET.md`.

El auditor compara:
`TASK_PACKET <-> WORKER_MISSION <-> WORKER_RESULT <-> produced artifacts`.

Comprueba:
- cumplimiento;
- type/notation consistency;
- hypotheses preserved;
- scope preserved;
- success/refutation criteria preserved;
- proof obligations and closure standards preserved;
- evidence level preserved;
- numerical/exact distinction;
- unauthorized strengthening;
- reproducibility;
- computation bridge/coverage/error when material;
- relevant skill gates.

Veredictos canónicos únicos:
`ACCEPT | REVISION_REQUIRED | SCIENTIFIC_REOPEN | BLOCKED`.

Una corrección puramente no científica que antes pudiera llamarse `ACCEPT_WITH_NONSCIENTIFIC_PATCH` debe representarse como:
- `ACCEPT` si el patch no es requisito previo de integración; o
- `REVISION_REQUIRED` si el patch debe aplicarse antes de integrar.

## 10. Revision loop

Si `REVISION_REQUIRED`:
- no sobrescribir la spec original;
- incrementar `revision` según la coordinación;
- crear delta packet con errores exactos;
- conservar relación `parent_revision`;
- worker corrige sólo lo objetado.

Máximo de revisiones pertenece a orchestrator policy; al excederlo usar `NEEDS_HUMAN` o `SCIENTIFIC_REOPEN`.

## 11. Scientific reopen

Si el worker/auditor descubre que corregir requiere cambiar claim, hipótesis, scope, definiciones, cuantificadores, success/refutation criteria o epistemic status:
- detener rendering/implementation;
- devolver al Scientific Lead;
- usar `SCIENTIFIC_REOPEN`;
- crear nueva revisión de contrato;
- preservar provenance;
- no parchear el output para aparentar cumplimiento.

## 12. Integration

Integrar al estado canónico sólo si:
- deterministic gate pasó cuando aplica;
- auditor verdict permite integración;
- no hay unauthorized modifications;
- Artifact Consistency Gate pasa cuando aplica;
- Certification Gate pasa si cambia status científico.

## 13. File ownership

Por defecto:
- Lead owns: objectives, claims, hypotheses, proof graph, canonical memory.
- Worker owns: task-local candidate artifacts.
- Auditor owns: audit verdict/report.
- Orchestrator owns: state machine metadata, locks, execution logs.

Workers producen patches/candidate files; no escriben directamente el canonical scientific source salvo autorización explícita y auditable.

## 14. Handoff artifacts and memory

Después de integración:
- durable scientific result -> WARM canonical memory;
- task packet/mission/result/audit -> WARM mientras sean materialmente relevantes;
- intermediate logs, rejected patches, raw worker chatter -> ARCHIVE;
- no guardar prompts/transcripts completos si no son necesarios para reproducibilidad.

## 15. Security against authority drift

Todo WORKER_RESULT debe repetir:
`I_DO_NOT_AUTHORIZE_SCIENTIFIC_STATUS_CHANGE: true`.

Si un worker escribe `CERTIFIED`, `proved`, `new`, `open dense`, etc. fuera del contract, tratarlo como texto no autorizado hasta audit.

## 16. Regla final

> El handoff transporta obligaciones y evidencia; la aceptación científica regresa siempre al rol autorizado.
