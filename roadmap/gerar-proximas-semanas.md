# Como gerar as próximas semanas

As aulas das semanas futuras são geradas **sob demanda**, de 4 em 4 semanas, para acompanharem o seu ritmo e não envelhecerem (principalmente nas Fases C e D, onde o ecossistema muda rápido).

## Quando gerar

No fim da última semana do bloco atual, depois da revisão semanal.

## Prompt sugerido

Copie, preencha os colchetes e envie ao Claude (no chat ou no Claude Code, dentro deste repositório):

```
Estou seguindo o Roadmap Definitivo (Engenharia de Software com foco em IA),
em 11 horas por semana. Acabei a semana [NN] da fase [X].

Contexto do meu progresso:
- O que concluí: [resumo da revisão semanal]
- O que foi difícil: [lista]
- Horas médias por semana: [número]

Gere as semanas [NN+1] a [NN+4] seguindo o modelo em modelos/modelo-aula.md,
com: plano de horas, recurso principal (com link), conceito em poucas linhas,
exercícios guiados com testes automáticos quando possível, desafio sem IA,
critério de pronto, cartões a criar e reflexão.

Regras:
- Não forneça as soluções dos exercícios.
- Aponte para recursos externos em vez de copiar conteúdo de terceiros.
- Marque o status de cada aula como "rascunho".
```

## Depois de gerar

1. **Verifique** cada aula: links, comandos e fatos contra a documentação oficial.
2. Rode os testes dos exercícios (devem falhar com "pendente" antes de você resolver).
3. Troque o status de `rascunho` para `revisada`.
4. Faça commit.
