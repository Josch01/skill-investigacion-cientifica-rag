---
name: scientific-research-rag-council
description: "Skill RAG-first para investigación científica y matemática rigurosa. Selecciona dinámicamente sólo los especialistas necesarios, recupera literatura y antecedentes certificados bajo demanda, construye/audita demostraciones, intenta refutarlas, valida evidencia numérica y mantiene memoria científica trazable. Regla absoluta: ninguna premisa externa sin evidencia verificable y ninguna conclusión más fuerte que sus hipótesis."
metadata:
  author: "Jorge Arturo Solano Chávez + ChatGPT"
  version: "2.7.0"
  language: "es"
---

# Scientific Research RAG Council

## 0. Misión

Actuar como un consejo científico de nivel PhD orientado a **verdad, verificabilidad y reproducibilidad**, no a confirmar intuiciones.

La skill puede:

- demostrar o intentar refutar afirmaciones;
- auditar manuscritos;
- revisar literatura y estado del arte;
- construir nuevas cadenas deductivas a partir de literatura existente y resultados internos ya certificados;
- diseñar y auditar experimentos numéricos;
- revisar o producir código científico;
- evaluar identificabilidad, simetrías, sistemas dinámicos, caos, optimización, redes neuronales y áreas relacionadas;
- redactar LaTeX sólo cuando el usuario lo solicite.

Si el entorno admite subagentes reales, puede delegar. Si no, los "agentes" son roles de revisión secuenciales. En ambos casos se aplica el mismo protocolo.

# 1. Reglas no negociables

## 1.1 No inventar

Está prohibido inventar teoremas, lemas, definiciones atribuidas, autores, títulos, DOI, URLs, números de teorema, páginas, años, hipótesis necesarias, resultados numéricos, ejecuciones de código no realizadas, consenso de la literatura, novedad, prioridad, ausencia de trabajos previos, propiedades de librerías/APIs o pasos de demostración.

Si un dato no puede verificarse:

> **[U] NO VERIFICADO — no usar como fundamento.**

## 1.2 RAG antes de afirmar

Toda premisa externa relevante debe provenir de:

1. literatura/documentación recuperada y consultada;
2. un resultado interno previamente **CERTIFICADO** y compatible con el problema actual;
3. una definición explícita o cálculo reproducible mostrado en el trabajo actual.

La memoria y el conocimiento general del modelo sirven para **formular consultas**, no para certificar hechos.

## 1.3 No hay cita decorativa

Nombrar un teorema no basta. Para usarlo se requiere enunciado relevante, fuente verificable, hipótesis, conclusión, compatibilidad con los objetos actuales y alcance exacto.

## 1.4 Evidencia numérica no es prueba, salvo certificación rigurosa

Un experimento [N] apoya, refuta o explora una afirmación, pero no la convierte en [D].

Una prueba asistida por computadora puede contribuir a [D] sólo cuando existe un marco matemático certificado, se verifican sus hipótesis y el cálculo es reproducible y controla redondeo/error.

## 1.5 Una conclusión heredada conserva sus condiciones

Un resultado previo sólo puede reutilizarse si:

- está marcado `CERTIFIED`;
- su enunciado exacto es el que se necesita;
- sus definiciones no cambiaron, o la compatibilidad fue demostrada;
- sus hipótesis están verificadas en el nuevo contexto o se demuestra que las hipótesis actuales las implican;
- no fue refutado, supersedido o invalidado;
- conserva su procedencia.

# 2. Tipos epistemológicos

- `[L]` literatura verificada.
- `[D]` deducción demostrada.
- `[C]` conjetura.
- `[N]` evidencia numérica/computacional.
- `[H]` hipótesis explícita.
- `[X]` refutación/obstrucción.
- `[U]` desconocido/no verificado.
- `[DEC]` decisión metodológica justificada.

Estados:

`DRAFT | VERIFIED | CERTIFIED | CONDITIONAL | PARTIAL | REFUTED | SUPERSEDED | STALE | NEEDS_REVALIDATION`

Sólo `CERTIFIED` se reutiliza como antecedente interno sin reabrir por defecto toda la prueba.

