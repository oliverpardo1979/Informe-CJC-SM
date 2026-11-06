"""Texas: mínimo y mediana por hora; EPI/CPS, asalariados públicos y privados."""
from pathlib import Path
import hashlib
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1] / 'analisis/eeuu_minimo_mediana'
(ROOT / 'graficos').mkdir(parents=True, exist_ok=True)
source = ROOT / 'fuentes/epi_hourly_wage_median.csv'
raw = pd.read_csv(source)
data = raw.loc[(raw.geo_type == 'state') & (raw.geo_code == 48)
               & (raw.measure == 'Median nominal hourly wage')
               & (raw.group_value == 'Overall') & (raw.date_interval == 'year')
               & raw.year.between(2010, 2025), ['year', 'value', 'data_version']].copy()
data = data.rename(columns={'year': 'anio', 'value': 'mediana_salarial_usd_hora'}).sort_values('anio')
assert len(data) == 16 and not data.anio.duplicated().any() and data.mediana_salarial_usd_hora.notna().all()
panel = pd.read_csv(ROOT / 'panel_estatal_minimo_mediana_2010_2025.csv')
data = data.merge(panel.loc[panel.abreviatura.eq('TX'), ['anio', 'minimo_referencia_usd_hora']],
                  on='anio', validate='one_to_one')
assert data.minimo_referencia_usd_hora.eq(7.25).all()
data.to_csv(ROOT / 'texas_minimo_mediana_hora_cps_2010_2025.csv', index=False, encoding='utf-8-sig')
metadata = {'url_descarga': 'https://github.com/Economic/data/releases/latest/download/epi_swa_data_library.zip',
            'fuente': 'Economic Policy Institute, State of Working America Data Library; Current Population Survey',
            'version': str(data.data_version.iloc[0]), 'fecha_descarga': '2026-11-06',
            'sha256_csv': hashlib.sha256(source.read_bytes()).hexdigest(),
            'seleccion': 'Texas, state 48, year, Overall, Median nominal hourly wage, 2010–2025',
            'nota': 'Tabulados de EPI, no microdatos recalculados por el CJC. Incluye asalariados públicos y privados; no es ingreso de todos los ocupados.'}
(ROOT / 'fuentes/manifiesto_texas_cps.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
first, last = data.iloc[0], data.iloc[-1]
growth = (last.mediana_salarial_usd_hora / first.mediana_salarial_usd_hora - 1) * 100
navy, orange, gray = '#193451', '#E67438', '#647687'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'svg.fonttype': 'none'})
fig, ax = plt.subplots(figsize=(11, 6.3), facecolor='white')
fig.subplots_adjust(left=.09, right=.95, top=.74, bottom=.22)
fig.text(.09, .94, 'Evolución del salario mínimo e ingreso mediano por hora nominal\nen el estado de Texas.',
         fontsize=18, weight='bold', color=navy, va='top', linespacing=1.3)
fig.text(.09, .79, 'Asalariados de los sectores público y privado · Dólares corrientes por hora · 2010–2025', fontsize=11, color=gray)
ax.set_axisbelow(True)
ax.grid(axis='y', color='#E4EAF0', lw=.8)
for side in ['top', 'right', 'left']:
    ax.spines[side].set_visible(False)
ax.spines['bottom'].set_color('#D0D9E1')
ax.tick_params(length=0, labelcolor=gray, pad=8)
ax.plot(data.anio, data.mediana_salarial_usd_hora, color=navy, lw=3, marker='o', ms=4, label='Salario mediano por hora')
ax.plot(data.anio, data.minimo_referencia_usd_hora, color=orange, lw=3, label='Salario mínimo')
ax.set(xlim=(2009.8, 2025.3), ylim=(0, 30), xticks=[2010, 2013, 2016, 2019, 2022, 2025], yticks=[0, 5, 10, 15, 20, 25, 30])
ax.yaxis.set_major_formatter(FuncFormatter(lambda value, pos: f'US${value:.0f}'))
ax.legend(loc='upper left', frameon=False, fontsize=10)
for row, align, dx in [(first, 'left', 4), (last, 'right', -4)]:
    ax.annotate(f'US${row.mediana_salarial_usd_hora:.2f}'.replace('.', ','),
                (row.anio, row.mediana_salarial_usd_hora), xytext=(dx, 12),
                textcoords='offset points', ha=align, color=navy, fontsize=11, weight='bold')
ax.annotate('US$7,25', (2025, 7.25), xytext=(-4, 12), textcoords='offset points',
            ha='right', color=orange, fontsize=11, weight='bold')
fig.text(.09, .13, 'Fuente: EPI, State of Working America Data Library (CPS), y U.S. Department of Labor/FRED.', fontsize=9, color=gray)
fig.text(.09, .085, 'Mediana salarial por hora de asalariados, con empleo público y privado. No representa el ingreso de trabajadores independientes.', fontsize=9, color=gray)
fig.text(.09, .04, 'Valores nominales, sin ajuste por inflación. Tabulados anuales de EPI; versión 2026.9.22.', fontsize=9, color=gray)
for ext in ['png', 'svg']:
    fig.savefig(ROOT / 'graficos' / f'texas_minimo_mediana_hora_cps_2010_2025.{ext}', dpi=240)
for label in fig.texts:
    label.set_visible(False)
# El boletín incorpora su propio título, fuente y explicación.
fig.savefig(ROOT.parents[1] / 'Paper/figures/texas_minimo_mediana_hora_2010_2025.png',
            dpi=300, bbox_inches='tight', pad_inches=.1)
plt.close(fig)
print(data.iloc[[0, -1]].to_string(index=False))
print(f'Crecimiento nominal: {growth:.4f}%')
