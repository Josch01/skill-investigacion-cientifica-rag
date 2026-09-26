# Manuscript Audit Coverage Gate

## 1. Propósito

Evitar auditorías "completas" que sólo inventarían el manuscrito o rellenan plantillas sin revisar materialmente cada objeto científico.

Este gate se activa cuando el usuario solicita una auditoría completa, integral o claim-by-claim de un manuscrito, tesis, preprint o paper.

## 2. Inventario canónico

Antes de auditar pruebas, extraer y numerar al menos:

- assumptions;
- definitions;
- lemmas;
- propositions;
- theorems;
- corollaries;
- claims de genericidad, minimalidad, sharpness, maximalidad, novedad o imposibilidad;
- claims computacionales que sostengan conclusiones científicas.

Registrar:

`N_FORMAL_OBJECTS`
`N_CENTRAL_CLAIMS`
`N_NUMERICAL_CLAIMS`
`N_LITERATURE_CLAIMS`

El inventario es la fuente de cobertura. Está prohibido reducir silenciosamente el scope.

## 3. Semántica por tipo de objeto

### ASSUMPTION

No se "demuestra". Auditar:
- enunciado exacto;
- tipo/dominio;
- consistencia;
- compatibilidad con el resto;
- descendientes que dependen de ella.

Status recomendado:
`EXPLICIT_HYPOTHESIS | INCONSISTENT | NEEDS_CLARIFICATION`.

### DEFINITION

No recibe proof status. Auditar:
- tipado;
- no circularidad;
- consistencia de notación;
- compatibilidad con usos posteriores.

Status recomendado:
`WELL_DEFINED | TYPE_AMBIGUITY | CIRCULAR | INCONSISTENT`.

### LEMMA / PROPOSITION / THEOREM / COROLLARY

Exigir:
- statement exacto;
- hipótesis;
- cuantificadores;
- dependencias concretas;
- proof obligations específicas;
- reconstrucción de al menos los pasos críticos;
- counterexample/adversarial attempt;
- second review cuando sea central o se pretenda certificar.

## 4. Invariantes de cobertura

Para una auditoría completa:

`AUDITED_FORMAL_OBJECTS = N_FORMAL_OBJECTS`

Toda exclusión debe declarar:
`Excluded_ID -> reason -> user_scope_basis`.

Para claims matemáticos centrales:

`CENTRAL_CLAIMS_WITH_SPECIFIC_PROOF_STATE = N_CENTRAL_CLAIMS`

No cuenta como específico:
- "standard assumptions";
- "previous results";
- "show rigor";
- "attempted refutation";
- texto idéntico copiado entre claims sin adaptación matemática.

## 5. Coverage failure

Bloquear `AUDIT_COMPLETE` si ocurre cualquiera:

- inventario incompleto;
- objeto formal sin registro;
- claim central con hipótesis/dependencias genéricas;
- definition tratada como theorem;
- assumption marcada REFUTED por no estar demostrada;
- second review requerido pero ausente;
- dependency graph incompleto sin justificación.

Salida:
`AUDIT_COVERAGE_STATUS = PASS | PARTIAL | FAIL`.

## 6. Regla final

> La existencia de un archivo por claim no demuestra cobertura; cada registro debe contener información específica del objeto auditado.
