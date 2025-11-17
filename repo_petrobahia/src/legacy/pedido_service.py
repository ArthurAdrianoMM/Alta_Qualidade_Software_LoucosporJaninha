from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .preco_calculadora import calcular_preco


@dataclass(frozen=True)
class Pedido:
    cliente: str
    produto: str
    quantidade: float
    cupom: str | None = None


CUPONS = {
    "MEGA10": lambda preco, produto: preco * 0.9,
    "NOVO5": lambda preco, produto: preco * 0.95,
    "LUB2": lambda preco, produto: max(0, preco - 2) if produto == "lubrificante" else preco,
}


def _normalizar_produto(valor: Any) -> str:
    return (valor or "").strip().lower() if isinstance(valor, str) else str(valor)


def _normalizar_cupom(valor: Any) -> str | None:
    if valor is None or not isinstance(valor, str):
        return None
    valor = valor.strip().upper()
    return valor or None


def processar_pedido(pedido: Dict[str, Any]) -> float:
    prod = _normalizar_produto(pedido.get("produto"))
    qtd = pedido.get("qtd")
    if qtd is None or qtd <= 0:
        print("qtd zero, retornando 0")
        return 0

    preco = calcular_preco(prod, qtd)
    if preco < 0:
        print("algo deu errado, preco negativo")
        preco = 0

    cupom = _normalizar_cupom(pedido.get("cupom"))
    if cupom and cupom in CUPONS:
        preco = CUPONS[cupom](preco, prod)

    preco = round(preco, 2 if prod != "diesel" else 0)
    print("pedido ok:", pedido.get("cliente", "desconhecido"), prod, qtd, "=>", preco)
    return preco
