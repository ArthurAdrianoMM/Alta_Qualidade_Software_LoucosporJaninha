from __future__ import annotations

import pytest

from legacy.pedido_service import processar_pedido


def test_processar_pedido_aplica_cupom_novo5(monkeypatch):
    pedido = {"cliente": "EcoFrota", "produto": "etanol", "qtd": 100, "cupom": "NOVO5"}

    valor = processar_pedido(pedido)

    # valor base: 3.59 * 100 * 0.97 = 348.23 -> cupom 5% => 330.8185 -> round(2)
    assert valor == pytest.approx(330.82)


def test_processar_pedido_zera_quantidade():
    pedido = {"cliente": "EcoFrota", "produto": "etanol", "qtd": 0}

    assert processar_pedido(pedido) == 0


def test_processar_pedido_cupom_lubrificante():
    pedido = {"cliente": "PetroPark", "produto": "lubrificante", "qtd": 5, "cupom": "LUB2"}

    valor = processar_pedido(pedido)

    assert valor == pytest.approx(123.0)
