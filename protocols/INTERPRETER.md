# Scientific Answer Interpreter

## 1. Propósito

Decide cómo responder cuando el proyecto ya contiene memoria, resultados certificados, grafos de dependencias, literatura verificada o rutas cerradas.

Principio: pregunta -> interpretar intención -> recuperar el mínimo contexto suficiente -> comprobar si ya existe respuesta certificada -> ampliar sólo si falta una dependencia -> investigar de nuevo sólo si hace falta -> adaptar profundidad y formato.

El Interpreter no modifica el estatus epistemológico de los resultados.

## 2. Distinción fundamental

RESOLVER != RECORDAR != EXPLICAR != ACTUALIZAR.

- Resolver: Research Loop, Proof, RAG, Numerics, etc.
- Recordar: memoria/certificados existentes.
- Explicar: traduce resultados existentes al nivel solicitado.
- Actualizar: vuelve a fuentes externas cuando el claim requiere información nueva o vigente.

Una pregunta explicativa no debe activar automáticamente una nueva investigación.

## 3. Clasificación de intención

RECALL_RESULT | EXPLAIN_SIMPLE | EXPLAIN_TECHNICAL | EXPLAIN_RIGOROUS | EXPLAIN_PAPER | SUMMARIZE | COMPARE | LIST_ASSUMPTIONS | LIST_LIMITATIONS | SHOW_PROOF | SHOW_DEPENDENCIES | WHY_TRUE | WHY_FALSE | WHAT_REMAINS_OPEN | NEXT_STEP | TEACH | REFRESH_EVIDENCE | RESEARCH_NEW

Si el usuario especifica nivel, respetarlo. Si no, elegir el nivel mínimo suficiente.

## 4. Niveles de profundidad

### SIMPLE
Comprensión conceptual, poca notación, analogías sólo si no deforman el resultado y sin omitir excepciones esenciales.

### TECHNICAL
Discusión científica compacta con notación relevante, hipótesis principales, resultado exacto, limitaciones y referencias/certificados pertinentes.

### RIGOROUS
Definiciones, cuantificadores, hipótesis, alcance, dependencias, certificados, fuentes y distinciones local/global, genérico/universal, exacto/numérico.

### PAPER
Formulación apta para manuscrito. Sólo si el usuario la solicita; aplicar LATEX.md si pide LaTeX.

## 5. Escalera de recuperación

Aplicar config/RETRIEVAL_POLICY.md.

LEVEL-0: MEMORY_CORE + MEMORY_INDEX.
LEVEL-1: certificado o nodo exacto.
LEVEL-2: dependencias directas del grafo.
LEVEL-3: fuente interna original o ledger detallado.
LEVEL-4: RAG externo / Context7 sólo si falta evidencia o se requiere actualización.
LEVEL-5: Research Loop sólo si la pregunta abre un problema nuevo.

Detener la expansión en el primer nivel que permita una respuesta fiel.

## 6. Regla de suficiencia

Antes de recuperar más contexto preguntar: ¿la evidencia ya recuperada basta para responder exactamente lo pedido sin añadir una afirmación nueva?

Si sí: STOP RETRIEVAL.

## 7. Uso de Proof Certificates

Un certificado válido puede responder qué se demostró, bajo qué hipótesis, con qué alcance, de qué depende, qué excepciones tiene y por qué puede reutilizarse.

No cargar la prueba completa salvo que el usuario la pida, se cuestione un paso, haya incompatibilidad, el certificado esté stale/superseded o falte un detalle esencial.

## 8. Uso del grafo

Para preguntas causales o de procedencia recuperar sólo el subgrafo pertinente. Ejemplo: CERT-D-021 -> H-004 -> X-007 -> REF-011.

No reconstruir todo el proyecto.

## 9. Cuándo refrescar fuentes externas

Activar REFRESH_EVIDENCE si se pregunta por lo más reciente, estado del arte, novedad, políticas/software cambiantes, si una fuente es parcial/stale, si el usuario pide revalidar o si el nuevo uso cambia el alcance.

No refrescar por rutina un teorema matemático ya verificado si el mismo claim y las mismas hipótesis siguen vigentes.

## 10. Cuándo abrir Research Loop

Activar RESEARCH_NEW sólo si no existe resultado suficiente en memoria, la pregunta exige un claim nuevo, se quiere extender un resultado más allá de su scope, hay contradicción real entre antecedentes o se pide demostrar/refutar algo aún no cerrado.

## 11. Regla anti-alucinación en explicación

El Interpreter no rellena huecos narrativamente. Nunca inferir local->global, conditional->unconditional, generic->universal o numerical->exact.

Si sólo existe un certificado local y preguntan si es global, responder que no está certificado globalmente; abrir Research Loop sólo si se quiere decidirlo.

## 12. Formatos de respuesta

Puede producir, según la petición: resultado + significado + hipótesis + limitaciones + fuente; lista de hipótesis; comparación; estado de investigación; dependencias; prueba; qué sigue.

No imponer una plantilla larga si una respuesta natural más corta basta.

## 13. Profundidad cambia presentación, no verdad

SIMPLE y RIGOROUS deben corresponder al mismo resultado epistemológico; sólo cambia la forma de explicarlo.

## 14. Política de citas

Si basta un certificado interno y el usuario no pide bibliografía, responder con el resultado interno de forma compacta. Si pide fuente original, rigor documental o publicación, seguir el certificado hasta LITERATURE_LEDGER y recuperar la fuente primaria necesaria.

## 15. Salida interna

INTENT | DEPTH | QUESTION_SCOPE | MEMORY_TAGS | CERTIFICATES | GRAPH_NODES | NEEDS_INTERNAL_SOURCE | NEEDS_EXTERNAL_REFRESH | NEEDS_RESEARCH_LOOP | OUTPUT_FORMAT | SUFFICIENCY_STATUS.

## 16. Principio final

Responder desde conocimiento certificado cuando ya existe; recuperar sólo el subgrafo necesario; investigar de nuevo únicamente cuando la pregunta realmente excede lo ya establecido.