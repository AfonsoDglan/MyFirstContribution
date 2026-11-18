#!/usr/bin/env bash
# Cria as labels e as issues iniciais do repositório de prática.
# Uso: gh auth login  &&  ./scripts/criar_issues.sh SEU-USUARIO/primeira-contribuicao
set -euo pipefail

REPO="${1:?Informe o repositório, ex.: ./scripts/criar_issues.sh AfonsoDglan/MyFirstContribution}"

label() { gh label create "$1" --repo "$REPO" --color "$2" --description "$3" --force; }

label "good first issue" "7057ff" "Boa para a primeira contribuição"
label "nível 2"          "fbca04" "Desafio extra: envolve conflito de merge"
label "nível 3"          "d93f0b" "Desafio extra: mexe em código (HTML/CSS/JS)"
label "documentação"     "0075ca" "Melhorias na documentação"
label "tarefa-1"         "0E8A16" "Primeira tarefa: perfil em participantes/"
label "ajuda"            "e99695" "Alguém travou e precisa de uma mão"
label "sugestão"         "a2eeef" "Ideia de melhoria"

issue() { gh issue create --repo "$REPO" --title "$1" --label "$2" --body "$3"; }

# A Tarefa 1 (perfil) é criada automaticamente para cada pessoa que faz fork:
# veja .github/workflows/boas-vindas-fork.yml

for par in "Repositorio|Repositório" "Comit|Commit" "Brench|Branch" "Pul Request|Pull Request"; do
  errado="${par%%|*}"; certo="${par##*|}"
  issue "fix: corrige \"$errado\" no glossário" "good first issue,documentação" \
"No arquivo \`docs/glossario.md\`, o termo **$errado** está escrito errado. O correto é **$certo**.

Comente aqui pedindo para pegar a issue antes de começar 🙋"
done

issue "fix: corrige acento em \"copia\" na definição de Fork" "good first issue,documentação" \
"Em \`docs/glossario.md\`, na definição de **Fork**, a palavra \`copia\` deveria ser \`cópia\`.

Comente aqui pedindo para pegar a issue antes de começar 🙋"

for termo in "Upstream" "Conflito" "Review" "Label"; do
  issue "docs: adiciona o termo \"$termo\" ao glossário" "good first issue,documentação" \
"O glossário (\`docs/glossario.md\`) ainda não explica o que é **$termo**.

Adicione o termo seguindo o mesmo formato dos outros (nome em negrito e definição curta na linha de baixo). Escreva com as suas palavras!

Comente aqui pedindo para pegar a issue antes de começar 🙋"
done

issue "🔥 Desafio nível 2: adicione sua linguagem favorita" "nível 2" \
"Adicione uma linha **no final** de \`linguagens.md\` no formato:

\`- **Linguagem**: motivo (@seu-usuario)\`

Como várias pessoas vão editar a mesma linha, é bem provável que seu PR fique com **conflito**. Isso é o objetivo! 😈

Dica: veja a seção *Resolver conflito* na [COLINHA.md](../blob/main/COLINHA.md).

Não precisa pedir esta issue: ela é coletiva. Use \`Refs #NUMERO\` em vez de \`Closes\`."

issue "🌙 Desafio nível 3: adiciona modo claro/escuro no mural" "nível 3,sugestão" \
"O mural (\`site/index.html\`) só tem tema escuro. Adicione um botão para alternar entre claro e escuro.

Dica: as cores estão em variáveis CSS no \`:root\`.

Comente aqui pedindo para pegar a issue antes de começar 🙋"

issue "🔀 Desafio nível 3: botão para embaralhar a ordem do mural" "nível 3,sugestão" \
"Hoje o mural mostra as pessoas em ordem alfabética. Adicione um botão \"Embaralhar\" em \`site/index.html\`.

Comente aqui pedindo para pegar a issue antes de começar 🙋"

echo "✅ Pronto!"
