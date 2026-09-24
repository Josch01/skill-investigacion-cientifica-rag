# Scientific Manuscript Edit Protocol

## 1. Propósito

Controlar la transformación de conocimiento científico ya verificado/certificado en manuscritos, informes, LaTeX, documentación técnica, código comentado o material de publicación sin introducir errores nuevos.

Principio central:
`CERTIFIED KNOWLEDGE -> STRUCTURED CLAIM -> MINIMAL PATCH -> SEMANTIC CHECK -> ARTIFACT READY`

El editor puede cambiar redacción, organización y presentación. No puede cambiar silenciosamente objetos, hipótesis, dominios, alcance, dependencias, métricas, poblaciones, versiones ni estatus epistemológico.

## 2. Aplicabilidad general

Este protocolo aplica a:
- matemática: símbolos, espacios, mapas, teoremas, cuantificadores;
- física/ingeniería: variables, unidades, modelos, condiciones iniciales/frontera;
- epidemiología/estadística: población, muestra, outcome, covariables, estimandos, intervalos, cohortes;
- ML: splits, métricas, arquitectura, datasets, seeds, hyperparameters;
- optimización: objetivo, restricciones, dominio, best-found vs optimum;
- software: APIs, tipos, versiones, contratos, parámetros;
- ciencia experimental: instrumentos, condiciones, réplicas, unidades, calibración;
- revisiones bibliográficas: claim, población/objeto, periodo, fuente, alcance.

## 3. Fuente de verdad

Antes de editar, identificar el artefacto normativo:
- Proof Certificate;
- Claim Signature;
- Experiment/Computation Certificate;
- Evidence Card;
- protocolo/resultado certificado;
- decisión metodológica verificada.

El manuscrito es una representación de ese conocimiento, no su autoridad.

## 4. Pre-edit gate

Antes de tocar el texto:
1. cargar el claim/certificado exacto;
2. cargar `memory/SYMBOL_TABLE.md` o crear las entradas necesarias;
3. crear/actualizar `templates/CLAIM_SIGNATURE.md` para claims centrales;
4. fijar hipótesis, scope, objetos y dependencias;
5. construir un proof/argument skeleton con una razón por cada transición no trivial;
6. registrar el patch mínimo necesario;
7. resolver cualquier objeto o término ambiguo antes de redactar.

Si falta cualquiera de estos elementos materiales, no reescribir libremente.

## 5. Minimal Patch Policy

Preferir el menor cambio que restaure corrección:
- insertar definición;
- añadir hipótesis faltante;
- reemplazar una dependencia;
- expandir un paso lógico;
- corregir scope;
- renombrar símbolo de forma consistente.

No reescribir una sección completa si bastan cambios locales, salvo que la estructura sea intrínsecamente inconsistente.

## 6. Argument graph before prose

Para cualquier prueba/argumento central, representar primero:
`NODE -> [justification/dependency] -> NODE`

Ejemplo genérico:
`observations equal -> [factorization] -> reduced observations equal -> [reduced uniqueness] -> reduced parameters equal -> [exact reduction] -> same orbit`.

Cada flecha debe tener una justificación registrada. El editor no puede colapsar varias flechas en una frase si al hacerlo atribuye la conclusión a una razón insuficiente.

## 7. Rendering constraints

Durante la redacción:
- no introducir símbolos/entidades no registrados;
- no sustituir objetos de tipos distintos sin identificación explícita;
- no eliminar hipótesis materiales;
- no cambiar universal por genérico, global por local, exacto por numérico, población por muestra, train por test, asociación por causalidad;
- no convertir evidencia en prueba;
- no convertir best-found en optimum;
- no actualizar versiones/APIs sin verificación.

## 8. Post-edit semantic audit

Después de editar, aplicar `protocols/TYPE_NOTATION_GATE.md` y `templates/SEMANTIC_DIFF.md`.

Comparar claim/certificado vs manuscrito:
- objetos;
- tipos/dominios;
- definiciones;
- hipótesis;
- conclusión;
- scope;
- dependencias;
- excepciones;
- estatus;
- unidades/escala;
- población/dataset/split;
- versión de software/modelo si aplica.

## 9. Compile/validation gate

Si es LaTeX:
- compilar cuando el entorno lo permita;
- revisar referencias/labels/comandos;
- no confundir compilación exitosa con corrección científica.

Si es código/documentación:
- validar sintaxis/tests pertinentes;
- comprobar API/versiones actuales cuando corresponda.

## 10. Independent manuscript consistency review

Para claims centrales, un segundo pase compara exclusivamente:
`certified source <-> rendered artifact`

Busca pérdida de hipótesis, type errors, scope drift, dependency compression, símbolos no definidos, cambios de población/métrica/dataset y strengthening accidental.

No necesita repetir toda la investigación si el certificado sigue vigente.

## 11. Artifact status

Estados sugeridos:
`DRAFT_RENDER | SEMANTIC_MISMATCH | NEEDS_PATCH | MANUSCRIPT_READY`

`MANUSCRIPT_READY` sólo significa consistencia con conocimiento certificado y validaciones editoriales; no sustituye peer review.

## 12. Regla final

> El editor puede cambiar palabras, nunca la identidad científica del claim sin reabrir investigación.

## 13. Exactness and state consistency before MANUSCRIPT_READY

Antes de `MANUSCRIPT_READY`:
- cualquier `exact/nonzero/generic` dependiente de witness debe pasar `protocols/EXACT_WITNESS.md`;
- ejecutar `protocols/ARTIFACT_CONSISTENCY.md` si se actualizaron certificados/ledgers;
- un manuscrito no puede renderizar `CERTIFIED` si falta el second-review record;
- no renderizar `CLOSED_EXACTLY` si Objective Closure conserva scope explícitamente no explorado.

El Semantic Diff debe comparar no sólo texto vs certificado, sino también certificado vs estado global activo.