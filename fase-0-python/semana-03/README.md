# Semana 3: Exceções, módulos e primeiros testes

**Duração estimada:** 11 horas  |  **Status:** rascunho

## Objetivo

Ao final da semana você saberá tratar e levantar exceções, organizar código em módulos e escrever testes automáticos com pytest, incluindo uma primeira experiência com TDD. Você também terá escrito a especificação de uma página do Projeto 1.

## Pré-requisitos

- Semanas 1 e 2 concluídas.
- Ambiente virtual ativo com `pytest` instalado (`pip install pytest`).

## Plano de horas

| Bloco | Horas | Atividade |
|---|---|---|
| Construção | 5,5 | Parte A (calculadora) e parte B (validação com TDD) |
| Prática sem IA | 2 | Spec do Projeto 1 em uma página (sem IA) |
| Estudo dirigido | 2 | Tutorial oficial (erros e exceções, módulos) e documentação do pytest (primeiros passos) |
| Revisão espaçada | 1 | Cartões do Anki + refazer o kata do cache LRU simples ou do contador de palavras |
| Revisão semanal | 0,5 | Preencher a revisão semanal |

## Recursos

- **Principal:** documentação do pytest, seção "Get started".
- **Referência:** tutorial oficial do Python, capítulos sobre erros e exceções e sobre módulos; CS50P, aulas sobre exceções e testes.

Confirme os links e a disponibilidade antes de começar.

## Conceito em poucas linhas

Uma **exceção** é a forma de um programa dizer "não consigo continuar assim". Você **levanta** (`raise`) quando detecta algo inválido e **trata** (`try`/`except`) quando sabe como se recuperar. Trate o erro **mais específico possível**: um `except` genérico esconde bugs. Um **módulo** é um arquivo `.py` que você importa em outro. Um **teste automático** transforma uma expectativa em código executável; no **TDD**, você escreve o teste antes, o vê falhar (vermelho), faz passar com o mínimo de código (verde) e então melhora o código com segurança (refatorar).

## Exercícios guiados

Siga `exercicios/README.md`:

- **Parte A:** faça os testes prontos da calculadora passarem.
- **Parte B:** escreva os seus testes para `validar_idade` e `parse_preco` e depois implemente.

Regra: 15 a 20 minutos sozinho antes de pedir ajuda à IA. Se usar a IA para sugerir casos de teste, **revise cada um** e descarte os que não fazem sentido.

## Desafio sem IA: especificação do Projeto 1

Escreva, em uma página e sem IA, a especificação do gerenciador de tarefas em `projetos/projeto-1-spec.md` (há um roteiro lá). Isso treina o hábito de **especificar antes de codar**, a habilidade mais valiosa do plano.

## Critério de pronto

- [ ] `python -m pytest -v` passa em `test_calculadora.py`
- [ ] Você escreveu pelo menos 8 testes próprios em `test_validacao.py` e todos passam
- [ ] Cada teste seu falhou antes de você implementar o código correspondente
- [ ] A spec do Projeto 1 está escrita e commitada
- [ ] Você sabe explicar a diferença entre `raise`, `try`/`except` e `finally`

## Cartões a criar

- Por que evitar `except:` sem tipo?
- O que significa o ciclo vermelho, verde, refatorar no TDD?
- O que acontece com um teste que nunca falhou antes de você implementar? (Dica: ele pode estar testando nada.)
- Qual a diferença entre `ValueError` e `TypeError`?

## Reflexão

- Qual teste meu pegou um bug que eu não tinha percebido?
- Que caso de borda eu esqueci e só descobri depois?
- Qual conceito ainda não consigo explicar com as minhas palavras?
