# Protocolo de demostración, refutación y certificación

## Fase A — Formalización

Escribir exactamente universo/espacios, objetos, dominios/codominios, parámetros, regularidad, cuantificadores, hipótesis, conclusión y alcance: local/global, genérico/universal, exacto/asintótico.

No aceptar símbolos cuyo tipo sea ambiguo.

## Fase B — Grafo de dependencias

```text
TARGET
├─ DEP-1 [certificado/literatura/nuevo]
├─ DEP-2
│  ├─ ...
└─ BRIDGE-X
```

Recuperar sólo los nodos necesarios.

### Fase B.1 — Enrutamiento por obligación de prueba

Para cada dependencia nueva o puente no certificado aplicar `protocols/PROOF_TACTICS.md` y, cuando sea material, registrar la obligación con `templates/PROOF_OBLIGATION.md`.

Cada obligación debe declarar al menos:

```text
subclaim -> tactic -> closure_standard -> epistemic_status
```

Tácticas posibles incluyen:

`CERTIFIED_INTERNAL_RESULT | EXTERNAL_THEOREM | DIRECT_ANALYTIC | SYMBOLIC_EXACT | EXHAUSTIVE_FINITE_COMPUTATION | VALIDATED_NUMERICS | RIGOROUS_COMPUTER_ASSISTED_PROOF | NUMERICAL_SCOUT | COUNTEREXAMPLE_SEARCH`.

No es obligatorio usar varias tácticas. Sí es obligatorio cerrar cada obligación esencial con fuerza suficiente para el claim.

Un nodo apoyado sólo por evidencia `[N]` exploratoria permanece abierto para una conclusión exacta.

## Fase C — Antecedentes certificados

Para cada resultado interno:

1. cargar su Proof Certificate;
2. comprobar compatibilidad de hipótesis;
3. comprobar versión de definiciones/modelo;
4. revisar estado `CERTIFIED`;
5. expandir la prueba original sólo si hay incompatibilidad, conflicto o auditoría explícita.

## Fase D — Resultados externos

Crear Evidence Card y matriz de aplicabilidad.

## Fase E — Construcción

Cada paso no trivial debe indicar su razón y, cuando sea relevante, el mecanismo de cierre de la obligación:

```text
A --[L-012 + APP-007]-----------------> B
B --[CERT-D-004]----------------------> C
C --[PO-021 / DIRECT_ANALYTIC]--------> D
D --[PO-022 / VALIDATED_NUMERICS]-----> TARGET
```

Los nuevos lemas se demuestran con el mismo protocolo.

Una computación rigurosa puede cerrar un paso positivo sólo si satisface `protocols/NUMERICS.md`, el estándar definido para esa obligación y el Computation Certificate cuando corresponda.

## Fase F — Ataque adversarial

Buscar activamente contraejemplos, pérdida de hipótesis, casos frontera, singularidades, componentes desconectadas, isotropías, ambigüedades discretas, pérdida de rango, conjuntos excepcionales, dependencias circulares, local usado como global, genérico como universal, asintótico como exacto, cambio de dominio/cuerpo, interacción con condiciones iniciales/frontera, falta de uniformidad, denominadores anulables y restricciones perdidas.

Atacar también el puente que convierte una computación en una conclusión matemática: cobertura, exhaustividad, error, redondeo, cuantificadores y correspondencia código-claim.

## Fase G — Computación como scout, falsificador o cierre riguroso

La computación puede desempeñar tres funciones distintas:

1. `NUMERICAL_SCOUT`: detectar patrones, regiones, candidatos, testigos o conjeturas;
2. `COUNTEREXAMPLE_SEARCH`: buscar refutaciones o regiones problemáticas;
3. `VALIDATED_NUMERICS | EXHAUSTIVE_FINITE_COMPUTATION | RIGOROUS_COMPUTER_ASSISTED_PROOF | SYMBOLIC_EXACT`: intentar cerrar una obligación con estándar matemático explícito.

