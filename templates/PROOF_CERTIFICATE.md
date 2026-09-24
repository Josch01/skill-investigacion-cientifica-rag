# Proof Certificate

```text
Certificate_ID: CERT-D-###
Title:
Status: CERTIFIED | CONDITIONAL | PARTIAL | NEEDS_REVALIDATION
Statement_version:
Definitions_version:
Exact_statement:
Hypotheses:
Scope:
Depends_on:
Dependency_audit:
Inherited_conditions:
Independence_claims_if_any:
Effective_status:
Literature_refs:
Applicability_records:
Proof_location:
Proof_skeleton:
Adversarial_review:
Independent_second_review:
Second_review_status: CONFIRMS|CONFIRMS_WITH_CONDITIONS|OBJECTS|UNRESOLVED
Counterexample_search:
Numerical_support_if_any:
Computation_certificates_if_essential:
Exact_witness_records_if_essential:
Known_exceptions:
Compatibility_notes:
Supersedes:
Downstream_dependents:
Invalidation_trigger:
Artifact_consistency_report:
Active_state_version:
Date_certified:
```

## Regla de reutilización

Este certificado puede usarse como antecedente sin abrir la prueba completa sólo si:

- las definiciones son compatibles;
- las hipótesis se satisfacen o existe una implicación verificada;
- el scope requerido no excede el certificado;
- el certificado sigue vigente.


## Regla de propagación

Si una dependencia esencial queda `REFUTED`, `SUPERSEDED` o `STALE`, este certificado debe pasar a `NEEDS_REVALIDATION` salvo demostración explícita de independencia.


## Hard gate

`Status: CERTIFIED` is invalid if `Independent_second_review` or `Second_review_status` is absent.
