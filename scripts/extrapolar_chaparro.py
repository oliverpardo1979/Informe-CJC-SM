"""Reescalamiento ilustrativo del resultado de Antioquia mediante afiliación a CCF.
No estima un efecto causal nacional ni reproduce el modelo econométrico regional.
Ejecutar desde cualquier directorio. Solo usa la biblioteca estándar.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv, hashlib, json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/extrapolacion_chaparro'
SOURCE=OUT/'ssf_dependientes_marzo_2025.csv'
with SOURCE.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==42
assert len({r['ccf'] for r in rows})==42
assert all(r['a_o']=='2025' and r['mes']=='3' for r in rows)
assert all(int(r['trabajadores_empleados_dependientes'])>0 for r in rows)
antioquia=[r for r in rows if r['ccf'] in {
    'Caja de Compensación Familiar COMFENALCO ANTIOQUIA',
    'Caja de Compensación Familiar de Antioquia: COMFAMA'}]
assert len(antioquia)==2
n_col=sum(int(r['trabajadores_empleados_dependientes']) for r in rows)
n_ant=sum(int(r['trabajadores_empleados_dependientes']) for r in antioquia)
assert n_col==9704786 and n_ant==1755360
factor=Decimal(n_col)/Decimal(n_ant)
effects={'menor_creacion':44557,'mayor_destruccion':5015,'menor_saldo_neto':49572}
assert effects['menor_creacion']+effects['mayor_destruccion']==effects['menor_saldo_neto']

def round_to(value,step=1000):
    return int((Decimal(value)/step).quantize(Decimal(1),rounding=ROUND_HALF_UP)*step)
def fmt(value,digits=0):
    return f'{value:,.{digits}f}'.replace(',','_').replace('.',',').replace('_','.')

result={k:{'antioquia_tabla_C1':v,'colombia_ilustrativo':str(Decimal(v)*factor),
           'colombia_redondeado_millar':round_to(Decimal(v)*factor)} for k,v in effects.items()}
assert sum(Decimal(result[k]['colombia_ilustrativo']) for k in ['menor_creacion','mayor_destruccion'])==Decimal(result['menor_saldo_neto']['colombia_ilustrativo'])
meta={'naturaleza':'Extrapolación mecánica ilustrativa del CJC. No estimación causal nacional.',
      'choque':'Aumento real de 1% en el salario mínimo, según interpretación de los autores regionales.',
      'horizonte':'Efecto anual regional estimado. No pérdida observada en 2026 ni pronóstico de 2027.',
      'fuente_efectos':{'autor':'Patiño, Chaparro y coautores (2026)','tabla':'C.1, fila C, pp. 33–34',
                       'muestra':'Empresas privadas de Antioquia con más de un trabajador y más de un periodo, enero 2022–febrero 2026.',
                       'url':'https://universidadeafit.widen.net/s/pk5kd8xjpm/efectos_del_incremento_del_salario_minimo_en_el_mercado_laboral_formal_de_antioquia'},
      'fuente_escala':{'entidad':'Superintendencia del Subsidio Familiar','dataset':'Población Sistema del Subsidio Familiar','id':'gim6-e69u',
                     'landing':'https://www.datos.gov.co/d/gim6-e69u','periodo':'Marzo de 2025','fecha_consulta':'2026-11-03',
                     'consulta':'https://www.datos.gov.co/resource/gim6-e69u.csv?$select=a_o,mes,ccf,trabajadores_empleados_dependientes&$where=a_o=%272025%27%20AND%20mes=3&$order=ccf&$limit=1000',
                     'archivo':str(SOURCE.relative_to(ROOT)),'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                     'registros':42,'variable':'trabajadores_empleados_dependientes','nacional':n_col,'dos_cajas_antioquia':n_ant,
                     'componentes_antioquia':antioquia},
      'factor_exacto':str(factor),'formula':'E_col_ilustrativo = E_ant_tablaC1 * N_CCF_nacional_mar2025 / N_CCF_dos_cajas_antioquia_mar2025',
      'resultados':result,'confianza_externa':'Low',
      'supuestos':['Mismo efecto por afiliado y exposición al mínimo comparables entre Antioquia y el país.',
                   'La razón de afiliados totales aproxima la razón entre las poblaciones privadas relevantes de la regresión.',
                   'El tamaño de marzo de 2025 permite reescalar un efecto regional estimado con información de 2022–2026.'],
      'limites':['El modelo regional no fue replicado por el CJC.',
                 'Los registros por caja no reproducen exactamente el universo de empresas privadas con más de un trabajador.',
                 'La afiliación por caja puede diferir de la ubicación del puesto de trabajo. No son todas las formas de empleo formal.',
                 'No corrige diferencias regionales de sectores, tamaños de empresa, informalidad o distribución salarial.',
                 'No se construye intervalo de confianza nacional a partir de errores estándar regionales.',
                 'No se multiplica por el aumento nominal de 23% ni por el aumento real de 2026. No se extrapola linealmente a choques grandes.']}
(OUT/'calculo_y_procedencia.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (OUT/'resultados.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f);w.writerow(['concepto','antioquia_tabla_C1','factor','colombia_ilustrativo_sin_redondear','colombia_redondeado_millar'])
    for k,r in result.items():w.writerow([k,r['antioquia_tabla_C1'],str(factor),r['colombia_ilustrativo'],r['colombia_redondeado_millar']])
lines=[r'\begin{table}[H]',r'\centering\small',
 r'\caption{Efecto regional y reescalamiento nacional ilustrativo ante un aumento real de 1\% del mínimo}',
 r'\label{tab:chaparro-escala}',r'\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}Xrr@{}}',r'\toprule',
 r'Puestos en un año & Antioquia & Colombia, ilustrativo\\',r'\midrule']
for label,key in [('Menor creación de puestos','menor_creacion'),('Mayor destrucción de puestos','mayor_destruccion'),('Reducción del saldo neto','menor_saldo_neto')]:
    rr=result[key];lines.append(f"{label} & {fmt(rr['antioquia_tabla_C1'])} & {fmt(rr['colombia_redondeado_millar'])}"+r' \\')
lines += [r'\bottomrule',r'\end{tabularx}',
 r'\fuente{Fuente: \citet[tabla~C.1]{chaparro}. Cálculo ilustrativo del CJC con afiliados dependientes a cajas de marzo de 2025 \citep{ssfAfiliados}. Los valores nacionales aproximan empleo dependiente afiliado a cajas, se redondean al millar y representan diferencias respecto del escenario sin el aumento. La extrapolación mantiene proporcionalmente los efectos regionales y no constituye una estimación causal para Colombia.}',r'\end{table}']
(ROOT/'Paper/sections/CuadroChaparro.tex').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'nacional':n_col,'antioquia':n_ant,'factor':str(factor),'resultados':result},ensure_ascii=False,indent=2))
