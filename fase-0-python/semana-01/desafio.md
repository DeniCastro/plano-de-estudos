# Desafio da semana 1: Adivinhe o número

**Regras:** sem IA, sem copiar solução. Consulte apenas a documentação oficial.

## Enunciado

Escreva `adivinhe.py`, um jogo de terminal:

1. O programa sorteia um número inteiro entre 1 e 100 (dica: módulo `random`).
2. O jogador tem **7 tentativas**.
3. A cada palpite, o programa diz se o número secreto é **maior** ou **menor**.
4. Se o jogador acertar, o programa mostra em quantas tentativas ele conseguiu.
5. Se as tentativas acabarem, o programa revela o número.

## Casos que o programa precisa tratar

- O jogador digita algo que não é número (por exemplo, "abc"): avise e **não gaste** uma tentativa.
- O jogador digita um número fora do intervalo de 1 a 100: avise e não gaste tentativa.

## Extras (opcionais)

- Ao final, perguntar se quer jogar de novo.
- Guardar o recorde (menos tentativas) em um arquivo.

## Pense depois de terminar

- Qual é o número máximo de tentativas necessárias para acertar sempre, usando a melhor estratégia? (Dica: pense em dividir o intervalo ao meio. Você acabou de descobrir a ideia da busca binária.)
- Que erro seu apareceu durante o desenvolvimento? Registre em `diario/bugs.md`.
