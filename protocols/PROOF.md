# Protocolo de demostración, refutación y certificación

## Fase A — Formalización

Escribir exactamente universo/espacios, objetos, dominios/codominios, parámetros, regularidad, cuantificadores, hipótesis, conclusión y alcance: local/global, genérico/universal, exacto/asintótico.

No aceptar símbolos cuyo tipo sea ambiguo.

## Fase B — Grafo de dependencias

```text
TARGET
├─ DEP-1 [certificado/literatura/nuevo]
├─ DEP-2
│  ├─ ...
└─ BRIDGE-X
```

Recuperar sólo los nodos necesarios.

## Fase C — Antecedentes certificados

Para cada resultado interno:

1. cargar su Proof Certificate;
2. comprobar compatibilidad de hipótesis;
3. comprobar versión de definiciones/modelo;
4. revisar estado `CERTIFIED`;
5. expandir la prueba original sólo si hay incompatibilidad, conflicto o auditoría explícita.

## Fase D — Resultados externos

Crear Evidence Card y matriz de aplicabilidad.

## Fase E — Construcción

Cada paso no trivial debe indicar su razón:

```text
A --[L-012 + APP-007]--> B
B --[CERT-D-004]-------> C
C --[nuevo lema]-------> TARGET
```

Los nuevos lemas se demuestran con el mismo protocolo.

## Fase F — Ataque adversarial

Buscar activamente contraejemplos, pérdida de hipótesis, casos frontera, singularidades, componentes desconectadas, isotropías, ambigüedades discretas, pérdida de rango, conjuntos excepcionales, dependencias circulares, local usado como global, genérico como universal, asintótico como exacto, cambio de dominio/cuerpo, interacción con condiciones iniciales/frontera, falta de uniformidad, denominadores anulables y restricciones perdidas.

## Fase G — Refutación computacional opcional

Usar numeración para buscar contraejemplos o regiones problemáticas cuando aporte valor.

Un contraejemplo numérico debe verificarse con tolerancias, precisión y, cuando sea posible, una segunda metodología.

No declarar refutación exacta sólo por residuo si la naturaleza del claim no lo permite.

## Fase H — Reparación mínima

Si falla el target:

- identificar el punto exacto;
- añadir sólo la hipótesis necesaria;
- restringir dominio;
- debilitar local/global o universal/genérico;
- o declarar refutación.

## Fase I — Certificación

Sólo certificar si:

- dependencias cerradas;
- fuentes verificadas;
- aplicabilidad completa;
- adversarial audit completado;
- no quedan `?` esenciales;
- alcance delimitado.

Crear Proof Certificate.

## Regla de herencia

Si `T2` depende de `T1`, y `T1` ya está certificado:

- `T2` referencia `CERT-T1`;
- no reimprimir `proof(T1)`;
- sólo demostrar compatibilidad de hipótesis de `T1` con el contexto de `T2`.

Si esa compatibilidad requiere un lema, ese lema se audita por separado.
