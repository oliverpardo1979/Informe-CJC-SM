# Productividad y salario mínimo

## Revisión del 1 de noviembre de 2026

Ver `REVISION_CRITICA.md` para hallazgos, cambios y verificaciones pendientes. Se incorporó un cuadro de distribución salarial por edad con GEIH 2025 y sus límites de interpretación. Los ocho insumos originales de Javeriana están en `insumos/SalarioMinimo_Edad`, con manifiesto SHA-256 y dependencias documentadas. `python scripts/integrar_revision.py` reproduce el cuadro a partir del CSV importado y conserva su manifiesto de procedencia si no existe la carpeta original. No reestima microdatos. El informe incorpora la actualización normativa y monetaria del 2 de noviembre y fuentes fiscales identificadas por fecha.

Primer borrador del Centro Javeriano de Competitividad. Edición del 2 de noviembre de 2026, con pronósticos identificados por fecha y actualización normativa y monetaria hasta esa fecha.

El argumento propone un ajuste del mínimo de 2027 cercano a la inflación de 2026, con un techo provisional de 7% bajo las proyecciones disponibles. Distingue resultados históricos, escenarios y recomendaciones.

## Documento

Compilar `main.tex` en Overleaf o con `tectonic main.tex`. `nota_tecnica.tex` genera el documento complementario de fuentes y medición. Se conserva la portada, el logo, las márgenes, la tipografía y los encabezados del informe CJC sobre propuestas para el PND.

La cursiva se reserva para usos que aporten información, como distinguir títulos de obras en las referencias y la notación matemática convencional. La portada, los encabezados y la nota de uso de IA se presentan en letra redonda.

## Cálculos

`python scripts/cuadro_salarios_medios.py` integra el cuadro de SMLMV y salario medio desde los tabulados directos de Jorge en `data/salario_medio_geih/salario_medio_comparable_2021_2026.csv`. Usa enero–agosto de entrevistas en todos los años. Reconcilia las 12 medias, sus numeradores, denominadores y muestras con los archivos mensuales y deposita el cuadro LaTeX, `data/smlmv_salario_medio_geih.csv` y un registro de procedencia con SHA-256. Requiere solo la biblioteca estándar de Python y no reestima microdatos. Sustituye la aproximación anterior con poblaciones redondeadas por edad.

El script de origen `scripts/tabular_salario_medio.py` reproduce los tabulados desde los archivos locales GEIH del responsable. Las definiciones, exclusión explícita de P6500=98/99, suma de ponderadores sin redondeo de presentación y auditorías están en `data/salario_medio_geih/LEEME.md`. La nota técnica conserva las limitaciones de identificación del marco de 2021 y de no respuesta. No se estiman errores estándar ni efectos causales.

`python scripts/figura_serie_minimo.py` reproduce la figura de salario nominal y variaciones anuales con el escenario de 7% para 2027. Los antecedentes de Javeriana están en `insumos/PTF_series` y la serie resultante en `data/serie_nominal_2014_2027.csv`. El script usa los archivos locales importados después de la primera copia. Genera PDF vectorial y PNG en `Paper/figures`; no utiliza los supuestos de simulación ni las propuestas de terceros de los gráficos originales.

La figura de distribución salarial por edad se genera con `python scripts/figura_edad.py`. Incluye una caché agregada de densidades, sin microdatos personales. Para recalcular desde GEIH 2025 en la base local, usar `python scripts/figura_edad.py --recalcular`; `--microdatos` permite indicar otra ruta al archivo consolidado. Requiere numpy, pandas, matplotlib y pyreadstat. Genera PDF vectorial y PNG de 300 ppp en `Paper/figures`. El método de suavizado reproduce el original; la normalización corresponde a la masa dentro del rango de estimación. Las medianas, los tamaños de muestra y las proporciones alrededor del mínimo se contrastan con el CSV de Javeriana al recalcular.

`data/series_2021_2025.csv` contiene los insumos y los índices sin redondear. `data/fuentes.json` identifica los anexos públicos del DANE, sus huellas SHA-256 y el alcance. El salario mínimo excluye auxilio de transporte. La figura histórica usa IPC promedio anual. El escenario de 2026 usa IPC de diciembre.

