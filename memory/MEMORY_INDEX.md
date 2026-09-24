# MEMORY INDEX

Formato canónico:

```text
TAG -> CANONICAL_ACTIVE_ID | WARM_IDS | ARCHIVE_POINTER
```

Ejemplos:

```text
IDENTIFIABILITY-GLOBAL -> C-001, CERT-D-004, X-002
DIFFERENTIAL-ALGEBRA -> L-003, CERT-D-005
CHAOS-LYAPUNOV -> N-011, REF-022
CMA-ES -> N-020, SW-004
```

No almacenar contenido largo aquí.


Objetos/editorial:

```text
SYMBOLS -> memory/SYMBOL_TABLE.md
CLAIM-SIGNATURES -> templates/CLAIM_SIGNATURE.md
MANUSCRIPT-SEMANTIC-DIFF -> templates/SEMANTIC_DIFF.md
```

## Política v2.8

- El primer puntero debe ser el resultado canónico vigente cuando exista.
- `SUPERSEDED` e históricos se mueven a `memory/ARCHIVE_INDEX.md`.
- No almacenar narrativa ni pruebas.
- Un alias semántico apunta al mismo canonical id.
- Conflictos científicos reales pueden mantener más de un active id, marcados `CONFLICT`.

Ejemplo:
```text
GENERALIZED-DUFFING -> CERT-D-012 | CERT-D-008[ARCHIVE]
```