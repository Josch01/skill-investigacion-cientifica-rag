# Presupuesto de contexto y ahorro de tokens

## Objetivo

Maximizar dependencias científicas útiles por token.

## Presupuesto por defecto

Valores orientativos:

- `MEMORY_CORE`: 600–1200 tokens.
- Working Set de ledger: 5–12 nodos.
- Fuentes iniciales: 3–5.
- Evidence Cards: sólo las usadas.
- Agentes: 2 por defecto.
- Case Packet: idealmente < 2500 tokens.
- Informe por agente: compacto y estructurado.

## Reglas

1. No cargar documentos completos si una sección basta.
2. No dar a cada agente su propia copia extensa de las fuentes.
3. El coordinador recupera una vez y comparte el Case Packet.
4. Cargar certificados antes que pruebas completas.
5. Expandir una dependencia sólo si hay incompatibilidad, contradicción, detalle omitido relevante o auditoría explícita.
6. Después de cerrar una tarea, guardar certificado y compactar contexto.
7. No guardar conversación; guardar resultados con procedencia.
8. No resumir eliminando hipótesis, excepciones o alcance.

## Estrategia de expansión

```text
CORE
  -> INDEX
     -> 5-12 nodos
        -> certificados
           -> fuentes exactas sólo si hace falta
```

## Stop rule

Si la evidencia recuperada basta para decidir que un paso no aplica, detener esa rama. No gastar tokens intentando probar una afirmación ya refutada bajo las hipótesis actuales.
