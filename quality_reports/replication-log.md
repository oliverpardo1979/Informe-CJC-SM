# Replication log

Registro acumulativo. Las correcciones se añaden como nuevas entradas.

## 2026-11-03 — CJC @ 6eebcf8 — inicial

79 cifras propias. 0 FAIL, 0 discrepancias PDF, 0 etiquetas ausentes.

| ID | Fuente/cálculo | Reportado | Calculado | Tolerancia | Estado |
|---|---|---:|---:|---:|---|
| SM_2021 | monto legal depositado 2021 | 908526 | 908526 | 0 | PASS |
| AUMENTO_2021 | 100*(SM[2021]/SM[2020]-1) | 3.5 | 3.49998804 | 0.005 | PASS |
| MEDIA_2021_todos | sum(meses 1:8 numerador 2021,todos_asalariados)/sum(ponderador)/1e6 | 1.53 | 1.53254283 | 0.005 | PASS |
| MEDIA_2021_40h_mas | sum(meses 1:8 numerador 2021,jornada_40h_mas)/sum(ponderador)/1e6 | 1.6 | 1.60370139 | 0.005 | PASS |
| SM_2022 | monto legal depositado 2022 | 1e+06 | 1000000 | 0 | PASS |
| AUMENTO_2022 | 100*(SM[2022]/SM[2021]-1) | 10.07 | 10.0683965 | 0.005 | PASS |
| MEDIA_2022_todos | sum(meses 1:8 numerador 2022,todos_asalariados)/sum(ponderador)/1e6 | 1.65 | 1.64792835 | 0.005 | PASS |
| MEDIA_2022_40h_mas | sum(meses 1:8 numerador 2022,jornada_40h_mas)/sum(ponderador)/1e6 | 1.73 | 1.72956345 | 0.005 | PASS |
| SM_2023 | monto legal depositado 2023 | 1.16e+06 | 1160000 | 0 | PASS |
| AUMENTO_2023 | 100*(SM[2023]/SM[2022]-1) | 16 | 16 | 0.005 | PASS |
| MEDIA_2023_todos | sum(meses 1:8 numerador 2023,todos_asalariados)/sum(ponderador)/1e6 | 1.85 | 1.85316848 | 0.005 | PASS |
| MEDIA_2023_40h_mas | sum(meses 1:8 numerador 2023,jornada_40h_mas)/sum(ponderador)/1e6 | 1.95 | 1.94741803 | 0.005 | PASS |
| SM_2024 | monto legal depositado 2024 | 1.3e+06 | 1300000 | 0 | PASS |
| AUMENTO_2024 | 100*(SM[2024]/SM[2023]-1) | 12.07 | 12.0689655 | 0.005 | PASS |
| MEDIA_2024_todos | sum(meses 1:8 numerador 2024,todos_asalariados)/sum(ponderador)/1e6 | 2.01 | 2.00799541 | 0.005 | PASS |
| MEDIA_2024_40h_mas | sum(meses 1:8 numerador 2024,jornada_40h_mas)/sum(ponderador)/1e6 | 2.11 | 2.11394442 | 0.005 | PASS |
| SM_2025 | monto legal depositado 2025 | 1.4235e+06 | 1423500 | 0 | PASS |
| AUMENTO_2025 | 100*(SM[2025]/SM[2024]-1) | 9.5 | 9.5 | 0.005 | PASS |
| MEDIA_2025_todos | sum(meses 1:8 numerador 2025,todos_asalariados)/sum(ponderador)/1e6 | 2.16 | 2.15977662 | 0.005 | PASS |
| MEDIA_2025_40h_mas | sum(meses 1:8 numerador 2025,jornada_40h_mas)/sum(ponderador)/1e6 | 2.25 | 2.25339366 | 0.005 | PASS |
| SM_2026 | monto legal depositado 2026 | 1.7509e+06 | 1750905 | 0 | PASS |
| AUMENTO_2026 | 100*(SM[2026]/SM[2025]-1) | 23 | 23 | 0.005 | PASS |
| MEDIA_2026_todos | sum(meses 1:8 numerador 2026,todos_asalariados)/sum(ponderador)/1e6 | 2.57 | 2.56790193 | 0.005 | PASS |
| MEDIA_2026_40h_mas | sum(meses 1:8 numerador 2026,jornada_40h_mas)/sum(ponderador)/1e6 | 2.7 | 2.69924166 | 0.005 | PASS |
| ANUAL_2022_0 | cálculo directo CSV, métrica 0, año 2022 | 10.07 | 10.0683965 | 0.005 | PASS |
| ANUAL_2022_1 | cálculo directo CSV, métrica 1, año 2022 | -0.1 | -0.098059944 | 0.005 | PASS |
| ANUAL_2022_2 | cálculo directo CSV, métrica 2, año 2022 | -2.7 | -2.69999163 | 0.005 | PASS |
| ANUAL_2022_3 | cálculo directo CSV, métrica 3, año 2022 | -0.28 | -0.284062524 | 0.005 | PASS |
| ANUAL_2022_4 | cálculo directo CSV, métrica 4, año 2022 | -2.2 | -2.20280932 | 0.005 | PASS |
| ANUAL_2023_0 | cálculo directo CSV, métrica 0, año 2023 | 16 | 16 | 0.005 | PASS |
| ANUAL_2023_1 | cálculo directo CSV, métrica 1, año 2023 | 3.82 | 3.81560204 | 0.005 | PASS |
| ANUAL_2023_2 | cálculo directo CSV, métrica 2, año 2023 | 6.15 | 6.15364508 | 0.005 | PASS |
| ANUAL_2023_3 | cálculo directo CSV, métrica 3, año 2023 | -1.1 | -1.10195312 | 0.005 | PASS |
| ANUAL_2023_4 | cálculo directo CSV, métrica 4, año 2023 | -2.49 | -2.48609047 | 0.005 | PASS |
| ANUAL_2024_0 | cálculo directo CSV, métrica 0, año 2024 | 12.07 | 12.0689655 | 0.005 | PASS |
| ANUAL_2024_1 | cálculo directo CSV, métrica 1, año 2024 | 5.12 | 5.12129909 | 0.005 | PASS |
| ANUAL_2024_2 | cálculo directo CSV, métrica 2, año 2024 | 6.53 | 6.53049373 | 0.005 | PASS |
| ANUAL_2024_3 | cálculo directo CSV, métrica 3, año 2024 | 2.23 | 2.22576434 | 0.005 | PASS |
| ANUAL_2024_4 | cálculo directo CSV, métrica 4, año 2024 | 0.55 | 0.55250203 | 0.005 | PASS |
| ANUAL_2025_0 | cálculo directo CSV, métrica 0, año 2025 | 9.5 | 9.5 | 0.005 | PASS |
| ANUAL_2025_1 | cálculo directo CSV, métrica 1, año 2025 | 4.14 | 4.144101 | 0.005 | PASS |
| ANUAL_2025_2 | cálculo directo CSV, métrica 2, año 2025 | 4.19 | 4.18572273 | 0.005 | PASS |
| ANUAL_2025_3 | cálculo directo CSV, métrica 3, año 2025 | 0.4 | 0.402731651 | 0.005 | PASS |
| ANUAL_2025_4 | cálculo directo CSV, métrica 4, año 2025 | -0.56 | -0.559123727 | 0.005 | PASS |
| ESCENARIO_6,7_0 | ROUND_HALF_UP(SM2026*6.7/100) | 117311 | 117311 | 0 | PASS |
| ESCENARIO_6,7_1 | ROUND_HALF_UP(SM2026*6.7/100 + SM2026) | 1.86822e+06 | 1868216 | 0 | PASS |
| ESCENARIO_6,8_0 | ROUND_HALF_UP(SM2026*6.8/100) | 119062 | 119062 | 0 | PASS |
| ESCENARIO_6,8_1 | ROUND_HALF_UP(SM2026*6.8/100 + SM2026) | 1.86997e+06 | 1869967 | 0 | PASS |
| ESCENARIO_6,9_0 | ROUND_HALF_UP(SM2026*6.9/100) | 120812 | 120812 | 0 | PASS |
| ESCENARIO_6,9_1 | ROUND_HALF_UP(SM2026*6.9/100 + SM2026) | 1.87172e+06 | 1871717 | 0 | PASS |
| ESCENARIO_7,0_0 | ROUND_HALF_UP(SM2026*7.0/100) | 122563 | 122563 | 0 | PASS |
| ESCENARIO_7,0_1 | ROUND_HALF_UP(SM2026*7.0/100 + SM2026) | 1.87347e+06 | 1873468 | 0 | PASS |
| REAL_ACUMULADO_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Conclusiones | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| PL_HORA_ACUMULADO_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Conclusiones | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_PERSONA_CAIDA_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 4.6 | 4.64339682 | 0.1 | PASS |
| PL_PERSONA_CAIDA_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 4.6 | 4.64339682 | 0.1 | PASS |
| REAL_2026_ResumenEjecutivo | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Cuerpo | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Metodologia | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_0 | CSV GEIH2025 menores de 25 pct_hasta_1,25_minimos | 81.3 | 81.25 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_1 | CSV GEIH2025 25 o mas pct_hasta_1,25_minimos | 60.2 | 60.24 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_0 | CSV GEIH2025 menores de 25 pct_mas_de_2_minimos | 3.8 | 3.8 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_1 | CSV GEIH2025 25 o mas pct_mas_de_2_minimos | 19.6 | 19.56 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_0 | CSV GEIH2025 menores de 25 pct_en_el_minimo_(±3%) | 34.8 | 34.79 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_1 | CSV GEIH2025 25 o mas pct_en_el_minimo_(±3%) | 28.3 | 28.28 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_0 | CSV GEIH2025 menores de 25 pct_bajo_el_minimo | 30.3 | 30.3 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_1 | CSV GEIH2025 25 o mas pct_bajo_el_minimo | 18.1 | 18.09 | 0.1 | PASS |
| RAZON_2021_todos | SMLMV/media exacta 2021,todos | 59.3 | 59.2822582 | 0.1 | PASS |
| RAZON_2026_todos | SMLMV/media exacta 2026,todos | 68.2 | 68.1842627 | 0.1 | PASS |
| RAZON_2025_todos | SMLMV/media exacta 2025,todos | 65.9 | 65.9095938 | 0.1 | PASS |
| RAZON_2021_40h_mas | SMLMV/media exacta 2021,40h_mas | 56.7 | 56.6518185 | 0.1 | PASS |
| RAZON_2026_40h_mas | SMLMV/media exacta 2026,40h_mas | 64.9 | 64.8665523 | 0.1 | PASS |
| EXCLUSION_10.560 | auditoria_filtros.csv enero_agosto | 10560 | 10560 | 0 | PASS |
| EXCLUSION_2.223 | auditoria_filtros.csv enero_agosto | 2223 | 2223 | 0 | PASS |
| EXCLUSION_303 | auditoria_filtros.csv enero_agosto | 303 | 303 | 0 | PASS |
## 2026-11-03 — CJC @ 6eebcf8-dirty — final

