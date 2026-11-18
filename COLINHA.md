# 📝 Colinha de Git

## Configuração (uma vez só)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
git config --global init.defaultBranch main
```

## Dia a dia

| Comando | O que faz |
|---|---|
| `git clone URL` | Baixa um repositório |
| `git status` | Mostra o que mudou (use sempre!) |
| `git switch -c nome-da-branch` | Cria uma branch e entra nela |
| `git switch main` | Volta para a main |
| `git branch` | Lista as branches |
| `git add arquivo` | Prepara um arquivo para o commit |
| `git add .` | Prepara tudo |
| `git commit -m "tipo: mensagem"` | Salva um ponto no histórico |
| `git push origin nome-da-branch` | Envia a branch para o GitHub |
| `git pull` | Traz alterações do GitHub |
| `git log --oneline` | Mostra o histórico resumido |
| `git diff` | Mostra exatamente o que mudou |

## Fluxo de contribuição

```
Fork → clone → branch → alteração → add → commit → push → Pull Request → revisão → merge 🎉
```

## Atualizar o fork

```bash
git remote add upstream URL-DO-ORIGINAL   # só na primeira vez
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

## Resolver conflito

1. `git merge upstream/main` (ou `git pull`) avisa: **CONFLICT**
2. Abra o arquivo e procure por:
   ```
   <<<<<<< HEAD
   sua versão
   =======
   versão que chegou
   >>>>>>> upstream/main
   ```
3. Deixe o arquivo do jeito certo e apague as marcações
4. `git add arquivo` → `git commit` → `git push`

## Socorro!

| Situação | Comando |
|---|---|
| Errei a mensagem do último commit (ainda sem push) | `git commit --amend -m "nova mensagem"` |
| Quero descartar alterações de um arquivo | `git restore arquivo` |
| Adicionei com `add` sem querer | `git restore --staged arquivo` |
| Fiz alterações na main em vez de numa branch (sem commit) | `git switch -c nova-branch` (as alterações vão junto) |
