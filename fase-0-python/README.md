# Fase 0: Python sólido e hábitos de engenheiro (meses 1 a 3)

**Objetivo:** sair de "pouco Python" para escrever programas organizados de 200 a 500 linhas, versionados e depurados.

**Carga:** cerca de 120 horas (aprox. 11 semanas de 11 horas, com 1 semana de folga).

## O que você vai dominar

- Python: tipos, coleções, funções, módulos, compreensões, exceções, arquivos e JSON
- Ambientes virtuais, type hints
- Git e GitHub: commits, branches, pull requests
- Terminal Linux/Unix básico
- Leitura de stack traces e uso do depurador
- Orientação a objetos básica (classes e composição)

## Mapa das semanas

| Semana | Foco | Entrega |
|---|---|---|
| [01](semana-01/README.md) | Ambiente e revisão de Python | Ambiente funcionando, 6 exercícios, jogo de adivinhação |
| [02](semana-02/README.md) | Funções, coleções, arquivos e JSON | 6 exercícios, contador de palavras |
| [03](semana-03/README.md) | Exceções, módulos e primeiros testes | Testes com pytest, spec do Projeto 1 |
| [04](semana-04/README.md) | Estrutura do Projeto 1 | Esqueleto do CLI com persistência |
| 05 | Projeto 1: comandos e `argparse` | A gerar sob demanda |
| 06 | Classes e objetos | A gerar sob demanda |
| 07 | Refatorar o Projeto 1 com classes e type hints | A gerar sob demanda |
| 08 | Fluxo Git: branches e pull requests; depurador | A gerar sob demanda |
| 09 | Projeto 1: testes e README | A gerar sob demanda |
| 10 | Depuração prática e stack traces | A gerar sob demanda |
| 11 | Revisão espaçada e katas | A gerar sob demanda |
| 12 | Fechamento: demo, retrospectiva, Fase A | A gerar sob demanda |

Veja [`../roadmap/gerar-proximas-semanas.md`](../roadmap/gerar-proximas-semanas.md) para gerar as semanas seguintes.

## Katas da fase

Implemente do zero e refaça sem consulta aos 7, 30 e 90 dias:

- Contador de palavras
- Parser de CSV (sem usar a biblioteca `csv`)
- Cache simples com dicionário (memoização do Fibonacci)

## Projeto 1

CLI de gerenciador de tarefas, em repositório próprio (`projeto-1-tarefas-cli`). A especificação fica em [`../projetos/projeto-1-spec.md`](../projetos/projeto-1-spec.md).

## Pronto quando

- [ ] O Projeto 1 está no GitHub, roda com um comando documentado e tem testes passando
- [ ] Você consegue explicar cada função do projeto
- [ ] Você escreve e depura um programa de 300 linhas sem seguir um tutorial passo a passo
- [ ] Os cartões da fase estão no Anki com revisão diária
