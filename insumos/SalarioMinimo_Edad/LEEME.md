# Insumos importados de Javeriana

Copia del 1 de noviembre de 2026. `procedencia.json` registra origen y SHA-256. Los ocho archivos originales se conservan sin modificaciones. Se excluyeron renders de revisión de `qa`; se preservó el boletín Word, su generador, las figuras y los resultados. No se copiaron microdatos GEIH, que ocupan varios gigabytes y permanecen en la base local.

`python scripts/integrar_revision.py`, desde la raíz de Informe-CJC-SM, verifica las copias y genera `Paper/sections/CuadroEdad.tex` con el CSV. No recalcula microdatos: las cifras son resultados previos, cotejados con el código y la tabla.

El script original de kernels mantiene una ruta absoluta a `C:/Users/jorge/Documents/Databases/GEIH`. Requiere numpy, pandas, matplotlib y pyreadstat. Antes de recalcular deben auditarse meses efectivamente presentes, filtros de valores especiales, ponderadores y diccionario de variables. No ejecutar automáticamente el generador Word: depende también de `PTF/Outputs/tables/indice_salario_minimo_real_productividad_2010_2025.csv`, que no forma parte de esta importación. Su primera figura es un antecedente, no la fuente de la serie principal de este repositorio.

El cuadro incorporado usa 2025 completo. El script define jóvenes como 15–24 años y mayores como 25 o más, posiciones 1, 2, 3 y 7, P6500 positivo, OCI igual a 1 y FEX_C18 positivo. El filtro adicional es P6800 >= 40. No identifica formalidad. Los resultados 2026 son enero–agosto y no se comparan como un año completo. La banda alrededor del mínimo es ±3%; las densidades están suavizadas sobre logaritmos y no son porcentajes de personas en cada punto.

Los antecedentes se incluyen en el repositorio para facilitar el trabajo conjunto y la trazabilidad del boletín.
