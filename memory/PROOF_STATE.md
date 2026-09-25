# PROOF STATE

## Target actual

```text
TARGET:
STATUS:
FRAMEWORK_VERSION:
FRAMEWORK_COMMIT:
DEFINITIONS_VERSION:
```

## Grafo

```text
TARGET
├─ ...
└─ ...
```

## Obligaciones activas

```text
[PO-###]
Statement:
Role: essential|auxiliary
Dependencies:
Active_tactic:
Closure_standard:
Computation_semantics_if_any:
Closure_class: OPEN|EVIDENCE_ONLY|CONDITIONAL|RIGOROUSLY_CLOSED|REFUTED
Evidence_or_certificate:
Failure_reason_if_any:
Fallback:
```

## Bloqueos
- ...

## Certificados disponibles
- CERT-D-...
- COMP-...
- WITNESS-...

## Ramas abandonadas
- ROUTE-... : razón

## Regla

El estado activo debe permitir reconstruir `target -> obligación -> táctica -> estándar -> certificado -> cierre`. Una obligación esencial `OPEN` o `EVIDENCE_ONLY` bloquea un cierre exacto.
