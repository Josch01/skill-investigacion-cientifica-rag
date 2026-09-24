# Artifact, Review & State Consistency Gate

## 1. Propósito

Impedir que el proyecto contenga simultáneamente estados incompatibles, certificados incompletos o artefactos activos con metadata obsoleta.

## 2. Active vs historical artifacts

Todo ledger/reporte debe ser clasificable como:
`ACTIVE_STATE | HISTORICAL_SNAPSHOT | SUPERSEDED_ARTIFACT`.

Un snapshot histórico puede conservar versión antigua, pero debe estar explícitamente etiquetado y no participar en el estado activo.

## 3. Framework/version consistency

Los artefactos ACTIVE_STATE de una misma corrida deben registrar una versión compatible de la skill/protocolo.

Si `PROOF_STATE` declara v2.7 y `ROUTE_LEDGER` activo declara v2.5, el cierre queda bloqueado hasta:
- actualizar metadata, o
- marcar el ledger como HISTORICAL_SNAPSHOT.

## 4. Mandatory second review record

Todo claim central con status `CERTIFIED` debe contener explícitamente:
`Independent_second_review:`
`Second_review_status:`

Valores válidos para certificar:
`CONFIRMS`
o `CONFIRMS_WITH_CONDITIONS` sólo si esas condiciones quedaron incorporadas/verificadas.

Si los campos faltan o dicen `OBJECTS|UNRESOLVED`, el claim no puede permanecer `CERTIFIED`; usar `NEEDS_REVALIDATION` o el estado apropiado.

## 5. Certificate completeness

Antes de aceptar `CERTIFIED`, comprobar presencia material de:
- exact statement;
- hypotheses;
- scope;
- dependencies;
- adversarial review;
- independent second review;
- exceptions;
- computation certificate si esencial;
- witness certificate si la no-anulación es esencial.

## 6. Cross-artifact status consistency

Para cada Claim_ID comparar:
`PROOF_STATE <-> CLAIM_SIGNATURE <-> ROUTE_LEDGER <-> manuscript <-> computation/witness records`.

No permitir, por ejemplo:
- PROOF_STATE=CERTIFIED y Claim Signature=CONJECTURE;
- certificado superseded todavía citado como activo;
- manuscript stronger than certificate;
- Objective Closure CLOSED_EXACTLY con scope items no explorados.

## 7. Closure invariant

Antes de finalizar:
`NO_ACTIVE_CONTRADICTIONS = true`.

Si no se cumple, el proyecto puede tener resultados locales certificados, pero el run no se marca cerrado.

## 8. Regla final

> La consistencia del estado científico es una propiedad global del conjunto de artefactos, no de un solo archivo.