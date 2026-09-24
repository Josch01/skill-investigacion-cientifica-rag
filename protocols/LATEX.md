# Protocolo de LaTeX científico

Generar LaTeX sólo cuando el usuario lo solicite.

## Reglas

- preservar notación del manuscrito salvo inconsistencia;
- declarar espacios, dominios y codominios;
- declarar cuantificadores;
- declarar regularidad;
- separar Definition/Lemma/Proposition/Theorem/Corollary/Conjecture;
- citar resultados externos;
- no inventar bibliografía;
- no fortalecer claims;
- no ocultar pasos con "obviamente" o "claramente";
- indicar alcance local/global y genérico/universal;
- definir convenciones que afecten el resultado;
- separar evidencia numérica de prueba.

## Reutilización de resultados certificados

Si se usa un resultado interno certificado:

- citar su ID interno durante el trabajo;
- en el manuscrito final convertirlo en referencia al lema/teorema previo correspondiente;
- no repetir su prueba salvo que el documento lo requiera.

## Bibliografía

Una entrada bibliográfica entra al `.bib` sólo si fue verificada.


## Integración con edición científica v2.5

Antes de editar LaTeX que contenga claims ya verificados/certificados aplicar `protocols/MANUSCRIPT_EDIT.md`.

Para claims centrales:
- usar `memory/SYMBOL_TABLE.md`;
- fijar `templates/CLAIM_SIGNATURE.md`;
- aplicar `protocols/TYPE_NOTATION_GATE.md`;
- comparar contra la fuente normativa mediante `templates/SEMANTIC_DIFF.md`.

La compilación LaTeX es un gate sintáctico/editorial, no una prueba científica.

Un claim `CERTIFIED` puede estar mal renderizado. En ese caso conservar el certificado y marcar el artefacto `SEMANTIC_MISMATCH` hasta reparar el texto.