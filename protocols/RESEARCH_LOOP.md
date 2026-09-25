# Goal-Directed Research Loop

## 1. Propósito

Este protocolo gobierna investigaciones cuyo usuario formula un **objetivo científico**, no sólo una pregunta aislada.

Ejemplos:

- determinar si un modelo es estructuralmente identificable;
- determinar si un sistema posee una simetría no trivial;
- demostrar una afirmación usando un paper de partida y literatura relacionada;
- decidir si una propiedad global puede sostenerse;
- establecer o refutar una conjetura;
- encontrar la formulación más fuerte que pueda certificarse.

El sistema no debe detenerse porque falle la primera ruta razonable. Debe aprender del fallo, registrar la obstrucción y escoger la siguiente ruta con mejor valor científico, hasta satisfacer una condición de parada legítima.

---

# 2. Principio de neutralidad del objetivo

Aunque el usuario formule:

> "Demuestra que P."

el objetivo interno debe reformularse como:

> **Determinar rigurosamente el estado de P bajo las definiciones, dominios e hipótesis especificados.**

Por tanto se mantienen dos tracks:

```text
TRACK-PROVE: intentar establecer P.
TRACK-FALSIFY: intentar establecer ¬P, encontrar contraejemplo u obstrucción.
```

No favorecer P por haber sido sugerida por el usuario.

---

# 3. Formalización del Research Objective

Crear primero un registro según `templates/RESEARCH_OBJECTIVE.md`.

Debe especificar:

- claim objetivo P;
- criterio exacto de éxito;
- criterio exacto de refutación;
- dominio y cuantificadores;
- definiciones;
- hipótesis;
- fuente inicial si existe;
- resultados certificados disponibles;
- alcance deseado: local/global, genérico/universal, exacto/asintótico.

Si no existe un criterio verificable de éxito o refutación, reformular antes de continuar.

---

# 4. Theory Scan antes de construir una prueba nueva

Antes de diseñar una cadena larga:

1. revisar el paper o teoría indicada por el usuario;
2. recuperar resultados certificados internos pertinentes;
3. buscar resultados directos en literatura primaria;
4. buscar versiones alternativas del mismo criterio;
5. buscar contraejemplos conocidos y límites de aplicabilidad;
6. registrar la búsqueda en `memory/SEARCH_LEDGER.md`.

Prioridad:

```text
resultado directo existente
    >
resultado certificado + lema corto
    >
cadena corta de literatura
    >
deducción nueva / cálculo exacto corto
    >
computer-assisted proof rigurosa bien acotada
    >
cadena interdisciplinaria larga
    >
exploración numérica abierta
```

No construir una teoría compleja si un resultado ya existente decide el objetivo.

---

# 5. Generación de rutas candidatas

Crear entre 1 y 4 rutas iniciales, no más salvo justificación.

Ejemplos para identificabilidad:

```text
ROUTE-A: álgebra diferencial / eliminación entrada-salida
ROUTE-B: simetrías y fibras observacionales
ROUTE-C: observabilidad / criterios de rango bajo hipótesis adecuadas
ROUTE-D: búsqueda numérica de indistinguibilidad como scout
```

Cada ruta debe declarar:

- objetivo parcial;
- método;
- resultados externos previstos;
- certificados internos reutilizables;
- hipótesis críticas;
- costo/contexto esperado;
- qué resultado produciría si tiene éxito;
- qué información reusable produce si falla.

Registrar cada una en `memory/ROUTE_LEDGER.md`.

Una ruta puede combinar tácticas distintas por subclaim. No exigir uniformidad metodológica cuando el grafo de prueba admita una composición rigurosa.

---

# 6. Priorización de rutas

No es necesario calcular un score numérico, pero ordenar conceptualmente por:

```text
valor esperado de cierre
× fuerza del resultado
÷ costo de recuperación/demostración
```

Preferir:

1. teorema directo plenamente aplicable;
2. certificado interno + pocos puentes;
3. deducción nueva corta o cálculo simbólico exacto;
4. cierre computacional riguroso bien delimitado cuando sea natural;
5. ruta larga interdisciplinaria;
6. exploración numérica amplia.

Una ruta con una hipótesis esencial ya falsa debe cerrarse inmediatamente.

---

# 7. Ejecución de una ruta

Para la ruta seleccionada:

1. recuperar sólo sus dependencias;
2. aplicar `protocols/RAG.md`;
3. crear Evidence Cards;
4. construir matrices de aplicabilidad;
5. aplicar `protocols/PROOF.md`;
6. construir/actualizar obligaciones de prueba y enrutar tácticas con `protocols/PROOF_TACTICS.md` cuando existan subclaims nuevos o puentes no certificados;
7. ejecutar red team;
8. usar `protocols/NUMERICS.md` cuando una obligación requiera scout, falsificación, corroboración o cierre computacional riguroso;
9. registrar el resultado de la ruta.

Estados de ruta:

`PLANNED | ACTIVE | PROMISING | BLOCKED | FAILED | SUCCEEDED | SUPERSEDED`

