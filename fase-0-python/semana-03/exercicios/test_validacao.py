"""Testes de validação: ESCREVA-OS VOCÊ (TDD).

Fluxo do TDD (ciclo vermelho, verde, refatorar):
1. Escreva UM teste que descreve um comportamento da especificação.
2. Rode `python -m pytest -v` e veja o teste FALHAR (vermelho).
3. Implemente o mínimo para ele passar (verde).
4. Refatore se necessário, mantendo tudo verde. Repita.

Cubra pelo menos: casos normais, limites (0 e 150), valores inválidos,
strings com espaços e preços com milhar.
"""

import pytest

from validacao import parse_preco, validar_idade


def test_validar_idade_aceita_string_numerica():
    # Exemplo para você começar. Escreva os demais abaixo.
    assert validar_idade("25") == 25


# TODO: teste do limite inferior (0)
# TODO: teste do limite superior (150)
# TODO: idade negativa levanta ValueError("idade fora do intervalo")
# TODO: texto não numérico levanta ValueError("idade inválida")
# TODO: "25.5" levanta ValueError("idade inválida")
# TODO: espaços nas pontas são aceitos
# TODO: parse_preco com "R$ 12,50"
# TODO: parse_preco com milhar ("R$ 1.234,56")
# TODO: parse_preco sem o símbolo
# TODO: parse_preco inválido levanta ValueError("preço inválido")