Para cualquier función computacional aplicar `protocols/NUMERICS.md`.

Un candidato numérico a contraejemplo debe verificarse con tolerancias, precisión y, cuando la naturaleza del claim lo requiera, elevarse a un testigo exacto/certificado antes de declarar `[X]` exacto.

Nunca declarar cierre exacto sólo por residuo pequeño, sweep exitoso, alta precisión decimal o acuerdo entre simulaciones.

## Fase H — Reparación mínima

Si falla el target:

- identificar el punto exacto;
- añadir sólo la hipótesis necesaria;
- restringir dominio;
- debilitar local/global o universal/genérico;
- cambiar de táctica para la obligación abierta;
- o declarar refutación.

No convertir una obligación abierta en hipótesis implícita.

## Fase I — Auditoría de dependencias

Antes de certificar:

1. identificar dependencias esenciales y auxiliares;
2. comprobar su estatus;
3. comprobar para cada obligación esencial `tactic -> closure_standard -> artifact -> closure_class`;
4. heredar condiciones de cualquier dependencia `CONDITIONAL`;
5. si una dependencia parece innecesaria, demostrar independencia y corregir el grafo;
6. si una dependencia está `REFUTED|SUPERSEDED|STALE`, marcar el target `NEEDS_REVALIDATION` hasta cerrar la reparación;
7. bloquear `CERTIFIED` si una obligación esencial sigue `OPEN` o `EVIDENCE_ONLY`.

Aplicar `protocols/CERTIFICATION.md`.

## Fase J — Segunda revisión independiente

Todo claim matemático central debe pasar una segunda revisión que reconstruya el argumento sin recibir el veredicto de la primera revisión.

Si existe una obligación computacional esencial, la revisión debe comprobar tanto el marco matemático como la suficiencia del certificado computacional.

Una objeción no resuelta impide `CERTIFIED`.

## Fase K — Certificación

Sólo certificar si:

- dependencias cerradas;
- obligaciones esenciales rigurosamente cerradas;
- fuentes verificadas;
- aplicabilidad completa;
- adversarial audit completado;
- no quedan `?` esenciales;
- computaciones esenciales superan su gate;
- alcance delimitado.

Crear Proof Certificate sólo después de superar el Certification Gate.

## Regla de herencia

Si `T2` depende de `T1`, y `T1` ya está certificado:

- `T2` referencia `CERT-T1`;
- no reimprimir `proof(T1)`;
- sólo demostrar compatibilidad de hipótesis de `T1` con el contexto de `T2`.

Si esa compatibilidad requiere un lema, ese lema se audita por separado como una nueva obligación.

## Regla de propagación

Un claim no puede quedar incondicionalmente `CERTIFIED` si depende esencialmente de un antecedente `CONDITIONAL` cuyas condiciones no se han incorporado o verificado.

Si el claim usa sólo una dirección o una consecuencia independiente del antecedente, demostrarlo explícitamente y eliminar/corregir la arista del grafo.

Una obligación esencial `EVIDENCE_ONLY` no puede elevarse por agregación de múltiples experimentos ordinarios a `RIGOROUSLY_CLOSED` sin puente certificado.

## Fase L — Fuerza del claim

Antes de aceptar `generic`, `open dense`, `maximal`, `minimal`, `only if`, `universal` o `impossible`, identificar la obligación lógica adicional asociada.

- `generic/open dense`: definir espacio + demostrar no-identidad del discriminante/minor mediante testigo exacto o argumento equivalente.
- `maximal`: definir universo + suficiencia + necesidad fuera de la clase.
- `sharp minimal`: lower bound + construcción alcanzable.
- `impossible`: obstrucción para una clase de métodos definida.
- `universal`: cuantificadores sobre toda la familia sin usar evidencia muestral como sustituto.

Si se pretende cubrir una familia por computación rigurosa, el certificado debe demostrar cobertura del dominio cuantificado, no sólo muestreo.

Una prueba de que una estrategia concreta falla sólo certifica esa obstrucción concreta.