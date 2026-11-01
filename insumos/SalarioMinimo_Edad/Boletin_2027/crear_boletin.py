from pathlib import Path
import csv
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)
NAVY, BLUE, ORANGE, TEAL = '#17294D', '#1769AA', '#D97732', '#16857A'
def font(n, bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/' + ('arialbd.ttf' if bold else 'arial.ttf'), n)
data = list(csv.DictReader(open(ROOT/'PTF/Outputs/tables/indice_salario_minimo_real_productividad_2010_2025.csv', encoding='utf-8-sig')))
im = Image.new('RGB',(1800,900),'white'); dr=ImageDraw.Draw(im)
x=lambda y:130+(y-2010)*100
y=lambda v:760-(v-100)*16
for v in range(100,141,10):
    dr.line((130,y(v),1630,y(v)),fill='#DEDFE2',width=2)
    dr.text((50,y(v)-20),str(v),font=font(30),fill='#555555')
for yr in [2010,2013,2016,2019,2021,2023,2025]:
    dr.text((x(yr)-35,785),str(yr),font=font(29),fill='#555555')
series=[('indice_smmlv_real','Salario mínimo real',ORANGE),('indice_prod_hora','Productividad por hora',BLUE),('indice_prod_ocupado','Productividad por ocupado',TEAL)]
for j,(key,label,col) in enumerate(series):
    dr.line((130,34+j*43,200,34+j*43),fill=col,width=7)
    dr.text((220,15+j*43),label,font=font(32),fill='#222222')
    pts=[(x(int(r['anio'])),y(float(r[key]))) for r in data]
    dr.line(pts,fill=col,width=6)
    for a,b in pts: dr.ellipse((a-5,b-5,a+5,b+5),fill=col)
    a,b=pts[-1]; dr.text((a+18,b-18),f'{float(data[-1][key]):.1f}'.replace('.',','),font=font(32,True),fill=col)
dr.text((130,845),'Índices con base 2010 = 100 · Salario deflactado por IPC promedio anual',font=font(28),fill='#555555')
im.save(OUT/'figura_1.png')

im=Image.new('RGB',(1800,630),'white'); dr=ImageDraw.Draw(im)
for i,(label,young,older) in enumerate([('Hasta 1,25 salarios mínimos',81.25,60.24),('Más de 2 salarios mínimos',3.80,19.56)]):
    yy=140+i*220
    dr.text((40,yy-75),label,font=font(36,True),fill='#222222')
    for j,(v,col) in enumerate([(young,ORANGE),(older,NAVY)]):
        by=yy+j*63; dr.rectangle((430,by,430+v*13,by+40),fill=col)
        dr.text((445+v*13,by-1),f'{v+1e-8:.1f} %'.replace('.',','),font=font(34,True),fill=col)
dr.rectangle((40,35,75,60),fill=ORANGE); dr.text((90,26),'15 a 24 años',font=font(33),fill='#222222')
dr.rectangle((600,35,635,60),fill=NAVY); dr.text((650,26),'25 años o más',font=font(33),fill='#222222')
dr.text((40,560),'Asalariados con 40 o más horas habituales por semana · GEIH 2025',font=font(29),fill='#555555')
im.save(OUT/'figura_3.png')

doc=Document(); sec=doc.sections[0]
sec.page_width=Inches(8.27); sec.page_height=Inches(11.69)
sec.top_margin=Inches(.72); sec.bottom_margin=Inches(.68)
sec.left_margin=sec.right_margin=Inches(.78)
for name in ['Normal','Title','Subtitle','Heading 1','Heading 2','Caption']:
    st=doc.styles[name]; st.font.name='Arial'; st.font.color.rgb=RGBColor(0,0,0)
    st.paragraph_format.space_after=Pt(7)
doc.styles['Normal'].font.size=Pt(10.5)
doc.styles['Normal'].paragraph_format.line_spacing=1.12
doc.styles['Title'].font.size=Pt(25)
doc.styles['Title'].font.bold=True
doc.styles['Subtitle'].font.size=Pt(12)
doc.styles['Heading 1'].font.size=Pt(16)
doc.styles['Heading 2'].font.size=Pt(12)
doc.styles['Caption'].font.size=Pt(8.5)
doc.styles['Caption'].paragraph_format.line_spacing=1.05
for name in ['Title','Subtitle','Heading 1','Heading 2']:
    doc.styles[name].paragraph_format.keep_with_next=True
sec.footer_distance=Inches(.3)
foot=sec.footer.paragraphs[0]; foot.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=foot.add_run('Centro Javeriano de Competitividad  |  '); r.font.size=Pt(8)
field=OxmlElement('w:fldSimple'); field.set(qn('w:instr'),'PAGE'); foot._p.append(field)
doc.core_properties.title='Salario mínimo 2027 El debate pendiente'
doc.core_properties.subject='Productividad, empleo formal y oportunidades para los jóvenes en Colombia'
doc.core_properties.author='Centro Javeriano de Competitividad'
def p(t,style=None): return doc.add_paragraph(t,style)
def h(t): doc.add_heading(t,1)
def page(): doc.add_page_break()
def picture(path,caption,note):
    par=doc.add_paragraph(); par.paragraph_format.keep_with_next=True
    par.add_run().add_picture(str(path),width=Inches(6.65))
    p(caption,'Caption'); p(note,'Caption')
def table(headers, rows, widths):
    t=doc.add_table(rows=1,cols=len(headers)); t.autofit=False
    for c,w in zip(t.columns,widths): c.width=Inches(w)
    for c,s in zip(t.rows[0].cells,headers): c.text=s
    for row in rows:
        for c,s in zip(t.add_row().cells,row): c.text=str(s)
    for i,row in enumerate(t.rows):
        pr=row._tr.get_or_add_trPr(); pr.append(OxmlElement('w:cantSplit'))
        if i==0: pr.append(OxmlElement('w:tblHeader'))
        for j,c in enumerate(row.cells):
            c.width=Inches(widths[j]); c.vertical_alignment=1
            cp=c._tc.get_or_add_tcPr()
            borders=OxmlElement('w:tcBorders')
            for edge in ['top','left','bottom','right']:
                e=OxmlElement('w:'+edge); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:color'),'D9D9D9'); borders.append(e)
            cp.append(borders)
            shade=OxmlElement('w:shd'); shade.set(qn('w:fill'),'17294D' if i==0 else ('F3F5F7' if i%2 else 'FFFFFF')); cp.append(shade)
            margins=OxmlElement('w:tcMar')
            for edge in ['top','bottom','left','right']:
                el=OxmlElement('w:'+edge); el.set(qn('w:w'),'90'); el.set(qn('w:type'),'dxa'); margins.append(el)
            cp.append(margins)
            for par in c.paragraphs:
                par.paragraph_format.space_after=Pt(2); par.paragraph_format.line_spacing=1.05
                if j>0: par.alignment=WD_ALIGN_PARAGRAPH.CENTER
                for r in par.runs:
                    r.font.size=Pt(9); r.bold=i==0
                    if i==0:r.font.color.rgb=RGBColor(255,255,255)
    p('')

p('Centro Javeriano de Competitividad','Subtitle')
p('Salario mínimo 2027\nEl debate pendiente','Title')
p('Productividad, empleo formal y oportunidades para los jóvenes en Colombia','Subtitle')
p('Boletín de análisis económico · 27 de octubre de 2026','Caption')
p('La discusión del salario mínimo para 2027 debe considerar la distancia acumulada entre su poder adquisitivo y la productividad laboral, así como las oportunidades de quienes buscan ingresar al empleo formal. Entre 2021 y 2025, el salario mínimo real aumentó 13,5 %, mientras la productividad por hora creció 1,2 % y la productividad por persona ocupada disminuyó 4,6 %. La divergencia justifica ampliar la discusión más allá del porcentaje de ajuste para el próximo año.')
p('El mínimo protege los ingresos de quienes reciben y conservan un empleo cubierto por la regulación. Su diseño también debe considerar a quienes todavía no acceden a ese empleo. Este boletín documenta las trayectorias del salario y la productividad, examina la distribución salarial por edad y propone evaluar un esquema transitorio de mínimo diferenciado para jóvenes, junto con alternativas de apoyo a su contratación.')
picture(OUT/'figura_1.png','Figura 1  Salario mínimo real y productividad laboral agregada','Fuentes: DANE, IPC y anexo de productividad laboral 2025; montos legales del salario mínimo. Cálculos propios. Salario mensual sin auxilio de transporte, deflactado por IPC promedio anual. Productividad 2025 preliminar. [1–3]')
p('La separación de las curvas es un resultado descriptivo. Por sí sola no permite atribuir cambios en el empleo, la informalidad o la inflación a los aumentos del salario mínimo. La evaluación de esos efectos requiere evidencia causal y atención a las diferencias entre empresas, sectores y trabajadores.')

page(); h('Una divergencia que exige ampliar el análisis')
p('Durante 2010–2019, el salario mínimo real y las dos medidas de productividad tuvieron crecimientos acumulados relativamente cercanos. Entre 2021 y 2025, el salario mínimo ganó poder adquisitivo mientras la productividad por hora avanzó poco y la productividad por ocupado retrocedió. Se trata de una divergencia acumulada entre los extremos del periodo; no significa que el salario real haya aumentado todos los años.')
table(['Periodo','Salario mínimo real','Productividad por hora','Productividad por ocupado'],[['2010–2019','14,1 %','15,8 %','14,5 %'],['2021–2025','13,5 %','1,2 %','−4,6 %'],['2010–2025','33,9 %','20,2 %','13,3 %']],[1.4,1.65,1.75,1.85])
p('La productividad por hora relaciona el valor agregado real con las horas trabajadas. La productividad por ocupado lo relaciona con el número de personas empleadas. Ambas son medidas de productividad laboral; difieren porque las horas por trabajador pueden cambiar. Una mejora por hora puede coexistir con estancamiento por ocupado si se trabajan menos horas.')
p('Cuando el costo de contratar aumenta más que la producción por trabajador, las empresas pueden ajustar márgenes, precios, inversión, contratación u horas. La intensidad de cada respuesta depende de la demanda, la competencia, la capacidad de financiarse y la posibilidad de mejorar sus procesos. La comparación agregada no determina cuál de estos ajustes ocurrió ni su magnitud.')
p('También importa qué estamos comparando. El salario mínimo es un piso legal mensual; la productividad describe el conjunto de la economía. El salario mínimo no es la remuneración media y el indicador agregado no mide directamente la productividad de quienes ganan el mínimo. Por tanto, la distancia entre los índices no equivale a una estimación del costo laboral unitario ni a una medida de cuánto debe aumentar el mínimo.')
doc.add_heading('La literatura exige considerar el contexto',2)
p('La revisión de Dube (2019), centrada en Estados Unidos, Reino Unido y otras economías desarrolladas, encuentra que numerosos aumentos del mínimo elevaron los ingresos de trabajadores de bajos salarios con efectos reducidos sobre el empleo. Estos resultados muestran que un aumento puede mejorar las remuneraciones sin generar necesariamente una pérdida importante de puestos de trabajo. Su aplicación a Colombia requiere considerar diferencias de cobertura, cumplimiento e informalidad. [4]')
p('Los estudios reunidos en ESPE 103 examinan específicamente el caso colombiano mediante análisis empíricos y modelos de equilibrio general. Sus autores encuentran riesgos para el empleo formal y efectos sobre informalidad, distribución del ingreso y precios. Los resultados dependen del método, la población y el horizonte estudiado; las simulaciones describen respuestas bajo supuestos y no deben leerse como efectos ya observados. [5]')
p('La divergencia reciente no vuelve imposible el análisis técnico. Hace necesario evaluar conjuntamente la protección del ingreso, la creación de empleo formal y la capacidad de absorción de las empresas. Tampoco permite deducir mecánicamente un porcentaje óptimo para 2027.')

page(); h('Los jóvenes se concentran en remuneraciones bajas')
p('La GEIH de 2025 muestra que los salarios de las personas de 15 a 24 años se concentran más cerca del mínimo y en la parte baja de la distribución que los de las personas de 25 años o más. La diferencia se mantiene al restringir el ejercicio a asalariados que reportan al menos 40 horas habituales por semana. Este filtro reduce la influencia de jornadas cortas, aunque no iguala las horas efectivamente trabajadas ni constituye una definición jurídica de tiempo completo.')
picture(ROOT/'SalarioMinimo_Edad/Outputs/Figures/fig_kernel_salario_edad_2025.png','Figura 2  Distribución del salario mensual según grupo de edad','Fuente: cálculos propios con GEIH 2025. Salario del empleo principal, ponderación con FEX_C18. Curvas de densidad suavizadas sobre el logaritmo del salario. La línea vertical marca el mínimo de 2025: $1.423.500. Los círculos señalan las medianas. [6]')
p('Entre los asalariados con 40 o más horas habituales, el 81,3 % de los jóvenes recibe hasta 1,25 salarios mínimos, frente al 60,2 % de los trabajadores de 25 años o más. En el extremo superior, el 3,8 % de los jóvenes supera dos mínimos, frente al 19,6 % del grupo de mayor edad. Estas diferencias describen posiciones salariales, no productividades individuales.')
table(['Indicador en 2025','15 a 24 años','25 años o más'],[['Salario mensual mediano','$1.423.500','$1.500.000'],['Hasta 1,25 salarios mínimos','81,3 %','60,2 %'],['Más de 2 salarios mínimos','3,8 %','19,6 %']],[3.45,1.6,1.6])
p('La mayor concentración juvenil hace pertinente estudiar cómo el piso salarial incide en la contratación y la permanencia. Pero estas distribuciones solo incluyen a quienes trabajan y reportan un salario positivo: no capturan a quienes no consiguieron empleo. Tampoco permiten atribuir a la edad diferencias que pueden reflejar experiencia, educación, ocupación, sector, horas o formalidad.')
p('Recibir un salario mensual inferior al mínimo no permite identificar automáticamente incumplimiento legal: se requiere conocer jornadas, tiempo remunerado, modalidad de vinculación y calidad del reporte. El análisis debe centrarse en la distribución observada y evitar convertirla en un diagnóstico jurídico de cada relación laboral.')

page(); h('Evaluar un salario mínimo diferenciado por edad')
picture(OUT/'figura_3.png','Figura 3  Concentración salarial entre asalariados con jornadas de 40 horas o más','Fuente: GEIH 2025 y cálculos propios. Porcentajes dentro de cada grupo de edad. Categorías salariales definidas en múltiplos del mínimo mensual de 2025. [6]')
p('Proponemos estudiar un esquema transitorio para jóvenes adultos que ingresan al empleo formal, con una trayectoria explícita hacia el mínimo general. La hipótesis es que una menor exigencia inicial de remuneración podría facilitar algunas contrataciones y abrir oportunidades de aprendizaje. Los datos descriptivos presentados no bastan para confirmar esa hipótesis ni para fijar edades y porcentajes.')
p('Países Bajos cuenta con mínimos juveniles diferenciados por edad. Esa experiencia muestra que el instrumento puede diseñarse, pero no acredita su conveniencia para Colombia. La edad es una aproximación imperfecta a la experiencia y a las necesidades de formación; por eso el diseño debe evaluar también la duración de la vinculación y la trayectoria laboral previa. [7]')
p('El esquema enfrentaría riesgos concretos: reemplazar trabajadores de mayor edad por jóvenes, reducir ingresos de contrataciones que habrían ocurrido de todas formas y promover rotación cuando termina el beneficio. Kabátek documenta incentivos y cambios en las separaciones laborales cerca de los cumpleaños que elevan el mínimo aplicable en Países Bajos. Este resultado exige transiciones graduales y seguimiento de la estabilidad del empleo. [8]')
p('Antes de una implementación, deberían definirse una duración limitada, progresión salarial verificable, formación efectiva y reglas frente a sustitución y recontratación oportunista. La propuesta requiere evaluación jurídica de sus criterios de diferenciación y protección de derechos. El corte de 25 años usado en las figuras es descriptivo: no constituye una recomendación de edad para el esquema.')
p('La evaluación debe comparar este instrumento con subsidios focalizados a la contratación juvenil y apoyos a formación e intermediación. Los subsidios pueden reducir el costo para el empleador manteniendo la remuneración del trabajador, aunque demandan recursos públicos y también pueden financiar contrataciones que habrían ocurrido sin apoyo. La elección debe considerar empleo adicional, ingresos, permanencia y costo por resultado.')
p('Una evaluación gradual, sujeta a viabilidad jurídica, permitiría medir entradas al empleo formal, duración de los contratos, ingresos acumulados y continuidad educativa. El éxito no debería medirse solo por el número inicial de contratos, sino por mejoras sostenidas en la trayectoria laboral de los jóvenes.')

page(); h('Una agenda para la negociación de 2027')
p('La negociación debería contar con un balance plurianual del salario mínimo real, la productividad por hora y por ocupado, y las condiciones de entrada al empleo formal. La actualización anual de ingresos necesita considerar el punto de partida: una misma variación porcentual puede tener implicaciones diferentes según el nivel acumulado del mínimo y la situación del mercado laboral.')
p('Proponemos acompañar la discusión del aumento con un seguimiento público de contratación y permanencia por edad, tamaño de empresa y actividad económica. Ese seguimiento debe incluir salarios por hora, horas trabajadas y transiciones entre formalidad, informalidad y desempleo. También debe comparar periodos equivalentes, para no confundir estacionalidad con efectos de una política.')
p('La agenda requiere criterios de evaluación definidos antes de adoptar cambios. Un esquema juvenil debería mejorar el acceso y la estabilidad sin deteriorar innecesariamente los ingresos de quienes ya consiguen empleo. Las alternativas deben contrastarse con grupos comparables, medir sustitución y distinguir creación neta de puestos de simples cambios en quién los ocupa.')
doc.add_heading('Qué añade el escenario de 2026',2)
p('El salario mínimo mensual de 2026 es $1.750.905, frente a $1.423.500 en 2025. Con una inflación de cierre supuesta de 6,7 %, el aumento real diciembre a diciembre sería aproximadamente 15,3 %, calculado como 1,23 / 1,067 − 1. La inflación utilizada es un supuesto de escenario, no un cierre observado. El monto legal excluye el auxilio de transporte. [3]')
table(['Indicador de escenario','Estimación central','Periodo y naturaleza'],[['Salario mínimo real','+15,3 %','2026 vs. 2025\nIPC de cierre supuesto'],['Productividad por hora','+3,78 %\nP5–P95: 1,97 a 5,59 %','Enero–septiembre 2026\nSimulación propia'],['Productividad por ocupado','+0,06 %\nP5–P95: −0,34 a 0,45 %','Enero–septiembre 2026\nSimulación propia']],[2.2,1.85,2.6])
p('Las simulaciones de productividad combinan insumos observados hasta agosto con supuestos para septiembre y ajustes de medición. Sus intervalos representan la incertidumbre incorporada al ejercicio. No corresponden a cifras oficiales del DANE ni al crecimiento de todo 2026. Por esa diferencia temporal, no se utiliza su comparación con el salario real de cierre para calcular una brecha anual definitiva.')
p('El argumento principal del boletín se sostiene en los datos de 2021–2025. El escenario de 2026 ilustra la importancia de actualizar el diagnóstico, pero no sustituye los resultados anuales ni determina el ajuste de 2027.')
p('La negociación de 2027 ofrece una oportunidad para discutir cómo sostener las mejoras del ingreso y ampliar el acceso al empleo formal. Un salario mínimo diferenciado por edad merece evaluarse junto con otras alternativas, con criterios explícitos de protección del ingreso, formación y estabilidad. El objetivo debe ser que más jóvenes accedan a un empleo formal y puedan progresar dentro de él.')

page(); h('Notas metodológicas y referencias')
doc.add_heading('Medición y alcance',2)
p('Salario real e índices. El análisis histórico utiliza el mínimo mensual legal sin auxilio de transporte, dividido por el promedio de los doce índices mensuales del IPC nacional de cada año. Las series se normalizan en 2010 = 100. Los índices de productividad son reconstrucciones analíticas mediante encadenamiento de las tasas anuales publicadas en los cuadros 1 y 2 del anexo DANE de 2025; no son niveles monetarios oficiales. Los crecimientos entre extremos se obtienen como la razón de los índices menos uno. Se usan las tasas sin redondear antes de calcular acumulados. El escenario salarial de 2026 utiliza IPC de diciembre, por lo que su variación no debe confundirse con la del promedio anual. [1–3]')
p('Muestra por edad. GEIH 2025, asalariados de 15 años o más con salario positivo del empleo principal (P6500), posiciones ocupacionales 1, 2, 3 y 7, y ponderación mensual FEX_C18. El filtro de jornada usa P6800 ≥ 40. La muestra de este subconjunto comprende 21.266 registros de jóvenes y 148.967 del grupo de 25 años o más; corresponde a observaciones de encuesta, no necesariamente personas únicas. Las proporciones se calculan con ponderadores. La categoría alrededor del mínimo en la figura 2 comprende ±3 % y la categoría inferior excluye ese margen. Las densidades usan un kernel gaussiano sobre logaritmos, con ancho de banda de 0,09. [6]')
p('Interpretación. Las comparaciones son descriptivas y agregadas. No estiman efectos causales del salario mínimo, productividad individual, costos laborales unitarios ni un porcentaje óptimo de ajuste. Las cifras de productividad de 2025 son preliminares. Las propuestas juveniles requieren evaluación distributiva, fiscal, jurídica y de impacto antes de definir su implementación.')
doc.add_heading('Referencias y fuentes',2)
refs=[
('[1] DANE (2026). Productividad Total de los Factores 2025pr y anexo de productividad laboral, cuadros 1 y 2. Publicación del 31 de marzo.','https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales/productividad'),
('[2] DANE. Índice de Precios al Consumidor. Índices, serie de empalme 2003–2025, diciembre de 2025.','https://www.dane.gov.co/files/operaciones/IPC/dic2025/anex-IPC-Indices-dic2025.xlsx'),
('[3] Gobierno de Colombia. Decretos anuales del salario mínimo; Decreto 159 de 2026 para el monto de 2026. Serie histórica disponible en Función Pública.','https://www.cancilleria.gov.co/normograma/compilacion/docs/decreto_0159_2026.htm'),
('[4] Dube, A. (2019). Impacts of minimum wages: Review of the international evidence. Informe independiente para el Gobierno del Reino Unido.','https://www.gov.uk/government/publications/impacts-of-minimum-wages-review-of-the-international-evidence'),
('[5] Banco de la República (2022). Efectos macroeconómicos del salario mínimo en Colombia. Ensayos sobre Política Económica, 103. Investigaciones de sus autores.','https://investiga.banrep.gov.co/es/espe103'),
('[6] DANE. Gran Encuesta Integrada de Hogares, microdatos 2025. Cálculos propios de distribución salarial por edad y horas habituales.','https://microdatos.dane.gov.co/index.php/catalog/GEIH'),
('[7] Gobierno de Países Bajos. Minimum wage amounts. Esquema de mínimos por edad. Consulta: 27 de octubre de 2026.','https://www.government.nl/themes/work/minimum-wage/minimum-wage-amounts'),
('[8] Kabátek, J. (2015). Happy Birthday, You’re Fired! The Effects of Age-Dependent Minimum Wage on Youth Employment Flows in the Netherlands. IZA Discussion Paper 9528.','https://www.econstor.eu/bitstream/10419/125037/1/dp9528.pdf')]
for txt,url in refs:
    par=p(txt); par.paragraph_format.space_after=Pt(5); par.paragraph_format.line_spacing=1.0
    for r in par.runs:r.font.size=Pt(8.5)
    rid=par.part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
    link=OxmlElement('w:hyperlink'); link.set(qn('r:id'),rid)
    run=OxmlElement('w:r'); prop=OxmlElement('w:rPr'); size=OxmlElement('w:sz');size.set(qn('w:val'),'17');prop.append(size)
    col=OxmlElement('w:color');col.set(qn('w:val'),'1769AA');prop.append(col);run.append(prop)
    text=OxmlElement('w:t');text.set(qn('xml:space'),'preserve');text.text=' Consultar fuente';run.append(text);link.append(run);par._p.append(link)
for par in doc.paragraphs:
    par.paragraph_format.widow_control=True
for i,shape in enumerate(doc.inline_shapes):
    shape._inline.docPr.set('descr',['Índices de salario real y productividad entre 2010 y 2025','Distribuciones salariales por edad en 2025','Proporciones por edad hasta 1,25 y por encima de dos salarios mínimos'][i])
doc.save(OUT/'Boletin_salario_minimo_2027.docx')
print(OUT/'Boletin_salario_minimo_2027.docx')
