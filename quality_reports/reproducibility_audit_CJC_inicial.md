# Auditoría acotada de reproducibilidad del CJC

Fecha: 3 de noviembre de 2026. Fase: inicial.

Se cotejan cifras propias contra CSV, JSON y PDF vectorial. No se reestiman microdatos GEIH ni modelos de fuentes externas. La comprobación de tokens en PDF verifica presencia, no unicidad semántica. Los tres gráficos también se leen por etiquetas y se inspeccionan visualmente.

Claims: 79. PASS: 79. FAIL: 0. Discrepancias de compilación: 0. Etiquetas de figura: 16, ausentes: 0.

## Cifras propias

| ID | Ubicación | Texto | Cálculo | Tolerancia | Estado |
|---|---|---:|---:|---:|---|
| SM_2021 | Paper/sections/CuadroSalariosMedios.tex:12 | 908526 | 908526 | 0 | PASS |
| AUMENTO_2021 | Paper/sections/CuadroSalariosMedios.tex:12 | 3.5 | 3.49998804 | 0.005 | PASS |
| MEDIA_2021_todos | Paper/sections/CuadroSalariosMedios.tex:12 | 1.53 | 1.53254283 | 0.005 | PASS |
| MEDIA_2021_40h_mas | Paper/sections/CuadroSalariosMedios.tex:12 | 1.6 | 1.60370139 | 0.005 | PASS |
| SM_2022 | Paper/sections/CuadroSalariosMedios.tex:13 | 1e+06 | 1000000 | 0 | PASS |
| AUMENTO_2022 | Paper/sections/CuadroSalariosMedios.tex:13 | 10.07 | 10.0683965 | 0.005 | PASS |
| MEDIA_2022_todos | Paper/sections/CuadroSalariosMedios.tex:13 | 1.65 | 1.64792835 | 0.005 | PASS |
| MEDIA_2022_40h_mas | Paper/sections/CuadroSalariosMedios.tex:13 | 1.73 | 1.72956345 | 0.005 | PASS |
| SM_2023 | Paper/sections/CuadroSalariosMedios.tex:14 | 1.16e+06 | 1160000 | 0 | PASS |
| AUMENTO_2023 | Paper/sections/CuadroSalariosMedios.tex:14 | 16 | 16 | 0.005 | PASS |
| MEDIA_2023_todos | Paper/sections/CuadroSalariosMedios.tex:14 | 1.85 | 1.85316848 | 0.005 | PASS |
| MEDIA_2023_40h_mas | Paper/sections/CuadroSalariosMedios.tex:14 | 1.95 | 1.94741803 | 0.005 | PASS |
| SM_2024 | Paper/sections/CuadroSalariosMedios.tex:15 | 1.3e+06 | 1300000 | 0 | PASS |
| AUMENTO_2024 | Paper/sections/CuadroSalariosMedios.tex:15 | 12.07 | 12.0689655 | 0.005 | PASS |
| MEDIA_2024_todos | Paper/sections/CuadroSalariosMedios.tex:15 | 2.01 | 2.00799541 | 0.005 | PASS |
| MEDIA_2024_40h_mas | Paper/sections/CuadroSalariosMedios.tex:15 | 2.11 | 2.11394442 | 0.005 | PASS |
| SM_2025 | Paper/sections/CuadroSalariosMedios.tex:16 | 1.4235e+06 | 1423500 | 0 | PASS |
| AUMENTO_2025 | Paper/sections/CuadroSalariosMedios.tex:16 | 9.5 | 9.5 | 0.005 | PASS |
| MEDIA_2025_todos | Paper/sections/CuadroSalariosMedios.tex:16 | 2.16 | 2.15977662 | 0.005 | PASS |
| MEDIA_2025_40h_mas | Paper/sections/CuadroSalariosMedios.tex:16 | 2.25 | 2.25339366 | 0.005 | PASS |
| SM_2026 | Paper/sections/CuadroSalariosMedios.tex:17 | 1.7509e+06 | 1750905 | 0 | PASS |
| AUMENTO_2026 | Paper/sections/CuadroSalariosMedios.tex:17 | 23 | 23 | 0.005 | PASS |
| MEDIA_2026_todos | Paper/sections/CuadroSalariosMedios.tex:17 | 2.57 | 2.56790193 | 0.005 | PASS |
| MEDIA_2026_40h_mas | Paper/sections/CuadroSalariosMedios.tex:17 | 2.7 | 2.69924166 | 0.005 | PASS |
| ANUAL_2022_0 | Paper/sections/Metodologia.tex:31 | 10.07 | 10.0683965 | 0.005 | PASS |
| ANUAL_2022_1 | Paper/sections/Metodologia.tex:31 | -0.1 | -0.098059944 | 0.005 | PASS |
| ANUAL_2022_2 | Paper/sections/Metodologia.tex:31 | -2.7 | -2.69999163 | 0.005 | PASS |
| ANUAL_2022_3 | Paper/sections/Metodologia.tex:31 | -0.28 | -0.284062524 | 0.005 | PASS |
| ANUAL_2022_4 | Paper/sections/Metodologia.tex:31 | -2.2 | -2.20280932 | 0.005 | PASS |
| ANUAL_2023_0 | Paper/sections/Metodologia.tex:32 | 16 | 16 | 0.005 | PASS |
| ANUAL_2023_1 | Paper/sections/Metodologia.tex:32 | 3.82 | 3.81560204 | 0.005 | PASS |
| ANUAL_2023_2 | Paper/sections/Metodologia.tex:32 | 6.15 | 6.15364508 | 0.005 | PASS |
| ANUAL_2023_3 | Paper/sections/Metodologia.tex:32 | -1.1 | -1.10195312 | 0.005 | PASS |
| ANUAL_2023_4 | Paper/sections/Metodologia.tex:32 | -2.49 | -2.48609047 | 0.005 | PASS |
| ANUAL_2024_0 | Paper/sections/Metodologia.tex:33 | 12.07 | 12.0689655 | 0.005 | PASS |
| ANUAL_2024_1 | Paper/sections/Metodologia.tex:33 | 5.12 | 5.12129909 | 0.005 | PASS |
| ANUAL_2024_2 | Paper/sections/Metodologia.tex:33 | 6.53 | 6.53049373 | 0.005 | PASS |
| ANUAL_2024_3 | Paper/sections/Metodologia.tex:33 | 2.23 | 2.22576434 | 0.005 | PASS |
| ANUAL_2024_4 | Paper/sections/Metodologia.tex:33 | 0.55 | 0.55250203 | 0.005 | PASS |
| ANUAL_2025_0 | Paper/sections/Metodologia.tex:34 | 9.5 | 9.5 | 0.005 | PASS |
| ANUAL_2025_1 | Paper/sections/Metodologia.tex:34 | 4.14 | 4.144101 | 0.005 | PASS |
| ANUAL_2025_2 | Paper/sections/Metodologia.tex:34 | 4.19 | 4.18572273 | 0.005 | PASS |
| ANUAL_2025_3 | Paper/sections/Metodologia.tex:34 | 0.4 | 0.402731651 | 0.005 | PASS |
| ANUAL_2025_4 | Paper/sections/Metodologia.tex:34 | -0.56 | -0.559123727 | 0.005 | PASS |
| ESCENARIO_6,7_0 | Paper/sections/CuadroEscenarios.tex:9 | 117311 | 117311 | 0 | PASS |
| ESCENARIO_6,7_1 | Paper/sections/CuadroEscenarios.tex:9 | 1.86822e+06 | 1868216 | 0 | PASS |
| ESCENARIO_6,8_0 | Paper/sections/CuadroEscenarios.tex:10 | 119062 | 119062 | 0 | PASS |
| ESCENARIO_6,8_1 | Paper/sections/CuadroEscenarios.tex:10 | 1.86997e+06 | 1869967 | 0 | PASS |
| ESCENARIO_6,9_0 | Paper/sections/CuadroEscenarios.tex:11 | 120812 | 120812 | 0 | PASS |
| ESCENARIO_6,9_1 | Paper/sections/CuadroEscenarios.tex:11 | 1.87172e+06 | 1871717 | 0 | PASS |
| ESCENARIO_7,0_0 | Paper/sections/CuadroEscenarios.tex:12 | 122563 | 122563 | 0 | PASS |
| ESCENARIO_7,0_1 | Paper/sections/CuadroEscenarios.tex:12 | 1.87347e+06 | 1873468 | 0 | PASS |
| REAL_ACUMULADO_ResumenEjecutivo | Paper/sections/ResumenEjecutivo.tex:5 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Cuerpo | Paper/sections/Cuerpo.tex:35 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Conclusiones | Paper/sections/Conclusiones.tex:3 | 13.5 | 13.5434128 | 0.1 | PASS |
| PL_HORA_ACUMULADO_ResumenEjecutivo | Paper/sections/ResumenEjecutivo.tex:5 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Cuerpo | Paper/sections/Cuerpo.tex:35 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Conclusiones | Paper/sections/Conclusiones.tex:3 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_PERSONA_CAIDA_ResumenEjecutivo | Paper/sections/ResumenEjecutivo.tex:5 | 4.6 | 4.64339682 | 0.1 | PASS |
| PL_PERSONA_CAIDA_Cuerpo | Paper/sections/Cuerpo.tex:35 | 4.6 | 4.64339682 | 0.1 | PASS |
| REAL_2026_ResumenEjecutivo | Paper/sections/ResumenEjecutivo.tex:5 | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Cuerpo | Paper/sections/Cuerpo.tex:49 | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Metodologia | Paper/sections/Metodologia.tex:19 | 15.1 | 15.0608045 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_0 | Paper/sections/CuadroEdad.tex:9 | 81.3 | 81.25 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_1 | Paper/sections/CuadroEdad.tex:9 | 60.2 | 60.24 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_0 | Paper/sections/CuadroEdad.tex:10 | 3.8 | 3.8 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_1 | Paper/sections/CuadroEdad.tex:10 | 19.6 | 19.56 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_0 | Paper/sections/CuadroEdad.tex:11 | 34.8 | 34.79 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_1 | Paper/sections/CuadroEdad.tex:11 | 28.3 | 28.28 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_0 | Paper/sections/CuadroEdad.tex:12 | 30.3 | 30.3 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_1 | Paper/sections/CuadroEdad.tex:12 | 18.1 | 18.09 | 0.1 | PASS |
| RAZON_2021_todos | Paper/sections/Cuerpo.tex:29 | 59.3 | 59.2822582 | 0.1 | PASS |
| RAZON_2026_todos | Paper/sections/Cuerpo.tex:29 | 68.2 | 68.1842627 | 0.1 | PASS |
| RAZON_2025_todos | Paper/sections/Cuerpo.tex:29 | 65.9 | 65.9095938 | 0.1 | PASS |
| RAZON_2021_40h_mas | Paper/sections/Cuerpo.tex:31 | 56.7 | 56.6518185 | 0.1 | PASS |
| RAZON_2026_40h_mas | Paper/sections/Cuerpo.tex:31 | 64.9 | 64.8665523 | 0.1 | PASS |
| EXCLUSION_10.560 | Paper/sections/Metodologia.tex:15 | 10560 | 10560 | 0 | PASS |
| EXCLUSION_2.223 | Paper/sections/Metodologia.tex:15 | 2223 | 2223 | 0 | PASS |
| EXCLUSION_303 | Paper/sections/Metodologia.tex:15 | 303 | 303 | 0 | PASS |

