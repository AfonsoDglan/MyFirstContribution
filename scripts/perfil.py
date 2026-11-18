"""Leitura dos arquivos de perfil em participantes/."""

import re

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.DOTALL)


def ler_perfil(texto: str):
    """Retorna (campos, frase) ou levanta ValueError com uma mensagem amigável."""
    texto = texto.replace("\r\n", "\n").lstrip("﻿")
    m = FRONT_MATTER.match(texto)
    if not m:
        raise ValueError(
            "o arquivo precisa começar com o bloco entre `---` (veja `participantes/_modelo.md`)"
        )
    campos = {}
    for linha in m.group(1).splitlines():
        if not linha.strip():
            continue
        if ":" not in linha:
            raise ValueError(f"linha inválida no cabeçalho: `{linha.strip()}` (use `campo: valor`)")
        chave, valor = linha.split(":", 1)
        campos[chave.strip().lower()] = valor.strip().strip('"').strip("'")
    frase = m.group(2).strip()
    return campos, frase