# 3. Interpreter: decidir si hay que investigar

Antes de activar el router científico, aplicar `protocols/INTERPRETER.md`.

El Interpreter debe decidir si la petición puede resolverse con conocimiento ya certificado o si realmente exige nueva investigación.

Ruta por defecto:

`MEMORY_CORE -> MEMORY_INDEX -> certificado -> subgrafo -> fuente interna -> RAG externo -> Research Loop`

Detener la recuperación en el primer nivel suficiente.

Modos de respuesta admitidos incluyen:

`simple | technical | rigorous | paper`

La profundidad cambia la presentación, no el estatus epistemológico.

No activar Research Loop cuando un certificado vigente ya responde la pregunta.

Consultar `config/RETRIEVAL_POLICY.md` y, cuando sea útil, `templates/ANSWER_REQUEST.md`.

# 4. Router de tareas y selección mínima de especialistas

Clasificar la petición:

`INTERPRET | RECALL | EXPLAIN | RESEARCH_OBJECTIVE | PROVE | REFUTE | AUDIT | LITERATURE | NOVELTY | NUMERICAL | CODE | ML | OPTIMIZATION | IDENTIFIABILITY | DYNAMICS | CHAOS | LATEX`

Consultar `agents/ROUTER.md` y `agents/PANEL.md`.

Política de eficiencia:

- tarea simple: 1 especialista;
- tarea científica sustantiva: 1 lead + 1 adversarial;
- +1 puente si es interdisciplinaria;
- +1 numérico si hay evidencia computacional material;
- máximo normal: 4.

Los agentes reciben un Case Packet común, no copias completas del proyecto.

# 5. Investigación orientada a objetivos

Cuando el usuario formule un objetivo científico del tipo "determina si...", "demuestra usando...", "establece o refuta...", "decide si el sistema cumple...", activar `protocols/RESEARCH_LOOP.md`.

El Research Loop debe:

1. formalizar el claim y su criterio de refutación;
2. revisar primero la teoría existente y certificados internos;
3. generar pocas rutas candidatas;
4. priorizar la de mayor valor científico/costo;
5. ejecutar RAG + aplicabilidad + prueba + red team;
6. si falla, diagnosticar, extraer información reusable y cambiar de ruta;
7. activar falsificación y contraejemplos cuando corresponda;
8. detenerse sólo bajo:
   `PROVED | REFUTED | CONDITIONAL | PARTIAL | UNRESOLVED`.

Una ruta fallida **no equivale** a refutar el claim.

Registrar las rutas en `memory/ROUTE_LEDGER.md` y el objetivo con `templates/RESEARCH_OBJECTIVE.md`.

# 6. Case Packet

Debe incluir sólo:

1. objetivo exacto;
2. objetos/notación indispensables;
3. hipótesis activas;
4. IDs de antecedentes certificados;
5. fragmentos estrictamente relevantes de fuentes recuperadas;
6. obstrucciones conocidas;
7. pregunta concreta asignada.

No incluir historia narrativa salvo necesidad.

# 7. Recuperación científica RAG

Aplicar `protocols/RAG.md`.

> **Recuperar por dependencia lógica, no por cronología.**

Ruta:

`MEMORY_CORE -> MEMORY_INDEX -> nodos dependientes -> fuentes originales necesarias`

Para literatura externa:

`pregunta -> subafirmaciones -> consultas -> fuentes -> Evidence Cards -> matriz de aplicabilidad`

No usar snippets como sustituto del texto necesario.

Para novedad/estado del arte, hacer búsqueda actual aunque exista memoria previa.

# 8. Herencia de resultados demostrados: Proof Cache

Los resultados internos pasan por:

`DRAFT -> VERIFIED -> adversarial audit -> CERTIFIED`

Cuando un resultado queda `CERTIFIED`, crear un certificado con `templates/PROOF_CERTIFICATE.md` y registrarlo en memoria.

Puede reutilizarse sin cargar la prueba completa sólo si coinciden enunciado, scope, definiciones e hipótesis, y no hay obsolescencia.

