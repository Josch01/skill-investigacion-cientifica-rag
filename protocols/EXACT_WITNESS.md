# Exact Witness & Rigorous Nonvanishing Gate

## 1. Propósito

Separar estrictamente:
`numerically nonzero` de `provably nonzero`.

Este protocolo se activa cuando una prueba usa un testigo exacto, no-anulación de un minor/discriminante, analytic nonidentity, cambio de signo certificado, singular value estrictamente positivo como hecho matemático, o cualquier paso donde `x != 0` sea esencial para elevar un claim exacto.

## 2. Evidencia aceptable para EXACT_NONZERO

Una cantidad Q puede marcarse `EXACT_NONZERO` sólo si existe al menos una de:
- expresión simbólica exacta + prueba de que sus factores relevantes no se anulan bajo hipótesis explícitas;
- aritmética exacta/racional/algebraica;
- interval arithmetic / validated numerics con intervalo certificado que excluye 0;
- cota analítica rigurosa `|Q| >= c > 0`;
- computer-assisted proof con control de redondeo y certificado reproducible;
- teorema externo plenamente aplicable que implique `Q != 0`.

## 3. Evidencia NO suficiente

No basta:
- float64/float128;
- `abs(Q) > tolerance`;
- acuerdo entre dos métodos numéricos;
- muchas cifras significativas;
- relative error pequeño;
- SVD positiva en una grilla;
- SymPy evaluando números aproximados;
- una fórmula exacta cuyos factores no nulos sólo fueron observados numéricamente.

Ejemplo crítico:
`Q = C * u3 * u5` con `C` exacto, pero `u3` y `u5` obtenidos por ODE numérica, NO es testigo analítico exacto.

## 4. Niveles de witness

`EXACT_NONZERO`
`RIGOROUS_NUMERIC_NONZERO`
`HIGH_PRECISION_NUMERIC_NONZERO`
`SCOUT_NONZERO`
`UNRESOLVED_NONZERO`

Sólo los dos primeros pueden sustentar un paso exacto cuando el segundo usa validated numerics con bounds rigurosos.

## 5. Genericity/nonidentity bridge

Para deducir que una función analítica `Delta` no es idénticamente cero:
- usar `EXACT_NONZERO`, o
- `RIGOROUS_NUMERIC_NONZERO` con un teorema de validación adecuado.

`HIGH_PRECISION_NUMERIC_NONZERO` sólo produce una conjetura fuerte / candidate witness.

## 6. Analytic branch existence

Si el witness vive sobre una rama analítica de soluciones, certificar por separado:
- existencia de la rama;
- regularidad/analiticidad;
- dominio conectado pertinente;
- hipótesis del IFT/continuation theorem;
- no degeneracy/invertibility condition.

Rango/identificabilidad del modelo NO implica automáticamente no degeneracy del Poincare map ni existencia de una rama periódica.

## 7. Regla final

> Exactitud del formato de la fórmula no convierte datos aproximados en un testigo exacto.