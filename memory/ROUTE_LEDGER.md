# ROUTE LEDGER

Registra rutas intentadas, fallos y resultados parciales reutilizables.

```text
[ROUTE-###]
Objective_ID:
Target:
Method:
Status: PLANNED|ACTIVE|PROMISING|BLOCKED|FAILED|SUCCEEDED|SUPERSEDED
Memory_tier: HOT|WARM|ARCHIVE
Priority:
Tags:
Starting_sources:
Internal_certificates:
Critical_assumptions:
Dependencies:
Evidence_cards:
Applicability_records:
Proof_obligations:
  - Obligation_ID:
    Active_tactic:
    Closure_standard:
    Computation_semantics_if_any:
    Closure_class: OPEN|EVIDENCE_ONLY|CONDITIONAL|RIGOROUSLY_CLOSED|REFUTED
    Artifact_or_certificate:
Numerical_support:
Computation_certificates:
Outcome:
Failure_reason:
Reusable_results:
New_obstructions:
Superseded_by:
Date_started:
Date_closed:
Compact_summary:
Archive_pointer:
Notes:
```

## Reglas

- Una ruta fallida no refuta el objetivo por sí sola.
- Una táctica fallida puede activar un fallback sin refutar automáticamente la ruta.
- Una ruta exacta no es `SUCCEEDED` si una obligación esencial sigue `OPEN` o `EVIDENCE_ONLY`.
- Extraer resultados parciales antes de cerrar.
- No repetir una ruta `FAILED` salvo cambio material de hipótesis, fuente o herramienta.
- HOT sólo para ACTIVE/PROMISING; SUCCEEDED se compacta tras certificado; FAILED/SUPERSEDED pasa a ARCHIVE salvo dependencia activa.
