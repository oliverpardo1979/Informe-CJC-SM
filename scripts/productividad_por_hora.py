"""Calcula horas efectivas GEIH y productividad de enero a junio de 2021 y 2026.

Uso: python scripts/productividad_por_hora.py DIRECTORIO_DE_ZIP
Requiere pandas. Nombrar 2021-1S.zip el archivo GEIH Marco 2018 (I semestre)
del catálogo DANE 701, y 2026-01.zip a 2026-06.zip los del catálogo 900.
"""

import argparse
from calendar import monthrange
from pathlib import Path
from zipfile import ZipFile

import pandas as pd


DATA = Path(__file__).resolve().parents[1] / "data"
CAMPOS = {"MES", "OCI", "FEX_C18", "P6850", "P7040", "P7045"}


def horas_mes(archivo, miembro, anio):
    with archivo.open(miembro) as entrada:
        cabecera = entrada.readline()
    separador = ";" if cabecera.count(b";") > cabecera.count(b",") else ","
    with archivo.open(miembro) as entrada:
        datos = pd.read_csv(entrada, sep=separador, encoding="latin1",
                            usecols=lambda c: c.upper() in CAMPOS, dtype=str)
    datos.columns = datos.columns.str.upper()
    datos = datos.apply(lambda c: pd.to_numeric(c.str.replace(",", ".", regex=False)))
    mes, = datos.MES.unique()
    mes = int(mes)
    if not datos.OCI.eq(1).all() or not datos.FEX_C18.gt(0).all():
        raise ValueError(f"Universo o pesos inesperados en {anio}-{mes:02}")
    pesos = datos.FEX_C18
    secundario = datos.P7045.where(datos.P7040.eq(1), 0)
    validos = (datos.P6850.between(0, 126) & datos.P7040.isin([1, 2])
               & secundario.between(0, 75))
    horas = datos.P6850 + secundario
    media = (pesos[validos] * horas[validos]).sum() / pesos[validos].sum()
    ocupados = pesos.sum()
    dias = monthrange(anio, mes)[1]
    return dict(anio=anio, mes=mes, dias=dias, ocupados_expandidos=ocupados,
                porcentaje_ponderado_excluido=100 * pesos[~validos].sum() / ocupados,
                horas_efectivas_semana_por_ocupado=media,
                horas_efectivas_mes=media * ocupados * dias / 7)


def calcular(directorio):
    archivos = [(2021, "2021-1S.zip"), *[(2026, f"2026-{m:02}.zip") for m in range(1, 7)]]
    filas = []
    for anio, nombre in archivos:
        with ZipFile(directorio / nombre) as archivo:
            for miembro in archivo.namelist():
                if miembro.lower().endswith("/ocupados.csv"):
                    filas.append(horas_mes(archivo, miembro, anio))
    mensual = pd.DataFrame(filas).sort_values(["anio", "mes"])
    if list(zip(mensual.anio, mensual.mes)) != [(a, m) for a in (2021, 2026) for m in range(1, 7)]:
        raise ValueError("Se requiere exactamente un archivo de ocupados por mes")
    semestral = mensual.groupby("anio").agg(
        horas=("horas_efectivas_mes", "sum"), ocupados=("ocupados_expandidos", "mean"))
    insumos = pd.read_csv(DATA / "brecha_primer_semestre_2021_2026.csv").set_index("anio")
    if (semestral.ocupados - 1000 * insumos.ocupados_promedio_miles).abs().max() > 1:
        raise ValueError("El promedio de ocupados no coincide con el anexo GEIH")
    valor = insumos.valor_agregado_real_miles_millones_cop_ref2015 * 1e9
    niveles = pd.DataFrame({"salario_minimo_real": insumos.smlmv_cop * 100 / insumos.ipc_medio_dic2018_100,
                            "valor_agregado_por_ocupado": valor / semestral.ocupados,
                            "valor_agregado_por_hora": valor / semestral.horas})
    mensual.to_csv(DATA / "horas_primer_semestre_2021_2026.csv", index=False, float_format="%.8f")
    print(niveles.to_string())
    print("Variaciones porcentuales:", ((niveles.loc[2026] / niveles.loc[2021] - 1) * 100).to_dict())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directorio_zip", type=Path)
    calcular(parser.parse_args().directorio_zip)
