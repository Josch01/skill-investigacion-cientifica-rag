# ROUTE LEDGER

Registra rutas de investigación intentadas para no repetir caminos muertos y para reutilizar resultados parciales.

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
Numerical_support:
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
- Registrar la causa exacta del fallo.
- Extraer resultados parciales antes de cerrar.
- No repetir una ruta `FAILED` salvo que cambie una hipótesis, fuente o herramienta material.


## Compaction v2.8

- HOT sólo para rutas ACTIVE/PROMISING y bloqueos inmediatos.
- SUCCEEDED se compacta una vez emitido el certificado.
- FAILED se compacta a razón de fallo + resultado reusable y pasa a ARCHIVE salvo dependencia activa.
- SUPERSEDED pasa a ARCHIVE.
- Máximo operativo recomendado: 8 rutas HOT por objetivo.