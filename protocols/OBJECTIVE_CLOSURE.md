# Objective Closure & Claim Strength Gate

## 1. Propósito

Evitar que una investigación se cierre con un resultado internamente correcto pero más débil, más estrecho o conceptualmente distinto del objetivo científico original.

También bloquea claims de fuerza elevada —como `generic`, `open dense`, `maximal`, `only if`, `unique`, `universal boundary`— cuando la evidencia sólo soporta una observación numérica, un caso particular o la falla de una ruta concreta.

Principio:
`CLAIM CORRECTNESS != OBJECTIVE CLOSURE`

Un claim puede estar `CERTIFIED` y aun así el objetivo quedar `PARTIAL`.

## 2. Objective-to-Claim Alignment

Antes de cerrar un Research Objective comparar:
- objeto/familia objetivo;
- parámetros incluidos;
- cuantificadores;
- dominio;
- scope local/global;
- scope universal/generic;
- nivel exacto/numérico;
- maximalidad/minimalidad solicitada;
- criterio de éxito original.

Crear conceptualmente:
`OBJECTIVE_ALIGNMENT: target -> achieved_claim -> relation -> missing_scope -> closure_status`

Relaciones permitidas:
`EQUIVALENT | STRICTLY_STRONGER | STRICTLY_WEAKER | DIFFERENT_OBJECT | DIFFERENT_SCOPE | INCOMPARABLE`.

Si el resultado es `STRICTLY_WEAKER`, `DIFFERENT_OBJECT`, `DIFFERENT_SCOPE` o `INCOMPARABLE`, no marcar el objetivo `PROVED` salvo que el usuario haya reformulado explícitamente el objetivo.

## 3. Maximality / Broadest-family Gate

Si el objetivo usa expresiones como:
`maximal`, `broadest`, `largest class`, `only class`, `if and only if frontier`, `exact boundary`,

entonces encontrar una familia que funciona NO cierra el objetivo.

Para sostener maximalidad exigir:
1. definición exacta del universo de familias/operadores permitidos;
2. propiedad que se quiere caracterizar;
3. prueba de suficiencia para la clase candidata;
4. prueba de necesidad para toda clase fuera de ella, o teorema estructural equivalente;
5. tratamiento de transformaciones/liftings/variables auxiliares permitidas;
6. tratamiento de excepciones y equivalencias de representación.

Mostrar que Rayleigh falla bajo una integración por partes específica no demuestra que Liénard sea maximal bajo todas las weak formulations.

Si sólo se demuestra falla de una estrategia, usar:
`ROUTE_SPECIFIC_OBSTRUCTION` o `METHOD_SPECIFIC_BOUNDARY`.

## 4. Generic / Open-Dense Gate

`generic`, `open dense`, `almost every`, `measure zero exception`, `proper analytic variety` son claims matemáticos exactos.

No pueden derivarse sólo de:
- sweeps numéricos;
- muchos casos exitosos;
- ausencia de contraejemplos;
- singular values positivos en una grilla.

Para un claim `open dense` basado en analiticidad exigir:
1. espacio de parámetros/orbitas bien definido;
2. función/minor analítico bien definido en ese espacio;
3. prueba de que no es idénticamente cero;
4. al menos un testigo analítico exacto o argumento teórico equivalente;
5. conexión rigurosa entre no-anulación del minor y full rank;
6. condiciones de conectividad/estratificación que realmente se necesiten.

Sin esto, clasificar como:
`GENERICITY_CONJECTURE_SUPPORTED_BY_NUMERICS` o `NUMERICALLY_SUPPORTED_OPENNESS_CANDIDATE`.

## 5. Numerical-to-Exact Strength Rule

Un sweep puede apoyar:
`[N] robustness`, `[N] counterexample search`, `[N] candidate witness`, `[N] degeneracy locator`.

No puede por sí solo promover:
`universal`, `generic`, `open dense`, `minimal exact`, `maximal`, `iff`, `impossible`.

Antes de usar uno de esos términos debe existir un puente analítico certificado.

## 6. First-success fallacy

Cuando el objetivo pide 'familia más amplia' o 'strongest sustainable theorem', no detenerse en el primer teorema demostrable.

Después de cada éxito preguntar:
1. ¿puede reintroducirse algún término/parámetro eliminado?
2. ¿puede ampliarse el dominio?
3. ¿puede debilitarse una hipótesis?
4. ¿existe una superfamilia natural todavía no refutada?
5. ¿la prueba depende realmente de la simplificación introducida?

Ejemplo abstracto:
`target: damped odd-power family`
`proved: undamped odd-power family`

Resultado: claim posiblemente correcto, pero objective closure = `PARTIAL` hasta estudiar el damping.

## 7. Claim Strength Ladder

Orden orientativo de fuerza:
`EXAMPLE < SUBFAMILY < CONDITIONAL FAMILY < GENERIC FAMILY < UNIVERSAL FAMILY < MAXIMAL/CHARACTERIZATION`.

No subir niveles sin un puente demostrado.

Para minimalidad:
`observed minimum < lower bound < sharp minimum`.

Para imposibilidad:
`method failure < obstruction for a defined method class < impossibility theorem`.

## 8. Closure statuses

Estados de cierre del objetivo:
`CLOSED_EXACTLY | CLOSED_STRONGER | PARTIAL_USEFUL | TARGET_MISALIGNED | OPEN_SCOPE_GAP | REFUTED | UNRESOLVED`.

Estos estados son distintos del status epistemológico de cada claim.

## 9. Required final comparison

Antes de cerrar una investigación orientada a objetivos producir:

`ORIGINAL_OBJECTIVE:`
`ACHIEVED_RESULT:`
`RELATION:`
`UNEXPLORED_SUPERFAMILIES:`
`UNJUSTIFIED_STRENGTH_WORDS:`
`OBJECTIVE_CLOSURE_STATUS:`
`NEXT_SCOPE_TEST:`

## 10. Regla final

> Probar algo interesante no equivale a haber respondido exactamente la pregunta original. La investigación termina sólo cuando el scope alcanzado y el scope pedido se comparan explícitamente.

## 11. Scope Completion Invariant

`CLOSED_EXACTLY` exige que TODOS los componentes explícitos del success criterion original estén:
- resueltos;
- refutados;
- o formalmente eliminados mediante reformulación explícita del objetivo por el usuario.

Si `Unexplored_superfamilies` contiene un elemento que formaba parte explícita del objetivo original, entonces:
`CLOSED_EXACTLY = forbidden`.

Usar `OPEN_SCOPE_GAP` o `PARTIAL_USEFUL` según corresponda.

Ejemplo:
`objective includes vector/coupled systems` + `unexplored_superfamilies = vector/coupled systems` => no puede ser `CLOSED_EXACTLY`.

## 12. Exact Witness Dependency

Si el cierre depende de `generic/open dense` mediante no-anulación analítica, consultar `protocols/EXACT_WITNESS.md`.

Un witness expresado mediante factores calculados sólo en float no satisface `Exact_nonzero_witness_available: yes`.

Debe registrarse el nivel real:
`EXACT_NONZERO | RIGOROUS_NUMERIC_NONZERO | HIGH_PRECISION_NUMERIC_NONZERO | ...`.