80 cifras propias. 0 FAIL, 0 discrepancias PDF, 0 etiquetas ausentes.

| ID | Fuente/cálculo | Reportado | Calculado | Tolerancia | Estado |
|---|---|---:|---:|---:|---|
| SM_2021 | monto legal depositado 2021 | 908526 | 908526 | 0 | PASS |
| AUMENTO_2021 | 100*(SM[2021]/SM[2020]-1) | 3.5 | 3.49998804 | 0.005 | PASS |
| MEDIA_2021_todos | sum(meses 1:8 numerador 2021,todos_asalariados)/sum(ponderador)/1e6 | 1.53 | 1.53254283 | 0.005 | PASS |
| MEDIA_2021_40h_mas | sum(meses 1:8 numerador 2021,jornada_40h_mas)/sum(ponderador)/1e6 | 1.6 | 1.60370139 | 0.005 | PASS |
| SM_2022 | monto legal depositado 2022 | 1e+06 | 1000000 | 0 | PASS |
| AUMENTO_2022 | 100*(SM[2022]/SM[2021]-1) | 10.07 | 10.0683965 | 0.005 | PASS |
| MEDIA_2022_todos | sum(meses 1:8 numerador 2022,todos_asalariados)/sum(ponderador)/1e6 | 1.65 | 1.64792835 | 0.005 | PASS |
| MEDIA_2022_40h_mas | sum(meses 1:8 numerador 2022,jornada_40h_mas)/sum(ponderador)/1e6 | 1.73 | 1.72956345 | 0.005 | PASS |
| SM_2023 | monto legal depositado 2023 | 1.16e+06 | 1160000 | 0 | PASS |
| AUMENTO_2023 | 100*(SM[2023]/SM[2022]-1) | 16 | 16 | 0.005 | PASS |
| MEDIA_2023_todos | sum(meses 1:8 numerador 2023,todos_asalariados)/sum(ponderador)/1e6 | 1.85 | 1.85316848 | 0.005 | PASS |
| MEDIA_2023_40h_mas | sum(meses 1:8 numerador 2023,jornada_40h_mas)/sum(ponderador)/1e6 | 1.95 | 1.94741803 | 0.005 | PASS |
| SM_2024 | monto legal depositado 2024 | 1.3e+06 | 1300000 | 0 | PASS |
| AUMENTO_2024 | 100*(SM[2024]/SM[2023]-1) | 12.07 | 12.0689655 | 0.005 | PASS |
| MEDIA_2024_todos | sum(meses 1:8 numerador 2024,todos_asalariados)/sum(ponderador)/1e6 | 2.01 | 2.00799541 | 0.005 | PASS |
| MEDIA_2024_40h_mas | sum(meses 1:8 numerador 2024,jornada_40h_mas)/sum(ponderador)/1e6 | 2.11 | 2.11394442 | 0.005 | PASS |
| SM_2025 | monto legal depositado 2025 | 1.4235e+06 | 1423500 | 0 | PASS |
| AUMENTO_2025 | 100*(SM[2025]/SM[2024]-1) | 9.5 | 9.5 | 0.005 | PASS |
| MEDIA_2025_todos | sum(meses 1:8 numerador 2025,todos_asalariados)/sum(ponderador)/1e6 | 2.16 | 2.15977662 | 0.005 | PASS |
| MEDIA_2025_40h_mas | sum(meses 1:8 numerador 2025,jornada_40h_mas)/sum(ponderador)/1e6 | 2.25 | 2.25339366 | 0.005 | PASS |
| SM_2026 | monto legal depositado 2026 | 1.7509e+06 | 1750905 | 0 | PASS |
| AUMENTO_2026 | 100*(SM[2026]/SM[2025]-1) | 23 | 23 | 0.005 | PASS |
| MEDIA_2026_todos | sum(meses 1:8 numerador 2026,todos_asalariados)/sum(ponderador)/1e6 | 2.57 | 2.56790193 | 0.005 | PASS |
| MEDIA_2026_40h_mas | sum(meses 1:8 numerador 2026,jornada_40h_mas)/sum(ponderador)/1e6 | 2.7 | 2.69924166 | 0.005 | PASS |
| ANUAL_2022_0 | cálculo directo CSV, métrica 0, año 2022 | 10.07 | 10.0683965 | 0.005 | PASS |
| ANUAL_2022_1 | cálculo directo CSV, métrica 1, año 2022 | -0.1 | -0.098059944 | 0.005 | PASS |
| ANUAL_2022_2 | cálculo directo CSV, métrica 2, año 2022 | -2.7 | -2.69999163 | 0.005 | PASS |
| ANUAL_2022_3 | cálculo directo CSV, métrica 3, año 2022 | -0.28 | -0.284062524 | 0.005 | PASS |
| ANUAL_2022_4 | cálculo directo CSV, métrica 4, año 2022 | -2.2 | -2.20280932 | 0.005 | PASS |
| ANUAL_2023_0 | cálculo directo CSV, métrica 0, año 2023 | 16 | 16 | 0.005 | PASS |
| ANUAL_2023_1 | cálculo directo CSV, métrica 1, año 2023 | 3.82 | 3.81560204 | 0.005 | PASS |
| ANUAL_2023_2 | cálculo directo CSV, métrica 2, año 2023 | 6.15 | 6.15364508 | 0.005 | PASS |
| ANUAL_2023_3 | cálculo directo CSV, métrica 3, año 2023 | -1.1 | -1.10195312 | 0.005 | PASS |
| ANUAL_2023_4 | cálculo directo CSV, métrica 4, año 2023 | -2.49 | -2.48609047 | 0.005 | PASS |
| ANUAL_2024_0 | cálculo directo CSV, métrica 0, año 2024 | 12.07 | 12.0689655 | 0.005 | PASS |
| ANUAL_2024_1 | cálculo directo CSV, métrica 1, año 2024 | 5.12 | 5.12129909 | 0.005 | PASS |
| ANUAL_2024_2 | cálculo directo CSV, métrica 2, año 2024 | 6.53 | 6.53049373 | 0.005 | PASS |
| ANUAL_2024_3 | cálculo directo CSV, métrica 3, año 2024 | 2.23 | 2.22576434 | 0.005 | PASS |
| ANUAL_2024_4 | cálculo directo CSV, métrica 4, año 2024 | 0.55 | 0.55250203 | 0.005 | PASS |
| ANUAL_2025_0 | cálculo directo CSV, métrica 0, año 2025 | 9.5 | 9.5 | 0.005 | PASS |
| ANUAL_2025_1 | cálculo directo CSV, métrica 1, año 2025 | 4.14 | 4.144101 | 0.005 | PASS |
| ANUAL_2025_2 | cálculo directo CSV, métrica 2, año 2025 | 4.19 | 4.18572273 | 0.005 | PASS |
| ANUAL_2025_3 | cálculo directo CSV, métrica 3, año 2025 | 0.4 | 0.402731651 | 0.005 | PASS |
| ANUAL_2025_4 | cálculo directo CSV, métrica 4, año 2025 | -0.56 | -0.559123727 | 0.005 | PASS |
| ESCENARIO_6,7_0 | ROUND_HALF_UP(SM2026*6.7/100) | 117311 | 117311 | 0 | PASS |
| ESCENARIO_6,7_1 | ROUND_HALF_UP(SM2026*6.7/100 + SM2026) | 1.86822e+06 | 1868216 | 0 | PASS |
| ESCENARIO_6,8_0 | ROUND_HALF_UP(SM2026*6.8/100) | 119062 | 119062 | 0 | PASS |
| ESCENARIO_6,8_1 | ROUND_HALF_UP(SM2026*6.8/100 + SM2026) | 1.86997e+06 | 1869967 | 0 | PASS |
| ESCENARIO_6,9_0 | ROUND_HALF_UP(SM2026*6.9/100) | 120812 | 120812 | 0 | PASS |
| ESCENARIO_6,9_1 | ROUND_HALF_UP(SM2026*6.9/100 + SM2026) | 1.87172e+06 | 1871717 | 0 | PASS |
| ESCENARIO_7,0_0 | ROUND_HALF_UP(SM2026*7.0/100) | 122563 | 122563 | 0 | PASS |
| ESCENARIO_7,0_1 | ROUND_HALF_UP(SM2026*7.0/100 + SM2026) | 1.87347e+06 | 1873468 | 0 | PASS |
| REAL_ACUMULADO_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Conclusiones | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| PL_HORA_ACUMULADO_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Conclusiones | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_PERSONA_CAIDA_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 4.6 | 4.64339682 | 0.1 | PASS |
| PL_PERSONA_CAIDA_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 4.6 | 4.64339682 | 0.1 | PASS |
| REAL_2026_ResumenEjecutivo | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Cuerpo | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Metodologia | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2027_ILUSTRATIVO | 100*(1.069/1.055-1), escenario de cierre | 1.3 | 1.32701422 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_0 | CSV GEIH2025 menores de 25 pct_hasta_1,25_minimos | 81.3 | 81.25 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_1 | CSV GEIH2025 25 o mas pct_hasta_1,25_minimos | 60.2 | 60.24 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_0 | CSV GEIH2025 menores de 25 pct_mas_de_2_minimos | 3.8 | 3.8 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_1 | CSV GEIH2025 25 o mas pct_mas_de_2_minimos | 19.6 | 19.56 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_0 | CSV GEIH2025 menores de 25 pct_en_el_minimo_(±3%) | 34.8 | 34.79 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_1 | CSV GEIH2025 25 o mas pct_en_el_minimo_(±3%) | 28.3 | 28.28 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_0 | CSV GEIH2025 menores de 25 pct_bajo_el_minimo | 30.3 | 30.3 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_1 | CSV GEIH2025 25 o mas pct_bajo_el_minimo | 18.1 | 18.09 | 0.1 | PASS |
| RAZON_2021_todos | SMLMV/media exacta 2021,todos | 59.3 | 59.2822582 | 0.1 | PASS |
| RAZON_2026_todos | SMLMV/media exacta 2026,todos | 68.2 | 68.1842627 | 0.1 | PASS |
| RAZON_2025_todos | SMLMV/media exacta 2025,todos | 65.9 | 65.9095938 | 0.1 | PASS |
| RAZON_2021_40h_mas | SMLMV/media exacta 2021,40h_mas | 56.7 | 56.6518185 | 0.1 | PASS |
| RAZON_2026_40h_mas | SMLMV/media exacta 2026,40h_mas | 64.9 | 64.8665523 | 0.1 | PASS |
| EXCLUSION_10.560 | auditoria_filtros.csv enero_agosto | 10560 | 10560 | 0 | PASS |
| EXCLUSION_2.223 | auditoria_filtros.csv enero_agosto | 2223 | 2223 | 0 | PASS |
| EXCLUSION_303 | auditoria_filtros.csv enero_agosto | 303 | 303 | 0 | PASS |
## 2026-11-03 — CJC @ c9cd945-dirty — chaparro

