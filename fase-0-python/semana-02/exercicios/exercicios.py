"""Semana 2: funções, coleções, arquivos e JSON.

Como usar:
1. Implemente cada função substituindo `raise NotImplementedError`.
2. Rode no terminal:  python exercicios.py

Regra: tente por 15 a 20 minutos sozinho antes de pedir ajuda à IA.
"""

import json  # noqa: F401  (você vai precisar dele)


def frequencia_palavras(texto):
    """Retorna um dicionário {palavra: quantidade}.

    - Tudo em minúsculas.
    - Palavras separadas por espaços.
    - Remova estes sinais das pontas de cada palavra: . , ; : ! ?
    - Ignore "palavras" vazias.

    Exemplo: "Oi, oi! Tudo bem?" -> {"oi": 2, "tudo": 1, "bem": 1}
    """
    raise NotImplementedError


def remover_duplicados(lista):
    """Retorna uma nova lista sem repetições, mantendo a ordem da primeira aparição.

    Exemplo: [3, 1, 3, 2, 1] -> [3, 1, 2]
    """
    raise NotImplementedError


def agrupar_por_tamanho(palavras):
    """Retorna {tamanho: [palavras com esse tamanho]}, mantendo a ordem de entrada.

    Exemplo: ["oi", "ola", "ai"] -> {2: ["oi", "ai"], 3: ["ola"]}
    """
    raise NotImplementedError


def media_notas(alunos):
    """Recebe {nome: [notas]} e retorna {nome: média arredondada em 2 casas}.

    Um aluno com lista vazia tem média 0.0.
    Exemplo: {"Ana": [7, 8], "Bia": []} -> {"Ana": 7.5, "Bia": 0.0}
    """
    raise NotImplementedError


def inverter_dicionario(d):
    """Troca chaves por valores. Assuma que os valores são únicos.

    Exemplo: {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    """
    raise NotImplementedError


def salvar_json(caminho, dados):
    """Grava `dados` em `caminho` como JSON legível.

    Requisitos: indentação de 2 espaços, acentos preservados (sem \\u00e9),
    arquivo em UTF-8. Use o gerenciador de contexto `with`.
    """
    raise NotImplementedError


def ler_json(caminho):
    """Lê o arquivo JSON em `caminho` e retorna os dados."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Verificações automáticas (não precisa alterar abaixo desta linha)
# ---------------------------------------------------------------------------

import os
import tempfile


def _teste_json_ida_e_volta():
    dados = {"nome": "José", "itens": [1, 2, 3], "ok": True}
    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, "dados.json")
        salvar_json(caminho, dados)
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
        if "José" not in conteudo:
            return "acentos não preservados"
        if '\n  "nome"' not in conteudo:
            return "indentação de 2 espaços ausente"
        if ler_json(caminho) != dados:
            return "dados lidos diferem dos gravados"
    return "ok"


VERIFICACOES = [
    (
        "frequencia_palavras('Oi, oi! Tudo bem?')",
        lambda: frequencia_palavras("Oi, oi! Tudo bem?"),
        {"oi": 2, "tudo": 1, "bem": 1},
    ),
    ("frequencia_palavras('')", lambda: frequencia_palavras(""), {}),
    (
        "frequencia_palavras('a A a.')",
        lambda: frequencia_palavras("a A a."),
        {"a": 3},
    ),
    (
        "remover_duplicados([3, 1, 3, 2, 1])",
        lambda: remover_duplicados([3, 1, 3, 2, 1]),
        [3, 1, 2],
    ),
    ("remover_duplicados([])", lambda: remover_duplicados([]), []),
    (
        "agrupar_por_tamanho(['oi', 'ola', 'ai'])",
        lambda: agrupar_por_tamanho(["oi", "ola", "ai"]),
        {2: ["oi", "ai"], 3: ["ola"]},
    ),
    (
        "media_notas({'Ana': [7, 8], 'Bia': []})",
        lambda: media_notas({"Ana": [7, 8], "Bia": []}),
        {"Ana": 7.5, "Bia": 0.0},
    ),
    (
        "media_notas({'Caio': [10, 9, 9]})",
        lambda: media_notas({"Caio": [10, 9, 9]}),
        {"Caio": 9.33},
    ),
    (
        "inverter_dicionario({'a': 1, 'b': 2})",
        lambda: inverter_dicionario({"a": 1, "b": 2}),
        {1: "a", 2: "b"},
    ),
    ("salvar_json e ler_json (ida e volta)", _teste_json_ida_e_volta, "ok"),
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
        except Exception as erro:  # noqa: BLE001
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
