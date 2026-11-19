# Projeto 1: CLI de gerenciador de tarefas (especificação)

Escreva a sua versão **sem IA**, em até uma página. Use este roteiro e substitua as perguntas pelas suas respostas.

## Problema

Quem usa isto e por quê? Que dor resolve que uma lista no papel não resolve?

## Funcionalidades essenciais (versão 1)

Responda e liste os comandos que existirão. Sugestão de partida:

- `adicionar "título"`: cria uma tarefa
- `listar`: mostra as tarefas (todas, só pendentes, só concluídas?)
- `concluir ID`: marca como concluída
- `remover ID`: apaga uma tarefa

## Fora do escopo (por enquanto)

O que você **não** vai fazer na versão 1 (por exemplo, prazos, categorias, sincronização)? Escrever isso protege você de aumentar o escopo.

## Entradas e saídas

- Exemplo de uso e saída esperada de cada comando.
- Onde os dados são guardados (arquivo, formato, local)?

## Casos de erro que precisam ser tratados

- ID inexistente
- Título vazio
- Arquivo de dados corrompido ou ausente
- Comando desconhecido

## Decisões de design

| Decisão | Alternativas | Por que escolhi |
|---|---|---|
| Formato de armazenamento | JSON, SQLite, CSV | |
| Como gerar o ID | contador, UUID | |

## Plano de testes

Que comportamentos serão testados? Liste pelo menos 10 em frases curtas ("adicionar com título vazio levanta erro").

## Critério de pronto do projeto

- [ ] Os quatro comandos funcionam e estão documentados no README
- [ ] Cobertura de testes nas regras de negócio acima de 70%
- [ ] README com como instalar, como usar e decisões de design
- [ ] Publicado no GitHub com histórico de commits legível

## Uso de IA (preencha ao final)

- O que a IA gerou, o que eu revisei e quais bugs ela introduziu.
