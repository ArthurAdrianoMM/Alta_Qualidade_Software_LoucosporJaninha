from __future__ import annotations

import re
from pathlib import Path
from typing import Any

REG_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CLIENTES_FILE = PROJECT_ROOT / "clientes.txt"


def _normalizar_cnpj(valor: Any) -> str:
    """Remove caracteres especiais e retorna apenas os dígitos do CNPJ."""
    return str(valor or "").replace(".", "").replace("/", "").replace("-", "").strip()


def _resolver_destino(output_path: str | Path | None) -> Path:
    if output_path is None:
        return DEFAULT_CLIENTES_FILE
    return Path(output_path).expanduser().resolve()


def cadastrar_cliente(dados: dict[str, Any], output_path: str | Path | None = None) -> bool:
    """Valida as informações e registra o cliente no arquivo alvo."""
    campos_obrigatorios = {"email", "nome", "cnpj"}
    if not campos_obrigatorios.issubset(dados):
        print("faltou campo")
        return False

    email = dados.get("email", "")
    if not REG_EMAIL.match(email or ""):
        print("email invalido")
        return False

    cnpj = _normalizar_cnpj(dados.get("cnpj"))
    if not (cnpj.isdigit() and len(cnpj) == 14):
        print("cnpj invalido")
        return False

    destino = _resolver_destino(output_path)
    destino.parent.mkdir(parents=True, exist_ok=True)

    try:
        registro = {"nome": dados["nome"], "email": email, "cnpj": cnpj}
        with destino.open("a", encoding="utf-8") as handler:
            handler.write(f"{registro}\n")
    except OSError as exc:
        print("erro ao escrever clientes.txt:", exc)
        return False

    print("enviando email de boas vindas para", email)
    return True
