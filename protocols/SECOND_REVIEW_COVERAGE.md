# Independent Second Review Coverage Gate

## 1. Propósito

Asegurar que "second review" signifique reconstrucción científica real y no la existencia nominal de un archivo.

## 2. Cuándo es obligatorio

Para cada claim central que pretenda:
`CERTIFIED | REFUTED | CONDITIONAL`
o sostenga un claim de fuerza alta (generic, sharp, minimal, universal, maximal, iff, impossible).

## 3. Registro mínimo por claim

```text
Second_Review_ID:
Claim_ID:
Independent_from_first_review: yes|no
Statement_seen:
Hypotheses_seen:
Definitions_seen:
Dependencies_rederived:
Critical_step_rederived:
External_results_rechecked:
Counterexample_attempt:
Numerical_bridge_checked_if_any:
Objections:
Verdict: CONFIRMS | CONFIRMS_WITH_CONDITIONS | OBJECTS | UNRESOLVED
```

## 4. Cobertura

Definir:

`N_SECOND_REVIEW_REQUIRED`
`N_SECOND_REVIEW_COMPLETE`.

Gate:
`N_SECOND_REVIEW_COMPLETE = N_SECOND_REVIEW_REQUIRED`.

Un resumen global no sustituye registros por claim.

## 5. Independencia

Si hay subagentes reales, el segundo revisor no recibe el veredicto del primero.

Si no hay subagentes reales, ejecutar un pase separado desde statement + hypotheses + evidence y comparar sólo al final.

Debe declararse explícitamente cuál de los dos modos se usó. Está prohibido afirmar independencia real si el runtime no la proporciona.

## 6. Fallo del gate

Si falta el registro para un claim que lo requiere:
- no `CERTIFIED`;
- usar `NEEDS_REVALIDATION|UNRESOLVED` según corresponda.
