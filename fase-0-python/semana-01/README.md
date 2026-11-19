# Semana 1: Ambiente e revisão de Python

**Duração estimada:** 11 horas  |  **Status:** rascunho

## Objetivo

Ao final da semana você terá o ambiente de desenvolvimento funcionando (Python, editor, Git, GitHub, terminal), terá revisado a sintaxe essencial do Python com exercícios automáticos e terá feito o primeiro commit deste repositório.

## Pré-requisitos

- Lógica de programação básica (você já tem).
- Um computador onde você possa instalar programas.

## Plano de horas

| Bloco | Horas | Atividade |
|---|---|---|
| Construção | 5,5 | Configurar o ambiente (2 h) e fazer os exercícios guiados (3,5 h) |
| Prática sem IA | 2 | Desafio "adivinhe o número" |
| Estudo dirigido | 2 | CS50P (aulas iniciais) ou o tutorial oficial do Python, e o básico de terminal |
| Revisão espaçada | 1 | Instalar o Anki e criar os primeiros cartões |
| Revisão semanal | 0,5 | Preencher `modelos/modelo-revisao-semanal.md` |

## Recursos

- **Principal:** CS50P, a introdução a Python de Harvard (gratuita, em inglês). Assista às primeiras aulas (funções, variáveis, condicionais e laços).
- **Referência:** tutorial oficial do Python em docs.python.org (há versão em português do Brasil).
- **Terminal:** MIT Missing Semester, aula sobre a linha de comando (apenas o básico por enquanto).
- **Git:** capítulo inicial do livro Pro Git (git-scm.com/book), que tem versão em português.

Confirme os links e a disponibilidade antes de começar.

## Parte 1: configurar o ambiente (cerca de 2 horas)

1. **Python:** instale a versão estável mais recente do site oficial (python.org). Confirme no terminal:

   ```bash
   python --version      # em alguns sistemas é python3 --version
   ```

2. **Editor:** instale o VS Code (ou outro de sua preferência) e a extensão oficial de Python.

3. **Ambiente virtual** (isola as dependências de cada projeto). Dentro da pasta deste repositório:

   ```bash
   python -m venv .venv

   # Linux ou macOS
   source .venv/bin/activate

   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   ```

   Quando ativo, o terminal mostra `(.venv)`. A pasta `.venv` já está no `.gitignore`.

4. **Git e GitHub:** instale o Git, crie uma conta no GitHub e configure sua identidade:

   ```bash
   git config --global user.name "Seu Nome"
   git config --global user.email "seu-email@exemplo.com"
   ```

5. **Primeiro commit:** crie um repositório no GitHub chamado `plano-de-estudos`, depois:

   ```bash
   git init
   git add .
   git commit -m "semana-01: estrutura inicial do repositório"
   git branch -M main
   git remote add origin <URL do seu repositório>
   git push -u origin main
   ```

6. **Terminal:** pratique estes comandos: `pwd`, `ls` (ou `dir` no Windows), `cd`, `mkdir`, `cat` (ou `type`), `cp`, `mv`. Atenção com `rm`: ele apaga sem lixeira.

## Conceito em poucas linhas

Um programa é uma sequência de instruções que transforma entradas em saídas. Em Python, funções agrupam instruções com um nome, e o ambiente virtual garante que as bibliotecas de um projeto não interfiram nas de outro. O Git registra o histórico de mudanças em "fotografias" (commits), o que permite voltar atrás e colaborar. Reescreva isto com suas palavras no fim da semana.

## Parte 2: exercícios guiados (cerca de 3,5 horas)

Abra `exercicios/exercicios.py` e implemente as seis funções: `par_ou_impar`, `fizzbuzz`, `soma_digitos`, `contar_vogais`, `eh_palindromo` e `tabuada`. Rode `python exercicios.py` a cada função para ver o resultado.

Regra: 15 a 20 minutos sozinho antes de pedir ajuda à IA. Se pedir, peça uma **dica** e não a solução.

## Desafio sem IA

Veja [`desafio.md`](desafio.md): o jogo "adivinhe o número".

## Critério de pronto

- [ ] `python --version` funciona e o ambiente virtual ativa
- [ ] O repositório está no GitHub com pelo menos 3 commits da semana
- [ ] `python exercicios.py` mostra todas as verificações como OK
- [ ] O desafio funciona e foi feito sem IA
- [ ] Você consegue explicar em voz alta o que faz cada função que escreveu
- [ ] O Anki está instalado e você criou os cartões abaixo

## Cartões a criar

Importe `cartoes/fase-0.csv` no Anki e adicione os seus próprios a partir dos erros da semana. Sugestões de perguntas:

- Para que serve um ambiente virtual e o que acontece se você não usar?
- Qual a diferença entre `=` e `==`?
- O que `range(1, 5)` produz?
- Qual a diferença entre `git add` e `git commit`?

## Reflexão

- O que foi mais difícil na configuração do ambiente?
- Qual exercício me fez travar e por quê?
- Qual conceito ainda não consigo explicar com as minhas palavras?
