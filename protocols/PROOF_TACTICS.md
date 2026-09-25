# Proof-Obligation Tactic Routing

## 1. Propósito

Este protocolo decide **cómo intentar cerrar cada obligación lógica** de una demostración sin imponer una única metodología a todo el teorema.

Principio central:

> Las tácticas son opcionales; las obligaciones lógicas esenciales no.

Una prueba puede ser completamente analítica, bibliográfica, simbólica, computacional rigurosa o híbrida. Lo obligatorio es que todo nodo esencial del grafo de prueba quede cerrado con un estándar compatible con la fuerza del claim.

Aplicar después de construir el grafo de dependencias en `protocols/PROOF.md` y antes de desarrollar una cadena larga.

## 2. Unidad de trabajo: Proof Obligation

Para cada dependencia nueva o puente no certificado crear o recuperar un registro según `templates/PROOF_OBLIGATION.md`.

### Invariante de identidad e idempotencia

Una obligación lógica material debe tener un único `Obligation_ID` activo por `Parent_claim + Statement + Domain_and_quantifiers` dentro de la misma revisión.

Si el protocolo se invoca otra vez sobre una obligación ya registrada:

- NO crear un segundo PO para el mismo subclaim;
- recuperar el `Obligation_ID` existente;
- conservar historial de tácticas fallidas;
- actualizar sólo `Active_tactic`, evidencia, failure reason, fallback o `Closure_class` cuando corresponda;
- no degradar ni promover el cierre sin nueva evidencia auditada.

Así `RESEARCH_LOOP -> PROOF -> PROOF_TACTICS` y una comprobación posterior del mismo subclaim son idempotentes, no recursivas.

Cada obligación debe declarar:

- `Obligation_ID`;
- subclaim exacto;
- hipótesis locales;
- cuantificadores y dominio;
- por qué es esencial o auxiliar;
- tácticas candidatas;
- táctica activa;
- estándar de cierre requerido;
- evidencia producida;
- estatus epistemológico;
- artefactos/certificados asociados;
- fallback si la táctica falla.

No seleccionar una táctica por familiaridad. Elegirla por adecuación lógica, fuerza potencial, costo y posibilidad de falsación.

## 3. Registro de tácticas

### `CERTIFIED_INTERNAL_RESULT`
Reutilizar un resultado interno `CERTIFIED` compatible. Cierre: statement, scope, definiciones, hipótesis e inexistencia de invalidación verificados.

### `EXTERNAL_THEOREM`
Usar literatura verificada. Cierre: Evidence Card + matriz de aplicabilidad completa + puente explícito al subclaim.

### `DIRECT_ANALYTIC`
Demostrar el subclaim mediante argumento matemático nuevo. Cierre: deducción completa + ataque adversarial.

### `SYMBOLIC_EXACT`
Usar álgebra/cálculo simbólico exacto. Cierre: supuestos, ramas, denominadores, dominios y simplificaciones auditados; no basta evaluación decimal.

### `EXHAUSTIVE_FINITE_COMPUTATION`
Resolver una obligación sobre un universo finito mediante enumeración exhaustiva exacta. Cierre sólo si la exhaustividad y exactitud/certificación quedan demostradas.

### `VALIDATED_NUMERICS`
Usar interval arithmetic, validated ODE/PDE integration, interval Newton/Krawczyk, validated continuation, bounds certificados u otro método con garantía equivalente. Cierre sólo si cubre cuantificadores, dominio y error/redondeo requeridos.

### `RIGOROUS_COMPUTER_ASSISTED_PROOF`
Combinar marco teórico con computación certificada. Cierre: reducción explícita + cobertura + aritmética/cotas rigurosas + reproducibilidad + Computation Certificate + auditoría.

### `NUMERICAL_SCOUT`
Simulación/sweep/optimización/diagnóstico no validado para descubrir estructura. Salida: `[N]`, candidato, región problemática o `[C]`; no cierra por sí solo una obligación exacta.

### `COUNTEREXAMPLE_SEARCH`
Buscar refutación analítica o computacional. Un candidato numérico se eleva a `[X]` exacto sólo tras verificación/certificación suficiente para la naturaleza del claim.

## 4. Clases de cierre

`OPEN | EVIDENCE_ONLY | CONDITIONAL | RIGOROUSLY_CLOSED | REFUTED`

- `[N]` ordinario -> normalmente `EVIDENCE_ONLY`;
- conjetura -> `OPEN`;
- prueba bajo `H_extra` -> `CONDITIONAL`;
- argumento exacto o computación rigurosa suficiente -> `RIGOROUSLY_CLOSED`;
- contraejemplo/contradicción rigurosa -> `REFUTED`.

El target no puede quedar `CERTIFIED` si alguna obligación esencial permanece `OPEN` o `EVIDENCE_ONLY`.

## 5. Selección y branching

Para cada obligación:

1. intentar resultado directo certificado/literatura plenamente aplicable;
2. preferir deducción corta o cálculo exacto antes que computación costosa;
3. usar numerics exploratorios como scout/falsificador cuando reduzcan incertidumbre;
4. si el subclaim admite cierre computacional riguroso, fijar `Computation_semantics` y `Closure_standard` antes de ejecutar `protocols/NUMERICS.md`;
5. si una táctica falla, registrar el fallo y cambiar de táctica/abrir subclaim sin declarar refutación injustificada.

No existe obligación de usar simultáneamente literatura, analítica y computación. Existe obligación de no ocultar huecos esenciales.

## 6. Claims sobre familias y cuantificadores fuertes

Un sweep no cubre por sí solo un cuantificador universal. Para cerrar `forall p in P: Q(p)` mediante cómputo riguroso, justificar cobertura de todo `P` por partición intervalar, cota uniforme, enumeración exhaustiva finita, reducción teórica u otro argumento equivalente.

`sampled_region != quantified_domain` salvo prueba explícita de cobertura.

Para `generic`, `open dense`, `maximal`, `sharp`, `iff`, `impossible` o `universal`, aplicar además los gates de fuerza del claim.

## 7. Integración con numerics

Cuando una obligación use computación, declarar:

`exploratory_numeric | falsification_search | corroborative_numeric | symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`.

Sólo `symbolic_exact`, `exhaustive_finite`, `validated_numeric` o `rigorous_computer_assisted_proof` pueden cerrar una obligación exacta, y sólo si satisfacen el estándar matemático específico del subclaim.

La dirección canónica es:

`PROOF_TACTICS -> NUMERICS -> artifact/certificate -> obligation audit`.

`NUMERICS` no vuelve a enrutar la obligación.

## 8. Auditoría

Antes de certificar revisar por obligación esencial:

`Obligation -> tactic -> closure_standard -> artifact -> epistemic_status -> closed?`

El auditor debe intentar romper tanto la deducción como el puente que convierte computación en evidencia de nivel prueba.

## 9. Regla de síntesis

La prueba puede ser un grafo heterogéneo de teoremas externos, lemas directos, identidades simbólicas, bounds numéricos validados y resultados internos certificados.

La heterogeneidad de métodos es válida. La mezcla de niveles epistemológicos sin puente certificado no lo es.
