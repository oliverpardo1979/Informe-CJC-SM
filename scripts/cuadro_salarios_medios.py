"""Integra tabulados directos de Jorge y reconcilia sus agregados mensuales.
No reestima microdatos. Usa enero-agosto de entrevistas en todos los años.
"""
from pathlib import Path
import csv
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'data/salario_medio_geih/salario_medio_comparable_2021_2026.csv'
MONTHLY = SOURCE.with_name('salario_medio_mensual_2021_2026.csv')
MEDIAN = SOURCE.with_name('salario_mediano_enero_agosto_2021_2026.csv')
IPC = ROOT / 'data/ipc_enero_agosto_2021_2026.csv'
MONTHS = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto')

def read(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def fmt(value, decimals=2):
    return f'{value:,.{decimals}f}'.replace(',', '_').replace('.', ',').replace('_', '.')

source, monthly = read(SOURCE), read(MONTHLY)
median_rows = read(MEDIAN)
assert [int(r['anio']) for r in median_rows] == list(range(2021, 2027))
medians = {int(r['anio']): float(r['mediana_ponderada_p6500_pesos_nominales'])
           for r in median_rows}
assert all(math.isfinite(value) and value > 0 for value in medians.values())
ipc_mean = {int(r['anio']): math.fsum(float(r[month]) for month in MONTHS) / len(MONTHS)
            for r in read(IPC)}
assert [int(r['anio']) for r in source] == list(range(2021, 2027))
assert set(ipc_mean) == set(range(2021, 2027))
output = []
for r in source:
    assert r['meses_cubiertos'] == '01|02|03|04|05|06|07|08'
    assert int(r['numero_meses']) == 8
    year, sm = int(r['anio']), int(r['smlmv_pesos'])
    prev = int(source[year-2022]['smlmv_pesos']) if year > 2021 else 877803
    row = {'anio': year, 'meses': 'enero-agosto de entrevistas',
           'smlmv_pesos': sm, 'aumento_nominal_pct': (sm/prev-1)*100}
    for label, suffix, population in [('todos', 'todos', 'todos_asalariados'),
                                       ('40h', '40h_mas', 'jornada_40h_mas')]:
        mm = [m for m in monthly if int(m['anio']) == year
              and m['poblacion'] == population and int(m['meses_cubiertos']) <= 8]
        assert len(mm) == 8
        sw = math.fsum(float(m['suma_ponderadores']) for m in mm)
        sx = math.fsum(float(m['suma_ponderada_p6500']) for m in mm)
        n = sum(int(m['muestra_registros']) for m in mm)
        mean = float(r[f'media_ponderada_p6500_pesos_{suffix}'])
        assert math.isclose(sw, float(r[f'suma_ponderadores_{suffix}']), rel_tol=1e-12)
        assert math.isclose(sx, float(r[f'suma_ponderada_p6500_{suffix}']), rel_tol=1e-12)
        assert math.isclose(sx/sw, mean, rel_tol=1e-12)
        assert n == int(r[f'muestra_registros_{suffix}'])
        row.update({f'{label}_media_pesos': mean, f'{label}_suma_ponderadores': sw,
                    f'{label}_suma_ponderada_p6500': sx, f'{label}_n_muestra': n,
                    f'{label}_smlmv_sobre_media_pct': sm/mean*100})
        previous_mean = output[-1][f'{label}_media_pesos'] if output else None
        row[f'{label}_aumento_nominal_pct'] = (
            (mean/previous_mean-1)*100 if previous_mean is not None else None)
    price_factor = ipc_mean[2026] / ipc_mean[year]
    row.update(ipc_promedio_enero_agosto=ipc_mean[year],
               smlmv_real_pesos_2026=sm * price_factor,
               salario_medio_real_pesos_2026=row['todos_media_pesos'] * price_factor,
               salario_mediano_nominal_pesos=medians[year],
               salario_mediano_real_pesos_2026=medians[year] * price_factor,
               smlmv_sobre_mediana_pct=sm / medians[year] * 100)
    output.append(row)
with (ROOT/'data/smlmv_salario_medio_geih.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(output[0]))
    writer.writeheader()
    writer.writerows(output)
table = [r'\begin{table}[H]', r'\centering\small',
         r'\caption{Salario mínimo, medio y mediano en términos reales, 2021--2026}',
         r'\label{tab:minimo-media}', r'\begin{tabular}{@{}lrrrrr@{}}', r'\toprule',
         r'Año & Salario mínimo & Salario medio & Salario mediano & \shortstack[r]{Mínimo como\\\% del medio} & \shortstack[r]{Mínimo como\\\% del mediano}\\',
         r'& \multicolumn{3}{c}{(millones de pesos de 2026)} & & \\',
         r'\midrule']
for r in output:
    table.append(f"{r['anio']} & {fmt(r['smlmv_real_pesos_2026']/1e6)} & "
                 f"{fmt(r['salario_medio_real_pesos_2026']/1e6)} & "
                 f"{fmt(r['salario_mediano_real_pesos_2026']/1e6)} & "
                 f"{fmt(r['todos_smlmv_sobre_media_pct'], 1)} & "
                 f"{fmt(r['smlmv_sobre_mediana_pct'], 1)}"+r' \\')
table += [r'\bottomrule', r'\end{tabular}',
          r'\fuente{Fuentes: normativa salarial \citep{decreto1785,salarioHistorico,decreto2613,decreto2024,decreto2025,decreto1469}, tabulados del CJC con GEIH \citep{geihTabulados} e IPC del DANE \citep{ipcEmpalme2026}. Los montos se expresan a precios promedio de enero a agosto de 2026. La media y la mediana se calculan con FEX\_C18 para asalariados de 15 años o más con salario válido positivo, entrevistados entre enero y agosto de cada año. Se incluyen todas las jornadas, asalariados formales e informales y salarios inferiores al mínimo. Los porcentajes se calculan antes de redondear los montos.}',
          r'\end{table}']
(ROOT/'Paper/sections/CuadroSalariosMedios.tex').write_text('\n'.join(table)+'\n', encoding='utf-8')
provenance = {'fuentes': [{'archivo': str(x.relative_to(ROOT)),
                          'sha256': hashlib.sha256(x.read_bytes()).hexdigest()}
                         for x in [SOURCE, MONTHLY, MEDIAN, IPC]],
              'formula': 'sum(P6500 * FEX_C18) / sum(FEX_C18)',
              'formula_aumento_nominal_pct': '(media_anio / media_anio_anterior - 1) * 100',
              'base_variacion': 'Mismos filtros y enero-agosto de entrevistas en ambos años. Medias sin redondear.',
              'variacion_2021': 'No disponible: los tabulados no incluyen una media comparable de 2020.',
              'ipc_fuente': {'url': 'https://www.dane.gov.co/files/operaciones/IPC/sep2026/anex-IPC-Indices-sep2026.xlsx',
                             'hoja_y_celdas': 'IndicesIPC!T10:Y17',
                             'sha256_xlsx': '56f8e5e6e9d235d411e487b2284beba1be8eaeee69b7b9516bfa8ea8443c0676'},
              'formula_salario_real': 'salario_nominal * IPC_promedio_enero_agosto_2026 / IPC_promedio_enero_agosto_anio',
              'formula_smlmv_sobre_mediana_pct': '100 * smlmv_pesos / salario_mediano_nominal_pesos',
              'presentacion_montos': 'Millones de pesos a precios promedio de enero a agosto de 2026, con dos decimales. Razones mínimo/media y mínimo/mediana en porcentaje con un decimal.',
              'ventana': 'enero-agosto de entrevistas en todos los años',
              'verificacion': 'Medias, numeradores, denominadores y muestras reconciliados con meses.',
              'reestimacion_microdatos_por_integrador': False,
              'limites': ['Sin errores estándar ni ajuste por composición o no respuesta.',
                         'Marco 2021 según responsable y variables compatibles. Sin identificador de descarga original.',
                         'Las cifras no estiman efectos causales ni productividad individual.']}
(ROOT/'data/smlmv_salario_medio_procedencia.json').write_text(
    json.dumps(provenance, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
for r in output:
    print(r['anio'], fmt(r['todos_media_pesos']), fmt(r['40h_media_pesos']),
          'mínimo/media (%)', fmt(r['todos_smlmv_sobre_media_pct']),
          'mínimo/mediana (%)', fmt(r['smlmv_sobre_mediana_pct']),
          'aumento medio nominal (%)',
          *(fmt(r[f'{label}_aumento_nominal_pct'])
            if r[f'{label}_aumento_nominal_pct'] is not None else 'ND'
            for label in ('todos', '40h')))
