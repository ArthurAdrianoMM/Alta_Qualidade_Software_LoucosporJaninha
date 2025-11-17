from __future__ import annotations

import pytest

from legacy.preco_calculadora import calcular_preco


@pytest.mark.parametrize(
    ("produto", "quantidade", "esperado"),
    [
        ("diesel", 1200, 3.99 * 1200 * 0.9),
        ("diesel", 600, 3.99 * 600 * 0.95),
        ("gasolina", 250, 5.19 * 250 * 0.97),
        ("etanol", 50, 3.59 * 50),
        ("lubrificante", 10, 25.0 * 10),
    ],
)
def test_calcular_preco_aplica_descontos(produto, quantidade, esperado):
    assert calcular_preco(produto, quantidade) == pytest.approx(esperado)


def test_calcular_preco_com_tipo_invalido():
    assert calcular_preco("kero", 10) == 0


def test_calcular_preco_com_quantidade_invalida():
    assert calcular_preco("diesel", -1) == 0