## Límites de la comprobación horizontal

Se revisan las apariciones del informe principal, nota técnica y tres figuras, sin diapositivas ni archivos privados originales. No hay passport con declaraciones exhaustivas de todos los displays. Los accesores y contextos literales están en el JSON de claims. Se usa redondeo de presentación más estricto para celdas de dos decimales. Los enteros en pesos usan redondeo al peso antes del cotejo.

## Cifras atribuidas a terceros

Las cifras fiscales del MFMP y CARF, los pronósticos, las transiciones de Antioquia y los plazos normativos no son resultados de este pipeline. Se verifican contra fuentes primarias en el informe sustantivo y quedan fuera del PASS de reproducibilidad propia. No se reproducen sus modelos. Tampoco se declara validación del diseño muestral, de la identificación causal ni de las estimaciones de los autores externos.

## Sensibilidad de meses

| Año | Media febrero–agosto entrevistas | SMLMV/media (%) |
|---|---:|---:|
| 2021 | 1540246.75 | 58.9857 |
| 2022 | 1654554.10 | 60.4392 |
| 2023 | 1870032.26 | 62.0310 |
| 2024 | 2008560.97 | 64.7230 |
| 2025 | 2157506.53 | 65.9789 |
| 2026 | 2580975.85 | 67.8389 |

P6500 refiere al mes anterior. Excluir enero evita que la ventana contenga salarios de diciembre del año previo. Es una sensibilidad descriptiva, no una corrección de composición o no respuesta. La tabla principal sigue usando enero–agosto.
