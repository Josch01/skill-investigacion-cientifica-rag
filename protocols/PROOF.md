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

## Fase I — Auditoría de dependencias

Antes de certificar:

1. identificar dependencias esenciales y auxiliares;
2. comprobar su estatus;
3. heredar condiciones de cualquier dependencia `CONDITIONAL`;
4. si una dependencia parece innecesaria, demostrar independencia y corregir el grafo;
5. si una dependencia está `REFUTED|SUPERSEDED|STALE`, marcar el target `NEEDS_REVALIDATION` hasta cerrar la reparación.

Aplicar `protocols/CERTIFICATION.md`.

## Fase J — Segunda revisión independiente

Todo claim matemático central debe pasar una segunda revisión que reconstruya el argumento sin recibir el veredicto de la primera revisión.

Una objeción no resuelta impide `CERTIFIED`.

## Fase K — Certificación

Sólo certificar si:

- dependencias cerradas;
- fuentes verificadas;
- aplicabilidad completa;
- adversarial audit completado;
- no quedan `?` esenciales;
- alcance delimitado.

Crear Proof Certificate sólo después de superar el Certification Gate.

## Regla de herencia

Si `T2` depende de `T1`, y `T1` ya está certificado:

- `T2` referencia `CERT-T1`;
- no reimprimir `proof(T1)`;
- sólo demostrar compatibilidad de hipótesis de `T1` con el contexto de `T2`.

Si esa compatibilidad requiere un lema, ese lema se audita por separado.


## Regla de propagación

Un claim no puede quedar incondicionalmente `CERTIFIED` si depende esencialmente de un antecedente `CONDITIONAL` cuyas condiciones no se han incorporado o verificado.

Si el claim usa sólo una dirección o una consecuencia independiente del antecedente, demostrarlo explícitamente y eliminar/corregir la arista del grafo.


## Fase L — Fuerza del claim

Antes de aceptar `generic`, `open dense`, `maximal`, `minimal`, `only if`, `universal` o `impossible`, identificar la obligación lógica adicional asociada.

- `generic/open dense`: definir espacio + demostrar no-identidad del discriminante/minor mediante testigo exacto o argumento equivalente.
- `maximal`: definir universo + suficiencia + necesidad fuera de la clase.
- `sharp minimal`: lower bound + construcción alcanzable.
- `impossible`: obstrucción para una clase de métodos definida.
- `universal`: cuantificadores sobre toda la familia sin usar evidencia muestral como sustituto.

Una prueba de que una estrategia concreta falla sólo certifica esa obstrucción concreta.