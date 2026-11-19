# Exercícios da semana 3

Instale o pytest no ambiente virtual ativo:

```bash
pip install pytest
```

## Parte A: calculadora (testes prontos)

1. Rode `python -m pytest -v` e veja os testes de `test_calculadora.py` **falharem**.
2. Implemente as funções de `calculadora.py` até todos passarem.

## Parte B: validação (TDD)

1. Leia a especificação nas docstrings de `validacao.py`.
2. Escreva os testes em `test_validacao.py` **antes** de implementar.
3. Implemente `validar_idade` e `parse_preco` fazendo um teste de cada vez passar.

Dica: rode apenas um arquivo com `python -m pytest test_validacao.py -v`.
