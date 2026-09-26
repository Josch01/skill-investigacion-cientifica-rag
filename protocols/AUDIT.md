# Protocolo de auditoría científica

## 1. Alcance

Una auditoría no reescribe primero; intenta determinar qué puede sostenerse.

## 2. Inventario de claims

Extraer definiciones, teoremas/lemas, afirmaciones de literatura, claims de novedad, claims numéricos, conclusiones, relaciones causales y claims de generalidad. Asignar IDs.

## 3. Auditoría matemática

Para cada claim:

- ¿está bien tipado?
- ¿sus hipótesis están declaradas?
- ¿las dependencias son no circulares?
- ¿el resultado citado existe y aplica?
- ¿el alcance fue fortalecido?
- ¿local/global?
- ¿genérico/universal?
- ¿casos excepcionales?
- ¿objetos transformados conservan restricciones?

## 4. Auditoría bibliográfica

Revisar fuente primaria, formulación exacta, ubicación, hipótesis, fecha cuando importa y que las citas realmente soporten la frase.

## 5. Auditoría numérica

Aplicar `NUMERICS.md`.

Cada experimento debe responder a un claim concreto y el claim no debe exceder la evidencia.

## 6. Auditoría de contribución

Separar:

```text
KNOWN: ya en literatura
COMBINATION: combinación de herramientas conocidas
NEW-DERIVATION: deducción nueva defendible
NEW-COMPUTATION: resultado computacional nuevo
CONJECTURAL: aún sin prueba
UNSUPPORTED: sin evidencia suficiente
```

No afirmar novedad absoluta por ausencia de coincidencia exacta.

## 7. Severidad

- `FATAL`: invalida el resultado central.
- `MAJOR`: requiere nueva prueba/datos/análisis.
- `MODERATE`: afecta alcance o reproducibilidad.
- `MINOR`: notación, claridad o presentación.

## 8. Salida

Entregar resumen del alcance, hallazgos por severidad, claims sostenibles/no sostenibles, condiciones para reparar, pruebas/experimentos faltantes, referencias verificadas y estado de contribución con lenguaje prudente.


## 9. Auditoría completa de manuscritos

Si el usuario solicita auditoría completa/integral/claim-by-claim:

1. aplicar `protocols/MANUSCRIPT_AUDIT_COVERAGE.md`;
2. construir inventario canónico antes de revisar pruebas;
3. clasificar cada objeto por tipo (assumption, definition, theorem-like, numerical/literature claim);
4. si hay más de 6 claims matemáticos centrales, aplicar `protocols/AUDIT_BATCHING.md`;
5. separar estado del claim, de la evidencia y del artefacto con `protocols/CLAIM_EVIDENCE_ARTIFACT_SEPARATION.md`;
6. someter toda objeción material del Red Team a `protocols/ADVERSARIAL_OBJECTION_GATE.md`;
7. comprobar second-review coverage con `protocols/SECOND_REVIEW_COVERAGE.md`;
8. comprobar completitud semántica de artefactos con `protocols/SEMANTIC_ARTIFACT_COMPLETENESS.md`.

Una auditoría no se considera completa sólo porque existan archivos con los nombres esperados.

### 9.1 Definitions y assumptions

- una `definition` no recibe proof status; auditar tipado, no circularidad y consistencia;
- una `assumption` no se refuta por no estar demostrada; registrar su alcance y descendientes;
- sólo claims demostrables reciben proof obligations.

### 9.2 Objeciones

Una objeción adversarial es otro claim científico y debe verificarse.
`might fail`, `could be singular` o `perhaps` no bastan para degradar un teorema.

### 9.3 Coverage status

Emitir:
`AUDIT_COVERAGE_STATUS = PASS | PARTIAL | FAIL`.

`PASS` exige correspondencia uno-a-uno entre el inventario dentro del scope y los registros auditados materialmente.
