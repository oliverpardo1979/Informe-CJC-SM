# Revisión crítica del boletín para la discusión del mínimo de 2027

## Registro de la edición de fluidez y consistencia

Actualización de la figura juvenil: se recalculó GEIH 2025 con el script `scripts/figura_edad.py`, que conserva los filtros y el método de suavizado originales. Se confirmó la cobertura de los doce meses y la coincidencia de tamaños de muestra, medianas y porcentajes alrededor del mínimo con las cuatro filas de 2025 del CSV de Javeriana. Esto actualiza el alcance de las notas anteriores sobre ausencia de reejecución: se reejecutó el cálculo de la figura de 2025, sin extenderlo a 2022–2026 ni completar una auditoría general de microdatos. Se depositan las densidades agregadas y las estadísticas de la figura en `data/`; el gráfico se publica como PDF vectorial y PNG de 300 ppp. El cuadro detallado pasa al anexo A.

Esta sección registra cambios posteriores al diagnóstico original que sigue abajo. Se redujeron reiteraciones de la propuesta y de los límites del análisis, se enlazó la evidencia de empleo con la distribución por edad y se armonizó el sentido de la recomendación: compensar la inflación pasada sin añadir un componente importante por encima de ella. Se distingue ese criterio de la variación real efectiva durante 2027. Se precisó que la muestra juvenil no distingue formalidad y que los rangos salariales del estudio de Antioquia dependen del mínimo de cada año. Se retiraron cuatro referencias que ya no se citaban y se ajustaron las letras de las publicaciones institucionales de 2026.

La comprobación aritmética contra `data/series_2021_2025.csv` confirmó los acumulados 13,5434%, 1,2181% y −4,6434%, las variaciones anuales del cuadro metodológico y la ganancia real de 2026 de 15,0608% bajo inflación de 6,9%. Los cuatro escenarios en pesos coinciden con el cálculo decimal y redondeo al peso. Las proporciones juveniles corresponden al CSV importado, con redondeo a un decimal; se explicó en el anexo que las categorías se superponen y no deben sumarse como una partición.

Esta comprobación valida consistencia interna y aritmética, no reestima GEIH ni constituye una auditoría completa de fuentes. Se consultaron las páginas oficiales de Banco de la República y Fedesarrollo; la segunda reproduce el registro de la expectativa de 6,87%. El enlace original de EAFIT no pudo abrirse mediante la consulta web, por lo que los resultados atribuidos a ese estudio conservan la verificación pendiente ya señalada en este archivo. El corte macroeconómico se mantiene en 29 de octubre de 2026.

Fecha: 1 de noviembre de 2026. Base: clon de Informe-CJC-SM y ocho archivos de SalarioMinimo_Edad, copiados de Javeriana. Esta revisión combina lectura del texto y auditoría del código y de las tablas previas; no es una nueva estimación con GEIH ni certifica todas las referencias externas del borrador.

## Dictamen editorial

El borrador tiene una base útil: identifica fuentes y fechas, diferencia IPC promedio y diciembre, evita sumar tasas para construir acumulados y reconoce que productividad agregada y salario mínimo describen objetos distintos. También distingue menor creación de empleo de destrucción de puestos. Debe conservarse esa disciplina.

Su principal problema es de inferencia. Una divergencia entre índices puede justificar estudiar riesgos y explicar una preferencia por moderación, pero no identifica el nivel eficiente del mínimo ni produce un techo de 7%. Ese techo depende de una decisión normativa —evitar otra mejora real importante— y de pronósticos de inflación. Conviene formular primero la condición económica y luego presentar 7% como escenario revisable. No debemos convertir una preferencia del borrador en resultado empírico.

## Hallazgos y cambios necesarios

| Prioridad | Hallazgo | Consecuencia y tratamiento |
|---|---|---|
| Alta | El resumen abre con un techo antes de exponer su fundamento y condiciones. | Reescribir la apertura para identificarlo como recomendación condicionada; conservar explícita la posibilidad de revisarlo. |
| Alta | «Conservar las ganancias reales» puede confundirse con garantizar poder adquisitivo durante 2027. | Separar compensación retrospectiva de inflación 2026 y variación real efectiva durante 2027. La segunda depende de los precios de 2027. |
| Alta | La brecha 2021–2025 depende de la base y no es costo laboral unitario. | Mostrar sensibilidad a periodos más largos y distinguir salario mensual, salario por hora y costos completos antes de usar la brecha para juzgar capacidad empresarial. El antecedente 2010–2025 de Javeriana necesita cotejo antes de incorporarlo. |
| Alta | El borrador casi no incorpora la distribución por edad ya disponible. | Se agregó una subsección y un cuadro de 2025 generado desde el CSV, con población, ponderación y tamaños de muestra. No se interpreta edad como productividad. |
| Alta | La GEIH seleccionada contiene asalariados ocupados, no exclusivamente formales. | No describir los porcentajes como cobertura formal, desempleo juvenil o probabilidades de contratación. Para ello hacen falta variables y universos adicionales. |
| Alta | El ejercicio no identifica efectos causales de diferenciar el mínimo por edad. | Presentar la diferenciación como alternativa a evaluar junto con subsidios, formación e intermediación; medir sustitución, ingresos y permanencia. |
| Alta | Hay cifras muy específicas atribuidas al estudio de Antioquia. | Antes de publicarlas, cotejar tabla C.1, unidad del choque, horizonte, población, incertidumbre y estrategia de identificación en el original. No multiplicar 49.500 por 23 ni extrapolar a Colombia. Esta revisión no revalidó esa cifra. |
| Media | La justificación jurídica se remite principalmente a la motivación de un decreto. | Explicitar el artículo 8 de la Ley 278 y C-815/1999: la decisión requiere considerar varios parámetros y protección del trabajo. Una propuesta económica no demuestra suficiencia jurídica. Revisar también actuaciones judiciales de 2026 antes del cierre. |
| Media | El cuadro internacional ocupa espacio y mezcla regímenes y ámbitos. | Mantener la distinción conceptual nivel/actualización/salvaguardas, y llevar el detalle por país al anexo en una edición breve. Los seis casos son seleccionados; no prueban qué mecanismo predomina en América. |
| Media | Se repiten los acumulados y la recomendación a lo largo del texto. | En una siguiente edición editorial, concentrar cifras en dos gráficos o cuadros y dejar interpretación en el cuerpo. La versión actual sigue teniendo formato de informe técnico, con el boletín breve aún pendiente. |

