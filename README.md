# PetroBahia S.A.

A **PetroBahia S.A.** é uma empresa fictícia do setor de óleo e gás cujo sistema calcula preços de combustíveis, valida clientes e processa pedidos. O código atual contém módulos legados que precisam ser refatorados para melhorar legibilidade, testabilidade e manutenção.

## Objetivos do repositório
- Entender e refatorar código legado mantendo comportamento atual.
- Aplicar PEP8, Clean Code e princípios SOLID (SRP, OCP).
- Extrair responsabilidades e melhorar testes.

## Estrutura do projeto
```
src/
├── main.py
└── legacy/
    ├── clientes.py
    ├── pedido_service.py
    └── preco_calculadora.py
tests/
```

## Como trabalhar aqui
1. Leia o código em src/legacy.
2. Liste problemas e proponha pequenas refatorações.
3. Não altere o comportamento observado nos testes existentes.
4. Documente decisões de design neste README.

---

## DECISÕES DE DESIGN (resumo das alterações propostas)
### Validação de clientes (`legacy/clientes.py`)
- Regex de e‑mail corrigido (raw string) e validação real.
- Exige `cnpj` numérico de 14 dígitos.
- Retorna `False` para entradas inválidas.
- I/O com `with` e caminho robusto para `clientes.txt`.

Por que: reduzir cadastros inválidos, evitar leaks de I/O e dependência do diretório atual.

### Cálculo de preços (`legacy/preco_calculadora.py`)
- Proteção contra `qtd` inválida (None ou negativa) retornando 0.
- Gasolina: desconto percentual (3%) para grandes volumes em vez de desconto fixo negativo.
- Lubrificante: cálculo direto sem loop O(n).
- Arredondamento consistente.

Por que: regras de negócio coerentes e melhor desempenho.

### Processamento de pedido (`legacy/pedido_service.py`)
- Normaliza entradas (`produto` lower, `cupom` upper).
- Tratar `qtd <= 0` como 0.
- Cupons: `MEGA10` = 10%, `NOVO5` = 5%, `LUB2` = 2% apenas para lubrificante.
- Arredondamento: diesel 0 casas, gasolina 2 casas, demais 2 casas.
- Evita KeyError ao acessar cliente.

Por que: robustez e consistência financeira.

### Execução (`src/main.py`)
- Protege execução com `if __name__ == "__main__":`.
- Exemplos ajustados com e‑mail/CNPJ válidos.

---

## Como executar
No terminal (Windows, na raiz do projeto):
```powershell
python -m src.main
```

## Testes
Rodar todos os testes:
```powershell
pytest
```

## Próximos passos sugeridos
- Extrair interfaces para validação e persistência.
- Substituir prints por logging configurável.
- Aumentar cobertura de testes (casos de borda).
- Introduzir tipagem estática (mypy) e docstrings.
