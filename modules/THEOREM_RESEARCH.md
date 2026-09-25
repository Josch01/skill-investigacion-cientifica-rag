# Module: THEOREM_RESEARCH

## Activar cuando

Se requiera demostrar, refutar, formular o auditar un lema/teorema o una afirmación matemática exacta.

## Requiere

Protocolos:
- `protocols/PROOF.md`
- `protocols/CERTIFICATION.md`
- `protocols/TYPE_NOTATION_GATE.md`
- `protocols/OBJECTIVE_CLOSURE.md` cuando el objetivo pida fuerza/maximalidad/genericidad.
- `protocols/EXACT_WITNESS.md` cuando la prueba dependa de no-anulación/cota estricta/witness.

Templates:
- `templates/CLAIM_SIGNATURE.md`
- `templates/APPLICABILITY_MATRIX.md`
- `templates/PROOF_CERTIFICATE.md` sólo después de Certification Gate.
- `templates/EXACT_WITNESS.md` cuando aplique.

## Obligaciones

- Fijar universo, tipos, dominios, cuantificadores, hipótesis, conclusión y scope.
- Construir grafo de dependencias.
- Verificar cada resultado externo antes de usarlo.
- Ejecutar ataque adversarial y búsqueda de contraejemplos.
- Reparar con el cambio mínimo si falla el target.
- Ejecutar second review independiente para claims centrales antes de `CERTIFIED`.
- No promover evidencia numérica a prueba exacta sin puente certificado.

## Salida

`statement | hypotheses | proof/refutation status | dependency audit | exceptions | strongest sustainable result | certification status`.