# Computation Certificate

Certificate_ID: COMP-###
Claim_supported:
Proof_Obligation_ID_if_any:
Role: essential | corroborative | scout
Computation_semantics: exploratory_numeric | falsification_search | corroborative_numeric | symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof
Status: VERIFIED | CERTIFIED_COMPUTATION | PARTIAL | FAILED

Mathematical_bridge:
Claim_quantifiers_covered:
Sampled_region_if_any:
Certified_domain_if_any:
Coverage_or_exhaustiveness_argument:
Arithmetic_model:
Rounding_error_control:
Rigorous_error_bound_if_any:
Closure_standard_if_any:
Formal_success_condition:
Formal_failure_condition:

Code_repository:
Code_commit_or_hash:
Exact_script:
Data_version_or_hash:
Environment:
OS_architecture:
Library_versions:
Precision:
Seed:
Solver_or_algorithm:
Tolerances:
Discretization:
Parameters:
Command:
Expected_output:
Observed_output:
Independent_rerun:
Second_method_check:
Independent_validation:
Artifacts:
Known_limitations:
Date:

## Reglas

`CERTIFIED_COMPUTATION` sólo puede usarse como soporte esencial cuando:

1. todos los elementos materiales son reproducibles;
2. la naturaleza del claim admite certificación computacional;
3. existe un puente matemático explícito entre la salida y el subclaim;
4. se cubren los cuantificadores/dominio que el claim exige;
5. redondeo/error/exhaustividad están controlados cuando son materiales;
6. el certificado satisface el `Closure_standard` de la obligación.

Reproducibilidad del programa no equivale por sí sola a prueba matemática.

`exploratory_numeric`, `falsification_search` y `corroborative_numeric` no se convierten en cierre exacto por aumentar el número de corridas, puntos o precisión decimal.
