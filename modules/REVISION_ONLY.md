# Module: REVISION_ONLY

## Activar cuando

Un auditor haya emitido `REVISION_REQUIRED` y exista una revisión previa válida.

## Principio

Corregir sólo el delta auditado. No reiniciar la investigación completa ni regenerar artefactos no afectados salvo dependencia explícita.

## Inputs mínimos

- contrato/task packet vigente;
- artefactos afectados;
- `REVISION_DELTA.md`;
- evidencia/gates fallidos relevantes.

## Obligaciones

1. Mantener claim, scope, hipótesis y definiciones salvo que el auditor ordene `SCIENTIFIC_REOPEN` o `CONTRACT_REVISION_REQUIRED`.
2. Resolver cada issue con evidencia verificable.
3. Registrar qué archivos cambiaron y por qué.
4. Reejecutar sólo deterministic checks y certificados afectados.
5. No convertir una corrección local en reescritura total.

## Salida

`issues addressed | files changed | checks rerun | remaining issues | completion signal`.