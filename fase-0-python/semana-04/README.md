# Semana 4: Estrutura do Projeto 1

**Duração estimada:** 11 horas  |  **Status:** rascunho

## Objetivo

Ao final da semana você terá o esqueleto do Projeto 1 (CLI de gerenciador de tarefas) em um repositório próprio, com persistência em arquivo JSON, as primeiras funcionalidades e os primeiros testes, além da revisão do primeiro mês.

## Pré-requisitos

- Semanas 1 a 3 concluídas.
- Spec do Projeto 1 escrita em `projetos/projeto-1-spec.md`.

## Plano de horas

| Bloco | Horas | Atividade |
|---|---|---|
| Construção | 5,5 | Esqueleto do projeto, modelo de dados e persistência em JSON |
| Prática sem IA | 2 | Implementar os comandos `adicionar` e `listar` sem IA |
| Estudo dirigido | 2 | Documentação do módulo `argparse` e do módulo `pathlib` |
| Revisão espaçada | 1 | Cartões do Anki + kata do cache simples (D+7 do primeiro kata) |
| Revisão semanal e do mês | 1 | Revisão semanal + checagem mensal (`modelos/modelo-checagem-mensal.md`) |

## Recursos

- **Referência:** documentação oficial do Python: `argparse`, `pathlib`, `json`.
- **Estrutura do projeto:** use o esqueleto em `../../projeto-1-tarefas-cli/` (fora desta pasta, no pacote que você baixou).

## Conceito em poucas linhas

Um projeto pequeno também precisa de **separação de responsabilidades**: uma parte cuida de guardar e ler dados (armazenamento), outra cuida das regras (lógica) e outra cuida de conversar com o usuário (interface de linha de comando). Separar assim facilita testar cada parte sozinha. **Persistência** é gravar o estado fora da memória para que ele sobreviva ao fim do programa; para começar, um arquivo JSON basta.

## Construção

1. Crie um repositório novo no GitHub chamado `projeto-1-tarefas-cli` e copie para ele o esqueleto fornecido.
2. Defina o **modelo de dados** de uma tarefa, por exemplo um dicionário com `id`, `titulo`, `concluida` e `criada_em`.
3. Implemente em `armazenamento.py` as funções de ler e gravar a lista de tarefas em um arquivo JSON, tratando o arquivo inexistente e o JSON corrompido.
4. Implemente em `tarefas.py` (lógica) as funções `adicionar`, `listar`, `concluir` e `remover`, **sem** usar `print` ou `input` dentro delas (isso fica na interface).
5. Escreva os testes de cada função **antes** (TDD) em `tests/`.

## Desafio sem IA

Implemente `adicionar` e `listar` de ponta a ponta, com testes, sem IA. Depois, use a IA apenas para **revisar** o que você escreveu (peça problemas e casos de borda) e registre em `diario/bugs.md` o que ela apontou e o que você aceitou.

## Critério de pronto

- [ ] O repositório do projeto está no GitHub com README inicial e `.gitignore`
- [ ] `adicionar` e `listar` funcionam e têm testes passando
- [ ] A persistência trata arquivo inexistente e JSON inválido sem quebrar
- [ ] Nenhuma função de lógica usa `print` ou `input`
- [ ] A checagem mensal está preenchida e o plano do mês 2 foi ajustado

## Cartões a criar

- Por que separar lógica, armazenamento e interface?
- O que pode dar errado ao ler um arquivo JSON e como tratar?
- Por que não colocar `print` dentro de funções de lógica?
- Qual a diferença entre erro do usuário e erro de programação?

## Reflexão

- Minha spec ajudou ou eu tive que mudar muito? O que faltou nela?
- O que a IA fez bem e o que ela errou neste projeto?
- Se eu recomeçasse hoje, o que eu faria diferente na estrutura?
