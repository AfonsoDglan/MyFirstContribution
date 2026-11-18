"""Gera _site/ com o mural de participantes para o GitHub Pages."""

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from perfil import ler_perfil  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "_site"


def main():
    pessoas = []
    for arq in sorted((RAIZ / "participantes").glob("*.md")):
        if arq.name.startswith("_"):
            continue
        try:
            campos, frase = ler_perfil(arq.read_text(encoding="utf-8"))
        except ValueError as e:
            print(f"Ignorando {arq.name}: {e}")
            continue
        pessoas.append(
            {
                "nome": campos.get("nome", arq.stem),
                "github": campos.get("github", arq.stem).lstrip("@"),
                "cidade": campos.get("cidade", ""),
                "frase": frase,
            }
        )
    pessoas.sort(key=lambda p: p["nome"].lower())

    SAIDA.mkdir(exist_ok=True)
    shutil.copy(RAIZ / "site" / "index.html", SAIDA / "index.html")
    (SAIDA / "participantes.json").write_text(
        json.dumps(pessoas, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"{len(pessoas)} participantes no mural.")


if __name__ == "__main__":
    main()
