"""Módulo de validação (semana 3).

Aqui você pratica TDD: ESCREVA OS TESTES PRIMEIRO em test_validacao.py,
veja-os falhar, e só então implemente as funções.
"""


def validar_idade(valor):
    """Converte `valor` (str ou int) em idade inteira válida.

    Regras:
    - Aceita inteiros e strings numéricas (inclusive com espaços nas pontas, como " 25 ").
    - A idade válida vai de 0 a 150, inclusive.
    - Se não for um número inteiro, levante ValueError("idade inválida").
    - Se estiver fora do intervalo, levante ValueError("idade fora do intervalo").
    - Valores decimais como "25.5" são inválidos.
    """
    raise NotImplementedError


def parse_preco(texto):
    """Converte um preço em formato brasileiro para float.

    Exemplos:
    - "R$ 12,50"     -> 12.5
    - "R$ 1.234,56"  -> 1234.56
    - "7,00"         -> 7.0
    - " R$3 "        -> 3.0

    Regras:
    - O ponto é separador de milhar e a vírgula é o separador decimal.
    - O símbolo "R$" e os espaços são opcionais.
    - Se o texto não puder ser convertido, levante ValueError("preço inválido").
    - Preço negativo é inválido.
    """
    raise NotImplementedError
