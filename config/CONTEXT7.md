# Integración opcional con Context7

Context7 se usa como **retriever de documentación de software**, no como memoria científica ni como base de literatura matemática.

Repositorio oficial: https://github.com/upstash/context7

## Activar cuando

- se necesita firma/API actual;
- cambió una librería;
- se requiere documentación específica de versión;
- se genera código que depende de comportamiento no estable.

## No activar cuando

- se busca un teorema matemático;
- se evalúa novedad científica;
- se necesita un paper;
- la pregunta puede resolverse con un certificado interno ya válido.

## Flujo

Si se conoce el library ID:

```text
query-docs(library_id, pregunta concreta)
```

Si no:

```text
resolve-library-id(nombre, tarea)
-> query-docs(id, pregunta concreta)
```

Evitar consultas genéricas.

## Cache local

Registrar en `memory/SOFTWARE_LEDGER.md`:

- librería;
- library ID si existe;
- versión;
- tema consultado;
- fecha;
- URL/documentación;
- claims soportados.

Una consulta previa puede reutilizarse sólo si la versión relevante no cambió y el claim es el mismo.

## Fallback

Si Context7 no está disponible:

1. documentación oficial;
2. changelog/release notes;
3. repositorio oficial.

Nunca inventar una API por memoria.
