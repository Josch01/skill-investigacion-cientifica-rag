# Router dinámico de especialistas

## Objetivo

Elegir el conjunto mínimo de perspectivas expertas que reduzca el riesgo de error sin duplicar contexto.

## Política base

- Tarea simple: 1 especialista.
- Tarea científica sustantiva: 1 lead + 1 adversarial.
- Interdisciplinaria: +1 puente.
- Con evidencia computacional material: +1 numérico.
- Máximo normal: 4.
- No añadir agentes "por si acaso".

## Matriz de activación

| Tipo de tarea | Lead recomendado | Revisor | Añadir si aplica |
|---|---|---|---|
| Demostración en álgebra diferencial | Differential Algebra | Proof Red Team | Identifiability / Symbolic |
| Identificabilidad estructural | Identifiability | Differential Algebra | Control / Symbolic |
| Sistemas dinámicos | Dynamical Systems | Analysis/Geometry | Numerical |
| Caos/bifurcaciones | Chaos & Bifurcation | Dynamical Systems | Numerical |
| Simetrías/acciones de grupo | Lie/Equivariant | Geometry/Topology | Identifiability |
| Optimización de modelos | Optimization | Numerical | Statistics/ML |
| Redes neuronales/PINN | ML | Numerical | Statistics/domain |
| Auditoría de manuscrito | Domain lead | Scientific Auditor | Numerical + Literature |
| Revisión de código científico | Numerical | Domain lead | Software/Reproducibility |
| Novedad/estado del arte | Literature | Domain lead | Scientific Auditor |
| LaTeX final | Scientific Editor | Domain lead | Auditor |

## Selección adversarial

El revisor debe ser suficientemente cercano para detectar errores, pero no idéntico al lead.

## Salida del router

```text
TASK_CLASS:
LEAD:
REVIEWER:
OPTIONAL:
WHY:
RETRIEVAL_TAGS:
CERTIFICATES_TO_LOAD:
```

No mostrar esta mecánica al usuario salvo que sea útil.
