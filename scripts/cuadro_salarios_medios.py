"""Construye el cuadro del mínimo y el salario medio desde tabulados GEIH del CJC.

Las medias por edad se agregan con población expandida, nunca con muestra sin ponderar.
El CSV fuente redondea población a 0,01 millones. Por eso el resultado es aproximado.
Los extremos guardados miden solo ese redondeo, no incertidumbre de muestreo.
No se imputan 2021 ni meses faltantes de 2026.
"""
from pathlib import Path
import csv
import hashlib
import itertools
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'insumos/SalarioMinimo_Edad/Outputs/tables/estadisticas_salario_por_edad.csv'
MINIMUM = {2021: 908526, 2022: 1000000, 2023: 1160000,
           2024: 1300000, 2025: 1423500, 2026: 1750905}

def fmt(value, decimals=2):
    return f'{value:,.{decimals}f}'.replace(',', '_').replace('.', ',').replace('_', '.')

def aggregate(rows):
    assert len(rows) == 2
    assert {r['grupo'] for r in rows} == {'menores de 25', '25 o mas'}
    w = [float(r['asalariados_millones']) for r in rows]
    x = [float(r['media']) for r in rows]
    mean = sum(a*b for a,b in zip(w,x)) / sum(w)
    candidates = [sum(a*b for a,b in zip(z,x))/sum(z)
                  for z in itertools.product(*[(a-.005,a+.005) for a in w])]
    lo, hi = min(candidates), max(candidates)
    # Acotar la aproximación antes de publicar cifras a decenas de miles de pesos.
    assert max(mean-lo,hi-mean)<1000, (lo, mean, hi)
    return mean, lo, hi, sum(int(r['muestra']) for r in rows)

with SOURCE.open(encoding='utf-8-sig', newline='') as f:
    source = list(csv.DictReader(f))
output = []
for year, sm in MINIMUM.items():
    row = {'anio': year, 'meses': 'enero-agosto' if year == 2026 else 'enero-diciembre',
           'smlmv_pesos': sm, 'aumento_nominal_pct': (sm/MINIMUM[year-1]-1)*100 if year>2021 else 3.5}
    for label, universe in [('todos','todos los asalariados'), ('40h','tiempo completo (>= 40 h)')]:
        selected = [r for r in source if int(r['anio']) == year and r['poblacion'] == universe]
        if not selected:
            for field in ['media_pesos','limite_inferior_redondeo','limite_superior_redondeo','n_muestra']:
                row[f'{label}_{field}'] = ''
            continue
        mean, lo, hi, n = aggregate(selected)
        row.update({f'{label}_media_pesos': mean,
                    f'{label}_limite_inferior_redondeo': lo,
                    f'{label}_limite_superior_redondeo': hi,
                    f'{label}_n_muestra': n})
    output.append(row)
dest = ROOT/'data/smlmv_salario_medio_geih.csv'
with dest.open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f, fieldnames=list(output[0]));writer.writeheader();writer.writerows(output)
table = [r'\begin{table}[H]', r'\centering\small',
         r'\caption{Salario mínimo y salario medio mensual, 2021--2026}',
         r'\label{tab:minimo-media}', r'\begin{tabular}{lrrrr}',r'\toprule',
         r'& SMLMV & Aumento & \multicolumn{2}{c}{Salario medio GEIH}\\',
         r'\cmidrule(lr){4-5}',
         r'Año & (pesos) & nominal (\%) & Todos & Jornada $\geq40$ h\\',
         r'& & & \multicolumn{2}{c}{(millones de pesos corrientes)}\\',r'\midrule']
for r in output:
    if r['anio'] == 2026: table.append(r'\midrule')
    a = str(r['anio']) + (r'$^{*}$' if r['anio']==2026 else '')
    means = [fmt(r[f'{u}_media_pesos']/1e6) if r[f'{u}_media_pesos']!='' else 'n.d.' for u in ['todos','40h']]
    table.append(f"{a} & {fmt(r['smlmv_pesos'],0)} & {fmt(r['aumento_nominal_pct'])} & {means[0]} & {means[1]}"+r' \\')
table += [r'\bottomrule',r'\end{tabular}',
          r'\fuente{Fuente: normativa salarial y tabulados del CJC con GEIH. Medias aproximadas de asalariados de 15 años o más con ingreso positivo del empleo principal, ponderadas por expansión. $^{*}$2026 cubre enero--agosto y no es directamente comparable con los años completos. n.d.: sin estimación bajo la misma definición. Detalles y validaciones pendientes en el anexo A.}',r'\end{table}']
(ROOT/'Paper/sections/CuadroSalariosMedios.tex').write_text('\n'.join(table)+'\n',encoding='utf-8')
provenance = {'fuente': str(SOURCE.relative_to(ROOT)),
              'sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'formula': 'sum(media_grupo * poblacion_expandida_grupo) / sum(poblacion_expandida_grupo)',
              'precision_fuente_poblacion_millones': .01,
              'precision_publicada_media_millones_pesos': .01,
              'comprobacion': 'La desviación máxima por redondeo de los pesos es inferior a 1.000 pesos en cada celda. Se publica una aproximación a decenas de miles de pesos.',
              'limites': ['No es una reestimación de los microdatos.', 'Sin 2021.',
                         '2026 enero-agosto, sin ventana equivalente previa.',
                         'El insumo filtra P6500>0, sin exclusión explícita de códigos 98 y 99.',
                         'Los límites por redondeo no son intervalos de confianza.']}
(ROOT/'data/smlmv_salario_medio_procedencia.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in output:print(r['anio'],r['todos_media_pesos'],r['40h_media_pesos'])
