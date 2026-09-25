# Module: NUMERICAL_STUDY

## Activar cuando

Haya simulación, ODE/PDE, optimización, cálculo simbólico, ML/PINN, caos numérico, sensibilidad, benchmark o cualquier computación material para un claim.

## Requiere

- `protocols/NUMERICS.md`
- `protocols/TYPE_NOTATION_GATE.md`
- `protocols/EXACT_WITNESS.md` si una computación pretende sostener una no-anulación exacta.
- `protocols/CERTIFICATION.md` si la computación es dependencia esencial de un claim fuerte.

Memoria:
- `memory/NUMERICAL_LEDGER.md`
- `memory/SOFTWARE_LEDGER.md`

Templates:
- `templates/EXPERIMENT_RECORD.md`
- `templates/COMPUTATION_CERTIFICATE.md` cuando la computación sea esencial.

## Obligaciones

- Registrar datos, versiones, seeds, precisión, solver/algoritmo, tolerancias, discretización y comandos/material reproducible.
- Separar evidencia exploratoria, corroborativa y esencial.
- Usar análisis de robustez/segunda metodología cuando sea material.
- Mantener el firewall `numerical != exact proof`.

## Prohibido

No inferir por sí solo `generic`, `open dense`, `universal`, `maximal`, `iff`, `sharp minimum`, `impossible` u `optimal global`.