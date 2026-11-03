# Meta Skill Review Oliver — Productividad y salario mínimo

Fecha: 3 de noviembre de 2026. Versión revisada: `6eebcf8`, informe principal de 16 páginas y nota técnica de cuatro páginas. Se comprobó que `origin/main` coincidía con esa revisión antes de empezar.

## Diagnóstico y selección

El aporte es ordenar evidencia descriptiva y fuentes externas para una recomendación de concertación salarial. El documento debe juzgarse como informe de política del CJC. La pregunta relevante es cuánto respaldo tienen la recomendación y sus mecanismos, manteniendo separados resultados propios, estimaciones de terceros y decisiones normativas.

Se aplicaron dos revisiones esenciales. El inventario local confirmó su instalación y se leyeron sus protocolos.

| Orden | Skill | Insumos y problema | Producto | Prioridad y costo relativo |
|---|---|---|---|---|
| 1 | `review-paper-santanna` | Texto completo, nota técnica, tres figuras, bibliografía y revisión anterior. Examinar argumento, interpretación, fuentes y presentación. Modo single-pass, `--no-cross-artifact`, sin revista objetivo. | Este diagnóstico y cuatro hallazgos validados. | Alta, medio. |
| 2 | `audit-reproducibility-santanna` | CSV/JSON depositados, cuadros, figuras vectoriales y PDF compilados. Cotejar cifras propias y coherencia entre documentos. | Auditoría de 80 cifras, 16 comprobaciones de etiquetas y registro reproducible. | Alta, medio. |

La revisión numérica es una aplicación acotada. Recalcula aritmética desde agregados y no reestima los microdatos ni reproduce modelos de terceros. La edición sigue `voz-oliver-pardo`. No se añadieron revisiones completas de estilo que repitan la lectura sustantiva, ni simulaciones de referees. La revisión y su verificación se realizaron en este chat, sin afirmar independencia de agentes.

Se reutilizó `REVISION_CRITICA.md` para distinguir problemas antiguos de nuevos. La ausencia de 2021, la mezcla de años completos con 2026 parcial y la falta de exclusión explícita de 98/99 del cuadro de salario medio están resueltas por el aporte posterior de Jorge. No se contabilizaron otra vez como errores vigentes.

## Evaluación del informe

Recomendación editorial inicial: revisar puntos concretos antes de difusión. Los cuatro hallazgos confirmados se corrigieron. El informe conserva el objetivo de compensar inflación de 2026, la condición de revisar 7% si la inflación lo supera, la introducción inicial y las conclusiones finales.

La comparación salario-productividad está descrita con dos medidas de productividad y distingue IPC promedio e IPC de diciembre. Los principales cálculos resisten el cotejo. La recomendación de 7% permanece como decisión condicionada de política. La evidencia disponible no estima un porcentaje óptimo, y el documento ya lo reconoce.

La limitación principal que permanece es de alcance. Una media de asalariados ocupados no identifica la contratación que habría ocurrido sin un aumento. Tampoco una distribución por edad en un solo año identifica compresión salarial en el tiempo. El texto conserva esas distinciones. La lectura no exige una nueva regresión al informe ni convierte la ausencia de identificación propia en un error de sus estadísticas descriptivas.

## Hallazgos confirmados y reparación

### MC1. Precisar la condición de convergencia — High

El texto decía que reducir la distancia requería que creciera la productividad. Eso expresa una condición necesaria, pero deja sin formular la comparación de tasas que sostiene el mecanismo propuesto.

Si el ajuste de 2027 fuera 6,9% y la inflación de ese año 5,5%, el mínimo real aumentaría 1,3270%. Con productividad creciendo 1%, la razón entre mínimo real y productividad todavía aumentaría 0,3238%. El 5,5% corresponde al pronóstico de Bancolombia del 23 de septiembre, ya citado por el informe. El 1% de productividad es un supuesto ilustrativo para probar la condición, no un pronóstico del CJC.

La condición exacta para que disminuya la razón es `(1 + aumento nominal)/(1 + inflación 2027) < 1 + crecimiento de productividad`. Se precisó en resumen, introducción, propuesta y conclusiones. El cambio conserva la recomendación y evita prometer convergencia solo porque la productividad crezca.

