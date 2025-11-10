import re
import os
from pathlib import Path

REG_EMAIL = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

def cadastrar_cliente(c):
    if "email" not in c or "nome" not in c or "cnpj" not in c:
        print("faltou campo")
        return False
    email = c.get("email", "")
    if not re.match(REG_EMAIL, email):
        print("email invalido")
        return False
    cnpj = str(c.get("cnpj", "")).replace(".", "").replace("/", "").replace("-", "").strip()
    if not (cnpj.isdigit() and len(cnpj) == 14):
        print("cnpj invalido")
        return False
    # Resolve arquivo de clientes de forma robusta (no raiz do projeto)
    project_root = Path(__file__).resolve().parents[2]
    out_path = project_root / "clientes.txt"
    try:
        with open(out_path, "a", encoding="utf-8") as f:
            f.write(str({"nome": c["nome"], "email": email, "cnpj": cnpj}) + "\n")
    except Exception as e:
        print("erro ao escrever clientes.txt:", e)
        return False
    print("enviando email de boas vindas para", email)
    return True
