# Experiment Record

```text
Experiment_ID: N-###
Scientific_claim:
Proof_Obligation_ID_if_any:
Role: essential|corroborative|scout|benchmark
Computation_semantics: exploratory_numeric|falsification_search|corroborative_numeric|symbolic_exact|exhaustive_finite|validated_numeric|rigorous_computer_assisted_proof
Closure_standard_if_any:
Model:
Code:
Data:
Environment:
Versions:
Seed:
Precision:
Solver_or_algorithm:
Tolerances:
Hyperparameters:
Bounds_or_constraints:
Stopping:
Replicates:
Baselines:
Validation:
Sensitivity:
Convergence:
Independent_check:
Sampled_region_if_any:
Certified_domain_if_any:
Coverage_or_exhaustiveness_argument_if_any:
Rounding_or_error_control_if_any:
Results:
Artifacts:
Computation_certificate_if_any:
Limitations:
Conclusion_allowed:
Conclusion_not_allowed:
```

## Regla

`Computation_semantics` usa exactamente la taxonomía canónica de `protocols/NUMERICS.md`.

Un `Experiment Record` documenta ejecución/evidencia. Si la computación es esencial para cerrar una obligación exacta, además debe producir `templates/COMPUTATION_CERTIFICATE.md` y satisfacer su `Closure_standard`.
