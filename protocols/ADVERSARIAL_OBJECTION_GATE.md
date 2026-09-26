# Adversarial Objection Gate

## 1. Propósito

Impedir que una objeción plausible del Red Team se convierta automáticamente en un hecho científico o en una refutación.

## 2. Objection Record

Toda objeción material debe registrar:

```text
Objection_ID:
Target_Claim_ID:
Exact_objection:
Failure_implication_if_true:
Objects_and_types:
Hypotheses_used:
Verification_route:
Proof_or_source:
Counterexample_if_any:
Status: PROPOSED | VERIFIED | REFUTED | UNRESOLVED
Severity_if_verified: FATAL | MAJOR | MODERATE | MINOR
Affected_obligations:
```

## 3. Fuerza permitida

- `PROPOSED`: hipótesis adversarial; puede motivar revisión, no degradar por sí sola.
- `UNRESOLVED`: puede bloquear `CERTIFIED` si es material; no permite `REFUTED`.
- `VERIFIED`: puede degradar/refutar según la implicación demostrada.
- `REFUTED`: deja de ser blocker y debe registrarse como ataque fallido.

## 4. Verificación de la objeción

El auditor debe intentar decidir la objeción con el mismo rigor que el claim:

- cálculo directo;
- teorema verificado y aplicable;
- contraejemplo exacto;
- symbolic exact;
- validated numerics si el estándar lo permite.

Una frase como "could fail", "might be singular", "perhaps non-analytic" no es una objeción verificada.

## 5. No circularidad

El Red Team no puede usar como evidencia:
- su propio veredicto;
- el status previo del claim;
- una salida float64 como contraejemplo exacto;
- una condición que contradice explícitamente las hipótesis sin demostrar que dichas hipótesis son inconsistentes.

## 6. Integración con Certification

Una objeción `UNRESOLVED` material bloquea `CERTIFIED`.
Una objeción `REFUTED` no puede seguir apareciendo como razón activa de downgrade.
