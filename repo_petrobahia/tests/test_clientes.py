from __future__ import annotations

from pathlib import Path

from legacy.clientes import cadastrar_cliente


def test_cadastrar_cliente_persiste_dados(tmp_path):
    destino = tmp_path / "clientes.txt"
    cliente = {"nome": "Ana", "email": "ana@example.com", "cnpj": "12.345.678/0001-99"}

    resultado = cadastrar_cliente(cliente, output_path=destino)

    assert resultado is True
    conteudo = destino.read_text(encoding="utf-8").strip()
    assert "Ana" in conteudo
    assert "12345678000199" in conteudo


def test_cadastrar_cliente_rejeita_email_invalido(tmp_path):
    destino = tmp_path / "clientes.txt"
    cliente = {"nome": "Ana", "email": "ana@", "cnpj": "12345678000199"}

    resultado = cadastrar_cliente(cliente, output_path=destino)

    assert resultado is False
    assert not destino.exists()
