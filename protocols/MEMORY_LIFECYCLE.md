# Memory Lifecycle, Compaction & Garbage Collection Protocol

## 1. Propósito

Mantener memoria científica acumulativa sin saturar el contexto activo, degradar la precisión del retrieval ni perder trazabilidad.

Principio:
`COMPACT != DELETE`

El sistema debe poder crecer durante años manteniendo acotado el working set activo.

## 2. Tres niveles de memoria

### HOT
Contiene sólo el estado necesario para el objetivo actual:
- pregunta/objetivo activo;
- objetos canónicos en uso;
- hipótesis vigentes;
- 5–12 nodos científicos relevantes;
- bottleneck actual;
- rutas activas/prometedoras;
- claims/certificados canónicos actualmente necesarios.

### WARM
Conocimiento reusable pero no necesariamente cargado:
- Proof Certificates vigentes;
- lemas certificados;
- resultados numéricos de referencia;
- Evidence Cards relevantes;
- rutas cerradas con resultados reutilizables;
- decisiones metodológicas vigentes.

### ARCHIVE
Historia recuperable pero excluida por defecto del retrieval:
- claims `SUPERSEDED`;
- snapshots históricos;
- versiones antiguas de manuscritos/auditorías;
- rutas fallidas cerradas sin dependencia activa;
- sweeps numéricos antiguos;
- búsquedas viejas ya resumidas;
- logs/raw outputs preservados por reproducibilidad.

## 3. Invariante de memoria activa

Objetivo operativo:
- `MEMORY_CORE`: <= 1200 tokens salvo excepción justificada;
- HOT working set: 5–12 nodos;
- fuentes iniciales: 3–5;
- Case Packet: idealmente < 2500 tokens;
- rutas HOT por objetivo: <= 8; el resto se compacta o archiva;
- para un mismo concepto debe existir un único `CANONICAL_ACTIVE` salvo conflicto científico explícito.

Si se excede un límite, activar `MEMORY_GC` antes de ampliar más el contexto, salvo emergencia científica justificada.

## 4. Identidad canónica y deduplicación

Cada nodo durable debe poder declarar:
`Memory_tier: HOT|WARM|ARCHIVE`
`Canonical_status: CANONICAL_ACTIVE|ALIAS|SUPERSEDED|HISTORICAL`
`Canonical_id:`
`Supersedes:`
`Superseded_by:`

Reglas:
- si CERT-B supersede CERT-A, el índice activo apunta a CERT-B;
- CERT-A permanece recuperable en ARCHIVE;
- aliases semánticos apuntan al canonical id en vez de duplicar contenido;
- dos claims incompatibles no se fusionan: se mantienen ambos y se registra el conflicto.

## 5. Memory GC triggers

Ejecutar compactación cuando ocurra cualquiera:
1. cierre de un Research Objective;
2. `MEMORY_CORE` excede el presupuesto;
3. HOT working set supera 12 nodos;
4. una nueva versión supersede un claim/certificado;
5. existen >= 3 artefactos activos que representan el mismo claim;
6. una ruta cerrada ya produjo certificado/obstrucción reusable;
7. Artifact Consistency detecta snapshots/versiones obsoletas;
8. antes de iniciar un objetivo nuevo si quedan residuos HOT del objetivo anterior;
9. retrieval devuelve repetidamente artefactos superseded/duplicados.

## 6. Compaction procedure

Para cada candidato:
1. identificar la unidad científica durable;
2. conservar statement, hypotheses, scope, status, dependencies, provenance, exceptions y canonical id;
3. generar/actualizar certificado o ledger compacto;
4. preservar prueba completa/raw outputs en fuente interna o archivo;
5. mover estado lógico de HOT -> WARM o ARCHIVE;
6. actualizar MEMORY_INDEX con puntero canónico;
7. actualizar ARCHIVE_INDEX para material histórico;
8. verificar que el nodo puede recuperarse desde su ID;
9. eliminar del CORE narración redundante, nunca hipótesis materiales.

## 7. Qué nunca debe eliminar GC

Sin instrucción explícita del usuario no borrar:
- fuente primaria;
- prueba original necesaria para auditoría;
- datos/raw outputs esenciales para reproducibilidad;
- Evidence Cards que sostienen claims activos;
- certificates vigentes;
- registro de una refutación relevante;
- provenance/hash/version material.

GC cambia nivel y representación activa; no destruye evidencia.

## 8. Route compaction

Una ruta cerrada debe reducirse a:
`Target | Status | Key reason | Reusable result | Obstruction | Source pointer`.

El desarrollo extenso puede quedar en archivo.

Una ruta `FAILED` sin reusable result se archiva por defecto y sólo se recupera para evitar repetirla.

## 9. Numerical compaction

No mantener en HOT grids completos, logs o cientos de ejecuciones.

Conservar en WARM:
- Computation Certificate;
- resumen estadístico/material;
- mejores/peores casos relevantes;
- degeneracies;
- pointers a raw output.

Raw sweeps -> ARCHIVE.

## 10. Search/literature compaction

SEARCH_LEDGER activo conserva sólo:
- query family;
- coverage date;
- closest prior art;
- unresolved gap;
- pointer al detalle.

Resultados irrelevantes y páginas completas no permanecen HOT.

## 11. Retrieval tier policy

Orden:
`HOT -> WARM canonical -> dependency subgraph -> ARCHIVE only on demand -> external refresh`.

No recuperar ARCHIVE por defecto.

ARCHIVE se abre cuando:
- se audita historia/provenance;
- hay conflicto entre versiones;
- el claim activo depende de un antecedente histórico;
- el usuario pide evolución del trabajo;
- se necesita reproducir una ruta anterior.

## 12. Rehydration

Un nodo ARCHIVE puede volver a WARM/HOT si:
- reaparece como dependencia;
- cambia el objetivo;
- un conflicto exige revalidación;
- una versión nueva requiere comparar con el antecedente.

Rehidratar sólo el subgrafo necesario.

## 13. Integrity check after GC

Después de compactar verificar:
- todos los IDs canónicos resolubles;
- no hay dependencia activa apuntando a contenido borrado;
- status y scope preservados;
- aliases no forman ciclos;
- superseded chain termina en un canonical active o histórico explícito;
- `MEMORY_CORE` describe sólo estado actual;
- INDEX no contiene contenido largo.

## 14. Reporte

Usar `templates/MEMORY_GC_REPORT.md` cuando la compactación sea material.

## 15. Regla final

> La memoria científica debe crecer en profundidad histórica, no en tamaño del contexto activo.

## 16. Delegated task artifacts

Para tareas multiagente:
- TASK_PACKET, WORKER_RESULT aceptado y AUDIT_PACKET permanecen WARM mientras sostengan un artefacto activo;
- revisiones rechazadas y salidas intermedias pasan a ARCHIVE;
- la memoria canónica conserva el resultado aceptado y punteros suficientes, no todas las iteraciones;
- los workers no escriben directamente memoria científica canónica como autoridad;
- al cerrar una tarea delegada, compactar sus revisiones intermedias.