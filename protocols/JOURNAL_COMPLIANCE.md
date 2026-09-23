# Cumplimiento dinámico de revista / editorial

## Principio

Las políticas editoriales, de datos, código, reporting y reproducibilidad cambian. Por tanto, **no se hardcodean como universales**.

## Cuando se activa

Si el usuario:

- nombra una revista/editorial/conferencia;
- pide "nivel publicable";
- pide auditoría conforme a estándares actuales;
- prepara supplementary material, data/code availability o reproducibility package.

## Procedimiento

1. Identificar publicación objetivo y fecha de consulta.
2. Recuperar instrucciones actuales desde fuente oficial.
3. Separar requisitos obligatorios, recomendaciones, políticas de datos/código, formato de referencias, límites de extensión, reporting checklist, preregistration/ethics si aplica y material suplementario.
4. Registrar fuente y fecha.
5. Auditar manuscrito/artefactos contra cada requisito.
6. No atribuir como requisito algo que sólo sea recomendación.
7. Si la política es ambigua, declararlo.

## Métodos numéricos

Además de la política de la revista, exigir `NUMERICS.md`. Si la revista es menos estricta, no reducir la reproducibilidad científica necesaria.

## Salida

```text
[JOURNAL-CHECK]
Target:
Date_checked:
Official_sources:
Mandatory:
Recommended:
Pass:
Fail:
Unknown:
Required_actions:
```
