"""Rediseña la figura GEIH 2025. Usa una caché agregada de densidades.
Primera ejecución o actualización: python scripts/figura_edad.py --recalcular
Después: python scripts/figura_edad.py
Los microdatos se leen en su ubicación original y no se copian al repositorio.
"""
from pathlib import Path
import argparse, csv, json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyreadstat
from matplotlib.lines import Line2D
from matplotlib.ticker import MultipleLocator, FuncFormatter
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--recalcular',action='store_true')
parser.add_argument('--microdatos',type=Path,default=Path(r'C:\Users\jorge\Documents\Databases\GEIH\GEIH_2025_total.dta'))
args=parser.parse_args()
cache=ROOT/'data/densidades_salario_edad_2025.csv'
stats_path=ROOT/'data/estadisticas_figura_edad_2025.json'
SM=1423500
grid=np.linspace(np.log(150000),np.log(9000000),1400)
def quantile(x,w):
    i=np.argsort(x)
    return float(np.interp(.5,np.cumsum(w[i])/w.sum(),x[i]))
def kernel(x,w):
    edges=np.append(grid-(grid[1]-grid[0])/2,grid[-1]+(grid[1]-grid[0])/2)
    hist,_=np.histogram(np.log(x),bins=edges,weights=w)
    density=hist/hist.sum()/(grid[1]-grid[0])
    k=np.exp(-.5*(np.arange(-400,401)*(grid[1]-grid[0])/.09)**2)
    return np.convolve(density,k/k.sum(),mode='same')
if args.recalcular or not cache.exists():
    _,meta=pyreadstat.read_dta(args.microdatos,metadataonly=True)
    names={c.upper():c for c in meta.column_names}
    age=names.get('P6040') or names['EDAD']
    columns={names['OCI']:'ocupado',names['P6500']:'salario',
             names['FEX_C18']:'peso',age:'edad',names['P6430']:'posicion',
             names['P6800']:'horas',names['MES']:'mes'}
    df,_=pyreadstat.read_dta(args.microdatos,usecols=list(columns))
    df=df.rename(columns=columns)
    for column in df.columns:
        df[column]=pd.to_numeric(df[column],errors='coerce')
    df=df[(df.ocupado==1)&(df.salario>0)&(df.peso>0)&(df.edad>=15)&df.posicion.isin([1,2,3,7])]
    if set(df.mes.unique())!=set(range(1,13)): raise ValueError('Cobertura mensual inesperada')
    with (ROOT/'insumos/SalarioMinimo_Edad/Outputs/tables/estadisticas_salario_por_edad.csv').open(encoding='utf-8-sig') as f:
        reference=[r for r in csv.DictReader(f) if r['anio']=='2025']
    curves=[grid]
    stats={}
    for panel in ['todos','40h']:
        for group in ['joven','mayor']:
            sub=df[(df.edad<25) if group=='joven' else (df.edad>=25)]
            if panel=='40h': sub=sub[sub.horas>=40]
            x=sub.salario.to_numpy(); w=sub.peso.to_numpy()
            label=panel+'_'+group
            around=100*w[(x>=.97*SM)&(x<=1.03*SM)].sum()/w.sum()
            stats[label]={'muestra':len(x),'mediana':quantile(x,w),'alrededor_minimo':float(around)}
            ref=next(r for r in reference if r['grupo']==('menores de 25' if group=='joven' else '25 o mas') and r['poblacion']==('todos los asalariados' if panel=='todos' else 'tiempo completo (>= 40 h)'))
            assert len(x)==int(ref['muestra'])
            assert abs(stats[label]['mediana']-float(ref['mediana']))<.01
            assert abs(around-float(ref['pct_en_el_minimo_(±3%)']))<.0051
            curves.append(kernel(x,w))
    np.savetxt(cache,np.column_stack(curves),delimiter=',',
               header='log_salario,todos_joven,todos_mayor,40h_joven,40h_mayor',comments='')
    stats_path.write_text(json.dumps({'anio':2025,'salario_minimo':SM,
        'ancho_banda_log':.09,'normalizacion':'Masa dentro de rejilla 150.000 a 9.000.000; mismo método del gráfico original.',
        'fuente':'DANE, GEIH 2025. Cálculos del Centro Javeriano de Competitividad.',
        'grupos':stats},ensure_ascii=False,indent=2),encoding='utf-8')
