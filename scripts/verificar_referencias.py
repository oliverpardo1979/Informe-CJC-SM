"""Comprueba citas, entradas y enlaces de los dos PDF tras compilar con BibTeX.

Requiere pypdf. No verifica por sí solo los metadatos contra fuentes externas
ni que un trabajo respalde cada afirmación. Esos controles requieren lectura.
"""
import json
import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def field(entry, name):
    """Lee campos entre llaves, incluidas llaves anidadas de BibTeX."""
    match = re.search(r"\b" + name + r"\s*=\s*\{", entry)
    if not match:
        return ""
    start = match.end()
    depth = 1
    for pos in range(start, len(entry)):
        if entry[pos] == "{":
            depth += 1
        elif entry[pos] == "}":
            depth -= 1
            if depth == 0:
                return entry[start:pos].strip()
    raise ValueError("Campo sin cerrar: " + name)


def verify():
    database = (ROOT / "Paper/referencias.bib").read_text(encoding="utf-8")
    entries = {}
    for entry in re.split(r"(?m)(?=^@)", database)[1:]:
        match = re.match(r"@(\w+)\{([^,]+),", entry)
        kind, key = match.groups()
        assert key not in entries, "Clave duplicada: " + key
        entries[key] = (kind.lower(), entry)
    results = []
    labels = {}
    for name in ("main", "nota_tecnica"):
        aux = (ROOT / (name + ".aux")).read_text(encoding="utf-8")
        cited = {key for group in re.findall(r"\\citation\{([^}]+)\}", aux)
                 for key in group.split(",")}
        bbl = (ROOT / (name + ".bbl")).read_text(encoding="utf-8")
        rendered = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", bbl))
        assert cited == rendered, (name, "Citas/entradas", cited ^ rendered)
        assert cited <= entries.keys(), (name, "Claves sin definir", cited - entries.keys())
        years = dict(re.findall(r"\\bibcite\{([^}]+)\}\{\{[^}]+\}\{([^}]+)\}", aux))
        for key in cited:
            kind, entry = entries[key]
            for required in ("author", "year", "title"):
                assert field(entry, required), (name, key, required)
            if kind != "unpublished":
                assert field(entry, "url") or field(entry, "doi"), (name, key, "Sin enlace")
            if key in labels:
                assert labels[key] == years[key], (key, "Año inconsistente entre documentos")
            labels[key] = years[key]
        pdf = PdfReader(ROOT / (name + ".pdf"))
        destinations = pdf.named_destinations
        citation_links = []
        uris = set()
        for page in pdf.pages:
            for ref in page.get("/Annots", []):
                annotation = ref.get_object()
                action = annotation.get("/A", {})
                if action.get("/S") == "/GoTo":
                    target = str(action["/D"])
                    assert target in destinations, (name, "Destino inexistente", target)
                    if target.startswith("cite."):
                        citation_links.append(target[5:])
                if action.get("/S") == "/URI":
                    uris.add(str(action["/URI"]))
                rect = annotation.get("/Rect")
                if rect:
                    assert (float(rect[0]) >= 0 and float(rect[1]) >= 0
                            and float(rect[2]) <= float(page.mediabox.right)
                            and float(rect[3]) <= float(page.mediabox.top)), (name, "Enlace fuera de página")
        assert set(citation_links) == cited, (name, "Citas sin enlace", cited - set(citation_links))
        for key in cited:
            entry = entries[key][1]
            url = field(entry, "url")
            if url:
                assert url in uris, (name, key, "URL ausente en PDF", url)
            doi = field(entry, "doi")
            if doi:
                assert "https://doi.org/" + doi in uris, (name, key, "DOI ausente en PDF")
        assert "cite.chaparro" in destinations
        text = "\n".join(page.extract_text() for page in pdf.pages)
        assert "Patiño et al. (2026" in text, (name, "Llamada autor–año ausente")
        log = (ROOT / (name + ".log")).read_text(encoding="utf-8")
        assert not re.search(r"Citation .* undefined|There were undefined citations|Overfull", log)
        blg = (ROOT / (name + ".blg")).read_text(encoding="utf-8")
        assert "Warning--" not in blg, (name, blg)
        results.append({"documento": name, "paginas": len(pdf.pages),
                        "referencias_citadas": len(cited), "claves": sorted(cited),
                        "enlaces_internos_a_citas": len(citation_links),
                        "urls_externas_distintas": len(uris), "resultado": "PASS"})
    return {"control": "Correspondencia bibliográfica y enlaces del PDF",
            "alcance": "No sustituye la verificación de metadatos ni la lectura de las fuentes.",
            "documentos": results}


if __name__ == "__main__":
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
