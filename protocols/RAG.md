# Protocolo RAG científico

## 1. Principio

La recuperación no busca "texto relacionado"; busca **premisas utilizables**.

Cada afirmación externa que sostenga un paso debe quedar conectada a una fuente mediante una Evidence Card.

## 2. Jerarquía de fuentes

Preferencia aproximada:

1. artículo original o fuente primaria;
2. monografía especializada;
3. artículo revisado por pares que formule el resultado;
4. libro avanzado;
5. proceedings académicos reconocidos;
6. preprint identificado, marcado como tal;
7. tesis;
8. documentación oficial para software;
9. fuente secundaria sólo para orientación.

Blogs, foros y Wikipedia pueden sugerir términos de búsqueda, pero no sostienen una demostración si existe fuente primaria accesible.

## 3. Descomposición de consulta

Antes de buscar, dividir el objetivo en afirmaciones atómicas:

```text
CLAIM-1: ...
CLAIM-2: ...
BRIDGE-1: ...
DEFINITION-1: ...
```

Buscar por separado nombre del resultado, formulaciones equivalentes, hipótesis críticas, contraejemplos, versiones locales/globales, caso finito/infinito dimensional y términos históricos/sinónimos.

## 4. Retrieval funnel

Comenzar pequeño:

- 3–5 fuentes candidatas;
- ampliar sólo si falta una dependencia o hay conflicto.

No recuperar veinte artículos si tres fuentes primarias bastan para decidir aplicabilidad.

## 5. Evidence Card

Registrar:

```text
EVIDENCE_ID:
TYPE: theorem | lemma | definition | numerical-method | software-doc | empirical
SOURCE:
SOURCE_VERSION/DATE:
EXACT_LOCATION:
CLAIM_SUPPORTED:
STATEMENT:
ASSUMPTIONS:
CONCLUSION:
SCOPE:
VERIFICATION: full | partial
NOTES:
```

Si sólo se pudo consultar resumen/snippet, `VERIFICATION=partial` y no certificar un teorema cuyo detalle dependa del texto completo.

## 6. Matriz de aplicabilidad

| Hipótesis fuente | Objeto actual | Evidencia | Estado |
|---|---|---|---|
| H1 | ... | ... | ✓/✗/? |

Si aparece `?` o `✗` en una condición esencial, no aplicar el resultado.

## 7. Fuentes contradictorias

- conservar ambas formulaciones;
- identificar definiciones distintas;
- comparar hipótesis;
- preferir fuente primaria cuando sea posible;
- no fabricar reconciliación;
- registrar el conflicto.

## 8. Estado del arte y novedad

Una búsqueda previa nunca prueba novedad futura.

Para claims de novedad: búsqueda actual, sinónimos, artículos cercanos, referencias hacia atrás/adelante cuando sea posible y comparación explícita de hipótesis/conclusión.

Lenguaje permitido:

> "No encontramos en la búsqueda realizada..."

No afirmar "nadie ha hecho esto" sin evidencia extraordinaria.

## 9. Literatura heredada

Una fuente ya verificada puede reutilizarse si la Evidence Card existe, el mismo resultado exacto se necesita y no cambió el contexto de aplicabilidad.

Si el nuevo uso depende de otra parte del artículo, crear una nueva Evidence Card.