91 cifras propias. 0 FAIL, 0 discrepancias PDF, 0 etiquetas ausentes.

| ID | Fuente/cálculo | Reportado | Calculado | Tolerancia | Estado |
|---|---|---:|---:|---:|---|
| SM_2021 | monto legal depositado 2021 | 908526 | 908526 | 0 | PASS |
| AUMENTO_2021 | 100*(SM[2021]/SM[2020]-1) | 3.5 | 3.49998804 | 0.005 | PASS |
| MEDIA_2021_todos | sum(meses 1:8 numerador 2021,todos_asalariados)/sum(ponderador)/1e6 | 1.53 | 1.53254283 | 0.005 | PASS |
| MEDIA_2021_40h_mas | sum(meses 1:8 numerador 2021,jornada_40h_mas)/sum(ponderador)/1e6 | 1.6 | 1.60370139 | 0.005 | PASS |
| SM_2022 | monto legal depositado 2022 | 1e+06 | 1000000 | 0 | PASS |
| AUMENTO_2022 | 100*(SM[2022]/SM[2021]-1) | 10.07 | 10.0683965 | 0.005 | PASS |
| MEDIA_2022_todos | sum(meses 1:8 numerador 2022,todos_asalariados)/sum(ponderador)/1e6 | 1.65 | 1.64792835 | 0.005 | PASS |
| MEDIA_2022_40h_mas | sum(meses 1:8 numerador 2022,jornada_40h_mas)/sum(ponderador)/1e6 | 1.73 | 1.72956345 | 0.005 | PASS |
| SM_2023 | monto legal depositado 2023 | 1.16e+06 | 1160000 | 0 | PASS |
| AUMENTO_2023 | 100*(SM[2023]/SM[2022]-1) | 16 | 16 | 0.005 | PASS |
| MEDIA_2023_todos | sum(meses 1:8 numerador 2023,todos_asalariados)/sum(ponderador)/1e6 | 1.85 | 1.85316848 | 0.005 | PASS |
| MEDIA_2023_40h_mas | sum(meses 1:8 numerador 2023,jornada_40h_mas)/sum(ponderador)/1e6 | 1.95 | 1.94741803 | 0.005 | PASS |
| SM_2024 | monto legal depositado 2024 | 1.3e+06 | 1300000 | 0 | PASS |
| AUMENTO_2024 | 100*(SM[2024]/SM[2023]-1) | 12.07 | 12.0689655 | 0.005 | PASS |
| MEDIA_2024_todos | sum(meses 1:8 numerador 2024,todos_asalariados)/sum(ponderador)/1e6 | 2.01 | 2.00799541 | 0.005 | PASS |
| MEDIA_2024_40h_mas | sum(meses 1:8 numerador 2024,jornada_40h_mas)/sum(ponderador)/1e6 | 2.11 | 2.11394442 | 0.005 | PASS |
| SM_2025 | monto legal depositado 2025 | 1.4235e+06 | 1423500 | 0 | PASS |
| AUMENTO_2025 | 100*(SM[2025]/SM[2024]-1) | 9.5 | 9.5 | 0.005 | PASS |
| MEDIA_2025_todos | sum(meses 1:8 numerador 2025,todos_asalariados)/sum(ponderador)/1e6 | 2.16 | 2.15977662 | 0.005 | PASS |
| MEDIA_2025_40h_mas | sum(meses 1:8 numerador 2025,jornada_40h_mas)/sum(ponderador)/1e6 | 2.25 | 2.25339366 | 0.005 | PASS |
| SM_2026 | monto legal depositado 2026 | 1.7509e+06 | 1750905 | 0 | PASS |
| AUMENTO_2026 | 100*(SM[2026]/SM[2025]-1) | 23 | 23 | 0.005 | PASS |
| MEDIA_2026_todos | sum(meses 1:8 numerador 2026,todos_asalariados)/sum(ponderador)/1e6 | 2.57 | 2.56790193 | 0.005 | PASS |
| MEDIA_2026_40h_mas | sum(meses 1:8 numerador 2026,jornada_40h_mas)/sum(ponderador)/1e6 | 2.7 | 2.69924166 | 0.005 | PASS |
| ANUAL_2022_0 | cálculo directo CSV, métrica 0, año 2022 | 10.07 | 10.0683965 | 0.005 | PASS |
| ANUAL_2022_1 | cálculo directo CSV, métrica 1, año 2022 | -0.1 | -0.098059944 | 0.005 | PASS |
| ANUAL_2022_2 | cálculo directo CSV, métrica 2, año 2022 | -2.7 | -2.69999163 | 0.005 | PASS |
| ANUAL_2022_3 | cálculo directo CSV, métrica 3, año 2022 | -0.28 | -0.284062524 | 0.005 | PASS |
| ANUAL_2022_4 | cálculo directo CSV, métrica 4, año 2022 | -2.2 | -2.20280932 | 0.005 | PASS |
| ANUAL_2023_0 | cálculo directo CSV, métrica 0, año 2023 | 16 | 16 | 0.005 | PASS |
| ANUAL_2023_1 | cálculo directo CSV, métrica 1, año 2023 | 3.82 | 3.81560204 | 0.005 | PASS |
| ANUAL_2023_2 | cálculo directo CSV, métrica 2, año 2023 | 6.15 | 6.15364508 | 0.005 | PASS |
| ANUAL_2023_3 | cálculo directo CSV, métrica 3, año 2023 | -1.1 | -1.10195312 | 0.005 | PASS |
| ANUAL_2023_4 | cálculo directo CSV, métrica 4, año 2023 | -2.49 | -2.48609047 | 0.005 | PASS |
| ANUAL_2024_0 | cálculo directo CSV, métrica 0, año 2024 | 12.07 | 12.0689655 | 0.005 | PASS |
| ANUAL_2024_1 | cálculo directo CSV, métrica 1, año 2024 | 5.12 | 5.12129909 | 0.005 | PASS |
| ANUAL_2024_2 | cálculo directo CSV, métrica 2, año 2024 | 6.53 | 6.53049373 | 0.005 | PASS |
| ANUAL_2024_3 | cálculo directo CSV, métrica 3, año 2024 | 2.23 | 2.22576434 | 0.005 | PASS |
| ANUAL_2024_4 | cálculo directo CSV, métrica 4, año 2024 | 0.55 | 0.55250203 | 0.005 | PASS |
| ANUAL_2025_0 | cálculo directo CSV, métrica 0, año 2025 | 9.5 | 9.5 | 0.005 | PASS |
| ANUAL_2025_1 | cálculo directo CSV, métrica 1, año 2025 | 4.14 | 4.144101 | 0.005 | PASS |
| ANUAL_2025_2 | cálculo directo CSV, métrica 2, año 2025 | 4.19 | 4.18572273 | 0.005 | PASS |
| ANUAL_2025_3 | cálculo directo CSV, métrica 3, año 2025 | 0.4 | 0.402731651 | 0.005 | PASS |
| ANUAL_2025_4 | cálculo directo CSV, métrica 4, año 2025 | -0.56 | -0.559123727 | 0.005 | PASS |
| ESCENARIO_6,7_0 | ROUND_HALF_UP(SM2026*6.7/100) | 117311 | 117311 | 0 | PASS |
| ESCENARIO_6,7_1 | ROUND_HALF_UP(SM2026*6.7/100 + SM2026) | 1.86822e+06 | 1868216 | 0 | PASS |
| ESCENARIO_6,8_0 | ROUND_HALF_UP(SM2026*6.8/100) | 119062 | 119062 | 0 | PASS |
| ESCENARIO_6,8_1 | ROUND_HALF_UP(SM2026*6.8/100 + SM2026) | 1.86997e+06 | 1869967 | 0 | PASS |
| ESCENARIO_6,9_0 | ROUND_HALF_UP(SM2026*6.9/100) | 120812 | 120812 | 0 | PASS |
| ESCENARIO_6,9_1 | ROUND_HALF_UP(SM2026*6.9/100 + SM2026) | 1.87172e+06 | 1871717 | 0 | PASS |
| ESCENARIO_7,0_0 | ROUND_HALF_UP(SM2026*7.0/100) | 122563 | 122563 | 0 | PASS |
| ESCENARIO_7,0_1 | ROUND_HALF_UP(SM2026*7.0/100 + SM2026) | 1.87347e+06 | 1873468 | 0 | PASS |
| REAL_ACUMULADO_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| REAL_ACUMULADO_Conclusiones | SM/IPC promedio o producto de tasas DANE 2022:2025 | 13.5 | 13.5434128 | 0.1 | PASS |
| PL_HORA_ACUMULADO_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_HORA_ACUMULADO_Conclusiones | SM/IPC promedio o producto de tasas DANE 2022:2025 | 1.2 | 1.21810139 | 0.1 | PASS |
| PL_PERSONA_CAIDA_ResumenEjecutivo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 4.6 | 4.64339682 | 0.1 | PASS |
| PL_PERSONA_CAIDA_Cuerpo | SM/IPC promedio o producto de tasas DANE 2022:2025 | 4.6 | 4.64339682 | 0.1 | PASS |
| REAL_2026_ResumenEjecutivo | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Cuerpo | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2026_Metodologia | 100*(1.23/1.069-1) | 15.1 | 15.0608045 | 0.1 | PASS |
| REAL_2027_ILUSTRATIVO | 100*(1.069/1.055-1), escenario de cierre | 1.3 | 1.32701422 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_0 | CSV GEIH2025 menores de 25 pct_hasta_1,25_minimos | 81.3 | 81.25 | 0.1 | PASS |
| EDAD_pct_hasta_1,25_minimos_1 | CSV GEIH2025 25 o mas pct_hasta_1,25_minimos | 60.2 | 60.24 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_0 | CSV GEIH2025 menores de 25 pct_mas_de_2_minimos | 3.8 | 3.8 | 0.1 | PASS |
| EDAD_pct_mas_de_2_minimos_1 | CSV GEIH2025 25 o mas pct_mas_de_2_minimos | 19.6 | 19.56 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_0 | CSV GEIH2025 menores de 25 pct_en_el_minimo_(±3%) | 34.8 | 34.79 | 0.1 | PASS |
| EDAD_pct_en_el_minimo_(±3%)_1 | CSV GEIH2025 25 o mas pct_en_el_minimo_(±3%) | 28.3 | 28.28 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_0 | CSV GEIH2025 menores de 25 pct_bajo_el_minimo | 30.3 | 30.3 | 0.1 | PASS |
| EDAD_pct_bajo_el_minimo_1 | CSV GEIH2025 25 o mas pct_bajo_el_minimo | 18.1 | 18.09 | 0.1 | PASS |
| RAZON_2021_todos | SMLMV/media exacta 2021,todos | 59.3 | 59.2822582 | 0.1 | PASS |
| RAZON_2026_todos | SMLMV/media exacta 2026,todos | 68.2 | 68.1842627 | 0.1 | PASS |
| RAZON_2025_todos | SMLMV/media exacta 2025,todos | 65.9 | 65.9095938 | 0.1 | PASS |
| RAZON_2021_40h_mas | SMLMV/media exacta 2021,40h_mas | 56.7 | 56.6518185 | 0.1 | PASS |
| RAZON_2026_40h_mas | SMLMV/media exacta 2026,40h_mas | 64.9 | 64.8665523 | 0.1 | PASS |
| EXCLUSION_10.560 | auditoria_filtros.csv enero_agosto | 10560 | 10560 | 0 | PASS |
| EXCLUSION_2.223 | auditoria_filtros.csv enero_agosto | 2223 | 2223 | 0 | PASS |
| EXCLUSION_303 | auditoria_filtros.csv enero_agosto | 303 | 303 | 0 | PASS |
| ESCALA_NACIONAL_CCF | sum(42 cajas marzo 2025 trabajadores dependientes) | 9.70479e+06 | 9704786 | 0 | PASS |
| ESCALA_ANTIOQUIA_CCF | sum(Comfama y Comfenalco Antioquia marzo 2025) | 1.75536e+06 | 1755360 | 0 | PASS |
| FACTOR_CCF | Fraction(total nacional, dos cajas Antioquia) | 5.53 | 5.52865851 | 0.005 | PASS |
| FACTOR_CCF_NOTA | Fraction(total nacional, dos cajas Antioquia) | 5.52866 | 5.52865851 | 5e-08 | PASS |
| COLOMBIA_TABLA_44557 | ROUND_HALF_UP(Fraction(44557*9704786,1755360), millar) | 246000 | 246000 | 0 | PASS |
| COLOMBIA_CUERPO_44557 | reescalamiento exacto, redondeado al millar y expresado en miles | 246 | 246 | 0 | PASS |
| COLOMBIA_TABLA_5015 | ROUND_HALF_UP(Fraction(5015*9704786,1755360), millar) | 28000 | 28000 | 0 | PASS |
| COLOMBIA_CUERPO_5015 | reescalamiento exacto, redondeado al millar y expresado en miles | 28 | 28 | 0 | PASS |
| COLOMBIA_TABLA_49572 | ROUND_HALF_UP(Fraction(49572*9704786,1755360), millar) | 274000 | 274000 | 0 | PASS |
| COLOMBIA_CUERPO_49572 | reescalamiento exacto, redondeado al millar y expresado en miles | 274 | 274 | 0 | PASS |
| PARTICIPACION_MENOR_CREACION | 100*44557/49572, aproximación al entero | 90 | 89.8834019 | 0.5 | PASS |
