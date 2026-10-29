# Productividad y salario mínimo

Primer borrador del Centro Javeriano de Competitividad, con corte al 29 de octubre de 2026.

El argumento propone un ajuste del mínimo de 2027 cercano a la inflación de 2026, con un techo provisional de 7% bajo las proyecciones disponibles. Distingue resultados históricos, escenarios y recomendaciones.

## Documento

Compilar `main.tex` en Overleaf o con `tectonic main.tex`. Se conserva la portada, el logo, las márgenes, la tipografía y los encabezados del informe CJC sobre propuestas para el PND.

## Cálculos

`data/series_2021_2025.csv` contiene los insumos y los índices sin redondear. `data/fuentes.json` identifica los anexos públicos del DANE, sus huellas SHA-256 y el alcance. El salario mínimo excluye auxilio de transporte. La figura histórica usa IPC promedio anual. El escenario de 2026 usa IPC de diciembre.

Para reproducir la figura y comprobar los principales acumulados, ejecutar `python scripts/graficas.py`. Requiere `reportlab`. Los cuadros reproducen las fórmulas descritas en el anexo metodológico.

## Alcance del primer borrador

La revisión bibliográfica de Jorge Orozco enviada el 26 de octubre es la base de una sección propia, situada antes del diagnóstico colombiano. Se desarrollan la distinción entre nivel, actualización y salvaguardas, seis mecanismos documentados en América y sus implicaciones para la propuesta de 2027. Los ejemplos de Canadá, Perú, Costa Rica, México y Estados Unidos se cotejaron con fuentes oficiales y se mantiene el marco colombiano. Los insumos privados se conservan fuera del repositorio público. Las cifras históricas centrales se recalcularon desde los anexos públicos del DANE.

El cuadro internacional no es un censo de los 35 países. La cifra de 12 de 35 del insumo original requiere revisar la evidencia por país y separar productividad laboral, PTF y crecimiento por habitante antes de utilizarla como resultado del informe. Los resultados de microdatos juveniles requieren revisar sus fuentes y scripts. La simulación de productividad de enero a septiembre de 2026 tampoco se presenta como una medición anual oficial. La discusión de un mínimo diferenciado por edad queda como una reforma que exige evaluación propia.

Antes de cerrar la versión para publicación deben actualizarse los pronósticos de inflación y la productividad disponible para la concertación, y revisarse las decisiones judiciales que puedan afectar el marco de fijación. El 7% no se presenta como una obligación jurídica ni como un óptimo estimado.