Estados de obligaciones materiales:

`OPEN | EVIDENCE_ONLY | CONDITIONAL | RIGOROUSLY_CLOSED | REFUTED`.

Una ruta no puede marcarse `SUCCEEDED` para un target exacto si una obligación esencial sigue `OPEN` o `EVIDENCE_ONLY`.

---

# 8. Regla crítica: ruta fallida no implica claim refutado

Si fallan una o varias rutas:

```text
ROUTE-A = FAILED
ROUTE-B = FAILED
ROUTE-C = FAILED
```

no se concluye:

```text
P = REFUTED
```

Sólo puede marcarse `REFUTED` si existe evidencia rigurosa suficiente, por ejemplo:

- contraejemplo matemático;
- construcción explícita incompatible con P;
- teorema cuya conclusión contradice P y aplica plenamente;
- contradicción lógica;
- familia de parámetros/estados indistinguibles demostrada;
- simetría no trivial demostrada que destruye la propiedad reclamada.

Si simplemente no se encontró prueba:

`UNRESOLVED`.

---

# 9. Reparación y branching

Cuando una ruta o táctica falla, clasificar la causa:

```text
A. hipótesis externa no satisfecha
B. puente lógico inexistente
C. resultado sólo local, target global
D. degeneración/caso excepcional
E. contradicción con teoría
F. contraejemplo
G. falta de información
H. costo desproporcionado
I. táctica insuficiente para la fuerza del subclaim
J. certificado computacional sin cobertura/error suficiente
```

Después decidir:

- reparar la misma ruta con el cambio mínimo;
- cambiar de táctica para una obligación concreta;
- debilitar el target;
- crear subobjetivo;
- cambiar de ruta;
- activar track de falsificación;
- detenerse si ya existe una condición de cierre.

Nunca parchear silenciosamente una hipótesis faltante.

---

# 10. Track de falsificación

En paralelo o cuando una ruta de prueba se bloquee, investigar activamente:

- simetrías;
- reparametrizaciones;
- ambigüedades discretas;
- escalamiento;
- permutaciones;
- fibras desconectadas;
- pérdida de rango;
- casos singulares;
- contraejemplos clásicos;
- límites de los teoremas usados.

La numeración puede actuar como **scout**:

```text
[N] patrón sospechoso
   -> [C] conjetura de transformación/obstrucción
      -> análisis simbólico/teórico o validación rigurosa
         -> [D] o [X] si se demuestra/certifica
```

Nunca promover directamente `[N] -> [D]`.

---

# 11. Reutilización de información de rutas fallidas

Una ruta fallida puede producir conocimiento durable:

- hipótesis necesaria;
- caso excepcional;
- referencia útil;
- transformación candidata;
- lema parcial;
- obstrucción;
- resultado local;
- benchmark numérico;
- proof obligation no cerrada y tácticas ya descartadas.

Registrar esos resultados antes de abandonar la ruta.

El objetivo es no repetir caminos muertos y aprovechar resultados parciales.

---

# 12. Condiciones legítimas de parada

## STOP-1 — PROVED / CERTIFIED

P queda demostrado y sólo se certifica después de superar `protocols/CERTIFICATION.md`: dependency propagation, cierre de obligaciones esenciales, second review, computation gate si aplica y alcance cerrado.

## STOP-2 — REFUTED

P queda refutado mediante contraejemplo, contradicción o teoría aplicable.

## STOP-3 — CONDITIONAL

Se demuestra:

```text
H_extra -> P
```

pero una o más hipótesis adicionales no están establecidas para el problema original.

## STOP-4 — PARTIAL / BEST SUSTAINABLE RESULT

El target completo no se cierra, pero sí una versión estrictamente más débil y científicamente útil, por ejemplo:

- local en vez de global;
- genérico en vez de universal;
- subclase de parámetros;
- resultado asintótico;
- necesidad pero no suficiencia.

Debe certificarse sólo la versión realmente demostrada.

## STOP-5 — UNRESOLVED

Después de revisar teoría relevante, ejecutar rutas razonables, cambiar tácticas cuando aporte información nueva y activar falsificación cuando corresponda, no existe prueba ni refutación suficiente.

Debe registrarse:

- rutas intentadas;
- tácticas fallidas en obligaciones esenciales;
- por qué fallaron;
- resultados parciales;
- cuello de botella exacto;
- qué nueva hipótesis, teoría, dato o herramienta podría desbloquearlo.

`UNRESOLVED` es una conclusión científica legítima.

---

# 13. Stop budget contra búsqueda infinita

Por defecto no ejecutar una búsqueda indefinida.

Detener o reformular cuando ocurra cualquiera:

1. todas las rutas de alto valor están bloqueadas por la misma laguna;
2. las nuevas rutas/tácticas sólo repiten dependencias ya fallidas;
3. la literatura recuperada deja de aportar herramientas materialmente distintas;
4. el siguiente paso requiere una hipótesis nueva no sustentada;
5. sólo quedan experimentos numéricos ordinarios incapaces de decidir un claim exacto y no existe ruta plausible de validación rigurosa;
6. el costo aumenta sin reducir la incertidumbre científica.

