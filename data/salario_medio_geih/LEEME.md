# Salario medio GEIH para el cuadro del boletín

Preparado el 2 de noviembre de 2026. Fuente: archivos locales `GEIH_2021_total.dta` a `GEIH_2026_total.dta`, en `C:/Users/jorge/Documents/Databases/GEIH`. Se exportan exclusivamente agregados.

## Archivo principal

`salario_medio_comparable_2021_2026.csv` contiene **una fila por año, enero–agosto en todos los años**, con dos conjuntos de columnas: sufijo `_todos` y sufijo `_40h_mas`. Cada media tiene su propio denominador y muestra. Incluye SMLMV sin auxilio de transporte y su razón respecto de cada media, en proporción (multiplicar por 100 para porcentaje).

Las columnas de cada conjunto son:

| Columna | Contenido |
|---|---|
| `media_ponderada_p6500_pesos_*` | Suma ponderada de P6500 dividida entre suma de ponderadores. Pesos nominales mensuales. |
| `suma_ponderadores_*` | Suma de FEX_C18 de los registros incluidos, sin dividir por meses ni expresar en millones. |
| `suma_ponderada_p6500_*` | Numerador de la media: suma de P6500 × FEX_C18. |
| `muestra_registros_*` | Registros válidos de encuesta; no necesariamente personas distintas. |
| `poblacion_promedio_mensual_*` | Suma de ponderadores dividida por ocho, separada del denominador original. |
| `smlmv_sobre_media_*` | SMLMV / media ponderada. |

## Universo y depuración

Ocupados (`OCI=1`) de 15 años o más, posición ocupacional `P6430` en 1, 2, 3 o 7, ponderador `FEX_C18` finito y positivo y salario `P6500` finito y positivo. Se excluyen explícitamente **98 y 99 en P6500**, que son códigos de no respuesta, además de ceros, negativos y faltantes. Los metadatos locales no declaran otros valores perdidos especiales; la auditoría registra los valores bajos y extremos para identificar problemas adicionales. No se impone un umbral monetario arbitrario, no se recortan las colas, no se excluyen remuneraciones inferiores al mínimo y no se restringe a formales. La media de 40 horas exige además `40 <= P6800 <= 168`, con horas finitas; no se observaron horas superiores a 168 en la muestra salarial válida.

Los códigos 98/99 **no se trasladan a otras variables**: en P6800 se interpretan como horas reportadas, no como los códigos monetarios de P6500. Las bases tienen edad en P6040, excepto 2022, donde está en EDAD; la correspondencia queda en el JSON de metadatos.

P6500 mide el ingreso monetario mensual del empleo principal antes de descuentos; no es ingreso laboral total, costo del empleador ni remuneración de todos los ocupados. El diccionario indica incluir propinas y comisiones y excluir subsidios, viáticos y pagos en especie. La ventana usa **mes de encuesta (`MES`)**: enero–agosto de entrevistas, manteniendo la referencia original de P6500 al mes pasado.

## Marco de 2021 y comparabilidad

Se identifica el marco **2018**, de acuerdo con la procedencia confirmada por el responsable de las bases y la revisión de la estructura local. La base 2021 contiene P3038, P3039, P3042, P3043 y la clasificación ocupacional OFICIO_C8, con información en los doce meses; `auditoria_marco_2021_mensual.csv` registra esa continuidad y los ponderadores. No se deduce el marco únicamente de la existencia de FEX_C18: una encuesta del marco anterior también puede incorporar ponderadores calibrados con el censo de 2018. La base consolidada no conserva una etiqueta explícita del marco ni un identificador de la descarga original; se documenta ese límite de trazabilidad.

Usar el mismo marco, universo y ventana temporal mejora la comparación, pero no corrige por sí solo cambios de composición ni diferencias de no respuesta. En enero–agosto de 2021 se excluyen 4.310 registros con P6500=98 y 6.250 con P6500=99; estos códigos no aparecen en los archivos de 2023–2026. La media es condicional a salarios monetarios válidos y positivos, sin imputación adicional de la no respuesta.

## Precisión y agregación

Los CSV utilizan coma como separador y punto decimal, con UTF-8 BOM. No se redondean cifras para presentación: se exporta la representación completa de los resultados float64. La precisión está limitada por los valores numéricos guardados en los archivos Stata; no equivale a precisión decimal infinita. Las sumas utilizan `math.fsum` para reducir errores de acumulación. La media del periodo se calcula agrupando registros y ponderadores; **no** como promedio simple de las medias mensuales. Dividir todos los ponderadores por ocho dejaría inalterada la media, pero aquí se conserva el denominador solicitado sin esa división.

## Respaldo y reproducción

- `salario_medio_enero_agosto_2021_2026.csv`: los mismos resultados en formato largo, 12 filas (año × población).
- `salario_medio_anual_2021_2025.csv`: complemento de enero–diciembre, 10 filas. No mezclar con 2026 enero–agosto como si fueran periodos equivalentes.
- `salario_medio_mensual_2021_2026.csv`: medias, sumas y muestras por mes, 136 filas.
- `auditoria_filtros.csv`: exclusiones y extremos por año y ventana. Las exclusiones son indicadores y no siempre categorías mutuamente excluyentes.
- `metadatos_bases.json`: nombres originales, tamaño de archivos, meses, variables y valores perdidos declarados.
- `auditoria_marco_2021_mensual.csv`: revisión de variables distintivas y continuidad mensual de 2021.

Ejecutar desde la raíz del repositorio: `python scripts/tabular_salario_medio.py`. La opción `--geih-dir` permite cambiar la carpeta de las bases. Requiere Python, numpy, pandas y pyreadstat. El script comprueba los meses, reconcilia muestras y sumas mensuales con el periodo agrupado y no modifica los microdatos. No se estiman errores estándar ni efectos causales.

## Referencias de definición y marco

- [DANE: definición e instrucciones de P6500](https://microdatos.dane.gov.co/index.php/catalog/819/variable/F64/V4097?name=P6500).
- [DANE: horas habituales P6800](https://microdatos.dane.gov.co/index.php/catalog/701/variable/F26/V1463?name=P6800).
- [DANE: metodología GEIH y transición de marcos](https://www.dane.gov.co/files/operaciones/GEIH/DSO-GEIH-MET-001-V11.pdf).
- [DANE: presentación de resultados de la GEIH marco 2018](https://www.dane.gov.co/files/investigaciones/boletines/ech/nuevo-enfoque-conceptual-metodologico-2018/Presentacion-resultados-GEIH2018-agregados.pdf).
