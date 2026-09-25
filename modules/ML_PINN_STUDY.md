# Module: ML_PINN_STUDY

## Activar cuando

El objetivo incluya redes neuronales, PINNs, surrogate models, aprendizaje híbrido física-datos o comparación de modelos ML en contexto científico.

## Composición

- `modules/CORE_RESEARCH.md`
- `modules/NUMERICAL_STUDY.md`
- `modules/LITERATURE_REVIEW.md` si hay comparación metodológica o novedad.
- `modules/CODE_VERIFICATION.md` si se produce código ejecutable.

## Firewalls

- menor loss != validez física;
- ajuste de entrenamiento != generalización;
- cumplimiento aproximado de residual != solución certificada;
- comparación con budgets/tuning desiguales != superioridad metodológica.

## Obligaciones

Registrar arquitectura, inicialización, seeds, datasets/splits, normalización, loss terms y pesos, optimizer/schedule, stopping, hardware si afecta resultados, métricas train/validation/test y residual físico.

## Salida

`model/architecture | data | physics constraints | training protocol | reproducibility | generalization evidence | failure modes | strongest sustainable ML/PINN claim`.