Para reproducir la figura y comprobar los principales acumulados, ejecutar `python scripts/graficas.py`. Requiere `reportlab`. Los cuadros reproducen las fórmulas descritas en la nota técnica de fuentes y medición.

## Alcance del primer borrador

La revisión bibliográfica de Jorge Orozco enviada el 26 de octubre es la base de la comparación internacional situada dentro de la propuesta para 2027. Se conservan la distinción entre nivel, actualización y salvaguardas, seis mecanismos documentados en América y sus implicaciones para la propuesta de 2027. Los ejemplos de Canadá, Perú, Costa Rica, México y Estados Unidos se cotejaron con fuentes oficiales y se mantiene el marco colombiano. Los insumos privados se conservan fuera del repositorio público. Las cifras históricas centrales se recalcularon desde los anexos públicos del DANE.

El cuadro internacional no es un censo de los 35 países. La cifra de 12 de 35 del insumo original requiere revisar la evidencia por país y separar productividad laboral, PTF y crecimiento por habitante antes de utilizarla como resultado del informe. Los resultados de microdatos juveniles requieren revisar sus fuentes y scripts. La simulación de productividad de enero a septiembre de 2026 tampoco se presenta como una medición anual oficial. La discusión de un mínimo diferenciado por edad queda como una reforma que exige evaluación propia.

Antes de cerrar la versión para publicación deben actualizarse los pronósticos de inflación y la productividad disponible para la concertación, y revisarse las decisiones judiciales que puedan afectar el marco de fijación. El 7% no se presenta como una obligación jurídica ni como un óptimo estimado.

Se incorpora una referencia breve al estudio de Patiño, Chaparro y coautores (EAFIT, agosto de 2026). Se distinguen empleos que dejan de crearse, destrucción de puestos y compresión salarial. Los resultados se atribuyen a sus autores y se mantienen en su ámbito de Antioquia. No se extrapolan a Colombia ni se multiplican por el aumento de 2026. El periodo de la regresión es enero de 2022 a febrero de 2026, distinto del periodo de la base descrito en el resumen del estudio.

## Estructura y revisión fiscal del 2 de noviembre de 2026

El informe sigue seis secciones: introducción, salarios y productividad, creación de empleo y compresión salarial, costos fiscales, propuesta para 2027 y conclusiones. La introducción presenta el problema, el objetivo y la recomendación, y después explica la fijación del mínimo y la negociación reciente. Las conclusiones cierran el argumento antes de las referencias. El resumen ejecutivo reúne cinco mensajes. El informe principal no tiene apéndices. La nota técnica conserva los procedimientos, los cuadros de cambios anuales, distribución por edad y escenarios alternativos, y las definiciones y limitaciones del salario medio GEIH.

La sección fiscal utiliza el MFMP 2026, páginas 60–61, 125 y 164–166, y el Comunicado 22 del CARF. Distingue la estimación preliminar del aumento de 2026 frente al 7,1% presupuestado del ejercicio del MFMP que incrementa un punto adicional cada año sobre su senda base. No se suman ambas estimaciones ni se presentan como ahorro de un ajuste de 7% en 2027. La cobertura de rentas vitalicias y los contratos de vigilancia y aseo se identifican sin imputar un costo total no observado. Los pagos históricos de deslizamiento se atribuyen a Hacienda y no al aumento de 2026.

## Revisión del 3 de noviembre de 2026

Se aplicó Meta Skill Review Oliver con una revisión sustantiva single-pass y una auditoría acotada de cifras propias. La condición de convergencia exige que la productividad crezca más rápido que el mínimo real. Se precisaron el comparador fiscal por componente, el redondeo de movilidad de Antioquia y la referencia temporal del ingreso GEIH. El script juvenil conserva y comprueba los insumos importados cuando falta la carpeta original, admitiendo únicamente diferencias LF/CRLF en los archivos de texto indicados. Los registros de auditoría y sus límites están en `quality_reports/`.
