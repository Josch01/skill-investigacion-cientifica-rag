# MEMORY LEDGER

## Esquema

```text
[ID]
Type: L|D|C|H|X|U|DEC
Status: DRAFT|VERIFIED|CERTIFIED|CONDITIONAL|PARTIAL|REFUTED|SUPERSEDED|STALE|NEEDS_REVALIDATION
Tags:
Memory_tier: HOT|WARM|ARCHIVE
Canonical_status: CANONICAL_ACTIVE|ALIAS|SUPERSEDED|HISTORICAL
Canonical_id:
Statement:
Hypotheses:
Scope:
Depends_on:
Inherited_conditions:
Dependency_status:
Evidence:
Internal_source:
Supersedes:
Superseded_by:
Date:
Archive_pointer:
Last_accessed_if_tracked:
Notes:
```

## Entradas

[AÑADIR AQUÍ]


## Lifecycle rules

- DRAFT/active bottlenecks pueden estar HOT.
- CERTIFIED reusable suele pasar a WARM después del cierre del objetivo.
- SUPERSEDED/HISTORICAL pasa a ARCHIVE.
- Un nodo archivado no se borra; se conserva por ID y pointer.
- Si un nodo vuelve a ser dependencia, puede rehidratarse temporalmente.