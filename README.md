# Productividad y salario mínimo

## Revisión del 1 de noviembre de 2026

Ver `REVISION_CRITICA.md` para hallazgos, cambios y verificaciones pendientes. Se incorporó un cuadro de distribución salarial por edad con GEIH 2025 y sus límites de interpretación. Los ocho insumos originales de Javeriana están en `insumos/SalarioMinimo_Edad`, con manifiesto SHA-256 y dependencias documentadas. `python scripts/integrar_revision.py` reproduce el cuadro a partir del CSV importado; no reestima microdatos. El corte macroeconómico del cuerpo sigue siendo el 29 de octubre.

Primer borrador del Centro Javeriano de Competitividad, con corte al 29 de octubre de 2026.

El argumento propone un ajuste del mínimo de 2027 cercano a la inflación de 2026, con un techo provisional de 7% bajo las proyecciones disponibles. Distingue resultados históricos, escenarios y recomendaciones.

## Documento

Compilar `main.tex` en Overleaf o con `tectonic main.tex`. Se conserva la portada, el logo, las márgenes, la tipografía y los encabezados del informe CJC sobre propuestas para el PND.

La cursiva se reserva para usos que aporten información, como distinguir títulos de obras en las referencias y la notación matemática convencional. La portada, los encabezados y la nota de uso de IA se presentan en letra redonda.

## Cálculos

`python scripts/figura_serie_minimo.py` reproduce la figura de salario nominal y variaciones anuales con el escenario de 7% para 2027. Los antecedentes de Javeriana están en `insumos/PTF_series` y la serie resultante en `data/serie_nominal_2014_2027.csv`. El script usa los archivos locales importados después de la primera copia. Genera PDF vectorial y PNG en `Paper/figures`; no utiliza los supuestos de simulación ni las propuestas de terceros de los gráficos originales.

La figura de distribución salarial por edad se genera con `python scripts/figura_edad.py`. Incluye una caché agregada de densidades, sin microdatos personales. Para recalcular desde GEIH 2025 en la base local, usar `python scripts/figura_edad.py --recalcular`; `--microdatos` permite indicar otra ruta al archivo consolidado. Requiere numpy, pandas, matplotlib y pyreadstat. Genera PDF vectorial y PNG de 300 ppp en `Paper/figures`. El método de suavizado reproduce el original; la normalización corresponde a la masa dentro del rango de estimación. Las medianas, los tamaños de muestra y las proporciones alrededor del mínimo se contrastan con el CSV de Javeriana al recalcular.

`data/series_2021_2025.csv` contiene los insumos y los índices sin redondear. `data/fuentes.json` identifica los anexos públicos del DANE, sus huellas SHA-256 y el alcance. El salario mínimo excluye auxilio de transporte. La figura histórica usa IPC promedio anual. El escenario de 2026 usa IPC de diciembre.

Para reproducir la figura y comprobar los principales acumulados, ejecutar `python scripts/graficas.py`. Requiere `reportlab`. Los cuadros reproducen las fórmulas descritas en el anexo metodológico.

## Alcance del primer borrador

La revisión bibliográfica de Jorge Orozco enviada el 26 de octubre es la base de una sección propia, situada antes del diagnóstico colombiano. Se desarrollan la distinción entre nivel, actualización y salvaguardas, seis mecanismos documentados en América y sus implicaciones para la propuesta de 2027. Los ejemplos de Canadá, Perú, Costa Rica, México y Estados Unidos se cotejaron con fuentes oficiales y se mantiene el marco colombiano. Los insumos privados se conservan fuera del repositorio público. Las cifras históricas centrales se recalcularon desde los anexos públicos del DANE.

El cuadro internacional no es un censo de los 35 países. La cifra de 12 de 35 del insumo original requiere revisar la evidencia por país y separar productividad laboral, PTF y crecimiento por habitante antes de utilizarla como resultado del informe. Los resultados de microdatos juveniles requieren revisar sus fuentes y scripts. La simulación de productividad de enero a septiembre de 2026 tampoco se presenta como una medición anual oficial. La discusión de un mínimo diferenciado por edad queda como una reforma que exige evaluación propia.

Antes de cerrar la versión para publicación deben actualizarse los pronósticos de inflación y la productividad disponible para la concertación, y revisarse las decisiones judiciales que puedan afectar el marco de fijación. El 7% no se presenta como una obligación jurídica ni como un óptimo estimado.

Se incorpora una referencia breve al estudio de Patiño, Chaparro y coautores (EAFIT, agosto de 2026). Se distinguen empleos que dejan de crearse, destrucción de puestos y compresión salarial. Las cifras de la tabla C.1 se atribuyen a sus autores y se mantienen en su ámbito de Antioquia. No se extrapolan a Colombia ni se multiplican por el aumento de 2026. El periodo de la regresión es enero de 2022 a febrero de 2026, distinto del periodo de la base descrito en el resumen del estudio.
