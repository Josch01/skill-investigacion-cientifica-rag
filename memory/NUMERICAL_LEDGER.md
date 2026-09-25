# NUMERICAL LEDGER

```text
[N-###]
Claim_tested:
Proof_Obligation_ID_if_any:
Role: essential|corroborative|scout|benchmark
Computation_semantics: exploratory_numeric|falsification_search|corroborative_numeric|symbolic_exact|exhaustive_finite|validated_numeric|rigorous_computer_assisted_proof
Closure_standard_if_any:
Closure_class_if_audited: OPEN|EVIDENCE_ONLY|CONDITIONAL|RIGOROUSLY_CLOSED|REFUTED|not_applicable
Computation_certificate_if_any:
Model_version:
Code_commit_or_hash:
Data_version_or_hash:
Environment:
Dependencies:
Hardware_if_relevant:
Seed:
Precision:
Method_or_solver:
Tolerances:
Discretization:
Parameters:
Bounds:
Stopping_rule:
Command:
Metrics:
Sampled_region_if_any:
Certified_domain_if_any:
Coverage_or_exhaustiveness_argument_if_any:
Rounding_or_error_control_if_any:
Result:
Robustness_checks:
Independent_check:
Artifacts:
Limitations:
Date:
Status:
```

## Reglas

- Usar la taxonomía `Computation_semantics` de `protocols/NUMERICS.md` sin aliases locales.
- `Closure_class_if_audited` sólo refleja un cierre aceptado por el rol autorizado; no inferirlo de una corrida exitosa.
- Un sweep ordinario permanece evidencia aunque no encuentre contraejemplos.
