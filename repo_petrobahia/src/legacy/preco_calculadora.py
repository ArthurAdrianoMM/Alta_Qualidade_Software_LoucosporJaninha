from __future__ import annotations

from typing import Callable, Dict

BASES: Dict[str, float] = {
    "diesel": 3.99,
    "gasolina": 5.19,
    "etanol": 3.59,
    "lubrificante": 25.0,
}


def _desconto_diesel(qtd: float) -> float:
    if qtd > 1000:
        return 0.9
    if qtd > 500:
        return 0.95
    return 1.0


def _desconto_gasolina(qtd: float) -> float:
    return 0.97 if qtd > 200 else 1.0


def _desconto_etanol(qtd: float) -> float:
    return 0.97 if qtd > 80 else 1.0


DESCONTOS: Dict[str, Callable[[float], float]] = {
    "diesel": _desconto_diesel,
    "gasolina": _desconto_gasolina,
    "etanol": _desconto_etanol,
    "lubrificante": lambda qtd: 1.0,
}


def calcular_preco(tipo: str | None, qtd: float | None) -> float:
    """Calcula o valor total com as regras de desconto por produto."""
    if qtd is None or qtd < 0:
        print("quantidade invalida, devolvendo 0")
        return 0

    tipo_normalizado = (tipo or "").strip().lower()
    base = BASES.get(tipo_normalizado)
    if base is None:
        print("tipo desconhecido, devolvendo 0")
        return 0

    desconto = DESCONTOS[tipo_normalizado](qtd)
    preco = base * qtd * desconto
    print(f"calc {tipo_normalizado}", preco)
    return preco
