# Texas: mínimo y mediana por hora

La figura del boletín compara el mínimo legal de referencia (DOL/FRED) con la mediana nominal por hora de los asalariados públicos y privados de Texas (tabulados EPI/CPS). No representa el ingreso de trabajadores independientes ni identifica efectos causales. Ambas series se expresan en dólares corrientes por hora; no se convierten ingresos anuales mediante una jornada supuesta.

Entre 2010 y 2025 el mínimo se mantiene en US$7,25 y la mediana pasa de US$14,2372 a US$24,3060 (+70,7%). Los valores del CSV se conservan sin redondear. La fuente CPS tiene observación para 2020.

- Fuente salarial: [EPI State of Working America Data Library](https://economic.github.io/data/), versión 2026.9.22; archivo `fuentes/epi_hourly_wage_median.csv`. Selección: Texas, código 48, frecuencia anual, grupo Overall, Median nominal hourly wage.
- Fuente del mínimo: U.S. Department of Labor, [FRED STTMINWGTX](https://fred.stlouisfed.org/series/STTMINWGTX); columna `minimo_referencia_usd_hora` para TX en el panel estatal incluido.
- Procedencia y hash de EPI: `fuentes/manifiesto_texas_cps.json`.
- Datos del gráfico: `texas_minimo_mediana_hora_cps_2010_2025.csv`.
- Figura para LaTeX: `Paper/figures/texas_minimo_mediana_hora_2010_2025.png` desde la raíz del repositorio.

Reproducción desde la raíz: `python scripts/eeuu_texas_mediana_hora_cps.py` (pandas y matplotlib). Antes de ejecutar en una copia limpia, crear `analisis/eeuu_minimo_mediana/graficos/` si no existe. El script también exporta versiones independientes PNG y SVG en ese directorio.
