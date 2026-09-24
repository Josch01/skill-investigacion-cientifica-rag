# Protocolo de métodos numéricos, optimización y ML

## 1. Regla base

Un resultado computacional es científico sólo si se relaciona con un claim, algoritmo, configuración, datos, versión de software, salida, análisis de error/robustez y límites explícitos.

## 2. Computation Certificate

Si una computación es esencial para un claim, crear `templates/COMPUTATION_CERTIFICATE.md`.

Una afirmación como "verificado con SymPy" o "confirmado numéricamente" no basta sin script/hash, versiones, parámetros, precisión/tolerancias, comando, salida y rerun o segundo método cuando sea material.

Si la computación sólo es corroborativa de una prueba analítica completa, marcarla como `corroborative`, no como dependencia esencial.

## 3. Reproducibilidad mínima

Registrar commit/script exacto, hash/versión de datos, entorno, dependencias, sistema operativo si importa, hardware si importa, semillas, precisión, solver/método, tolerancias, discretización, criterios de parada, parámetros/cotas, comando, métricas y archivos de salida.

## 4. Integración ODE/PDE

Revisar unidades, condiciones iniciales/frontera, rigidez, método/orden, tolerancias absolutas/relativas, eventos, conservación/invariantes, positividad, sensibilidad a paso/tolerancia, benchmark/solución exacta cuando exista, segundo solver cuando sea sensible y convergencia al refinar.

## 5. Sistemas caóticos

Exigir:

- tratamiento justificado de transitorios;
- ventana temporal;
- sensibilidad a integrador/tolerancias;
- estabilidad de diagnósticos;
- metodología del exponente de Lyapunov;
- longitud de trayectoria;
- resolución de secciones/mapas;
- continuación adecuada;
- no usar coincidencia de trayectorias largas como criterio de validez;
- distinguir evidencia de caos de prueba matemática de caos.

## 6. Optimización

Registrar función objetivo, restricciones, tratamiento de infeasibilidad, dominio/bounds, presupuesto de evaluaciones, población/partículas, semillas, criterio de parada, inicialización, baselines, varias ejecuciones, distribución de métricas, sensibilidad a hiperparámetros y validación fuera de muestra cuando haya datos.

Nunca escribir "óptimo global" salvo prueba/certificación.

## 7. Redes neuronales / PINNs

Comprobar train/validation/test, leakage, normalización, arquitectura, función de pérdida, pesos físicos, optimizador/schedule, seeds, early stopping, número de ejecuciones, baseline, ablation, incertidumbre, error físico y de datos por separado, generalización y extrapolación.

## 8. Identificabilidad

Distinguir identificabilidad estructural/práctica, observabilidad, sensibilidad, correlación y rango numérico.

Un rango numérico no sustituye una prueba estructural.

## 9. Cálculo simbólico

Registrar software/versión, supuestos, simplificaciones, divisiones, factores descartados, denominadores, ramas, conjuntos excepcionales, dominio R/C y verificación por sustitución cuando sea posible.

## 10. Prueba asistida por computadora

Para elevar cálculo a parte de una demostración exigir marco teórico, aritmética rigurosa/certificados, control de redondeo, código reproducible, versión exacta y límites del certificado.

## 11. Documentación actual

Antes de usar una API o comportamiento cambiante: Context7 si está disponible; de lo contrario documentación oficial actual.

No confiar en firmas de API recordadas.


## 12. Numerical Claim-Strength Firewall

Resultados numéricos pueden:
- localizar degeneraciones;
- sugerir genericidad;
- hallar candidatos a testigos;
- buscar contraejemplos;
- medir robustez.

No pueden, sin puente analítico certificado, establecer:
`open dense | generic | universal | maximal | iff | exact minimality | impossibility`.

Para elevar `generic/open dense`, exigir un objeto analítico exacto no idénticamente nulo o un teorema aplicable equivalente.

Para elevar `minimal`, exigir lower bound teórico y construcción que lo alcance.

Para elevar `maximal/impossible`, exigir caracterización del universo de métodos/modelos considerado y prueba de necesidad.

Los sweeps con 100% de éxito se reportan como `[N] no counterexample found in sampled region`, nunca como prueba de genericidad.

## 13. Exactness firewall

Si un resultado numérico se usa para afirmar `Q != 0` en una prueba exacta, aplicar `protocols/EXACT_WITNESS.md`.

`Q = 0.003688` en float64 no es un witness exacto, aunque la fórmula que lo contiene sea simbólica.

Opciones válidas para elevarlo:
- interval arithmetic con intervalo que excluya 0;
- validated ODE/shooting bounds;
- prueba analítica de signos/no-anulación;
- aritmética exacta;
- computer-assisted proof riguroso.

Sin eso, etiquetar como `[N] high-confidence candidate witness`.