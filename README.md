# Productividad y salario mínimo

Primer borrador del Centro Javeriano de Competitividad, con corte al 29 de octubre de 2026.

El argumento propone un ajuste del mínimo de 2027 cercano a la inflación de 2026, con un techo provisional de 7% bajo las proyecciones disponibles. Distingue resultados históricos, escenarios y recomendaciones.

## Documento

Compilar `main.tex` en Overleaf o con `tectonic main.tex`. Se conserva la portada, el logo, las márgenes, la tipografía y los encabezados del informe CJC sobre propuestas para el PND.

## Cálculos

`data/series_2021_2025.csv` contiene los insumos y los índices sin redondear. `data/fuentes.json` identifica los anexos públicos del DANE, sus huellas SHA-256 y el alcance. El salario mínimo excluye auxilio de transporte. La figura histórica usa IPC promedio anual. El escenario de 2026 usa IPC de diciembre.

Para reproducir la figura y comprobar los principales acumulados, ejecutar `python scripts/graficas.py`. Requiere `reportlab`. Los cuadros reproducen las fórmulas descritas en el anexo metodológico.

## Alcance del primer borrador

Se incorporan el marco conceptual y el diagnóstico histórico de los dos documentos de Jorge Orozco enviados el 26 y 27 de octubre. Los insumos privados se conservan fuera del repositorio público. Las cifras históricas centrales se recalcularon desde los anexos públicos del DANE.

La clasificación internacional de 35 países y los resultados de microdatos juveniles requieren revisar sus fuentes y scripts antes de usarlos como cifras del informe. La simulación de productividad de enero a septiembre de 2026 tampoco se presenta como una medición anual oficial. La discusión de un mínimo diferenciado por edad queda como una reforma que exige evaluación propia.

Antes de cerrar la versión para publicación deben actualizarse los pronósticos de inflación y la productividad disponible para la concertación, y revisarse las decisiones judiciales que puedan afectar el marco de fijación. El 7% no se presenta como una obligación jurídica ni como un óptimo estimado.