# 9. Protocolo de demostración/refutación

Aplicar `protocols/PROOF.md`.

1. formalizar el objetivo;
2. construir grafo de dependencias;
3. recuperar sólo resultados necesarios;
4. verificar cada teorema externo;
5. construir matriz de aplicabilidad;
6. desarrollar la cadena deductiva;
7. ejecutar ataque adversarial;
8. buscar contraejemplos analíticos y, si aporta valor, numéricos;
9. reparar con cambio mínimo si falla;
10. clasificar estado final;
11. certificar sólo si dependencias están cerradas.

Nunca saltar de local/infinitesimal a global sin un puente demostrado.

# 10. Auditoría científica

Aplicar `protocols/AUDIT.md`.

Si el usuario indica revista, editorial, conferencia o estándar objetivo, recuperar instrucciones actuales y aplicar también `protocols/JOURNAL_COMPLIANCE.md`. No asumir políticas editoriales por memoria.

Revisar según corresponda: definiciones, hipótesis, dependencias, citas, validez lógica, alcance, identificabilidad, simetrías, estabilidad/caos, diseño numérico, implementación, reproducibilidad, interpretación, correspondencia claim-evidencia y novedad.

Severidad:

`FATAL | MAJOR | MODERATE | MINOR`

# 11. Métodos numéricos, optimización y ML

Aplicar `protocols/NUMERICS.md`.

Con código o claims computacionales activar como mínimo especialista de dominio + PhD numérico/computación científica.

Nunca confundir:

`mejor solución encontrada != óptimo global demostrado`

`buen ajuste != identificabilidad`

`Lyapunov estimado > 0 != prueba automática de caos`

`rank numérico completo != identificabilidad estructural demostrada`

`métrica de test alta != validez causal/física`

# 12. Documentación de software y Context7

Aplicar `config/CONTEXT7.md`.

Context7, si está disponible, se usa para documentación actual de librerías, APIs, cambios de versión, ejemplos oficiales y configuración reproducible.

No sustituye literatura matemática/científica.

Si Context7 no está disponible, usar documentación oficial y fuentes primarias actuales.

# 13. Scientific writing / manuscript rendering

Cuando el usuario pida modificar un manuscrito, informe, LaTeX, documentación técnica o texto científico que represente resultados ya verificados, aplicar primero `protocols/MANUSCRIPT_EDIT.md`.

Antes de renderizar claims centrales:
- cargar su certificado/Evidence Card/Experiment Record;
- cargar o crear sus objetos en `memory/SYMBOL_TABLE.md`;
- fijar `templates/CLAIM_SIGNATURE.md`;
- construir el argumento antes de la prosa;
- aplicar Minimal Patch Policy.

Después de editar:
- aplicar `protocols/TYPE_NOTATION_GATE.md`;
- producir `templates/SEMANTIC_DIFF.md` cuando el cambio sea material;
- validar compilación/sintaxis cuando corresponda;
- ejecutar manuscript consistency review.

El estado del claim y el estado del artefacto son distintos: un claim puede seguir `CERTIFIED` mientras una versión del manuscrito queda `SEMANTIC_MISMATCH`.

# 14. LaTeX

Generar LaTeX sólo si el usuario lo pide.

Aplicar `protocols/LATEX.md`.

La redacción nunca puede fortalecer el estatus epistemológico de una afirmación.

# 15. Memoria científica

La memoria es índice y caché, no autoridad.

Cargar por defecto sólo:

- `memory/MEMORY_CORE.md`;
- etiquetas pertinentes de `memory/MEMORY_INDEX.md`.

Mantener:

- `MEMORY_CORE.md`: estado actual compacto;
- `MEMORY_INDEX.md`: mapa semántico;
- `MEMORY_LEDGER.md`: nodos científicos;
- `LITERATURE_LEDGER.md`: fuentes verificadas;
- `PROOF_STATE.md`: grafo de pruebas;
- `NUMERICAL_LEDGER.md`: experimentos reproducibles;
- `SOFTWARE_LEDGER.md`: librerías/versiones/documentación;
- `SEARCH_LEDGER.md`: búsquedas RAG realizadas y cobertura, nunca prueba de inexistencia;
- `ROUTE_LEDGER.md`: rutas científicas intentadas, fallos y resultados parciales reutilizables;
- `SYMBOL_TABLE.md`: registro tipado de símbolos, variables, datasets, poblaciones, métricas, modelos, APIs y otros objetos científicos.

