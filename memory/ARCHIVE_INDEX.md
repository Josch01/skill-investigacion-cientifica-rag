# ARCHIVE INDEX

Historical and superseded scientific material is indexed here and excluded from default retrieval.

Formato:
```text
ARCHIVE_TAG -> ID | status | canonical_successor | source_pointer | reason_archived
```

Reglas:
- No almacenar contenido largo aquí.
- Todo `SUPERSEDED` debe apuntar a `Superseded_by` cuando exista.
- Historical snapshots deben declarar versión/fecha.
- El archive se recupera sólo bajo necesidad explícita o dependencia.

Ejemplo:
```text
GENERALIZED-DUFFING-HISTORY -> CERT-D-008 | SUPERSEDED | CERT-D-012 | proofs/CERT-D-008 | stronger damped theorem available
```