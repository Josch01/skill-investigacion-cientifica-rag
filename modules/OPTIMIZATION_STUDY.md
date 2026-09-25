# Module: OPTIMIZATION_STUDY

## Activar cuando

El objetivo trate optimización científica, ajuste de parámetros, metaheurísticas, convexidad/no convexidad, benchmarking de optimizadores o análisis de landscape.

## Composición

- `modules/CORE_RESEARCH.md`
- `modules/NUMERICAL_STUDY.md`
- `modules/LITERATURE_REVIEW.md` si se comparan métodos o claims de novedad.
- `protocols/CERTIFICATION.md` sólo si existe un certificado aplicable.

## Firewalls

- mejor solución encontrada != óptimo global;
- una corrida != robustez;
- menor loss en un dataset != superioridad general;
- tuning desigual invalida comparaciones fuertes;
- ausencia de mejora observada != imposibilidad de mejora.

## Obligaciones

Definir objective function, restricciones, dominio, seeds, budgets, stopping criteria, baselines y métricas; registrar múltiples corridas cuando el método sea estocástico; separar evidencia empírica de garantías teóricas.

## Salida

`objective/domain | algorithms | budgets | reproducibility | results distribution | failure modes | strongest sustainable optimization claim`.