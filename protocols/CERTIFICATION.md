# Certification Gate

## 1. Propósito

Este protocolo se activa únicamente cuando un claim, prueba, resultado computacional o conclusión pretende alcanzar un estatus fuerte como `CERTIFIED` o sostener una afirmación de novedad.

Su función es impedir certificaciones prematuras, inconsistencias en el grafo y lenguaje más fuerte que la evidencia.

## 2. Dependency Status Propagation

Para cada claim TARGET construir su conjunto de dependencias esenciales.

Regla base:

`effective_status(TARGET) <= weakest_required_dependency`

salvo que exista una demostración explícita de que TARGET no necesita esa dependencia o que las condiciones de esa dependencia han sido descargadas dentro del propio teorema.

Ejemplos:

- Si TARGET depende esencialmente de D1=CONDITIONAL, TARGET no puede quedar incondicionalmente CERTIFIED.
- Si TARGET sólo usa una dirección de D1 que fue demostrada independientemente, eliminar esa arista del grafo y justificar la independencia.
- Si D1 requiere H-extra y TARGET declara H-extra entre sus hipótesis, TARGET puede certificarse condicionado a H-extra.
- Si una dependencia pasa a REFUTED, SUPERSEDED o STALE, todos sus descendientes directos e indirectos deben reabrirse o marcarse STALE hasta demostrar independencia.

Antes de certificar, producir conceptualmente:

`DEPENDENCY_AUDIT: dependency -> required? -> status -> inherited_conditions -> resolution`

## 3. Taint propagation

Dependencias con estado `[U]`, `partial`, `unverified`, `CONDITIONAL` no descargado o evidencia bibliográfica incompleta contaminan el target.

No ocultar esta contaminación mediante redacción.

## 4. Independent Second Review

Todo claim matemático central que vaya a `CERTIFIED` debe pasar una segunda revisión independiente.

Si existen subagentes reales:
- el segundo revisor recibe statement, hipótesis, definiciones y fuentes necesarias;
- NO recibe el veredicto del primer revisor ni frases como 'la prueba es correcta';
- intenta rederivar, refutar o localizar un hueco por su cuenta.

Si no existen subagentes reales:
- realizar un segundo pase separado;
- ocultar conceptualmente el veredicto anterior;
- reconstruir la prueba desde statement + hypotheses + evidence;
- comparar sólo al final.

Estados del segundo review:

`CONFIRMS | CONFIRMS_WITH_CONDITIONS | OBJECTS | UNRESOLVED`

Una discrepancia entre revisiones bloquea `CERTIFIED` hasta resolverla.

## 5. Computation Certificate Gate

Si una computación es esencial para el claim, exigir `templates/COMPUTATION_CERTIFICATE.md`.

Debe incluir como mínimo:
- script/archivo exacto;
- hash o commit;
- versión de datos si aplica;
- versiones de librerías;
- SO/arquitectura si material;
- precisión;
- semillas si aplican;
- solver/algoritmo;
- tolerancias;
- comando de ejecución;
- salida relevante;
- verificación independiente o rerun;
- limitaciones.

Si falta un artefacto esencial:
- la computación puede quedar como `[N] VERIFIED`;
- no puede ser fundamento único de un `CERTIFIED` exacto.

Si la computación sólo es corroborativa y existe una prueba analítica completa, su falta no invalida la prueba; debe reclasificarse como soporte no esencial.

## 6. Novelty Coverage Gate

La novedad NO se certifica como teorema matemático.

Usar `templates/NOVELTY_COVERAGE.md`.

Estados permitidos:

`PRIOR_ART_FOUND | KNOWN_COMPONENTS_NEW_COMBINATION | APPARENTLY_NEW_WITHIN_SEARCH_SCOPE | STRONG_NOVELTY_SUPPORT | NOVELTY_UNRESOLVED`

No usar `CERTIFIED NEW`, `FIRST`, `UNIQUE`, `NO ONE HAS DONE THIS` salvo evidencia extraordinaria que realmente justifique ese lenguaje.

Para `STRONG_NOVELTY_SUPPORT` exigir como mínimo:
- descomposición del claim;
- múltiples familias de consultas;
- sinónimos y terminología histórica;
- prior art más cercano;
- backward citation chaining cuando material;
- forward citation chaining cuando disponible;
- al menos una segunda estrategia/base/herramienta de búsqueda cuando sea posible;
- comparación explícita hipótesis/objeto/conclusión/método;
- fecha y alcance de búsqueda;
- limitaciones.

Incluso `STRONG_NOVELTY_SUPPORT` significa soporte fuerte dentro del alcance documentado, no prueba lógica de inexistencia mundial.

## 7. Calibration of Language

Evitar expresiones absolutas no formales como:

`100% sound`, `flawless`, `obviously correct`, `completely proven beyond doubt`, `certainly novel`.

Preferir:

`NO_GAP_FOUND_UNDER_STATED_HYPOTHESES`
`CERTIFIED_WITHIN_CURRENT_FORMAL_SCOPE`
`INDEPENDENT_REVIEW_CONFIRMED`
`APPARENTLY_NEW_WITHIN_DOCUMENTED_SEARCH_SCOPE`

La prosa debe ser tan fuerte como el estatus, nunca más fuerte.

## 8. Certification decision

Un claim central sólo alcanza `CERTIFIED` si:

1. statement exacto;
2. hipótesis completas;
3. dependency audit cerrado;
4. condiciones heredadas descargadas o explícitas;
5. Evidence Cards aplicables;
6. prueba cerrada;
7. red team completado;
8. second review no objeta;
9. computation gate satisfecho si la computación es esencial;
10. alcance y excepciones declarados.

Si falla un gate usar el estatus más informativo: `VERIFIED`, `CONDITIONAL`, `PARTIAL`, `UNRESOLVED`, `REFUTED` o `STALE`.

## 9. Invalidation propagation

Cuando un certificado cambia:

`CERTIFIED -> REFUTED|SUPERSEDED|STALE`

recorrer descendientes en el grafo y marcar:

`NEEDS_REVALIDATION`

hasta que se demuestre independencia o se reparen condiciones.

## 10. Regla final

> Certificar no significa que una sola revisión quedó satisfecha; significa que el claim sobrevivió dependencias, prueba, ataque adversarial, revisión independiente y todos los gates materiales.

## 11. Separation of scientific status and artifact status

El Certification Gate certifica conocimiento, no prosa.

Después de certificar un claim, cualquier manuscrito/informe que lo represente debe pasar `protocols/MANUSCRIPT_EDIT.md` y `protocols/TYPE_NOTATION_GATE.md`.

Si el render introduce un objeto mal tipado, una hipótesis perdida, scope drift, una dependencia comprimida incorrectamente o un cambio de población/dataset/métrica/unidad/versión, NO degradar automáticamente el claim certificado si el certificado sigue correcto.

Marcar el artefacto `SEMANTIC_MISMATCH | NEEDS_PATCH` y repararlo desde la fuente normativa.

Sólo reabrir la certificación científica si el mismatch revela que el propio certificado era incorrecto.