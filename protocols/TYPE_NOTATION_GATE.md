# Type, Notation & Entity Consistency Gate

## 1. Propósito

Detectar errores introducidos durante explicación/redacción por sustitución silenciosa de objetos, dominios, poblaciones, métricas, unidades, datasets, versiones o símbolos.

## 2. Object registry

Usar `memory/SYMBOL_TABLE.md` como registro general de objetos científicos.

Cada objeto material debe poder registrar:
`ID | symbol/name | kind/type | domain/source | codomain/unit | meaning | scope | version | aliases | compatibility`.

## 3. Hard type rule

Dos objetos de tipos distintos no son intercambiables por similitud semántica.

Ejemplos:
- `q in P_phys` no reemplaza `theta in Theta` sin `Theta=P_phys` o mapa explícito;
- incidencia no reemplaza prevalencia;
- población objetivo no reemplaza muestra;
- RMSE normalizado no reemplaza RMSE original;
- validation set no reemplaza test set;
- API v1 no reemplaza v2;
- concentración molar no reemplaza masa sin conversión.

## 4. Identity/bridge rule

Toda identificación requiere una de:
- igualdad declarada;
- inclusión;
- isomorfismo/bijección;
- mapa/conversión;
- regla de agregación;
- transformación de unidades;
- correspondencia de versión;
- argumento de transportabilidad/generalización.

Registrar el puente y sus hipótesis.

## 5. Claim typing

Antes de aceptar un claim verificar que cada término esté bien tipado.

Matemática: dominios/codominios, espacios, cuerpos, cuantificadores.
Estadística: estimando, población, sample, escala, unidad.
ML: dataset, split, métrica, preprocesamiento, checkpoint.
Numerics: variables, discretización, solver, unidades.
Software: tipo, firma, versión, contrato.

## 6. Scope consistency

Bloquear cambios silenciosos:
`local -> global`, `generic -> universal`, `conditional -> unconditional`, `sample -> population`, `association -> causation`, `retrospective -> prospective`, `in-sample -> out-of-sample`, `numerical -> exact`.

## 7. Notation collision

Detectar:
- mismo símbolo para objetos diferentes;
- varios símbolos para mismo objeto sin alias declarado;
- símbolo usado antes de definición;
- dimensión incompatible;
- unidad incompatible;
- versión incompatible.

## 8. Cross-section consistency

Cuando un objeto aparece en varias secciones, verificar continuidad de significado, scope y versión.

Un cambio deliberado debe declararse explícitamente.

## 9. Gate output

`PASS | PASS_WITH_EXPLICIT_BRIDGE | BLOCKED_TYPE_MISMATCH | BLOCKED_UNDEFINED_OBJECT | BLOCKED_SCOPE_DRIFT | BLOCKED_VERSION_MISMATCH`

Todo bloqueo debe indicar el objeto, las dos interpretaciones y la reparación mínima.

## 10. Regla final

> Ninguna prosa elegante compensa un objeto mal tipado.