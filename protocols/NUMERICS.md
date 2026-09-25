# Protocolo de métodos numéricos, optimización y ML

## 1. Regla base

Un resultado computacional es científico sólo si se relaciona con un claim, algoritmo, configuración, datos, versión de software, salida, análisis de error/robustez y límites explícitos.

Antes de ejecutar una computación material para una demostración, declarar su semántica:

`exploratory_numeric | falsification_search | corroborative_numeric | symbolic_exact | exhaustive_finite | validated_numeric | rigorous_computer_assisted_proof`.

La semántica determina qué fuerza epistemológica puede alcanzar el resultado.

## 2. Computation Certificate

Si una computación es esencial para un claim, crear `templates/COMPUTATION_CERTIFICATE.md`.

Una afirmación como "verificado con SymPy" o "confirmado numéricamente" no basta sin script/hash, versiones, parámetros, precisión/tolerancias, comando, salida y rerun o segundo método cuando sea material.

Si la computación sólo es corroborativa de una prueba analítica completa, marcarla como `corroborative`, no como dependencia esencial.

Si pretende cerrar una obligación de prueba, el certificado debe contener además el **puente matemático** que conecta salida y claim: dominio cubierto, cuantificadores cubiertos, exhaustividad/cobertura, modelo aritmético, control de redondeo/error y criterio formal de éxito/refutación.

Reproducibilidad del programa y suficiencia matemática del certificado son condiciones distintas; ambas son necesarias cuando la computación es parte esencial de una prueba exacta.

## 3. Reproducibilidad mínima

Registrar commit/script exacto, hash/versión de datos, entorno, dependencias, sistema operativo si importa, hardware si importa, semillas, precisión, solver/método, tolerancias, discretización, criterios de parada, parámetros/cotas, comando, métricas y archivos de salida.

## 4. Integración ODE/PDE

Revisar unidades, condiciones iniciales/frontera, rigidez, método/orden, tolerancias absolutas/relativas, eventos, conservación/invariantes, positividad, sensibilidad a paso/tolerancia, benchmark/solución exacta cuando exista, segundo solver cuando sea sensible y convergencia al refinar.

Una integración ordinaria convergente puede ser evidencia fuerte, pero no constituye automáticamente `validated_numeric`.

Para cierre riguroso exigir un método validado o una cota analítica/certificada que controle el error relevante para el claim.

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

Poincaré, continuation, Lyapunov/Floquet estimados y diagramas de bifurcación ordinarios son normalmente `exploratory_numeric` o `corroborative_numeric` salvo que exista un marco de validación rigurosa que cierre los cuantificadores del claim.

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

`symbolic_exact` puede cerrar una obligación sólo si la cadena simbólica preserva exactitud y se auditan supuestos, divisiones, ramas y excepciones.

## 10. Prueba asistida por computadora

Para elevar cálculo a parte de una demostración exigir:

1. marco teórico explícito;
2. reducción del subclaim a una obligación computable bien definida;
3. cuantificadores y dominio exactos;
4. aritmética rigurosa/certificados o cálculo exacto apropiado;
5. control de redondeo y error;
6. cobertura/exhaustividad cuando el claim lo exige;
7. código reproducible y versión exacta;
8. criterio formal de éxito/refutación;
9. límites del certificado;
10. verificación independiente o segundo método cuando sea material.

Métodos admisibles pueden incluir, según el problema: aritmética intervalar, interval Newton/Krawczyk, integración ODE/PDE validada, continuation validada, bounds uniformes certificados, enumeración finita exhaustiva exacta y otras técnicas con garantía matemática equivalente.

Cuando una computación cierre una obligación, registrar el `Proof_Obligation_ID` y su `Closure_standard`.

## 11. Enumeración finita exhaustiva

Una computación sobre muchos casos no es automáticamente exhaustiva.

Para `exhaustive_finite` exigir:

- definición exacta del universo finito;
- prueba o fuente certificada de que la enumeración cubre todo el universo;
- ausencia de filtros que eliminen casos no justificados;
- exactitud/certificación del predicado evaluado;
- trazabilidad de la enumeración.

Si falta exhaustividad, reclasificar como `exploratory_numeric` o `corroborative_numeric`.

## 12. Claims sobre familias y cobertura

Para un claim

```text
forall p in P: Q(p)
```

un sweep finito de puntos de `P` no demuestra el cuantificador universal.

Para cierre computacional riguroso exigir una cobertura de todo `P`, por ejemplo mediante:

- partición intervalar certificada;
- cota uniforme;
- reducción teórica a una familia finita exhaustiva;
- monotonía/convexidad/estructura demostrada que reduzca el continuo;
- otro argumento equivalente de cobertura.

Registrar explícitamente:

`sampled_region`, `certified_domain`, `coverage_argument`.

## 13. Documentación actual

Antes de usar una API o comportamiento cambiante: Context7 si está disponible; de lo contrario documentación oficial actual.

No confiar en firmas de API recordadas.

## 14. Numerical Claim-Strength Firewall

Resultados numéricos ordinarios pueden:
- localizar degeneraciones;
- sugerir genericidad;
- hallar candidatos a testigos;
- buscar contraejemplos;
- medir robustez.

No pueden, sin puente analítico o computacional riguroso certificado, establecer:
`open dense | generic | universal | maximal | iff | exact minimality | impossibility`.

Para elevar `generic/open dense`, exigir un objeto analítico exacto no idénticamente nulo o un teorema/certificado riguroso equivalente.

Para elevar `minimal`, exigir lower bound teórico/certificado y construcción que lo alcance.

Para elevar `maximal/impossible`, exigir caracterización del universo de métodos/modelos considerado y prueba de necesidad.

Los sweeps con 100% de éxito se reportan como `[N] no counterexample found in sampled region`, nunca como prueba de genericidad.

## 15. Exactness firewall

Si un resultado numérico se usa para afirmar `Q != 0` en una prueba exacta, aplicar `protocols/EXACT_WITNESS.md`.

`Q = 0.003688` en float64 no es un witness exacto, aunque la fórmula que lo contiene sea simbólica.

Opciones válidas para elevarlo:
- interval arithmetic con intervalo que excluya 0;
- validated ODE/shooting bounds;
- prueba analítica de signos/no-anulación;
- aritmética exacta;
- computer-assisted proof riguroso.

Sin eso, etiquetar como `[N] high-confidence candidate witness`.

## 16. Integración con Proof Tactics

Si la computación pertenece a una demostración, aplicar también `protocols/PROOF_TACTICS.md`.

Regla de cierre:

```text
exploratory_numeric -> EVIDENCE_ONLY
falsification_search -> candidate [X] until rigorously verified
corroborative_numeric -> support only
symbolic_exact -> may RIGOROUSLY_CLOSE
exhaustive_finite -> may RIGOROUSLY_CLOSE
validated_numeric -> may RIGOROUSLY_CLOSE
rigorous_computer_assisted_proof -> may RIGOROUSLY_CLOSE
```

El verbo `may` es deliberado: la clase de método no basta; debe satisfacer el estándar específico de la obligación.