Antes de detener, intentar al menos una ruta de falsificación si es materialmente distinta.

---

# 14. Salida final del Research Loop

La respuesta debe indicar:

```text
OBJECTIVE:
FINAL_STATUS:
STRONGEST_SUSTAINABLE_RESULT:
SUCCESSFUL_ROUTE:
FAILED_ROUTES_AND_REASONS:
PROOF_OBLIGATIONS_SUMMARY:
CERTIFIED_DEPENDENCIES:
NEW_CERTIFICATES:
REFUTATION_EVIDENCE:
NUMERICAL_EVIDENCE:
RIGOROUS_COMPUTATION_IF_ANY:
UNRESOLVED_GAP:
NEXT_HIGHEST_VALUE_STEP:
```

No es necesario mostrar toda la exploración interna; sí las decisiones científicas que cambian la conclusión.

---

# 15. Integración con los demás protocolos

Este archivo es un **orquestador**, no sustituye:

- `RAG.md` para recuperación;
- `PROOF.md` para cada demostración;
- `PROOF_TACTICS.md` para seleccionar cómo cerrar cada obligación;
- `NUMERICS.md` para computación;
- `NOVELTY.md` para contribución;
- `AUDIT.md` para revisión;
- Proof Certificates para herencia.

Flujo principal:

```text
RESEARCH OBJECTIVE
        ↓
THEORY SCAN
        ↓
ROUTE GENERATION
        ↓
BEST ROUTE
        ↓
RAG → PROOF GRAPH → OBLIGATION/Tactic ROUTING
        ↓
ANALYTIC / LITERATURE / SYMBOLIC / RIGOROUS COMPUTATION / SCOUT
        ↓
RED TEAM → CERTIFICATION GATE
        ↓
SUCCEED? ── yes ──> CERTIFY
   │
   no
   ↓
DIAGNOSE FAILURE
   ↓
FALSIFY / REPAIR / RETACTIC / NEXT ROUTE
   ↓
repeat
   ↓
PROVED | REFUTED | CONDITIONAL | PARTIAL | UNRESOLVED
```

---

# 16. Revalidación de inconsistencias del grafo

Si se detecta un caso donde un claim hijo aparece más fuerte que una dependencia:

1. NO degradar ni confirmar automáticamente;
2. reconstruir la dependencia exacta;
3. preguntar si el hijo necesita realmente toda la proposición padre o sólo una dirección más débil;
4. intentar una prueba independiente de esa dirección;
5. si existe, corregir el grafo y certificar el hijo por la ruta independiente;
6. si no existe, heredar las condiciones del padre;
7. si tampoco pueden satisfacerse, abrir rutas de reparación, cambio de táctica o falsificación;
8. finalizar con `CERTIFIED | CONDITIONAL | PARTIAL | REFUTED | UNRESOLVED`.

Esto permite mejorar o refutar una afirmación que no supera el certificado sin forzar un resultado.

---

# 17. Objective Closure Gate

Antes del status final del Research Loop aplicar `protocols/OBJECTIVE_CLOSURE.md`.

Especialmente cuando se solicita `broadest`, `maximal`, `strongest`, `generic`, `universal`, `sharp`, `minimal`, `only if` o `exact boundary`.

Procedimiento:
1. recuperar el Research Objective original;
2. comparar target vs strongest sustainable result;
3. detectar parámetros/términos eliminados durante las rutas;
4. listar superfamilias naturales no exploradas;
5. comprobar que un éxito particular no haya activado la first-success fallacy;
6. separar status del claim y status de cierre del objetivo;
7. crear `templates/OBJECTIVE_CLOSURE.md`.

Si se pidió la familia más amplia y sólo se probó una subfamilia, la salida correcta es `PARTIAL_USEFUL` o `OPEN_SCOPE_GAP`, incluso si el teorema de esa subfamilia está `CERTIFIED`.

Si un claim de genericidad depende de numeración sin testigo analítico exacto o certificado riguroso equivalente, mantenerlo como conjetura/evidencia numérica y continuar una ruta de cierre o cerrar como `PARTIAL`.

Si se reclama maximalidad pero sólo se mostró una obstrucción para una estrategia concreta, reclasificarla como `METHOD_SPECIFIC_BOUNDARY` y mantener abierto el objetivo de maximalidad.

# 18. Exact witness and global state closure

Antes de STOP final:
1. si un puente exacto usa no-anulación, ejecutar Exact Witness Gate;
2. si hay múltiples artefactos modificados, ejecutar Artifact Consistency Gate;
3. comprobar que ninguna obligación esencial siga `OPEN` o `EVIDENCE_ONLY` para un target exacto;
4. comprobar que ningún item explícito del success criterion siga simultáneamente listado como `unexplored`;
5. comprobar second review explícito de cada claim central nuevo;
6. sólo entonces emitir el Objective Closure Status.

`CLOSED_EXACTLY` requiere scope completion, no sólo que los claims actualmente elegidos sean correctos.