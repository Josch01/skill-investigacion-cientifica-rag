# Claim, Evidence & Artifact Separation Gate

## 1. Propósito

Separar tres estados que nunca deben colapsarse:

`CLAIM_STATUS != EVIDENCE_STATUS != ARTIFACT_STATUS`.

## 2. Claim status

Describe el estado epistemológico de la afirmación científica:

`DRAFT | VERIFIED | CERTIFIED | CONDITIONAL | PARTIAL | REFUTED | SUPERSEDED | STALE | NEEDS_REVALIDATION | UNRESOLVED`.

Un claim se evalúa por sus dependencias esenciales y obligaciones de prueba.

## 3. Evidence status

Describe una pieza de evidencia concreta, por ejemplo una prueba simbólica, experimento, SVD, witness o fuente:

`SUPPORTS | CORROBORATIVE | ESSENTIAL | INVALID | REFUTED | SUPERSEDED | UNVERIFIED`.

Toda evidencia debe declarar:
- Evidence_ID;
- Parent_Claim_ID;
- Role: essential | auxiliary | corroborative;
- epistemic type [L]/[D]/[N]/...;
- validity/status.

## 4. Artifact status

Describe el archivo/representación que contiene un claim o evidencia:

`ACTIVE_STATE | HISTORICAL_SNAPSHOT | SUPERSEDED_ARTIFACT | NEEDS_PATCH | SEMANTIC_MISMATCH | INVALID_ARTIFACT`.

Un artefacto incorrecto no refuta automáticamente el conocimiento si existe una fuente canónica correcta.

## 5. Regla de propagación

Si una evidencia se vuelve `INVALID|REFUTED`:

1. comprobar su `Role`;
2. si era corroborativa/auxiliar, NO degradar automáticamente el claim;
3. si era esencial, reabrir sólo las obligaciones que dependían de ella;
4. recalcular el claim desde las dependencias restantes;
5. refutar el claim sólo si existe refutación del claim, no mera pérdida de soporte.

Ejemplo:

`float64 SVD invalid as EXACT_ZERO`
no implica
`analytic rank theorem REFUTED`.

## 6. Regla de cierre

Antes de cambiar un Claim_Status por fallo de evidencia, registrar:

`Evidence_failure -> essential? -> affected_obligation -> surviving_routes -> recomputed_claim_status`.

Sin este registro, el downgrade es inválido.
