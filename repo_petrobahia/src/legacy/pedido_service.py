from legacy.preco_calculadora import calcular_preco

def processar_pedido(p):
    prod = (p.get("produto") or "").strip().lower() if isinstance(p.get("produto"), str) else p.get("produto")
    qtd = p.get("qtd")
    cupom = (p.get("cupom") or "").strip().upper() if isinstance(p.get("cupom"), str) else p.get("cupom")

    if qtd is None or qtd <= 0:
        print("qtd zero, retornando 0")
        return 0

    preco = calcular_preco(prod, qtd)
    if preco < 0:
        print("algo deu errado, preco negativo")
        preco = 0

    if cupom == "MEGA10":
        preco = preco * 0.9
    elif cupom == "NOVO5":
        preco = preco * 0.95
    elif cupom == "LUB2" and prod == "lubrificante":
        preco = max(0, preco - 2)

    if prod == "diesel":
        preco = round(preco, 0)
    elif prod == "gasolina":
        preco = round(preco, 2)
    else:
        preco = round(preco, 2)

    print("pedido ok:", p.get("cliente", "desconhecido"), prod, qtd, "=>", preco)
    return preco
