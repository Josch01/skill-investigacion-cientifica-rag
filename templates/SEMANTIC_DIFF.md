# Semantic Diff

Compara una fuente científica normativa con su representación editada.

```text
Source_ID:
Rendered_location:

OBJECTS:
  source:
  rendered:
  status: SAME|EXPLICIT_BRIDGE|MISMATCH

HYPOTHESES:
  source:
  rendered:
  lost:
  added:

CONCLUSION:
  source:
  rendered:
  status:

SCOPE:
  source:
  rendered:
  drift:

DEPENDENCIES:
  source:
  rendered:
  compressed_steps:

UNITS_SCALES_POPULATIONS_DATASETS_VERSIONS:
  differences:

EPISTEMIC_STATUS:
  source:
  rendered:

VERDICT: PASS|NEEDS_PATCH|SEMANTIC_MISMATCH
MINIMAL_REPAIR:
```

## Regla

Un diff textual limpio no implica un diff semántico limpio. Este registro compara significado científico.