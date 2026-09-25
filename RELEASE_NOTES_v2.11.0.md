# Release Notes v2.11.0 — Proof-Obligation Tactic Routing

## Objetivo de la versión

Esta versión formaliza una capacidad antes distribuida entre `PROOF.md`, `NUMERICS.md` y el Research Loop: **cada subclaim u obligación de una demostración puede elegir una táctica distinta, con un estándar explícito de cierre y fuerza epistemológica controlada**.

Principio central:

> Las tácticas son opcionales; las obligaciones lógicas esenciales no.

Una prueba puede combinar literatura, deducción analítica, cálculo simbólico exacto, enumeración finita exhaustiva, numerics validados y pruebas asistidas por computadora sin exigir que todas esas tácticas aparezcan en todos los problemas.

## Cambios principales

### 1. Nuevo protocolo `protocols/PROOF_TACTICS.md`

Introduce routing por obligación de prueba:

```text
proof obligation
    -> candidate tactics
    -> active tactic
    -> closure standard
    -> artifact/certificate
    -> closure class
```

Tácticas:

- `CERTIFIED_INTERNAL_RESULT`
- `EXTERNAL_THEOREM`
- `DIRECT_ANALYTIC`
- `SYMBOLIC_EXACT`
- `EXHAUSTIVE_FINITE_COMPUTATION`
- `VALIDATED_NUMERICS`
- `RIGOROUS_COMPUTER_ASSISTED_PROOF`
- `NUMERICAL_SCOUT`
- `COUNTEREXAMPLE_SEARCH`

El routing es idempotente: una obligación ya registrada conserva su `Obligation_ID`; cambiar de táctica no crea un subclaim duplicado.

### 2. Nuevo template `templates/PROOF_OBLIGATION.md`

Registra subclaim, hipótesis/cuantificadores locales, rol esencial/auxiliar, táctica, estándar de cierre, evidencia/certificados, fallback y clase de cierre:

`OPEN | EVIDENCE_ONLY | CONDITIONAL | RIGOROUSLY_CLOSED | REFUTED`.

### 3. `PROOF.md` permite cierre computacional positivo

La computación puede actuar como scout, falsificador, simbólico exacto, enumeración exhaustiva, numerics validados o computer-assisted proof rigurosa.

Una obligación exacta no puede cerrarse por sweep, residuo pequeño o alta precisión decimal sin un puente matemático riguroso.

### 4. `NUMERICS.md` separa semántica computacional y fuerza de prueba

Taxonomía canónica única:

`exploratory_numeric | falsification_search | corroborative_numeric | symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`.

La reproducibilidad del programa y la suficiencia matemática del certificado son condiciones distintas.

La dirección canónica es acíclica:

```text
PROOF -> PROOF_TACTICS -> NUMERICS -> artifact/certificate -> obligation audit
```

`NUMERICS` no vuelve a enrutar la obligación.

### 5. `COMPUTATION_CERTIFICATE.md` reforzado

Añade `Proof_Obligation_ID`, `Computation_semantics`, puente matemático, cuantificadores cubiertos, región muestreada vs dominio certificado, cobertura/exhaustividad, modelo aritmético, control de redondeo/error, estándar de cierre y condiciones formales de éxito/fallo.

### 6. Research Loop y branching

Una ruta puede contener múltiples tácticas por subclaim. El fallo de una táctica no implica fallo del claim ni refutación; puede activarse otra táctica para la misma obligación.

### 7. Router, Module Selection y Task Packet

Propagan proof-tactic routing, rol computacional, closure methods permitidos y estándar de cómputo riguroso.

### 8. Handoff end-to-end preservado

Tras auditoría de arquitectura se endureció la cadena:

```text
TASK_PACKET
   -> Contract Preservation Check
   -> WORKER_MISSION
   -> WORKER_RESULT
   -> AUDIT_PACKET
```

`WORKER_MISSION` conserva ahora objetos/tipos, hipótesis, scope, definiciones, cuantificadores, éxito/refutación, allowed/forbidden actions, file ownership, proof obligations, `Computation_semantics`, `Closure_standard`, outputs y acceptance criteria.

`WORKER_RESULT` devuelve las obligaciones atendidas, táctica, estándar, evidencia/certificado, claims no demostrados y preguntas abiertas sin autorizar cambios de estatus científico.

`AUDIT_PACKET` audita explícitamente cada obligación y su puente computacional.

### 9. Veredictos y revisiones unificados

Veredictos canónicos únicos:

`ACCEPT | REVISION_REQUIRED | SCIENTIFIC_REOPEN | BLOCKED`.

Se eliminó la etiqueta huérfana `CONTRACT_REVISION_REQUIRED`; todo cambio material de contrato usa `SCIENTIFIC_REOPEN`.

### 10. Objective Closure compatible con computación rigurosa

El gate ya no exige un puente exclusivamente analítico. Claims fuertes pueden cerrarse mediante **puente matemático riguroso** analítico, simbólico exacto, exhaustivo finito o computacional certificado, siempre que cubra los cuantificadores y dominio relevantes.

Un sweep ordinario sigue sin poder demostrar genericidad, universalidad, maximalidad, minimalidad exacta o imposibilidad.

### 11. Memoria/ledgers alineados con v2.11

`RESEARCH_OBJECTIVE`, `EXPERIMENT_RECORD`, `NUMERICAL_LEDGER`, `PROOF_STATE`, `ROUTE_LEDGER` y `ARTIFACT_CONSISTENCY` registran ahora proof obligations, computation semantics, closure standards/classes y certificados materiales donde corresponde.

### 12. Coordinación determinista reforzada

Nuevos schemas:

- `templates/CODEX_PLAN_DONE.json`
- `templates/CODEX_AUDIT_DONE.json`

`WORKER_DONE.json` incluye `mission_hash` y `task_execution_completed`; ya no permite al worker declarar `objective_completed`.

Los prompts de Codex requieren la skill canónica `>= 2.11.0`.

### 13. Validación estática y CI

Nuevo `scripts/validate_skill.py` comprueba:

- versión canónica;
- archivos requeridos;
- referencias internas rotas;
- JSON de coordinación;
- taxonomía `Computation_semantics`;
- veredictos de auditoría;
- campos contractuales de `WORKER_MISSION`;
- dirección Proof Tactics → Numerics;
- reglas de Objective Closure.

`.github/workflows/validate-skill.yml` ejecuta esta validación en `push` y `pull_request`.

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
    -> preservar el contrato al delegar
    -> producir/auditar certificados
    -> propagar fuerza epistemológica
    -> certificar
```

Esto permite pruebas heterogéneas rigurosas sin confundir evidencia numérica exploratoria con demostración matemática y sin perder semántica científica entre Lead, worker y auditor.
