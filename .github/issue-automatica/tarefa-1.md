Olá, @{{USUARIO}}! 👋 Que bom ter você aqui.

Você acabou de fazer o **fork** deste repositório. Esse é o primeiro passo de qualquer contribuição open source! Esta issue é a sua **Tarefa 1**.

## 🎯 Objetivo

Adicionar o seu perfil na pasta `participantes/`. Quando o seu Pull Request for aceito, você aparece no mural da turma.

## 🛠️ Passo a passo

1. Leia o [CONTRIBUTING.md](../blob/main/CONTRIBUTING.md) **até o fim** (tem uma regra secreta 👀).
2. Clone o **seu** fork:
   ```bash
   git clone https://github.com/{{USUARIO}}/MyFirstContribution.git
   cd MyFirstContribution
   ```
3. Crie uma branch:
   ```bash
   git switch -c perfil/{{USUARIO}}
   ```
4. Copie `participantes/_modelo.md` para `participantes/{{USUARIO}}.md` e preencha com os seus dados.
5. Faça o commit e o push:
   ```bash
   git add participantes/{{USUARIO}}.md
   git commit -m "docs: adiciona perfil de {{USUARIO}}"
   git push origin perfil/{{USUARIO}}
   ```
6. No GitHub, clique em **Compare & pull request** e preencha o modelo. Não esqueça do `Closes #` com o número desta issue (ele aparece no comentário abaixo).

## 🤖 E depois?

- Um robô vai revisar o seu PR e comentar se algo estiver fora do padrão.
- Quem mantém o projeto pode pedir ajustes: é normal, faz parte!
- Terminou? Procure as issues com a label `good first issue` para os próximos desafios.

Travou? Comente aqui nesta issue explicando o que aconteceu. 💬