## Qué incorpora el insumo juvenil

Con jornadas habituales de al menos 40 horas en 2025, 81,25% de los asalariados de 15–24 años recibe hasta 1,25 mínimos, frente a 60,24% de quienes tienen 25 o más: diferencia de 21,01 puntos. Por encima de dos mínimos, las proporciones son 3,80% y 19,56%. Es evidencia de concentración de los salarios de los ocupados; no de la productividad individual ni del efecto del piso salarial sobre quienes no lograron trabajar.

El corte de 40 horas es analítico y no una definición jurídica. Salarios mensuales inferiores al mínimo requieren estudiar tiempo remunerado, horas y reporte. La banda ±3% alrededor del mínimo debe mantenerse visible: la columna «bajo el mínimo» del CSV corresponde estrictamente a menos del 97% del piso, no a todo valor inferior al 100%.

El código contiene 2026 enero–agosto y los años previos completos. No debe interpretarse la diferencia como efecto del aumento de 2026 sin igualar ventanas, estudiar composición y controlar otros cambios. El denominador también cambia al expresar los ingresos en múltiplos del mínimo. El grupo 15–24 utilizado aquí no coincide necesariamente con el universo de los boletines oficiales de juventud: cualquier contraste debe armonizar edades.

## Auditoría pendiente del cálculo con microdatos

1. Confirmar meses presentes por archivo y que dividir los ponderadores por 12 u 8 produce promedios mensuales válidos. Documentar la fecha y procedencia de cada archivo consolidado.
2. Revisar diccionarios GEIH por año, códigos de no respuesta y valores especiales de P6500 y P6800. El filtro positivo por sí solo no garantiza validez. Contrastar P6500 con el concepto de remuneración relevante y sus componentes.
3. Estimar incertidumbre de los porcentajes con el diseño de encuesta y documentar unidades repetidas. Los registros anuales no son automáticamente personas distintas.
4. Comparar enero–agosto en todos los años, añadir remuneración por hora y explorar sensibilidad del umbral de jornada y de la banda del mínimo.
5. En las densidades, verificar sensibilidad al ancho de banda y al rango. El algoritmo normaliza la masa dentro de la rejilla: al excluir colas, la curva puede representar una distribución condicionada al rango. Las proporciones del cuadro se calculan directamente y no integrando la curva.
6. Para evaluar política juvenil, añadir situación laboral, formalidad, educación, experiencia, sexo, sector y territorio; diseñar identificación y un contrafactual antes de atribuir efectos.

## Fuentes externas consultadas y límites

- [Corte Constitucional, C-815/1999, texto en Función Pública](https://www1.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=3383): respalda que la motivación debe integrar varios parámetros. No establece un techo de 7%.
- [DANE, mercado laboral de la juventud](https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/mercado-laboral-de-la-juventud): referencia para armonizar población y periodos; no se importaron tasas agregadas a este cuadro.

Las proyecciones 6,7–6,9%, los montos y las referencias históricas permanecen como insumos del borrador recibido. No se declara una actualización macroeconómica completa al 1 de noviembre. Antes de difusión: actualizar inflación observada y pronosticada con fecha de publicación; cotejar el monto legal vigente; verificar productividad disponible y decisiones judiciales; revalidar el estudio de Antioquia y completar trazabilidad GEIH. El corte estadístico del cuerpo sigue siendo 29 de octubre de 2026.

## Propuesta de edición breve

Organizar el boletín alrededor de cuatro preguntas: qué decisión se propone y bajo qué condiciones; qué muestran salario y productividad; quiénes están más expuestos, incorporando el cuadro juvenil; y qué alternativas y seguimiento se proponen. Mantener fórmulas, comparación internacional y detalles de reproducción en anexo. La suficiencia del ingreso de los hogares requiere indicadores adicionales de composición familiar y perceptores; no se resuelve con productividad agregada.

## Trabajo realizado

Se conservaron los ocho archivos fuente sin alterarlos y se registraron sus huellas en `insumos/SalarioMinimo_Edad/procedencia.json`. Se generó el cuadro juvenil desde el CSV y se integró una subsección con interpretación y limitaciones al documento LaTeX. Se precisó el lenguaje sobre indexación y el carácter condicional de la recomendación. El generador Word original requiere una tabla externa de PTF: la dependencia está documentada, por lo que no se presenta como un flujo autónomo. No se ejecutó nuevamente el cálculo sobre varios gigabytes de microdatos.
