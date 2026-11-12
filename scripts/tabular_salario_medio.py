"""Tabulados P6500: GEIH 2021–2026, ventanas comparables y anual disponible.
Uso: python scripts/tabular_salario_medio.py [--geih-dir RUTA]
No exporta registros individuales. Precisión: repr de sumas float64 con math.fsum.
"""
from pathlib import Path
import argparse,csv,json,math
import numpy as np
import pandas as pd
import pyreadstat
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--geih-dir',type=Path,default=Path(r'C:\Users\jorge\Documents\Databases\GEIH'))
args=parser.parse_args()
OUT=ROOT/'data/salario_medio_geih'
OUT.mkdir(parents=True,exist_ok=True)
SM={2021:908526,2022:1000000,2023:1160000,2024:1300000,2025:1423500,2026:1750905}
principal=[];anual=[];monthly=[];audit=[];metaout=[];frame_audit=[]
medianas=[]

def mediana_ponderada(df):
    ingresos = df.ingreso.to_numpy(dtype=np.float64)
    pesos = df.peso.to_numpy(dtype=np.float64)
    orden = np.argsort(ingresos, kind='stable')
    mitad = math.fsum(pesos) / 2
    indice = np.searchsorted(np.cumsum(pesos[orden]), mitad, side='left')
    mediana = float(ingresos[orden[indice]])
    assert math.fsum(pesos[ingresos < mediana]) < mitad
    assert math.fsum(pesos[ingresos <= mediana]) >= mitad
    return mediana

def tabulate(df,y,pop,months):
    if pop=='jornada_40h_mas':
        df=df[np.isfinite(df.horas)&df.horas.between(40,168)]
    assert len(df)>0
    seen=sorted(int(m) for m in df.mes.unique())
    assert seen==months,(y,pop,seen,months)
    weights=df.peso.to_numpy(dtype=np.float64)
    income=df.ingreso.to_numpy(dtype=np.float64)
    sw=math.fsum(weights)
    sxw=math.fsum(float(x)*float(w) for x,w in zip(income,weights))
    return {'anio':y,'periodo':'enero_agosto' if months==list(range(1,9)) else ('anual' if len(months)==12 else f'mes_{months[0]:02d}'),
        'poblacion':pop,'meses_cubiertos':'|'.join(f'{m:02d}' for m in months),'numero_meses':len(months),
        'media_ponderada_p6500_pesos':sxw/sw,'suma_ponderadores':sw,
        'suma_ponderada_p6500':sxw,'muestra_registros':len(df),
        'poblacion_promedio_mensual':sw/len(months),
        'smlmv_pesos':SM[y],'smlmv_sobre_media':SM[y]/(sxw/sw),
        'variable_ponderador':'FEX_C18','marco':'2018'}
