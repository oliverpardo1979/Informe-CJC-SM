"""Auditoría acotada de cifras propias del informe CJC.
No reestima GEIH ni reproduce modelos externos. Ejecutar desde cualquier directorio.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv, json, math, hashlib, sys, platform, subprocess
import importlib.metadata as metadata
import pypdfium2 as pdfium
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'quality_reports'
PHASE=sys.argv[1] if len(sys.argv)>1 else 'inicial'
D=Decimal

def readcsv(name):
    with (ROOT/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def num(x):return float(x.strip().replace('\\$','').replace('$','').replace('.','').replace(',','.'))
def dec(x):return D(str(x))
def rounded(x,digits):return float(dec(x).quantize(D(1).scaleb(-digits),rounding=ROUND_HALF_UP))
def fmt(x,digits):return f'{rounded(x,digits):,.{digits}f}'.replace(',','_').replace('.',',').replace('_','.')
def text(path):return (ROOT/path).read_text(encoding='utf-8')
def pdftext(path):
    doc=pdfium.PdfDocument(ROOT/path)
    return '\n'.join(doc[i].get_textpage().get_text_range() for i in range(len(doc)))
def loc(path,needle):
    for i,line in enumerate(text(path).splitlines(),1):
        if needle in line:return f'{path}:{i}'
    raise ValueError((path,needle))
claims=[]
def add(cid,path,needle,reported,computed,tol,how,kind='percentage',unit='%'):
    claims.append({'claim_id':cid,'location':loc(path,needle),'kind':kind,'reported_value':float(reported),
                   'computed_value':float(computed),'tolerance':tol,'unit':unit,'how_computed':how,
                   'raw_context':next(l for l in text(path).splitlines() if needle in l),
                   'status':'PASS' if abs(float(reported)-float(computed))<=tol+1e-12 else 'FAIL'})
def table(path):
    rows=[]
    for line in text(path).splitlines():
        if '&' in line and line.rstrip().endswith('\\\\'):
            cells=[c.strip() for c in line.rstrip()[:-2].split('&')]
            if re.fullmatch(r'20\d\d|[67],[0789]',cells[0]):rows.append((cells[0],cells[1:]))
    return rows
series=readcsv('data/series_2021_2025.csv')
nominal={int(r['anio']):dec(r['minimo_nominal']) for r in series}
nominal[2020]=D(877803);nominal[2026]=D(1750905)
wide=readcsv('data/salario_medio_geih/salario_medio_comparable_2021_2026.csv')
monthly=readcsv('data/salario_medio_geih/salario_medio_mensual_2021_2026.csv')
path='Paper/sections/CuadroSalariosMedios.tex'
for year,values in table(path):
    y=int(year);w=next(r for r in wide if int(r['anio'])==y)
    add(f'SM_{y}',path,year+' &',num(values[0]),nominal[y],0,f'monto legal depositado {y}','count','pesos')
    add(f'AUMENTO_{y}',path,year+' &',num(values[1]),100*(nominal[y]/nominal[y-1]-1),.005,f'100*(SM[{y}]/SM[{y-1}]-1)')
    for i,(suf,pop) in enumerate([('todos','todos_asalariados'),('40h_mas','jornada_40h_mas')]):
        months=[r for r in monthly if int(r['anio'])==y and r['poblacion']==pop and int(r['meses_cubiertos'])<=8]
        assert len(months)==8
        sw=sum(dec(r['suma_ponderadores']) for r in months);sx=sum(dec(r['suma_ponderada_p6500']) for r in months)
        assert math.isclose(float(sw),float(w['suma_ponderadores_'+suf]),rel_tol=1e-12)
        assert math.isclose(float(sx),float(w['suma_ponderada_p6500_'+suf]),rel_tol=1e-12)
        assert sum(int(r['muestra_registros']) for r in months)==int(w['muestra_registros_'+suf])
        add(f'MEDIA_{y}_{suf}',path,year+' &',num(values[i+2]),sx/sw/D(1e6),.005,
            f'sum(meses 1:8 numerador {y},{pop})/sum(ponderador)/1e6','point_estimate','millones de pesos')
path='Paper/sections/Metodologia.tex'
for year,values in table(path):
    y=int(year);r=next(x for x in series if int(x['anio'])==y);prev=next(x for x in series if int(x['anio'])==y-1)
    computed=[100*(nominal[y]/nominal[y-1]-1),
              100*((nominal[y]/dec(r['ipc_promedio']))/(nominal[y-1]/dec(prev['ipc_promedio']))-1),
              100*((nominal[y]/dec(r['ipc_diciembre']))/(nominal[y-1]/dec(prev['ipc_diciembre']))-1),
              dec(r['pl_hora_tasa']),dec(r['pl_ocupado_tasa'])]
    for j,v in enumerate(computed):add(f'ANUAL_{y}_{j}',path,year+' &',num(values[j]),v,.005,f'cálculo directo CSV, métrica {j}, año {y}')
path='Paper/sections/CuadroEscenarios.tex'
for g,values in table(path):
    rate=dec(g.replace(',','.'))
    for j,v in enumerate([nominal[2026]*rate/100,nominal[2026]*(1+rate/100)]):
        add(f'ESCENARIO_{g}_{j}',path,g+' &',num(values[j]),rounded(v,0),0,f'ROUND_HALF_UP(SM2026*{rate}/100'+(' + SM2026' if j else '')+')','count','pesos')
# Published cumulative numbers, independently recomputed from annual inputs.
last,first=series[-1],series[0]
real=100*((nominal[2025]/dec(last['ipc_promedio']))/(nominal[2021]/dec(first['ipc_promedio']))-1)
ph=100*(math.prod(1+float(r['pl_hora_tasa'])/100 for r in series[1:])-1)
po=100*(math.prod(1+float(r['pl_ocupado_tasa'])/100 for r in series[1:])-1)
for token,v,label in [('13,5',real,'REAL_ACUMULADO'),('1,2',ph,'PL_HORA_ACUMULADO'),('4,6',abs(po),'PL_PERSONA_CAIDA')]:
    for path in ['Paper/sections/ResumenEjecutivo.tex','Paper/sections/Cuerpo.tex','Paper/sections/Conclusiones.tex']:
        if token+'\\%' in text(path):add(label+'_'+Path(path).stem,path,token+'\\%',float(token.replace(',','.')),v,.1,'SM/IPC promedio o producto de tasas DANE 2022:2025')
for path in ['Paper/sections/ResumenEjecutivo.tex','Paper/sections/Cuerpo.tex','Paper/sections/Metodologia.tex']:
    add('REAL_2026_'+Path(path).stem,path,'15,1\\%',15.1,100*(D('1.23')/D('1.069')-1),.1,'100*(1.23/1.069-1)')
if '1,3\\%' in text('Paper/sections/Cuerpo.tex'):
    add('REAL_2027_ILUSTRATIVO','Paper/sections/Cuerpo.tex','1,3\\%',1.3,100*(D('1.069')/D('1.055')-1),.1,'100*(1.069/1.055-1), escenario de cierre')
# Every numeric age table cell against the deposited aggregate CSV.
ages=readcsv('insumos/SalarioMinimo_Edad/Outputs/tables/estadisticas_salario_por_edad.csv')
selected=[r for r in ages if r['anio']=='2025' and r['poblacion']=='tiempo completo (>= 40 h)']
young=next(r for r in selected if r['grupo']=='menores de 25');older=next(r for r in selected if r['grupo']=='25 o mas')
path='Paper/sections/CuadroEdad.tex'
keys=['pct_hasta_1,25_minimos','pct_mas_de_2_minimos','pct_en_el_minimo_(±3%)','pct_bajo_el_minimo']
lines=[l for l in text(path).splitlines() if '&' in l and l.split('&')[0].strip()!='Indicador']
for line,k in zip(lines,keys):
    cells=line.rstrip()[:-2].split('&')
    for j,r in enumerate([young,older]):add('EDAD_'+k+'_'+str(j),path,cells[0],num(cells[j+1]),r[k],.1,f'CSV GEIH2025 {r["grupo"]} {k}')
# Body ratios against the exact comparable aggregates.
for y,suf,token in [(2021,'todos','59,3'),(2026,'todos','68,2'),(2025,'todos','65,9'),(2021,'40h_mas','56,7'),(2026,'40h_mas','64,9')]:
    w=next(r for r in wide if int(r['anio'])==y)
    add(f'RAZON_{y}_{suf}','Paper/sections/Cuerpo.tex',token+'\\%',float(token.replace(',','.')),100*dec(w['smlmv_pesos'])/dec(w['media_ponderada_p6500_pesos_'+suf]),.1,f'SMLMV/media exacta {y},{suf}')
# Technical-note exclusions.
audit=readcsv('data/salario_medio_geih/auditoria_filtros.csv')
a=next(r for r in audit if r['anio']=='2021' and r['periodo']=='enero_agosto')
b=next(r for r in audit if r['anio']=='2026' and r['periodo']=='enero_agosto')
for token,v in [('10.560',int(a['p6500_98'])+int(a['p6500_99'])),('2.223',int(a['p6500_faltante_no_finito'])),('303',int(b['p6500_faltante_no_finito']))]:
    add('EXCLUSION_'+token,'Paper/sections/Metodologia.tex',token,num(token),v,0,'auditoria_filtros.csv enero_agosto','count','registros')
# Figures: the rendered PDF is read, not inferred solely from the drawing code.
figures={name:pdftext('Paper/figures/'+name) for name in ['salario_productividad_2021_2025.pdf','distribucion_salarios_edad_2025.pdf','serie_salario_minimo_2027_7pct.pdf']}
fig_checks=[]
for v,label in [(100+float(real),'mínimo real'),(100+ph,'productividad hora'),(100+po,'productividad persona')]:
    token=fmt(v,1);fig_checks.append({'figure':'salario_productividad_2021_2025.pdf','label':label,'expected':token,'found':token in figures['salario_productividad_2021_2025.pdf']})
stats=json.loads(text('data/estadisticas_figura_edad_2025.json'))['grupos']
for key,r in stats.items():
    for field,digits in [('mediana',0),('alrededor_minimo',1)]:
        token=('$' if field=='mediana' else '')+fmt(r[field],digits)+('%' if field!='mediana' else '')
        fig_checks.append({'figure':'distribucion_salarios_edad_2025.pdf','label':key+'_'+field,'expected':token,'found':token in figures['distribucion_salarios_edad_2025.pdf']})
for y in [2014,2021,2023,2026,2027]:
    r=next(r for r in readcsv('data/serie_nominal_2014_2027.csv') if int(r['anio'])==y)
    token='$'+fmt(r['salario_basico_pesos'],0)
    fig_checks.append({'figure':'serie_salario_minimo_2027_7pct.pdf','label':str(y),'expected':token,'found':token in figures['serie_salario_minimo_2027_7pct.pdf']})
# Horizontal agreement for each own claim wherever repeated in main / note PDFs.
main_pdf=pdftext('main.pdf');note_pdf=pdftext('nota_tecnica.pdf')
for c in claims:
    c['display_token']=fmt(c['reported_value'], 2 if c['claim_id'].startswith(('MEDIA_','AUMENTO_','ANUAL_')) else (0 if c['kind']=='count' else 1))
    # Not a manuscript-wide search certification. All claims have their LaTeX display located.
    c['horizontal_status']='CHECKED: LaTeX and corresponding compiled PDF' if c['display_token'] in (note_pdf if c['location'].startswith(('Paper/sections/Metodologia','Paper/sections/CuadroEdad','Paper/sections/CuadroEscenarios')) else main_pdf) else 'FAIL: token missing in compiled PDF'
# Disclose sensitivity; the official table remains unchanged.
sensitivity=[]
for y in range(2021,2027):
    mm=[r for r in monthly if int(r['anio'])==y and r['poblacion']=='todos_asalariados' and 2<=int(r['meses_cubiertos'])<=8]
    mean=sum(dec(r['suma_ponderada_p6500']) for r in mm)/sum(dec(r['suma_ponderadores']) for r in mm)
    sensitivity.append({'anio':y,'ventana_entrevistas':'febrero-agosto','media':float(mean),'smlmv_sobre_media_pct':float(100*nominal[y]/mean)})
(OUT/f'reproducibility_claims_CJC_{PHASE}.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/f'figure_checks_CJC_{PHASE}.json').write_text(json.dumps(fig_checks,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'sensibilidad_ventana_GEIH.json').write_text(json.dumps(sensitivity,ensure_ascii=False,indent=2),encoding='utf-8')
fail=[r for r in claims if r['status']=='FAIL'];drift=[r for r in claims if r['horizontal_status'].startswith('FAIL')]
fig_fail=[r for r in fig_checks if not r['found']]
report=['# Auditoría acotada de reproducibilidad del CJC','',f'Fecha: 3 de noviembre de 2026. Fase: {PHASE}.',
'','Se cotejan cifras propias contra CSV, JSON y PDF vectorial. No se reestiman microdatos GEIH ni modelos de fuentes externas. La comprobación de tokens en PDF verifica presencia, no unicidad semántica. Los tres gráficos también se leen por etiquetas y se inspeccionan visualmente.',
'',f'Claims: {len(claims)}. PASS: {len(claims)-len(fail)}. FAIL: {len(fail)}. Discrepancias de compilación: {len(drift)}. Etiquetas de figura: {len(fig_checks)}, ausentes: {len(fig_fail)}.',
'','## Cifras propias','', '| ID | Ubicación | Texto | Cálculo | Tolerancia | Estado |','|---|---|---:|---:|---:|---|']
for c in claims:report.append(f'| {c["claim_id"]} | {c["location"]} | {c["reported_value"]:g} | {c["computed_value"]:.9g} | {c["tolerance"]:g} | {c["status"]} |')
report += ['','## Límites de la comprobación horizontal','', 'Se revisan las apariciones del informe principal, nota técnica y tres figuras, sin diapositivas ni archivos privados originales. No hay passport con declaraciones exhaustivas de todos los displays. Los accesores y contextos literales están en el JSON de claims. Se usa redondeo de presentación más estricto para celdas de dos decimales. Los enteros en pesos usan redondeo al peso antes del cotejo.',
'','## Cifras atribuidas a terceros','', 'Las cifras fiscales del MFMP y CARF, los pronósticos, las transiciones de Antioquia y los plazos normativos no son resultados de este pipeline. Se verifican contra fuentes primarias en el informe sustantivo y quedan fuera del PASS de reproducibilidad propia. No se reproducen sus modelos. Tampoco se declara validación del diseño muestral, de la identificación causal ni de las estimaciones de los autores externos.',
'','## Sensibilidad de meses','', '| Año | Media febrero–agosto entrevistas | SMLMV/media (%) |','|---|---:|---:|']
for r in sensitivity:report.append(f'| {r["anio"]} | {r["media"]:.2f} | {r["smlmv_sobre_media_pct"]:.4f} |')
report+=['','P6500 refiere al mes anterior. Excluir enero evita que la ventana contenga salarios de diciembre del año previo. Es una sensibilidad descriptiva, no una corrección de composición o no respuesta. La tabla principal sigue usando enero–agosto.']
(OUT/f'reproducibility_audit_CJC_{PHASE}.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
env={'python':sys.version,'platform':platform.platform(),'packages':{n:metadata.version(n) for n in ['pypdfium2','reportlab']}}
(OUT/'sessionInfo.json').write_text(json.dumps(env,indent=2),encoding='utf-8')
revision=subprocess.check_output(['git','rev-parse','--short','HEAD'],cwd=ROOT,text=True).strip()
dirty=subprocess.check_output(['git','status','--porcelain','--','.',':(exclude)quality_reports'],cwd=ROOT,text=True).strip()
if dirty:revision+='-dirty'
log=OUT/'replication-log.md'
with log.open('a',encoding='utf-8') as f:
    if log.stat().st_size==0:f.write('# Replication log\n\nRegistro acumulativo. Las correcciones se añaden como nuevas entradas.\n\n')
    f.write(f'## 2026-11-03 — CJC @ {revision} — {PHASE}\n\n{len(claims)} cifras propias. {len(fail)} FAIL, {len(drift)} discrepancias PDF, {len(fig_fail)} etiquetas ausentes.\n\n')
    f.write('| ID | Fuente/cálculo | Reportado | Calculado | Tolerancia | Estado |\n|---|---|---:|---:|---:|---|\n')
    for c in claims:f.write(f'| {c["claim_id"]} | {c["how_computed"]} | {c["reported_value"]:g} | {c["computed_value"]:.9g} | {c["tolerance"]:g} | {c["status"]} |\n')
print(json.dumps({'phase':PHASE,'claims':len(claims),'fail':len(fail),'pdf_drift':len(drift),'figure_checks':len(fig_checks),'figure_fail':len(fig_fail)},ensure_ascii=False))
if fail or drift or fig_fail:raise SystemExit(1)
