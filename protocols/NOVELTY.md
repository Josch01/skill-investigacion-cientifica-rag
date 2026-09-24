# Protocolo de novedad y contribución

## Descomposición

Separar la supuesta contribución en:

- objeto nuevo;
- hipótesis nuevas;
- conclusión nueva;
- generalización;
- método;
- combinación;
- algoritmo;
- evidencia/benchmark;
- aplicación.

## Búsqueda

Para cada unidad buscar término exacto, sinónimos, formulaciones históricas, trabajos que citan resultados centrales, aplicaciones equivalentes con terminología distinta y métodos cercanos.

## Comparación

| Trabajo | Hipótesis | Objeto | Resultado | Método | Diferencia con nosotros |
|---|---|---|---|---|---|

## Salida permitida

- "La búsqueda realizada no encontró..."
- "El componente X parece no estar cubierto por las fuentes consultadas..."
- "La contribución defendible está en..."

No usar "primero", "único", "nadie" sin evidencia extraordinaria.


## Novelty Coverage Gate

Antes de sostener una afirmación fuerte de novedad crear `templates/NOVELTY_COVERAGE.md`.

Estados permitidos:

`PRIOR_ART_FOUND | KNOWN_COMPONENTS_NEW_COMBINATION | APPARENTLY_NEW_WITHIN_SEARCH_SCOPE | STRONG_NOVELTY_SUPPORT | NOVELTY_UNRESOLVED`

Para `STRONG_NOVELTY_SUPPORT` exigir, cuando sea posible:

- descomposición del claim;
- varias familias de consultas;
- sinónimos/terminología histórica;
- comparación con prior art cercano;
- backward citation chaining;
- forward citation chaining;
- segunda estrategia/base/herramienta de búsqueda;
- alcance, fecha y limitaciones explícitos.

Incluso `STRONG_NOVELTY_SUPPORT` no significa prueba lógica de inexistencia mundial.

No usar `CERTIFIED NEW`, `FIRST`, `UNIQUE` o equivalentes sin evidencia extraordinaria.
