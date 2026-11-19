"""Testes da calculadora. Estes testes já estão prontos: faça-os passar.

Rode com:  python -m pytest -v
"""

import pytest

from calculadora import dividir, media, multiplica, soma, subtrai


def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0


def test_subtrai():
    assert subtrai(5, 3) == 2
    assert subtrai(3, 5) == -2


def test_multiplica():
    assert multiplica(4, 3) == 12
    assert multiplica(7, 0) == 0


def test_dividir():
    assert dividir(10, 4) == 2.5


def test_dividir_por_zero_levanta_erro():
    with pytest.raises(ValueError, match="divisão por zero"):
        dividir(1, 0)


def test_media():
    assert media([2, 4, 6]) == 4
    assert media([5]) == 5


def test_media_lista_vazia_levanta_erro():
    with pytest.raises(ValueError, match="lista vazia"):
        media([])
