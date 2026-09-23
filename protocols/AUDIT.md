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