Fuente del pronóstico: [Bancolombia, actualización del 23 de septiembre de 2026](https://prensa.bancolombia.com/noticias/economia-finanzas/proyecciones-de-inflacion-bancolombia).

### MC2. La reproducción del cuadro juvenil vaciaba la procedencia — High

En una copia aislada, el comando documentado `python scripts/integrar_revision.py` terminó con código 0 pero sustituyó un manifiesto de ocho insumos por uno vacío. Ocurre cuando no existe la carpeta original de Jorge y el script escribe el resultado vacío de la búsqueda.

Se corrigió para conservar y verificar el manifiesto depositado cuando no se importan originales. Se probaron dos casos. Los insumos existentes generan el cuadro y conservan el manifiesto byte por byte. Un cambio de contenido en el CSV provoca un error y también conserva el manifiesto. Se admite únicamente la equivalencia LF/CRLF para las extensiones de texto indicadas, porque dos insumos del clon difieren del hash original solo por los finales de línea. Las imágenes y documentos binarios mantienen comparación exacta.

No se reestimaron porcentajes juveniles ni se cambiaron sus filtros. La prueba se hizo fuera de los archivos de producción y su resultado queda en `verification_manifest_fix.json`.

### mc1. Redondeo de una transición de Antioquia — High

La figura C.2.A, página 22 del estudio de Patiño, Chaparro y coautores, muestra 7,15% para la transición 2024–2025 y 4,71% para 2025–2026. La edición anterior usaba 7,1%, obtenido como 4,7 + 2,4 a partir de cifras ya redondeadas. Se corrigió a 7,2%, el redondeo directo a un decimal. La diferencia era de presentación y no cambia la interpretación.

El cotejo vertical con tolerancia de 0,1 puntos porcentuales por sí solo no detectaría este problema de redondeo. La figura se inspeccionó directamente. No se presenta esta corrección como una falla sustantiva de los autores del estudio.

### mc2. Identificar el comparador fiscal por componente — High

La nota del cuadro extendía la referencia al 7,1% presupuestado a todo el ejercicio del CARF. Las notas 2 y 3 del Comunicado 22 documentan el contraste con presupuesto para pensiones y nómina. La nota 4 describe el cálculo de renta mediante costos y márgenes.

Se limitó el comparador presupuestal a los dos primeros componentes y se describió por separado la estimación de renta. También se precisó que el componente pensional incorpora el efecto compensatorio de cotizaciones. No cambiaron los montos atribuidos al CARF ni se sumaron a los escenarios del MFMP.

Fuente: [CARF, Comunicado 22](https://www.carf.gov.co/documents/d/guest/comunicado-22-estimacion-preliminar-efecto-fiscal-de-aumento-de-salario-minimo-2026?download=true).

## Cotejo numérico

La auditoría inicial verificó 79 cifras propias, sin discrepancias superiores a las tolerancias. Tras añadir el ejemplo de poder adquisitivo de 2027, la auditoría final verificó 80. También localizó 16 etiquetas numéricas de los tres gráficos vectoriales. No encontró referencias indefinidas ni desbordes en la compilación.

Los acumulados calculados desde las series depositadas son 13,5434% para mínimo real, 1,2181% para productividad por hora y −4,6434% para productividad por ocupado. El escenario de 2026 con inflación de 6,9% da 15,0608% de ganancia real. Los escenarios en pesos y las celdas del cuadro de salario medio coinciden con sus fuentes agregadas.

La auditoría verifica consistencia entre datos depositados y publicaciones. No certifica la calidad de los microdatos, las cifras fiscales como resultados observados ni la validez causal de modelos externos. La comprobación automatizada de presencia en PDF se complementa con la lectura de cuadros y figuras. No existe un passport exhaustivo de todos los materiales privados o versiones anteriores, de modo que no se declara una auditoría horizontal de artefactos no suministrados.

## Medición GEIH y sensibilidad

La ventana principal usa enero–agosto de entrevistas, pero P6500 refiere al mes anterior. Por ello contiene diciembre del año previo. Se hizo visible ese desfase en la nota del cuadro.

Una sensibilidad calculada con febrero–agosto de entrevistas, sin enero, conserva el aumento de la razón mínimo/media. Pasa de 58,9857% en 2021 a 67,8389% en 2026, frente a 59,2823% y 68,1843% en el cuadro principal. El ejercicio no cambia el cuadro canónico ni corrige composición o no respuesta. Sus agregados quedan en `sensibilidad_ventana_GEIH.json`.

La trazabilidad incompleta del marco de 2021 y los cambios de no respuesta permanecen como límites de confianza Medium para interpretar la evolución como un cambio de la distribución salarial poblacional. La aritmética de los tabulados tiene confianza High. No se añadieron errores estándar que no hayan sido estimados.

Se hizo explícito en la nota técnica que la densidad juvenil se normaliza dentro de la rejilla de 150 mil a nueve millones de pesos. Las proporciones del cuadro se calculan sobre los registros válidos y no se obtienen integrando esa curva. Es una aclaración de un límite ya registrado, no un hallazgo nuevo ni una reestimación.

## Objeciones que debe poder responder el informe

1. **¿Por qué usar inflación pasada si el argumento busca moderar ganancias reales futuras?** La respuesta es una decisión de compensación retrospectiva, compatible con ganancias reales durante 2027 si baja la inflación. El texto ahora hace explícita esa consecuencia y la condición de convergencia.
2. **¿La base 2021 y la composición explican parte del contraste?** Pueden influir. La ventana común resuelve estacionalidad básica, pero no no respuesta, selección de ocupados ni composición. La comparación descriptiva no se interpreta como costo laboral unitario ni productividad individual.
3. **¿Cuánto empleo se deja de crear a escala nacional?** El informe no tiene una estimación nacional identificada. No debe extrapolar mecánicamente los resultados de Antioquia ni multiplicar sus efectos marginales por el aumento de 23%.
4. **¿Cuánto ahorra al fisco la propuesta de 2027?** Las fuentes aportan mecanismos y escenarios distintos, sin un cálculo integral del ahorro de la propuesta. La ausencia de ese cálculo está declarada y no se reemplazó por una regla de tres.

## Decisiones y verificaciones pendientes

**Cuantificación de Chaparro.** La petición inicial de Oliver incluía una magnitud por aumento del mínimo, pero la última edición conserva solo la referencia cualitativa y la movilidad. La tabla C.1 y el texto de la página 34 atribuyen a un aumento real de 1% aproximadamente 44.500 puestos que dejan de crearse y 5.000 de mayor destrucción, unos 49.500 menos en el saldo de Antioquia. Es la interpretación de los autores, para empresas privadas con más de un trabajador y su muestra de enero de 2022 a febrero de 2026. Su modelo no fue replicado. La decisión de reincorporar esa magnitud debe considerar la escala del efecto, su metodología y la edición del coautor que la retiró. No se restauró automáticamente ni se produjo una cifra nacional.

**Actualización macroeconómica.** El comunicado del Banco de la República del 30 de octubre respalda la expectativa de analistas de 6,9% para diciembre de 2026. La agenda oficial anuncia el IPM de octubre para el 4 de noviembre. Esa publicación aún no estaba disponible en la revisión del 3 de noviembre. Hay que cotejarla antes de una difusión posterior, sin anticipar su resultado. [Banco de la República](https://www.banrep.gov.co/es).

**Reproducción desde microdatos.** Los resultados agregados de Jorge se reconciliaron con sus meses. La lectura del código no sustituye su reejecución sobre los archivos GEIH originales y el diseño de encuesta. La fuente de 2021 sigue sin identificador de descarga original.

**Extensiones opcionales.** Una comparación por hora y sensibilidad a una base histórica más larga ayudarían a separar jornada, productividad y nivel salarial. No se añadieron como resultados sin estimarlos. No son condiciones para que los cuadros actuales describan sus universos.

## Valoración por dimensión

| Dimensión | Diagnóstico tras las correcciones |
|---|---|
| Argumento | La recomendación queda condicionada y el mecanismo de convergencia explicita la comparación de tasas. |
| Identificación | El informe propio es descriptivo. Los modelos citados se mantienen atribuidos y limitados a su ámbito. |
| Especificación y medición | Universo y ventanas documentados. Permanecen no respuesta, composición y falta de inferencia muestral. |
| Literatura | Revisión internacional seleccionada, Dube y evidencia colombiana. No se afirma un censo ni una síntesis sistemática exhaustiva. |
| Redacción | Se preservan introducción inicial, conclusiones finales y uso restringido de cursiva. Las correcciones se concentran en significado y comparadores. |
| Presentación | Cuadros y gráficos compilados y cotejados. Los flotantes todavía dejan espacios amplios en algunas páginas, una mejora editorial opcional. |

Scorecard: 7/10. Es un diagnóstico editorial del borrador, no una probabilidad de aceptación ni una certificación de causalidad.

Los cuatro hallazgos se conservan en un JSON validado, con evidencia, caso que falla y reparación. La instantánea anterior permite comprobar las citas después de las correcciones.
