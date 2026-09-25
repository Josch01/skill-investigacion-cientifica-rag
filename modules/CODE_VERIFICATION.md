# Module: CODE_VERIFICATION

## Activar cuando

Se deba producir, revisar, ejecutar o validar código científico que soporte claims, resultados numéricos o artefactos reproducibles.

## Composición

- `modules/NUMERICAL_STUDY.md` cuando el código produzca evidencia científica.
- `protocols/ARTIFACT_CONSISTENCY.md`
- deterministic checks autorizados por el runtime.

## Obligaciones

1. Separar código de exploración de código que sustenta resultados reportados.
2. Registrar entradas, versiones, seeds, tolerancias y outputs relevantes.
3. No afirmar ejecuciones que no ocurrieron.
4. Verificar que scripts y resultados correspondan al mismo task/revision/hash cuando el runtime lo soporte.
5. Tratar fallos, timeouts o policy rejection como evidencia operativa, no científica.

## Salida

`code purpose | inputs | environment | deterministic checks | execution evidence | hashes if available | failures | scientific claims supported/not supported`.