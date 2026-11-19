# Desafio da semana 2: Contador de palavras de um arquivo

**Regras:** sem IA, sem copiar solução. Consulte apenas a documentação oficial.

## Enunciado

Escreva `contador.py`, que recebe o caminho de um arquivo de texto pela linha de comando e mostra as **10 palavras mais frequentes**:

```bash
python contador.py meu_texto.txt
```

Saída esperada (exemplo):

```
 1. de        42
 2. que       31
 3. o         29
 ...
```

## Requisitos

- Use `sys.argv` para ler o caminho do arquivo.
- Tudo em minúsculas, sem pontuação nas pontas das palavras.
- Em caso de empate, ordene alfabeticamente.
- Se o arquivo não existir, mostre uma mensagem amigável (sem stack trace) e saia com código de erro 1.
- Salve também o resultado completo em `resultado.json` (palavra para quantidade).

## Textos para testar

Use um texto em domínio público (por exemplo, uma obra clássica em português) ou um texto seu.

## Extras (opcionais)

- Ignorar uma lista de palavras comuns ("de", "a", "o", "que"), lida de um arquivo.
- Aceitar a opção `--top N` para escolher quantas palavras mostrar.

## Kata da semana

Implemente a **memoização do Fibonacci** com um dicionário (sem `functools`). Refaça sem consulta aos 7, 30 e 90 dias.