for y in range(2021,2027):
    path=args.geih_dir/f'GEIH_{y}_total.dta'
    _,m=pyreadstat.read_dta(path,metadataonly=True)
    names={n.upper():n for n in m.column_names}
    rename={names['MES']:'mes',names['P6500']:'ingreso',names['P6800']:'horas',
        names['FEX_C18']:'peso',names.get('P6040',names.get('EDAD')):'edad',
        names['P6430']:'posicion',names['OCI']:'ocupado'}
    frame_vars=[n for n in m.column_names if n.upper() in ['P3038','P3039','P3042','P3043','OFICIO_C8','OFICIO_C8_2D','FEX_C18']]
    extra=[c for c in frame_vars if c not in rename] if y==2021 else []
    df,_=pyreadstat.read_dta(path,usecols=list(rename)+extra,user_missing=True)
    df=df.rename(columns=rename).apply(pd.to_numeric,errors='coerce')
    if y==2021:
        for month,part in df.groupby('mes'):
            frame_audit.append({'anio':y,'mes':int(month),'registros':len(part),
                **{c+'_no_faltantes':int(part[c].notna().sum()) for c in extra},
                'suma_fex_total_archivo':math.fsum(part.peso.dropna())})
    months=sorted(int(v) for v in df.mes.dropna().unique())
    assert months==(list(range(1,9)) if y==2026 else list(range(1,13))),(y,months)
    target=df[(df.edad>=15)&df.posicion.isin([1,2,3,7])&(df.ocupado==1)]
    salary_valid=np.isfinite(target.ingreso)&(target.ingreso>0)&~target.ingreso.isin([98,99])
    weight_valid=np.isfinite(target.peso)&(target.peso>0)
    valid=target[salary_valid&weight_valid].copy()
    metaout.append({'anio':y,'archivo':path.name,'bytes':path.stat().st_size,
        'registros_archivo':m.number_rows,'etiqueta_archivo':m.file_label,
        'variables':rename,'variables_compatibles_marco_2018':frame_vars,
        'meses_presentes':months,'missing_user_values':m.missing_user_values,
        'missing_ranges':m.missing_ranges})
    for period,allowed in [('enero_agosto',list(range(1,9))),('anual_disponible',months)]:
        raw=target[target.mes.isin(allowed)]
        sub=valid[valid.mes.isin(allowed)]
        audit.append({'anio':y,'periodo':period,'candidatos_asalariados_15_mas':len(raw),
            'p6500_98':int((raw.ingreso==98).sum()),'p6500_99':int((raw.ingreso==99).sum()),
            'p6500_cero_negativo':int((raw.ingreso<=0).sum()),
            'p6500_faltante_no_finito':int((~np.isfinite(raw.ingreso)).sum()),
            'fex_invalido':int((~np.isfinite(raw.peso)|(raw.peso<=0)).sum()),
            'muestra_final_todos':len(sub),
            'horas_faltantes_no_finitas':int((~np.isfinite(sub.horas)).sum()),
            'horas_fuera_0_168':int((np.isfinite(sub.horas)&~sub.horas.between(0,168)).sum()),
            'p6500_min':float(sub.ingreso.min()),'p6500_max':float(sub.ingreso.max()),
            'p6500_valores_hasta_1000':json.dumps(sub.loc[sub.ingreso<=1000,'ingreso'].value_counts().sort_index().to_dict()),
            'horas_98':int((sub.horas==98).sum()),'horas_99':int((sub.horas==99).sum())})
    enero_agosto = valid[valid.mes.between(1,8)]
    medianas.append({'anio': y, 'mediana_ponderada_p6500_pesos_nominales': mediana_ponderada(enero_agosto)})
    for pop in ['todos_asalariados','jornada_40h_mas']:
        principal.append(tabulate(enero_agosto,y,pop,list(range(1,9))))
        if y<2026:anual.append(tabulate(valid,y,pop,months))
        for month in months:
            monthly.append(tabulate(valid[valid.mes==month],y,pop,[month]))
    # Reconciliar meses con ventana agrupada y media; asegura ponderación por registros.
    for row in principal[-2:]:
        mm=[r for r in monthly if r['anio']==y and r['poblacion']==row['poblacion'] and int(r['meses_cubiertos'])<=8]
        assert sum(r['muestra_registros'] for r in mm)==row['muestra_registros']
        assert math.isclose(math.fsum(r['suma_ponderadores'] for r in mm),row['suma_ponderadores'],rel_tol=1e-14)
        assert math.isclose(math.fsum(r['suma_ponderada_p6500'] for r in mm)/row['suma_ponderadores'],row['media_ponderada_p6500_pesos'],rel_tol=1e-14)
    print(y,'meses',months,'medias ene-ago',[(r['poblacion'],round(r['media_ponderada_p6500_pesos'],2),r['muestra_registros']) for r in principal[-2:]],flush=True)
def save(name,rows):
    with (OUT/name).open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
save('salario_medio_enero_agosto_2021_2026.csv',principal)
save('salario_mediano_enero_agosto_2021_2026.csv',medianas)
save('salario_medio_anual_2021_2025.csv',anual)
save('salario_medio_mensual_2021_2026.csv',monthly)
save('auditoria_filtros.csv',audit)
save('auditoria_marco_2021_mensual.csv',frame_audit)
# Una fila por año para la construcción directa del cuadro del boletín.
wide=[]
for year in range(2021,2027):
    pair=[r for r in principal if r['anio']==year]
    row={k:pair[0][k] for k in ['anio','periodo','meses_cubiertos','numero_meses','marco','variable_ponderador','smlmv_pesos']}
    for entry in pair:
        suffix='todos' if entry['poblacion']=='todos_asalariados' else '40h_mas'
        for key in ['media_ponderada_p6500_pesos','suma_ponderadores','suma_ponderada_p6500','muestra_registros','poblacion_promedio_mensual','smlmv_sobre_media']:
            row[key+'_'+suffix]=entry[key]
    wide.append(row)
save('salario_medio_comparable_2021_2026.csv',wide)
(OUT/'metadatos_bases.json').write_text(json.dumps(metaout,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
print('Exportados:',len(principal),'filas comparables,',len(anual),'anuales,',len(monthly),'mensuales.')

