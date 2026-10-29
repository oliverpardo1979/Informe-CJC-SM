"""Reproduce la figura y verifica los cálculos a partir del CSV depositado.
Requiere reportlab. Ejecutar desde cualquier directorio con Python 3.
"""
from pathlib import Path
import csv, math, json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'data/series_2021_2025.csv').open(encoding='utf-8') as f:
    data=[{k:float(v) for k,v in row.items()} for row in csv.DictReader(f)]
def n(x):return f'{x:.1f}'.replace('.',',')
for kind in ['hora','ocupado']:
    annual=math.prod(1+r[f'pl_{kind}_tasa']/100 for r in data[1:])
    assert abs(annual-data[-1][f'pl_{kind}_indice']/100)<1e-12
assert abs(data[-1]['salario_real_prom_indice']-113.54341275793085)<1e-8
assert abs(data[-1]['salario_real_dic_indice']-114.63835290742146)<1e-8
target=ROOT/'Paper/figures/salario_productividad_2021_2025.pdf'
c=canvas.Canvas(str(target),pagesize=(660,335))
c.setTitle('Salario mínimo real y productividad laboral, 2021-2025')
left,right,bottom,top=56,475,53,286
def xx(y):return left+(y-2021)*(right-left)/4
def yy(v):return bottom+(v-94)*(top-bottom)/22
c.setFont('Helvetica',13)
for value in [95,100,105,110,115]:
    c.setStrokeColor(HexColor('#D9DFE4'));c.setLineWidth(.5)
    c.line(left,yy(value),right,yy(value))
    c.setFillColor(HexColor('#384858'));c.drawRightString(left-9,yy(value)-3,str(value))
for year in range(2021,2026):
    c.drawCentredString(xx(year),bottom-20,str(year))
c.saveState();c.translate(15,169);c.rotate(90);c.drawCentredString(0,0,'Índice, 2021 = 100');c.restoreState()
series=[('salario_real_prom_indice','#B95B22','Salario mínimo real','IPC promedio anual'),('pl_hora_indice','#245777','Productividad por hora',''),('pl_ocupado_indice','#2C7C69','Productividad por ocupado','')]
for key,color,label,sub in series:
    c.setStrokeColor(HexColor(color));c.setFillColor(HexColor(color));c.setLineWidth(2.2)
    if key=='pl_hora_indice':c.setDash(6,3)
    elif key=='pl_ocupado_indice':c.setDash(2,2)
    else:c.setDash()
    p=c.beginPath();p.moveTo(xx(2021),yy(100))
    for r in data[1:]:p.lineTo(xx(r['anio']),yy(r[key]))
    c.drawPath(p)
    for r in data:c.circle(xx(r['anio']),yy(r[key]),2.5,fill=1,stroke=0)
    end=data[-1][key]
    c.setFont('Helvetica-Bold',14);c.drawString(right+13,yy(end)+8,n(end))
    c.setFont('Helvetica',12);c.drawString(right+13,yy(end)-9,label)
    if sub:c.drawString(right+13,yy(end)-24,sub)
c.setDash();c.setFont('Helvetica',9);c.setFillColor(HexColor('#384858'))
c.drawString(left,18,'Fuente: DANE y montos legales del salario mínimo. Cálculos del CJC. 2025 preliminar.')
c.showPage();c.save()
print(json.dumps({'figura':str(target),'aumento_real_2026_pi_6_9':100*(1.23/1.069-1),'minimo_2027_7_por_ciento':1750905*1.07},indent=2))
