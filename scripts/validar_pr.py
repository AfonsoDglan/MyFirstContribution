"""Robô revisor: confere se o PR segue o CONTRIBUTING e comenta o resultado.

Roda com `pull_request_target`, a partir do código da branch principal.
Nunca executa nada vindo do PR: os arquivos do PR são lidos só como texto.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from perfil import ler_perfil  # noqa: E402

TITULO = re.compile(r"^(docs|feat|fix|chore)(\([\w\-/]+\))?: \S.{3,}$")
MARCA = "<!-- robo-revisor -->"


def validar(titulo, corpo, autor, arquivos, conteudos):
    """arquivos: {caminho: status}; conteudos: {caminho: texto}. Retorna (erros, avisos)."""
    erros, avisos = [], []
    corpo = corpo or ""

    if not TITULO.match(titulo.strip()):
        erros.append(
            f"O título `{titulo}` não segue o padrão. Use `tipo: descrição`, "
            "com tipo `docs`, `feat`, `fix` ou `chore`. Ex.: `docs: adiciona perfil de "
            f"{autor}`."
        )

    if not re.search(r"(closes|fixes|resolves|fecha|resolve|refs)\s+#\d+", corpo, re.I):
        avisos.append("Não encontrei `Closes #NUMERO` na descrição. Ligue o PR à issue!")

    if not re.search(r"-\s*\[x\]\s*li o contributing", corpo, re.I):
        avisos.append("A caixinha **Li o CONTRIBUTING** não está marcada. 👀")

    removidos = [c for c, s in arquivos.items() if s == "removed"]
    for c in removidos:
        erros.append(f"O PR apaga o arquivo `{c}`. Isso foi de propósito?")

    de_perfil = [c for c in arquivos if c.startswith("participantes/")]
    outros = [c for c in arquivos if not c.startswith("participantes/")]

    if de_perfil and outros:
        erros.append(
            "Este PR mistura o seu perfil com outras alterações "
            f"({', '.join(f'`{c}`' for c in outros)}). Regra 3: um PR = um assunto."
        )

    esperado = f"participantes/{autor.lower()}.md"
    for caminho in de_perfil:
        if arquivos[caminho] == "removed":
            continue
        if caminho == "participantes/_modelo.md":
            erros.append("Não altere o `_modelo.md`. Copie ele para um arquivo novo com o seu usuário.")
            continue
        if caminho.lower() != esperado:
            erros.append(
                f"O arquivo `{caminho}` deveria se chamar `{esperado}` "
                "(o seu usuário do GitHub, em minúsculas, terminando em `.md`)."
            )
            continue
        try:
            campos, frase = ler_perfil(conteudos.get(caminho, ""))
        except ValueError as e:
            erros.append(f"Em `{caminho}`: {e}.")
            continue
        if not campos.get("nome") or campos["nome"] == "Seu Nome":
            erros.append(f"Em `{caminho}`: preencha o campo `nome`.")
        if campos.get("github", "").lower().lstrip("@") != autor.lower():
            erros.append(f"Em `{caminho}`: o campo `github` deve ser `{autor}`.")
        if len(frase) < 10 or frase.startswith("Escreva aqui"):
            erros.append(f"Em `{caminho}`: escreva uma frase sobre você depois do bloco `---`.")

    return erros, avisos


def montar_comentario(autor, erros, avisos):
    linhas = [MARCA]
    if erros:
        linhas.append(f"Oi @{autor}! 🤖 Sou o robô revisor. Encontrei algumas coisas para ajustar:\n")
        linhas += [f"- ❌ {e}" for e in erros]
    else:
        linhas.append(f"Oi @{autor}! 🤖 Sou o robô revisor. Está tudo dentro das regras! ✅\n")
        linhas.append("Agora é só aguardar a revisão de uma pessoa mantenedora.")
    if avisos:
        linhas.append("\n**Dicas:**\n")
        linhas += [f"- 💡 {a}" for a in avisos]
    if erros:
        linhas.append(
            "\nPara corrigir: edite na **mesma branch**, faça commit e push. "
            "O PR atualiza sozinho e eu confiro de novo. "
            "(Título e descrição você edita direto aqui no GitHub.)"
        )
    return "\n".join(linhas)


def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout


def main():
    repo = os.environ["REPO"]
    numero = os.environ["PR_NUMBER"]

    pr = json.loads(gh("api", f"repos/{repo}/pulls/{numero}"))
    arquivos_api = json.loads(gh("api", "--paginate", f"repos/{repo}/pulls/{numero}/files"))

    autor = pr["user"]["login"]
    arquivos = {f["filename"]: f["status"] for f in arquivos_api}
    conteudos = {}
    for f in arquivos_api:
        if f["filename"].startswith("participantes/") and f["status"] != "removed":
            conteudos[f["filename"]] = gh(
                "api", f["contents_url"], "-H", "Accept: application/vnd.github.raw"
            )

    erros, avisos = validar(pr["title"], pr.get("body"), autor, arquivos, conteudos)
    comentario = montar_comentario(autor, erros, avisos)

    # Atualiza o comentário anterior do robô em vez de criar vários.
    comentarios = json.loads(gh("api", "--paginate", f"repos/{repo}/issues/{numero}/comments"))
    anterior = next((c for c in comentarios if MARCA in (c.get("body") or "")), None)
    if anterior:
        gh("api", "-X", "PATCH", f"repos/{repo}/issues/comments/{anterior['id']}", "-f", f"body={comentario}")
    else:
        gh("api", f"repos/{repo}/issues/{numero}/comments", "-f", f"body={comentario}")

    print(comentario)
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
