# Audit Batching Gate

## 1. Propósito

Evitar `breadth collapse`: cubrir muchos claims nominalmente a costa de sustituir razonamiento por plantillas.

## 2. Activación

Para auditorías matemáticas completas:

- si `N_CENTRAL_CLAIMS <= 6`, puede usarse un único bloque;
- si `N_CENTRAL_CLAIMS > 6`, dividir por defecto en bloques de 4–6 claims relacionados por dependencia.

Se puede exceder el tamaño sólo con justificación explícita y evidencia de cobertura material.

## 3. Flujo obligatorio para manuscritos grandes

### Fase 1 — Inventory
Inventario exhaustivo + dependency skeleton.

### Fase 2 — Partition
Particionar el DAG en bloques lógicos. Priorizar foundations antes de descendientes.

### Fase 3 — Block audits
Para cada bloque:
- reconstruir statements/hipótesis;
- proof obligations;
- type audit;
- adversarial objections;
- evidence/numerics;
- local status.

### Fase 4 — Cross-block reconciliation
Propagar dependencias y condiciones entre bloques.

### Fase 5 — Global Red Team
Atacar resultados centrales usando el estado reconciliado.

### Fase 6 — Second Review
Aplicar `protocols/SECOND_REVIEW_COVERAGE.md`.

### Fase 7 — Global certification
Artifact consistency + coverage + objective closure.

## 4. Invariante

Un bloque no puede certificarse usando como dependencia otro bloque aún no auditado salvo que esa dependencia ya tenga un certificado previo vigente y compatible.

## 5. Salida

Registrar:
`AUDIT_BATCH_PLAN`,
claims por bloque,
orden,
dependencias cruzadas,
estado de cada bloque.

Una auditoría grande no se considera completa hasta integrar todos los bloques incluidos en el scope.
