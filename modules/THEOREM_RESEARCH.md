# Module: THEOREM_RESEARCH

## Activar cuando

Se requiera demostrar, refutar, formular o auditar un lema/teorema o una afirmación matemática exacta.

## Requiere

Protocolos:
- `protocols/PROOF.md`
- `protocols/PROOF_TACTICS.md`
- `protocols/CERTIFICATION.md`
- `protocols/TYPE_NOTATION_GATE.md`
- `protocols/OBJECTIVE_CLOSURE.md` cuando el objetivo pida fuerza/maximalidad/genericidad.
- `protocols/EXACT_WITNESS.md` cuando la prueba dependa de no-anulación/cota estricta/witness.
- `protocols/NUMERICS.md` cuando una obligación use computación material, ya sea como scout, falsificación o cierre riguroso.

Templates:
- `templates/CLAIM_SIGNATURE.md`
- `templates/APPLICABILITY_MATRIX.md`
- `templates/PROOF_OBLIGATION.md` para subclaims/puentes materiales.
- `templates/PROOF_CERTIFICATE.md` sólo después de Certification Gate.
- `templates/COMPUTATION_CERTIFICATE.md` cuando una computación sea esencial.
- `templates/EXACT_WITNESS.md` cuando aplique.

## Obligaciones

- Fijar universo, tipos, dominios, cuantificadores, hipótesis, conclusión y scope.
- Construir grafo de dependencias.
- Para cada dependencia nueva o puente no certificado, declarar `subclaim -> tactic -> closure_standard -> status`.
- Verificar cada resultado externo antes de usarlo.
- No imponer una táctica única a toda la prueba: literatura, deducción directa, simbólico exacto, enumeración exhaustiva, numerics validados y computer-assisted proof pueden coexistir si cada puente está certificado.
- Mantener `NUMERICAL_SCOUT` y evidencia muestral ordinaria como `[N]`/`[C]` salvo puente riguroso.
- Ejecutar ataque adversarial y búsqueda de contraejemplos.
- Reparar con el cambio mínimo o cambiar de táctica sólo en la obligación afectada si falla una vía.
- Ejecutar second review independiente para claims centrales antes de `CERTIFIED`.
- No promover evidencia numérica a prueba exacta sin puente certificado.

## Salida

`statement | hypotheses | proof/refutation status | proof obligations/tactics | dependency audit | exceptions | strongest sustainable result | certification status`.