curves=np.genfromtxt(cache,delimiter=',',names=True)
stats=json.loads(stats_path.read_text(encoding='utf-8'))['grupos']
NAVY='#243B53'; ORANGE='#C76A32'; GRAY='#52616F'; RED='#A13D3D'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'pdf.fonttype':42,'ps.fonttype':42})
fig,axes=plt.subplots(1,2,figsize=(8.4,5.1),sharey=True,facecolor='white')
fig.subplots_adjust(left=.075,right=.985,top=.81,bottom=.34,wspace=.14)
legend=[Line2D([0],[0],color=ORANGE,lw=2.4,label='15–24 años'),
        Line2D([0],[0],color=NAVY,lw=2.4,label='25 años o más'),
        Line2D([0],[0],color=GRAY,marker='o',mfc='white',lw=0,label='Mediana')]
fig.legend(handles=legend,loc='upper center',bbox_to_anchor=(.52,1.01),ncol=3,frameon=False,
           handlelength=2,columnspacing=1.7,fontsize=10)
fig.text(.53,.905,'Salario mínimo 2025: $1.423.500',ha='center',color=RED,fontsize=10,weight='bold')
ymax=max(max(curves[k]) for k in curves.dtype.names[1:])*1.08
def pesos(x):return '$'+f'{x:,.0f}'.replace(',','.')
def dec(x):return f'{x:.1f}'.replace('.',',')
for ax,panel,title in zip(axes,['todos','40h'],['A. Todos los asalariados','B. Jornada habitual ≥ 40 horas']):
    ax.set_title(title,loc='left',color=NAVY,weight='bold',fontsize=10,pad=13)
    ax.set_axisbelow(True)
    ax.grid(axis='y',color='#E3E8EC',lw=.6)
    for side in ['top','right','left']: ax.spines[side].set_visible(False)
    ax.spines['bottom'].set_color('#BAC5CD')
    ax.tick_params(length=0,labelsize=9,labelcolor=GRAY,pad=5)
    for group,col in [('mayor',NAVY),('joven',ORANGE)]:
        y=curves[panel+'_'+group]
        ax.fill_between(grid,y,color=col,alpha=.09,lw=0)
        ax.plot(grid,y,color=col,lw=2,zorder=3)
        med=stats[panel+'_'+group]['mediana']
        ax.scatter([np.log(med)],[np.interp(np.log(med),grid,y)],s=28,
                   facecolor='white',edgecolor=col,lw=1.6,zorder=5)
    ax.axvline(np.log(SM),color=RED,lw=1.1,ls=(0,(4,3)),zorder=2)
    ticks=[250000,500000,1000000,2000000,4000000,8000000]
    ax.set_xticks(np.log(ticks),['0,25','0,5','1','2','4','8'])
    ax.set_xlim(np.log(200000),np.log(8500000)); ax.set_ylim(0,ymax)
    ax.set_xlabel('Salario mensual (millones de pesos)',color=GRAY,fontsize=9,labelpad=8)
    # Resumen bajo los paneles: sin recuadros superpuestos a las curvas.
    ax.text(0,-.29,'Grupo',transform=ax.transAxes,color=GRAY,fontsize=8.5)
    ax.text(.56,-.29,'Mediana',transform=ax.transAxes,color=GRAY,fontsize=8.5,ha='right')
    ax.text(1,-.29,'En torno al mínimo',transform=ax.transAxes,color=GRAY,fontsize=8.5,ha='right')
    for yy,group,col,label in [(-.38,'joven',ORANGE,'15–24 años'),(-.47,'mayor',NAVY,'25 años o más')]:
        st=stats[panel+'_'+group]
        ax.text(0,yy,label,transform=ax.transAxes,color=col,fontsize=9,weight='bold')
        ax.text(.56,yy,pesos(st['mediana']),transform=ax.transAxes,color=col,fontsize=9,ha='right')
        ax.text(1,yy,dec(st['alrededor_minimo'])+'%',transform=ax.transAxes,color=col,fontsize=9,ha='right')
axes[0].set_ylabel('Densidad del logaritmo del salario',fontsize=9,color=GRAY,labelpad=8)
axes[0].yaxis.set_major_locator(MultipleLocator(.5))
axes[0].yaxis.set_major_formatter(FuncFormatter(lambda value, _: f'{value:g}'.replace('.',',')))
fig.text(.075,.045,'Escala salarial logarítmica · En torno al mínimo: ±3% del valor legal.',color=GRAY,fontsize=8.5)
out=ROOT/'Paper/figures'
out.mkdir(exist_ok=True,parents=True)
for suffix in ['pdf','png']:
    fig.savefig(out/f'distribucion_salarios_edad_2025.{suffix}',dpi=300,facecolor='white')
plt.close(fig)
print('Figura vectorial y PNG generados; cifras contrastadas con el insumo original.')

