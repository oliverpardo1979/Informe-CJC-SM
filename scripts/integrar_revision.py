"""Importa los insumos autorizados y genera el cuadro juvenil desde el CSV."""
from pathlib import Path
import csv
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r'C:\Users\jorge\Documents\Trabajo-Profesional\Javeriana\SalarioMinimo_Edad')
DEST = ROOT / 'insumos' / 'SalarioMinimo_Edad'
manifest = []
for source in sorted(SOURCE.rglob('*')):
    if not source.is_file() or 'qa' in source.relative_to(SOURCE).parts:
        continue
    relative = source.relative_to(SOURCE)
    target = DEST / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() != source.read_bytes():
        raise RuntimeError(f'La copia local cambió: {target}')
    shutil.copy2(source, target)
    manifest.append({'archivo': relative.as_posix(), 'bytes': target.stat().st_size,
                     'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
(DEST / 'procedencia.json').write_text(json.dumps({'origen': str(SOURCE),
    'fecha_copia': '2026-11-01', 'archivos': manifest}, ensure_ascii=False, indent=2), encoding='utf-8')
with (DEST / 'Outputs/tables/estadisticas_salario_por_edad.csv').open(encoding='utf-8-sig') as f:
    rows = [r for r in csv.DictReader(f) if r['anio'] == '2025' and r['poblacion'] == 'tiempo completo (>= 40 h)']
assert len(rows) == 2
young = next(r for r in rows if r['grupo'] == 'menores de 25')
older = next(r for r in rows if r['grupo'] == '25 o mas')
def pct(r, key):
    return str(Decimal(r[key]).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
lines = [r'\begin{table}[H]', r'\centering\small',
    r'\caption{Distribución salarial por edad, asalariados con 40 horas habituales o más, 2025}',
    r'\label{tab:edad}', r'\begin{tabular}{lrr}', r'\toprule',
    r'Indicador & 15--24 años & 25 años o más \\', r'\midrule']
for label, key in [('Hasta 1,25 mínimos (\\%)', 'pct_hasta_1,25_minimos'),
                   ('Más de 2 mínimos (\\%)', 'pct_mas_de_2_minimos'),
                   ('Alrededor del mínimo, $\\pm3\\%$ (\\%)', 'pct_en_el_minimo_(±3%)'),
                   ('Menos de 0,97 mínimos (\\%)', 'pct_bajo_el_minimo')]:
    lines.append(f'{label} & {pct(young, key)} & {pct(older, key)} ' + r'\\')
lines += [r'\bottomrule', r'\end{tabular}',
    r'\fuente{Fuente: DANE, GEIH 2025. Cálculos del Centro Javeriano de Competitividad.}',
    r'\end{table}']
(ROOT / 'Paper/sections/CuadroEdad.tex').write_text('\n'.join(lines)+'\n', encoding='utf-8')
print(f'{len(manifest)} insumos copiados; cuadro 2025 generado desde CSV.')
