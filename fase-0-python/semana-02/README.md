# Semana 2: Funções, coleções, arquivos e JSON

**Duração estimada:** 11 horas  |  **Status:** rascunho

## Objetivo

Ao final da semana você terá domínio das estruturas de dados nativas do Python (listas, dicionários, conjuntos, tuplas), saberá escrever funções claras e saberá ler e gravar arquivos de texto e JSON.

## Pré-requisitos

- Semana 1 concluída (ambiente funcionando, exercícios básicos feitos).

## Plano de horas

| Bloco | Horas | Atividade |
|---|---|---|
| Construção | 5,5 | Exercícios guiados e começo do desafio |
| Prática sem IA | 2 | Terminar o desafio do contador de palavras |
| Estudo dirigido | 2 | CS50P (funções, coleções, arquivos) e documentação do módulo `json` |
| Revisão espaçada | 1 | Cartões do Anki + kata de memoização do Fibonacci |
| Revisão semanal | 0,5 | Preencher a revisão semanal |

## Recursos

- **Principal:** CS50P, partes sobre bibliotecas, arquivos e dicionários.
- **Referência:** tutorial oficial do Python, seções sobre estruturas de dados e sobre leitura e escrita de arquivos; documentação do módulo `json`.

Confirme os links e a disponibilidade antes de começar.

## Conceito em poucas linhas

Cada coleção resolve um problema diferente: **lista** guarda itens em ordem e permite repetição; **tupla** é uma lista imutável; **conjunto** guarda itens únicos e responde rápido "este item está aqui?"; **dicionário** associa chaves a valores com busca rápida pela chave. Escolher a coleção certa muda a clareza e a velocidade do código. Arquivos devem ser abertos com `with`, que garante o fechamento mesmo se acontecer um erro. JSON é o formato de texto que usamos para trocar dados entre programas.

## Exercícios guiados

Implemente as sete funções de `exercicios/exercicios.py` (`frequencia_palavras`, `remover_duplicados`, `agrupar_por_tamanho`, `media_notas`, `inverter_dicionario`, `salvar_json` e `ler_json`).

Regra: 15 a 20 minutos sozinho antes de pedir ajuda. Peça dica, não a solução.

## Desafio sem IA

Veja [`desafio.md`](desafio.md): o contador de palavras de um arquivo.

## Critério de pronto

- [ ] `python exercicios.py` mostra todas as verificações como OK
- [ ] O contador de palavras funciona e trata arquivo inexistente sem stack trace
- [ ] Você sabe explicar quando usar lista, tupla, conjunto e dicionário
- [ ] O kata da memoização do Fibonacci está feito e registrado com a data
- [ ] Pelo menos 10 cartões novos criados (inclua os erros da semana)

## Cartões a criar

- Quando usar um conjunto em vez de uma lista?
- Por que é perigoso usar uma lista como valor padrão de um parâmetro de função?
- O que o `with open(...)` garante?
- Qual a diferença entre `dict[chave]` e `dict.get(chave)` quando a chave não existe?

## Reflexão

- Qual coleção eu usei sem necessidade e que poderia ter sido outra?
- Que erro de arquivo (caminho, codificação) me custou mais tempo?
- Qual conceito ainda não consigo explicar com as minhas palavras?
