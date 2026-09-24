# Hierarchical Retrieval Policy

## Objetivo

Minimizar tokens y latencia sin degradar rigor ni procedencia. La recuperación debe ser escalonada, detenible y guiada por suficiencia.

## LEVEL-0 — Orientation

Cargar MEMORY_CORE y tags pertinentes de MEMORY_INDEX. Sirve para localizar conocimiento, no para reemplazar evidencia exacta.

## LEVEL-1 — Certified answer

Recuperar Proof Certificate, nodo exacto del ledger, estado epistemológico, scope e hipótesis. Si responde completamente, detenerse.

## LEVEL-2 — Dependency subgraph

Recuperar sólo dependencias pertinentes: CERT -> H / X / REF / DEC / N. Expandir recursivamente sólo si la respuesta depende de ellas.

## LEVEL-3 — Internal original source

Abrir sección exacta del manuscrito, prueba original, script/resultado o ledger detallado sólo si el usuario pide detalle, el certificado resume demasiado, existe discrepancia o se necesita una ecuación/paso exacto.

## LEVEL-4 — External refresh

Buscar literatura/documentación externa sólo cuando falta evidencia, se pide fuente original, se requiere novedad/estado del arte, la información puede haber cambiado, el claim cambia de alcance o la fuente almacenada es parcial/stale.

Para software usar Context7/documentación oficial según CONTEXT7.md.

## LEVEL-5 — New research

Activar RESEARCH_LOOP.md sólo si los niveles anteriores no pueden responder sin crear una afirmación nueva.

## Sufficiency Gate

Después de cada nivel: ¿puedo responder exactamente la pregunta sin añadir un claim no respaldado? Si sí, STOP. Si no, EXPAND ONE LEVEL.

No saltar directamente a LEVEL-4/5 salvo que la naturaleza de la pregunta lo requiera.

## Scope Compatibility Gate

Antes de reutilizar certificado comprobar: mismas definiciones, mismo dominio, mismas hipótesis, mismo alcance local/global, mismo alcance genérico/universal y mismo estatus exacto/numérico.

Si no, el certificado es antecedente, no respuesta completa.

## Freshness Gate

Refrescar por defecto: software/APIs, políticas de revistas, estado del arte, novedad, resultados 'más recientes' y benchmarks dependientes de versiones actuales.

No refrescar automáticamente: teorema matemático ya verificado, definición estable o prueba interna certificada, salvo cambio de uso o conflicto.

## Context sharing

Si hacen falta agentes: recuperar una vez, construir Case Packet, compartir IDs/extractos y no duplicar papers completos.

## Regla final

Orientation -> Certificate -> Subgraph -> Original -> External -> New Research. Cada escalón debe justificarse por insuficiencia del anterior.