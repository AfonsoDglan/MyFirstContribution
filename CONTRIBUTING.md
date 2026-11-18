# 🤝 Como contribuir

Que bom ter você aqui! Este guia é curto, mas **cada regra existe por um motivo**. Em projetos reais, PRs que ignoram o CONTRIBUTING costumam ser fechados sem revisão.

## 📋 As regras

1. **Peça a issue antes de começar.** Comente na issue algo como: *"Olá! Posso trabalhar nesta issue?"* e espere alguém te atribuir. Isso evita duas pessoas fazendo a mesma coisa.
   - Exceção: a issue **"Adicione seu perfil"** é para todo mundo, não precisa pedir.
2. **Nunca trabalhe na `main`.** Crie uma branch com nome descritivo:
   `perfil/seu-usuario`, `docs/corrige-glossario-commit`, `feat/adiciona-termo-rebase`.
3. **Um PR = um assunto.** Não misture seu perfil com correção do glossário.
4. **Mensagem de commit e título do PR seguem o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/):**

   ```
   tipo: descrição curta no imperativo
   ```

   Tipos aceitos aqui: `docs`, `feat`, `fix`, `chore`.
   ✅ `docs: adiciona perfil de mariasilva`
   ✅ `fix: corrige grafia de "commit" no glossário`
   ❌ `atualização`
   ❌ `Update README.md`

5. **Referencie a issue no PR** escrevendo `Closes #NUMERO` na descrição. Assim a issue fecha sozinha quando o PR é aceito.
6. **Seja gentil.** Leia o [Código de Conduta](CODE_OF_CONDUCT.md).

> 🕵️ Regra secreta para provar que você leu até aqui: na descrição do seu PR, marque a caixinha **"Li o CONTRIBUTING"** e escreva qual é o seu emoji favorito. 😉

## 🛠️ Passo a passo

### 1. Faça o fork

Clique em **Fork** no canto superior direito. Agora você tem uma cópia do projeto na sua conta.

### 2. Clone o **seu** fork

```bash
git clone https://github.com/SEU-USUARIO/primeira-contribuicao.git
cd primeira-contribuicao
```

### 3. Crie uma branch

```bash
git switch -c perfil/seu-usuario
```

### 4. Faça a sua alteração

**Para adicionar seu perfil:** copie `participantes/_modelo.md` para `participantes/SEU-USUARIO.md` (o nome do arquivo **tem que ser** o seu usuário do GitHub) e preencha:

```markdown
---
nome: Maria Silva
github: mariasilva
cidade: Palmas - TO
---

Estou aprendendo Python e quero contribuir com projetos de educação.
```

### 5. Commit e push

```bash
git add participantes/seu-usuario.md
git commit -m "docs: adiciona perfil de seu-usuario"
git push origin perfil/seu-usuario
```

### 6. Abra o Pull Request

No GitHub, vai aparecer um botão **"Compare & pull request"**. Preencha o modelo de PR com calma.

### 7. Acompanhe a revisão

- Um robô 🤖 vai checar seu PR e comentar se algo estiver fora do padrão.
- Quem mantém o projeto pode pedir alterações. Isso é **normal**, não é bronca!
- Para ajustar, edite na mesma branch, faça commit e push de novo. O PR atualiza sozinho.

## 🔄 Mantendo seu fork atualizado (desafio extra)

```bash
git remote add upstream https://github.com/DONO-ORIGINAL/primeira-contribuicao.git
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

## 💬 Como conversar com mantenedores

- Seja específico: diga o que você entendeu e o que pretende fazer.
- Recebeu um pedido de mudança? Agradeça, ajuste e avise: *"Ajustado, obrigado pela revisão!"*
- Ficou sem resposta? Espere uns dias e comente educadamente. Mantenedores são, muitas vezes, voluntários.
