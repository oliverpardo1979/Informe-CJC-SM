"""Series nominales históricas y escenario de ajuste de 7% para 2027."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv, json, shutil, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
ROOT=Path(__file__).resolve().parents[1]
SRC=Path(r'C:\Users\jorge\Documents\Trabajo-Profesional\Javeriana\PTF')
DEST=ROOT/'insumos/PTF_series'
DEST.mkdir(parents=True,exist_ok=True)
files=['Code/17_Figuras_series_simulacion_2026.py',
       'Outputs/tables/indice_salario_minimo_real_productividad_2010_2025.csv',
       'Outputs/Figures/fig_serie_salario_minimo_2027.png',
       'Outputs/Figures/fig_serie_salario_minimo_pesos_2027.png']
# Conservar los antecedentes originales; el nuevo gráfico usa una regla determinista.
manifest=[]
for relative in files:
    source=SRC/relative; target=DEST/relative
    target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists(): shutil.copy2(source,target)
    manifest.append({'archivo':relative,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
(DEST/'procedencia.json').write_text(json.dumps({'origen':str(SRC),'archivos':manifest,
    'uso':'Antecedentes de las series. Los supuestos de simulación y propuestas de terceros no se usan en la nueva figura.'},ensure_ascii=False,indent=2),encoding='utf-8')
with (DEST/files[1]).open(encoding='utf-8-sig') as f:
    amounts={int(r['anio']):int(float(r['smmlv_nominal'])) for r in csv.DictReader(f)}
with (ROOT/'data/series_2021_2025.csv').open(encoding='utf-8') as f:
    for row in csv.DictReader(f):
        assert amounts[int(row['anio'])]==int(float(row['minimo_nominal']))
amounts[2026]=1750905
adjustment=Decimal('7')
proposal=int((Decimal(amounts[2026])*(1+adjustment/100)).quantize(Decimal(1),rounding=ROUND_HALF_UP))
assert proposal==1873468
years=np.arange(2014,2027)
values=np.array([amounts[int(y)] for y in years])
rates=np.array([100*(amounts[int(y)]/amounts[int(y)-1]-1) for y in years])
with (ROOT/'data/serie_nominal_2014_2027.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['anio','salario_basico_pesos','aumento_nominal_pct','naturaleza'])
    for y,v,r in zip(years,values,rates): w.writerow([y,v,r,'historico'])
    w.writerow([2027,proposal,'7','escenario_CJC'])
from diseno_serie_minimo import dibujar
dibujar(ROOT,years,values,rates,proposal)
