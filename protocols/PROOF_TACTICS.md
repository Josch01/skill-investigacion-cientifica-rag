# Proof-Obligation Tactic Routing

## 1. Propósito

Este protocolo decide **cómo intentar cerrar cada obligación lógica** de una demostración sin imponer una única metodología a todo el teorema.

Principio central:

> Las tácticas son opcionales; las obligaciones lógicas esenciales no.

Una prueba puede ser completamente analítica, bibliográfica, simbólica, computacional rigurosa o híbrida. Lo obligatorio es que todo nodo esencial del grafo de prueba quede cerrado con un estándar compatible con la fuerza del claim.

Aplicar después de construir el grafo de dependencias en `protocols/PROOF.md` y antes de desarrollar una cadena larga.

## 2. Unidad de trabajo: Proof Obligation

Para cada dependencia nueva o puente no certificado crear conceptualmente un registro según `templates/PROOF_OBLIGATION.md`.

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

Tácticas permitidas, no exhaustivas:

### `CERTIFIED_INTERNAL_RESULT`
Reutilizar un resultado interno `CERTIFIED` compatible.

Cierre: verificar statement, scope, definiciones, hipótesis e inexistencia de invalidación.

### `EXTERNAL_THEOREM`
Usar literatura verificada.

Cierre: Evidence Card + matriz de aplicabilidad completa + puente explícito al subclaim.

### `DIRECT_ANALYTIC`
Demostrar el subclaim mediante argumento matemático nuevo.

Cierre: deducción completa + ataque adversarial correspondiente.

### `SYMBOLIC_EXACT`
Usar álgebra/cálculo simbólico exacto.

Cierre: supuestos, ramas, denominadores, dominios y simplificaciones auditados; el resultado debe ser exacto, no sólo una evaluación decimal.

### `EXHAUSTIVE_FINITE_COMPUTATION`
Resolver una obligación sobre un universo finito mediante enumeración exhaustiva exacta.

Cierre sólo si se demuestra que el universo enumerado es completo, la enumeración no omite casos, el cálculo relevante es exacto o certificado y existe `COMPUTATION_CERTIFICATE` cuando sea material.

### `VALIDATED_NUMERICS`
Usar interval arithmetic, validated ODE/PDE integration, interval Newton/Krawczyk, validated continuation, bounds certificados u otro método numérico riguroso.

Cierre sólo si el método cubre los cuantificadores requeridos, controla redondeo/error y produce una cota/certificado matemáticamente suficiente.

### `RIGOROUS_COMPUTER_ASSISTED_PROOF`
Combinar un marco teórico con computación certificada como parte esencial de la prueba.

Cierre: marco matemático explícito + reducción del claim a obligaciones computables + cobertura + aritmética/cotas rigurosas + reproducibilidad + Computation Certificate + auditoría independiente.

### `NUMERICAL_SCOUT`
Usar simulación, sweep, optimización, Lyapunov/Floquet estimado, Poincaré, continuation no validada u otra computación exploratoria para descubrir estructura.

Salida permitida: `[N]`, candidato, hipótesis, región problemática o `[C]`.

`NUMERICAL_SCOUT` no cierra por sí solo una obligación exacta.

### `COUNTEREXAMPLE_SEARCH`
Buscar una refutación analítica o computacional.

Un candidato numérico debe elevarse a contraejemplo exacto/certificado cuando la naturaleza del claim lo requiera antes de etiquetar `[X]` exacto.

## 4. Clases de cierre

Cada obligación debe usar una de estas clases:

`OPEN | EVIDENCE_ONLY | CONDITIONAL | RIGOROUSLY_CLOSED | REFUTED`

Reglas:

- `[N]` ordinario -> normalmente `EVIDENCE_ONLY`;
- una conjetura -> `OPEN`;
- una prueba bajo `H_extra` -> `CONDITIONAL`;
- un argumento exacto o una computación rigurosa que satisface el estándar -> `RIGOROUSLY_CLOSED`;
- un contraejemplo o contradicción rigurosa -> `REFUTED`.

El target no puede quedar `CERTIFIED` si alguna obligación esencial permanece `OPEN` o `EVIDENCE_ONLY`.

## 5. Selección y branching

Para cada obligación:

1. intentar primero un resultado directo certificado/literatura plenamente aplicable;
2. preferir una deducción corta o cálculo exacto antes que una ruta computacional costosa;
3. usar numerics exploratorios como scout o falsificador cuando reduzcan incertidumbre;
4. si el subclaim es apto para cierre computacional riguroso, activar `protocols/NUMERICS.md` y fijar explícitamente el estándar de certificación antes de correr código;
5. si una táctica falla, registrar por qué y cambiar de táctica o abrir un subclaim, sin fingir que el claim quedó refutado.

No existe obligación de usar simultáneamente literatura, analítica y computación. Existe obligación de no ocultar ningún hueco esencial.

## 6. Claims sobre familias y cuantificadores fuertes

Un sweep de parámetros, aunque no encuentre contraejemplos, no cubre por sí solo un cuantificador universal.

Para cerrar un claim del tipo

```text
forall p in P: Q(p)
```

una táctica computacional rigurosa debe justificar cobertura de todo `P`, por ejemplo mediante partición intervalar, cota uniforme, enumeración exhaustiva finita o reducción teórica equivalente.

`sampled_region != quantified_domain` salvo prueba explícita de cobertura.

Para `generic`, `open dense`, `maximal`, `sharp`, `iff`, `impossible` o `universal`, aplicar además los gates de fuerza del claim.

## 7. Integración con numerics

Cuando una obligación use computación, declarar `Computation_semantics`:

`exploratory_numeric | falsification_search | corroborative_numeric | symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`

Sólo `symbolic_exact`, `exhaustive_finite`, `validated_numeric` o `rigorous_computer_assisted_proof` pueden cerrar una obligación exacta, y sólo cuando satisfacen el estándar matemático específico del subclaim.

La mera reproducibilidad del programa no demuestra que la salida tenga fuerza de prueba.

## 8. Auditoría

Antes de certificar un target revisar para cada obligación esencial:

```text
Obligation -> tactic -> closure_standard -> artifact -> epistemic_status -> closed?
```

El auditor debe intentar romper tanto la deducción como el puente que convierte una computación en evidencia de nivel prueba.

## 9. Regla de síntesis

La prueba final puede entenderse como un grafo heterogéneo:

```text
TARGET
  <- external theorem
  <- direct lemma
  <- symbolic exact identity
  <- validated numerical bound
  <- certified internal result
```

La heterogeneidad de métodos es válida. La mezcla de niveles epistemológicos sin puente certificado no lo es.
