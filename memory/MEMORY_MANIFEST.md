# MEMORY MANIFEST

Resumen operativo del estado de memoria. No sustituye ledgers ni certificados.

```text
Framework_version:
Last_gc_run:

HOT:
  current_objective:
  active_claim_ids:
  active_route_ids:
  active_hypothesis_ids:

WARM:
  canonical_certificate_count:
  reusable_lemma_count:
  reusable_computation_count:

ARCHIVE:
  superseded_count:
  historical_snapshot_count:
  closed_route_count:

Budget:
  core_within_budget:
  hot_nodes_within_budget:
  gc_required:
```

Actualizar después de una compactación material o cambio de objetivo.