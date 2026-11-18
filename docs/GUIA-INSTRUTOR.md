# 🎓 Guia da pessoa instrutora

Como preparar e conduzir a prática com este repositório.

## Antes do evento (uns 30 min)

### 1. Suba o repositório

```bash
cd primeira-contribuicao
git init && git add . && git commit -m "chore: estrutura inicial"
gh repo create primeira-contribuicao --public --source . --push
```

### 2. Troque os textos provisórios

Procure e substitua:

- `SEU-USUARIO` e `DONO-ORIGINAL` → seu usuário do GitHub (em `CONTRIBUTING.md` e `.github/ISSUE_TEMPLATE/config.yml`)
- `SEU NOME` → no `LICENSE`
- `@instrutor` → seu usuário, em `linguagens.md`

```bash
grep -rn "SEU-USUARIO\|DONO-ORIGINAL\|SEU NOME\|@instrutor" .
```

### 3. Ative o mural (GitHub Pages)

**Settings → Pages → Source: GitHub Actions.** Depois rode o workflow **Publicar mural** em **Actions → Publicar mural → Run workflow**. O site fica em `https://SEU-USUARIO.github.io/primeira-contribuicao/`.

### 4. Crie as labels e issues

```bash
gh auth login
./scripts/criar_issues.sh SEU-USUARIO/primeira-contribuicao
```

Depois **fixe (pin) a issue #1**.

### 5. Proteja a main (recomendado)

**Settings → Rules → Rulesets → New branch ruleset**, alvo `main`:
- ✅ Require a pull request before merging
- ✅ Require status checks to pass → adicione `validar` (aparece depois do primeiro PR)

Como dona(o) do repositório, você continua podendo fazer merge.

### 6. Teste você mesmo

Com uma segunda conta (ou peça a alguém), faça um PR de perfil **com erros de propósito** e veja o robô comentar. Depois corrija e veja o comentário atualizar.

### 7. Mensagem para a turma (enviar uns dias antes)

> Oi! Para aproveitarmos melhor o minicurso, antes do dia:
> 1. Crie uma conta em github.com (escolha um usuário profissional, ex.: nome-sobrenome)
> 2. Instale o Git: git-scm.com/downloads
> 3. Opcional: instale o GitHub CLI (cli.github.com) e rode `gh auth login`
> Se travar, sem problema, resolvemos no dia!

## Durante a prática

### Roteiro sugerido (60 min)

| Tempo | O que fazer |
|---|---|
| 0–10 | Tour ao vivo pelo repositório: README → CONTRIBUTING → Issues → filtro `good first issue` |
| 10–15 | Você faz o fluxo inteiro projetado na tela, com o seu próprio perfil |
| 15–45 | Turma faz o perfil. Você revisa e faz merge dos PRs aprovados pelo robô |
| 45–60 | Quem terminou pega issues do glossário, nível 2 ou nível 3 |

### Dicas de revisão ao vivo

- **Peça uma alteração em alguns PRs**, mesmo que estejam certos ("Que tal contar o que você está estudando?"). Isso simula o code review real e ensina a atualizar o PR.
- Use **Request changes** e depois **Approve**, para mostrar os estados de revisão.
- Projete o **mural** na tela e atualize a cada merge. A reação da turma vale a pena.
- Faça merge dos PRs do `linguagens.md` **um de cada vez**: a partir do segundo, todos ficam com conflito. Resolva um junto com a turma.

### Problemas mais comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| `Permission denied` / `403` no push | Clonou o repositório original, não o fork | `git remote set-url origin https://github.com/USUARIO/primeira-contribuicao.git` |
| Pede senha e não aceita | GitHub não aceita senha no terminal | `gh auth login` ou criar um Personal Access Token |
| `Author identity unknown` | Faltou `git config` | Rodar os dois `git config --global` da colinha |
| Commit foi feito na main | Esqueceu de criar a branch | `git switch -c perfil/usuario` e dar push dessa branch |
| Robô não comentou | Workflow só roda depois que existe na main | Confira em Actions se o workflow está habilitado |
| Mural não atualizou | Workflow de Pages ainda rodando | Espere ~1 min e recarregue com Ctrl+F5 |

## Depois do evento

- Para reutilizar com outra turma, mantenha os perfis antigos: o mural cresce a cada turma e mostra que o projeto está vivo. Só recrie as issues do glossário (reverta as correções em `docs/glossario.md` e rode de novo a parte de issues do script).
- Incentive a turma a escolher um **projeto real** em até uma semana, enquanto a motivação está alta.

## Sobre a segurança do robô

O workflow usa `pull_request_target` para conseguir comentar em PRs de forks. Esse gatilho roda com permissões do repositório, por isso o script **nunca faz checkout nem executa código do PR**: ele lê os arquivos do PR como texto pela API. Se você alterar o workflow, mantenha essa regra.