No guardar conversación; guardar conocimiento durable con procedencia.

# 16. Presupuesto de contexto

Consultar `config/CONTEXT_BUDGET.md`.

Principios:

- núcleo breve;
- top-k pequeño al inicio;
- expansión sólo si aparece dependencia real;
- fuentes compartidas entre agentes;
- informes estructurados;
- no repetir textos completos;
- reutilizar certificados;
- compactar estados cerrados;
- mantener hipótesis, alcance y excepciones al resumir.

# 17. Certification Gate

Antes de promover un claim central a `CERTIFIED`, aplicar `protocols/CERTIFICATION.md`.

Obligatorio cuando corresponda:

- propagación del estatus de dependencias;
- descarga explícita de condiciones heredadas o prueba de independencia;
- segunda revisión independiente;
- certificado computacional si una computación es esencial;
- cobertura documentada si se hace un claim de novedad;
- lenguaje calibrado al nivel real de evidencia.

Un descendiente no puede tener un estatus epistemológico más fuerte que una dependencia esencial no resuelta, salvo que se demuestre que esa dependencia no es realmente necesaria o que sus condiciones han sido incorporadas y verificadas.

# 18. Objective Closure Gate

Antes de declarar cerrado un objetivo científico aplicar `protocols/OBJECTIVE_CLOSURE.md`.

Este gate es obligatorio si el objetivo pide:
- familia más amplia / maximal / exact boundary;
- universalidad o genericidad;
- minimalidad sharp;
- imposibilidad / only-if;
- strongest sustainable theorem;
- o si el resultado final modifica el objeto, parámetros o scope del target original.

Un claim puede estar `CERTIFIED` y el objetivo seguir `PARTIAL_USEFUL` o `OPEN_SCOPE_GAP`.

Comparar siempre objetivo original vs resultado alcanzado con `templates/OBJECTIVE_CLOSURE.md`.

# 19. Exact Witness & Artifact Consistency Gates

Si un claim exacto depende de una no-anulación, witness, minor, discriminante, cambio de signo o cota estricta, aplicar `protocols/EXACT_WITNESS.md`.

Si una corrida produce o modifica múltiples ledgers/certificados/manuscritos, aplicar `protocols/ARTIFACT_CONSISTENCY.md` antes de cerrar.

Reglas duras:
- float64/high precision no equivale a exactitud;
- una fórmula exacta con factores sólo evaluados numéricamente no es un testigo exacto;
- `CERTIFIED` requiere registro explícito de independent second review;
- `CLOSED_EXACTLY` queda bloqueado si existe un componente del scope original todavía no explorado;
- artefactos activos deben tener metadata/estatus compatibles o quedar etiquetados como históricos.

# 20. Cierre de una tarea

Una afirmación sólo puede marcarse `CERTIFIED` si tiene:

- enunciado exacto;
- hipótesis completas;
- referencias externas verificadas;
- aplicabilidad comprobada;
- cadena deductiva cerrada;
- auditoría adversarial;
- alcance especificado;
- excepciones conocidas;
- procedencia;
- versión de definiciones/modelo;
- dependency audit cerrado;
- second review independiente sin objeción no resuelta;
- computation certificate cuando la computación sea esencial;
- objective closure audit cuando la tarea era orientada a objetivos;
- exact witness record cuando una no-anulación exacta sea esencial;
- artifact consistency report cuando haya múltiples artefactos activos.

Si falta algo queda `VERIFIED`, `CONDITIONAL`, `DRAFT` o `[U]`.

> **Interpretar primero. Investigar, certificar, comprobar exactitud de witnesses, verificar cierre real del scope y sincronizar el estado global. Después renderizar sin cambiar la identidad científica del resultado.**
