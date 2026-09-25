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

## 2.1 Proof-Obligation Closure Audit

Si la prueba contiene subclaims nuevos o puentes no certificados, aplicar `protocols/PROOF_TACTICS.md` y auditar cada obligación esencial:

```text
Obligation_ID -> tactic -> closure_standard -> artifact/certificate -> closure_class
```

Reglas:

- `OPEN` bloquea `CERTIFIED`;
- `EVIDENCE_ONLY` bloquea `CERTIFIED` para un claim exacto;
- `CONDITIONAL` propaga sus condiciones al target salvo descarga explícita;
- `RIGOROUSLY_CLOSED` sólo cuenta si el método realmente satisface el estándar de cierre declarado;
- una obligación refutada puede refutar el target o invalidar la ruta, según su papel lógico.

No elevar una obligación a cerrada por acumulación de experimentos ordinarios.

## 3. Taint propagation

Dependencias con estado `[U]`, `partial`, `unverified`, `CONDITIONAL` no descargado o evidencia bibliográfica incompleta contaminan el target.

También contaminan el target las obligaciones esenciales `OPEN|EVIDENCE_ONLY` y los certificados computacionales que sólo demuestran reproducibilidad pero no suficiencia matemática.

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

Si hay obligaciones computacionales esenciales, el segundo review debe comprobar además:
- que el subclaim realmente se reduce a la computación declarada;
- cobertura/exhaustividad;
- control de error/redondeo;
- correspondencia entre salida y conclusión matemática.

Estados del segundo review:

`CONFIRMS | CONFIRMS_WITH_CONDITIONS | OBJECTS | UNRESOLVED`

Una discrepancia entre revisiones bloquea `CERTIFIED` hasta resolverla.

## 5. Computation Certificate Gate

Si una computación es esencial para el claim, exigir `templates/COMPUTATION_CERTIFICATE.md`.

Debe incluir como mínimo:
- `Proof_Obligation_ID_if_any`;
- `Computation_semantics`;
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
- puente matemático entre salida y claim;
- cuantificadores/dominio cubiertos;
- cobertura/exhaustividad cuando aplique;
- control de redondeo/error cuando aplique;
- `Closure_standard` si pretende cerrar una obligación;
- verificación independiente o rerun;
- limitaciones.

La reproducibilidad es necesaria pero no suficiente para una prueba asistida por computadora.

Si falta un artefacto o puente esencial:
- la computación puede quedar como `[N] VERIFIED`;
- no puede ser fundamento único de un `CERTIFIED` exacto.

Si la computación sólo es corroborativa y existe una prueba analítica completa, su falta no invalida la prueba; debe reclasificarse como soporte no esencial.

Para `symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`, comprobar específicamente que el método satisface el estándar matemático de la obligación; el nombre de la técnica por sí solo no basta.

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
4. proof-obligation closure audit cerrado cuando aplica;
5. condiciones heredadas descargadas o explícitas;
6. Evidence Cards aplicables;
7. prueba cerrada;
8. red team completado;
9. second review no objeta;
10. computation gate satisfecho si la computación es esencial;
11. alcance y excepciones declarados.

Si falla un gate usar el estatus más informativo: `VERIFIED`, `CONDITIONAL`, `PARTIAL`, `UNRESOLVED`, `REFUTED` o `STALE`.

## 9. Invalidation propagation

Cuando un certificado cambia:

`CERTIFIED -> REFUTED|SUPERSEDED|STALE`

recorrer descendientes en el grafo y marcar:

`NEEDS_REVALIDATION`

hasta que se demuestre independencia o se reparen condiciones.

La invalidación de un Computation Certificate esencial también reabre los claims que dependan de la obligación cerrada por ese certificado.

## 10. Regla final

> Certificar no significa que una sola revisión quedó satisfecha; significa que el claim sobrevivió dependencias, obligaciones de prueba, estándares de cierre, ataque adversarial, revisión independiente y todos los gates materiales.

## 11. Separation of scientific status and artifact status

El Certification Gate certifica conocimiento, no prosa.

Después de certificar un claim, cualquier manuscrito/informe que lo represente debe pasar `protocols/MANUSCRIPT_EDIT.md` y `protocols/TYPE_NOTATION_GATE.md`.

Si el render introduce un objeto mal tipado, una hipótesis perdida, scope drift, una dependencia comprimida incorrectamente o un cambio de población/dataset/métrica/unidad/versión, NO degradar automáticamente el claim certificado si el certificado sigue correcto.

Marcar el artefacto `SEMANTIC_MISMATCH | NEEDS_PATCH` y repararlo desde la fuente normativa.

Sólo reabrir la certificación científica si el mismatch revela que el propio certificado era incorrecto.

## 12. Claim Strength Gate

Antes de certificar palabras de fuerza elevada comprobar `protocols/OBJECTIVE_CLOSURE.md`.

Bloqueos explícitos:
- `generic/open dense` no puede derivarse de un sweep numérico o ausencia de contraejemplos;
- `maximal/only class/iff boundary` no puede derivarse de mostrar que una sola familia rival o una sola técnica falla;
- `sharp minimum` requiere lower bound + matching construction;
- `impossible` requiere obstrucción para una clase de métodos definida, no fracaso de una implementación;
- `universal` requiere cuantificadores cerrados sobre toda la clase declarada.

Una prueba computacional rigurosa puede participar en estos claims sólo si el certificado cubre la obligación adicional correspondiente; un muestreo no sustituye cuantificadores.

Si falta el puente analítico o computacional riguroso, degradar a la categoría informativa apropiada, por ejemplo `CONJECTURAL`, `NUMERICALLY_SUPPORTED`, `METHOD_SPECIFIC_OBSTRUCTION`, `PARTIAL` o `UNRESOLVED`.

Un claim puede superar Certification Gate pero no cerrar el Research Objective; esa decisión pertenece al Objective Closure Gate.

## 13. Exact Witness Gate

Si la prueba de un claim exacto depende de `Q != 0`, un minor/discriminante no idénticamente nulo, o una cota estricta, aplicar `protocols/EXACT_WITNESS.md`.

`float64`, high precision o acuerdo numérico no son suficientes para `EXACT_NONZERO`.

Si la no-anulación sólo está apoyada numéricamente:
- no certificar el puente exacto;
- usar `CONDITIONAL`, `PARTIAL` o conjetura numéricamente soportada;
- o producir validated numerics / bound riguroso / prueba simbólica exacta.

## 14. Mandatory review/state gate

Antes de aceptar un nuevo `CERTIFIED` aplicar `protocols/ARTIFACT_CONSISTENCY.md`.

Un certificado central sin:
`Independent_second_review` y `Second_review_status`

no es válido como `CERTIFIED`.

Si el second review falta: `NEEDS_REVALIDATION`.

Si los artefactos activos discrepan sobre status/version/scope, bloquear el cierre hasta reconciliar.