"""Semana 1: exercícios de revisão de Python.

Como usar:
1. Implemente cada função substituindo `raise NotImplementedError`.
2. Rode no terminal:  python exercicios.py
3. A saída mostra quais verificações passaram (OK), falharam (FALHOU)
   ou ainda estão pendentes (PENDENTE).

Regra: tente por 15 a 20 minutos sozinho antes de pedir ajuda à IA.
"""


def par_ou_impar(n):
    """Retorna "par" ou "impar" (sem acento) conforme o inteiro n."""
    raise NotImplementedError


def fizzbuzz(n):
    """Retorna uma lista de strings de 1 até n.

    Múltiplos de 3 viram "Fizz", de 5 viram "Buzz",
    de 3 e 5 viram "FizzBuzz". Os demais viram o próprio número como string.
    """
    raise NotImplementedError


def soma_digitos(n):
    """Retorna a soma dos dígitos de um inteiro não negativo.

    Exemplo: soma_digitos(1234) -> 10
    """
    raise NotImplementedError


def contar_vogais(texto):
    """Conta as vogais a, e, i, o, u (sem acento), ignorando maiúsculas."""
    raise NotImplementedError


def eh_palindromo(texto):
    """Retorna True se o texto é palíndromo, ignorando maiúsculas e espaços.

    Exemplo: eh_palindromo("Socorram me subi no onibus em Marrocos") -> True
    """
    raise NotImplementedError


def tabuada(n, ate=10):
    """Retorna a lista [n*1, n*2, ..., n*ate]."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Verificações automáticas (não precisa alterar abaixo desta linha)
# ---------------------------------------------------------------------------

VERIFICACOES = [
    ("par_ou_impar(4)", lambda: par_ou_impar(4), "par"),
    ("par_ou_impar(7)", lambda: par_ou_impar(7), "impar"),
    ("par_ou_impar(0)", lambda: par_ou_impar(0), "par"),
    ("fizzbuzz(5)", lambda: fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"]),
    ("fizzbuzz(15)[-1]", lambda: fizzbuzz(15)[-1], "FizzBuzz"),
    ("len(fizzbuzz(30))", lambda: len(fizzbuzz(30)), 30),
    ("soma_digitos(1234)", lambda: soma_digitos(1234), 10),
    ("soma_digitos(0)", lambda: soma_digitos(0), 0),
    ("soma_digitos(9)", lambda: soma_digitos(9), 9),
    ("contar_vogais('Python')", lambda: contar_vogais("Python"), 1),
    ("contar_vogais('AEIOU aeiou')", lambda: contar_vogais("AEIOU aeiou"), 10),
    ("contar_vogais('')", lambda: contar_vogais(""), 0),
    (
        "eh_palindromo('Socorram me subi no onibus em Marrocos')",
        lambda: eh_palindromo("Socorram me subi no onibus em Marrocos"),
        True,
    ),
    ("eh_palindromo('Python')", lambda: eh_palindromo("Python"), False),
    ("eh_palindromo('Arara')", lambda: eh_palindromo("Arara"), True),
    ("tabuada(3, 4)", lambda: tabuada(3, 4), [3, 6, 9, 12]),
    ("len(tabuada(7))", lambda: len(tabuada(7)), 10),
    ("tabuada(2)[-1]", lambda: tabuada(2)[-1], 20),
]


def verificar():
    ok = falhou = pendente = 0
    for nome, executar, esperado in VERIFICACOES:
        try:
            obtido = executar()
        except NotImplementedError:
            print(f"PENDENTE  {nome}")
            pendente += 1
            continue
        except Exception as erro:  # noqa: BLE001 (queremos mostrar qualquer erro)
            print(f"FALHOU    {nome}: erro {type(erro).__name__}: {erro}")
            falhou += 1
            continue
        if obtido == esperado:
            print(f"OK        {nome}")
            ok += 1
        else:
            print(f"FALHOU    {nome}: esperado {esperado!r}, obtido {obtido!r}")
            falhou += 1
    print(f"\nResumo: {ok} OK, {falhou} falharam, {pendente} pendentes")
    return falhou == 0 and pendente == 0


if __name__ == "__main__":
    verificar()
