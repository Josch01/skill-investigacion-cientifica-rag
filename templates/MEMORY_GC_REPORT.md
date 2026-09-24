# Memory GC / Compaction Report

```text
Run_ID:
Date:
Framework_version:

Trigger:

Before:
  memory_core_tokens_estimate:
  hot_nodes:
  warm_nodes:
  archived_nodes:
  duplicate_groups:

Canonicalization_actions:
  - old_ids:
    canonical_id:
    action: MERGE_ALIAS|SUPERSEDE|ARCHIVE|KEEP_CONFLICT

Tier_moves:
  - id:
    from:
    to:
    reason:

Compacted_routes:
Compacted_numerics:
Compacted_search_records:

Archive_pointers_created:
Index_updates:

Integrity_checks:
  canonical_ids_resolve: yes|no
  active_dependencies_resolve: yes|no
  aliases_acyclic: yes|no
  superseded_chains_valid: yes|no
  core_within_budget: yes|no
  hot_working_set_within_budget: yes|no

Deleted_evidence: none|required_user_authorization

Final_status: PASS|NEEDS_REPAIR
Notes:
```