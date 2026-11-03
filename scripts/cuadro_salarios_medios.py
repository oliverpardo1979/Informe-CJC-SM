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

def read(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def fmt(value, decimals=2):
    return f'{value:,.{decimals}f}'.replace(',', '_').replace('.', ',').replace('_', '.')

source, monthly = read(SOURCE), read(MONTHLY)
assert [int(r['anio']) for r in source] == list(range(2021, 2027))
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
    output.append(row)
with (ROOT/'data/smlmv_salario_medio_geih.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(output[0]))
    writer.writeheader()
    writer.writerows(output)
table = [r'\begin{table}[H]', r'\centering\small',
         r'\caption{Salario mínimo y salario medio mensual, enero--agosto de 2021--2026}',
         r'\label{tab:minimo-media}', r'\begin{tabular}{lrrrr}', r'\toprule',
         r'& SMLMV & Aumento & \multicolumn{2}{c}{Salario medio GEIH}\\',
         r'\cmidrule(lr){4-5}',
         r'Año & (pesos) & nominal (\%) & Todos & Jornada $\geq40$ h\\',
         r'& & & \multicolumn{2}{c}{(millones de pesos corrientes)}\\', r'\midrule']
for r in output:
    table.append(f"{r['anio']} & {fmt(r['smlmv_pesos'],0)} & {fmt(r['aumento_nominal_pct'])} & "
                 f"{fmt(r['todos_media_pesos']/1e6)} & {fmt(r['40h_media_pesos']/1e6)}"+r' \\')
table += [r'\bottomrule', r'\end{tabular}',
          r'\fuente{Fuente: normativa salarial \citep{decreto1785,salarioHistorico,decreto2613,decreto2024,decreto2025,decreto1469} y tabulados del CJC con GEIH \citep{geihTabulados}. Enero--agosto de entrevistas en todos los años, con salario referido al mes anterior. Medias de P6500 para asalariados de 15 años o más, ponderadas por FEX\_C18, con salario válido positivo y exclusión de códigos 98/99. Se incluyen formales e informales y salarios inferiores al mínimo. La nota técnica documenta la identificación del marco de 2021 y las diferencias de no respuesta.}',
          r'\end{table}']
(ROOT/'Paper/sections/CuadroSalariosMedios.tex').write_text('\n'.join(table)+'\n', encoding='utf-8')
provenance = {'fuentes': [{'archivo': str(x.relative_to(ROOT)),
                          'sha256': hashlib.sha256(x.read_bytes()).hexdigest()}
                         for x in [SOURCE, MONTHLY]],
              'formula': 'sum(P6500 * FEX_C18) / sum(FEX_C18)',
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
          'mínimo/media (%)', fmt(r['todos_smlmv_sobre_media_pct']))
