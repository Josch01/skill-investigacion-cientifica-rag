# Multi-Agent Scientific Handoff Protocol

## 1. Propósito

Delegar trabajo científico/technical entre agentes sin perder identidad del claim, trazabilidad, scope ni control epistemológico.

Flujo:
`LEAD -> TASK_PACKET -> WORKER -> WORKER_RESULT -> DETERMINISTIC_GATE -> AUDIT_PACKET -> AUDITOR -> ACCEPT|REVISION|BLOCKED`.

## 2. No transferir conversación completa ni razonamiento privado

El handoff debe contener sólo información científica útil y verificable:
- objective/claim;
- objetos y tipos;
- hipótesis;
- ecuaciones/resultados certificados necesarios;
- proof/argument skeleton si aplica;
- inputs exactos;
- acceptance criteria;
- allowed/forbidden operations;
- provenance/pointers.

No es necesario ni deseable transferir transcript completo o chain-of-thought.

## 3. TASK_PACKET obligatorio

Usar `templates/TASK_PACKET.md`.

Debe fijar un `SCIENTIFIC_CONTRACT` inmutable durante esa revision:
- Claim_ID / Objective_ID;
- exact task;
- scientific inputs;
- hypotheses/scope;
- evidence level actual;
- expected outputs;
- acceptance criteria;
- forbidden strengthenings;
- file ownership;
- revision number;
- hashes/pointers de inputs materiales.

## 4. Minimal context

El worker recibe sólo el subgrafo necesario.

Preferir:
`certificate/claim signature + exact source slice + task spec`

sobre:
`entire repository + entire manuscript + historical ledgers`.

Aplicar Memory v2.8: HOT packet pequeño; WARM/ARCHIVE sólo bajo necesidad.

## 5. Worker execution

El worker debe:
1. validar que entiende el contrato;
2. no reinterpretar silenciosamente el claim;
3. producir sólo artefactos autorizados;
4. registrar comandos/código/output material;
5. declarar desviaciones;
6. emitir `SCIENTIFIC_OBJECTION` si encuentra un problema conceptual;
7. crear `WORKER_RESULT.md`.

## 6. Worker result statuses

`COMPLETED`
`PARTIAL`
`SCIENTIFIC_OBJECTION`
`TECHNICAL_BLOCK`
`FAILED`.

`COMPLETED` significa que produjo lo pedido, no que el claim científico sea correcto.

## 7. Deterministic gate

Antes de gastar auditoría científica cuando aplique, verificar mecánicamente:
- required files;
- hashes/schema;
- execution/tests;
- compile;
- specified numerical outputs;
- no unauthorized file edits.

Resultados:
`PASS | FAIL | NOT_APPLICABLE`.

Un FAIL normalmente vuelve a worker sin convocar auditor científico, salvo que revele un problema conceptual.

## 8. Audit

Usar `templates/AUDIT_PACKET.md`.

El auditor compara:
`TASK_PACKET <-> WORKER_RESULT <-> produced artifacts`.

Comprueba:
- cumplimiento;
- type/notation consistency;
- hypotheses preserved;
- scope preserved;
- evidence level preserved;
- numerical/exact distinction;
- unauthorized strengthening;
- reproducibility;
- relevant skill gates.

Verdict:
`ACCEPT | ACCEPT_WITH_NONSCIENTIFIC_PATCH | REVISION_REQUIRED | SCIENTIFIC_REOPEN | BLOCKED`.

## 9. Revision loop

Si `REVISION_REQUIRED`:
- no sobrescribir la spec original;
- incrementar `revision`;
- crear delta packet con errores exactos;
- conservar relación `parent_revision`;
- worker corrige sólo lo objetado.

Máximo de revisiones pertenece a orchestrator policy; al excederlo usar `NEEDS_HUMAN` o `SCIENTIFIC_REOPEN`.

## 10. Scientific reopen

Si el worker/auditor descubre que el TASK_PACKET contiene una hipótesis falsa, objeto mal tipado o claim insostenible:
- detener rendering/implementation;
- devolver al Scientific Lead;
- reabrir sólo el claim afectado;
- no parchear el output para aparentar cumplimiento.

## 11. Integration

Integrar al estado canónico sólo si:
- deterministic gate pasó cuando aplica;
- auditor verdict permite integración;
- no hay unauthorized modifications;
- Artifact Consistency Gate pasa;
- Certification Gate pasa si cambia status científico.

## 12. File ownership

Por defecto:
- Lead owns: objectives, claims, hypotheses, proof graph, canonical memory.
- Worker owns: task-local candidate artifacts.
- Auditor owns: audit verdict/report.
- Orchestrator owns: state machine metadata, locks, execution logs.

Workers producen patches/candidate files; no escriben directamente el canonical scientific source salvo autorización explícita y auditable.

## 13. Handoff artifacts and memory

Después de integración:
- durable scientific result -> WARM canonical memory;
- task packet/result/audit -> WARM mientras sean materialmente relevantes;
- intermediate logs, rejected patches, raw worker chatter -> ARCHIVE;
- no guardar prompts/transcripts completos si no son necesarios para reproducibilidad.

## 14. Security against authority drift

Todo WORKER_RESULT debe repetir:
`I_DO_NOT_AUTHORIZE_SCIENTIFIC_STATUS_CHANGE: true`.

Si un worker escribe `CERTIFIED`, `proved`, `new`, `open dense`, etc. fuera del contract, tratarlo como texto no autorizado hasta audit.

## 15. Regla final

> El handoff transporta obligaciones y evidencia; la aceptación científica regresa siempre al rol autorizado.