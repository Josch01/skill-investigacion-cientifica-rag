# Scientific Object & Symbol Table

Registro compacto para símbolos, variables, entidades, datasets, poblaciones, métricas, mapas, unidades, modelos, APIs y versiones.

## Esquema

```text
[OBJ-###]
Canonical_name:
Symbol_or_label:
Kind: mathematical_object|parameter|state|dataset|population|sample|metric|estimand|unit|model|software|api|instrument|other
Type:
Domain_or_source:
Codomain_or_unit:
Meaning:
Scope:
Version:
Aliases:
Defined_in:
Compatible_with:
Explicit_bridges:
Forbidden_substitutions:
Notes:
```

## Reglas

- No registrar conversación; registrar identidad científica durable.
- Toda sustitución entre objetos distintos requiere puente explícito.
- Si un alias cambia significado entre secciones, crear objetos separados.
- Mantener sólo objetos que afecten corrección, interpretación o reproducibilidad.