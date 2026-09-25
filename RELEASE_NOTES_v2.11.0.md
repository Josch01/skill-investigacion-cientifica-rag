# Release Notes v2.11.0 — Proof-Obligation Tactic Routing

## Objetivo de la versión

Esta versión formaliza una capacidad que antes estaba distribuida entre `PROOF.md`, `NUMERICS.md` y el Research Loop: **cada subclaim u obligación de una demostración puede elegir una táctica distinta, con un estándar explícito de cierre y fuerza epistemológica controlada**.

Principio central:

> Las tácticas son opcionales; las obligaciones lógicas esenciales no.

Una prueba puede combinar literatura, deducción analítica, cálculo simbólico exacto, enumeración finita exhaustiva, numerics validados y pruebas asistidas por computadora sin exigir que todas esas tácticas aparezcan en todos los problemas.

## Cambios principales

### 1. Nuevo protocolo `protocols/PROOF_TACTICS.md`

Introduce el routing por obligación de prueba:

```text
proof obligation
    -> candidate tactics
    -> active tactic
    -> closure standard
    -> artifact/certificate
    -> epistemic status
```

Tácticas iniciales:

- `CERTIFIED_INTERNAL_RESULT`
- `EXTERNAL_THEOREM`
- `DIRECT_ANALYTIC`
- `SYMBOLIC_EXACT`
- `EXHAUSTIVE_FINITE_COMPUTATION`
- `VALIDATED_NUMERICS`
- `RIGOROUS_COMPUTER_ASSISTED_PROOF`
- `NUMERICAL_SCOUT`
- `COUNTEREXAMPLE_SEARCH`

### 2. Nuevo template `templates/PROOF_OBLIGATION.md`

Permite registrar cada subclaim material con:

- hipótesis y cuantificadores locales;
- rol esencial/auxiliar;
- táctica activa;
- estándar de cierre;
- evidencia/certificados;
- clase de cierre;
- fallback si falla la táctica.

Clases:

`OPEN | EVIDENCE_ONLY | CONDITIONAL | RIGOROUSLY_CLOSED | REFUTED`.

### 3. `PROOF.md` permite cierre computacional positivo

La computación deja de aparecer únicamente como refutación opcional. Puede actuar como:

- scout;
- falsificador;
- cálculo simbólico exacto;
- enumeración exhaustiva;
- numerics validados;
- computer-assisted proof rigurosa.

Una obligación exacta no puede cerrarse por sweep, residuo pequeño o alta precisión decimal sin un puente riguroso.

### 4. `NUMERICS.md` separa semántica computacional y fuerza de prueba

Nueva clasificación:

`exploratory_numeric | falsification_search | corroborative_numeric | symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`.

La reproducibilidad del programa y la suficiencia matemática del certificado se tratan como condiciones distintas.

### 5. `COMPUTATION_CERTIFICATE.md` reforzado

Añade:

- `Proof_Obligation_ID_if_any`;
- `Computation_semantics`;
- `Mathematical_bridge`;
- cuantificadores cubiertos;
- región muestreada vs dominio certificado;
- argumento de cobertura/exhaustividad;
- modelo aritmético;
- control de redondeo/error;
- estándar de cierre;
- condiciones formales de éxito/fallo.

### 6. `RESEARCH_LOOP.md` incorpora cambio de táctica dentro de una ruta

Una ruta puede contener múltiples tácticas por subclaim. El fallo de una táctica no implica automáticamente fallo del claim ni refutación; puede activarse otra táctica para la obligación concreta.

### 7. Router y contratos de delegación

`agents/ROUTER.md`, `templates/MODULE_SELECTION.md` y `templates/TASK_PACKET.md` ahora distinguen:

- si se requiere proof-tactic routing;
- el rol de numerics;
- si se permite cierre computacional riguroso;
- el estándar que debe cumplir un worker antes de que una computación pueda apoyar un claim exacto.

### 8. Certificación

`CERTIFICATION.md` y `PROOF_CERTIFICATE.md` añaden auditoría explícita:

```text
Obligation_ID -> tactic -> closure_standard -> artifact/certificate -> closure_class
```

Una obligación esencial `OPEN` o `EVIDENCE_ONLY` bloquea `CERTIFIED` para un claim exacto.

## Resultado conceptual

La arquitectura pasa de:

```text
hilar resultados
```

a:

```text
construir un grafo de prueba
    -> descomponer en obligaciones
    -> seleccionar táctica por obligación
    -> exigir estándar de cierre
    -> propagar fuerza epistemológica
    -> auditar
    -> certificar
```

Esto permite pruebas heterogéneas rigurosas sin confundir evidencia numérica exploratoria con demostración matemática.