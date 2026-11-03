# Referencias bibliográficas del informe CJC

Revisión acotada del 3 de noviembre de 2026, sobre los cambios de Oliver en `c903565`. Se conservaron el resumen ejecutivo, el subtítulo y la etiqueta de edición de esa versión. Se recuperó una cita del resumen que había quedado dentro de un comentario de LaTeX.

## Cambios

Se sustituyeron las llamadas numéricas y las bibliografías manuales por `natbib`, estilo académico `abbrvnat`, citas autor–año con hipervínculo y una base compartida, `Paper/referencias.bib`. Las fuentes de tablas y figuras también tienen llamadas bibliográficas. Las normas antes agrupadas bajo una sola clave se identifican por separado. Los sufijos de los años institucionales se mantienen entre los dos documentos.

El estudio de Antioquia se cita como Patiño et al. (2026). La entrada incluye los siete autores, título, serie, número 9, Universidad EAFIT, agosto y enlace institucional. Las llamadas a sus resultados precisan tabla C.1, pp. 33–34, y p. 22 para movilidad salarial. La atribución y los metadatos se contrastaron con el PDF institucional conservado en la sesión. El enlace institucional respondió HTTP 200. No se asignó un DOI inexistente.

Se contrastaron con las páginas primarias los metadatos de Dube (2019), Arango-Thomas et al. (2022), la publicación de Bancolombia y Castellares et al. (2024). ESPE 103 conserva su DOI enlazado. La ficha de BCRP confirma autores y fecha de la referencia peruana. Su PDF presenta restricciones de acceso automatizado, por lo que no se añadieron páginas sin verificarlas en el original. La revisión interna del CJC se identifica como documento no publicado y no recibe un enlace público inventado.

## Verificación

`python scripts/verificar_referencias.py` pasó en ambos documentos después de compilarlos. El archivo JSON adjunto registra claves y recuentos. Se comprobó correspondencia entre citas activas y entradas renderizadas, metadatos básicos presentes, años consistentes, destinos internos, URLs y DOI presentes en las anotaciones del PDF. No hay citas indefinidas, avisos de BibTeX ni desbordamientos de texto o enlaces fuera de página.

Se renderizaron todas las páginas de ambos documentos. Se inspeccionaron sus mosaicos y, a tamaño de lectura, las citas de Patiño et al., la tabla comparada y las referencias. La revisión visual confirmó legibilidad, enlaces sin desbordamientos y conservación del formato CJC.

## Alcance y regla persistente

El control mecánico no acredita por sí solo la exactitud de todos los metadatos, la disponibilidad en línea de cada URL ni el respaldo de cada afirmación. Esta corrección no repite la auditoría económica anterior ni presenta una auditoría bibliográfica integral como completada.

Se añadió un control bibliográfico mínimo obligatorio a `meta-skill-review-oliver` y se guardó la preferencia de formato académico autor–año en `voz-oliver-pardo` y su guía de informes. El control abarca resumen, cuerpo, notas, tablas, figuras y documentos complementarios, exige revisar los enlaces del PDF y distingue esta revisión mínima de `bibcheck-cunningham`. Ambas skills pasaron `quick_validate.py` del Skill Creator. Las versiones anteriores se conservaron localmente antes de modificarlas.
