# PetroBahia S.A.

A **PetroBahia S.A.** é uma empresa fictícia do setor de óleo e gás. Seu sistema interno calcula preços de combustíveis, valida clientes e gera relatórios. 
O código está **mal estruturado** e **difícil de manter**. O objetivo é **refatorar** aplicando **PEP8**, **Clean Code** e **princípios SOLID** (SRP e OCP).

## Objetivos
- Melhorar legibilidade e clareza do código
- Extrair funções e classes coesas
- Eliminar duplicações e efeitos colaterais
- Melhorar nomes e modularidade

## Estrutura
```
src/
├── main.py
└── legacy/
    ├── clientes.py
    ├── pedido_service.py
    └── preco_calculadora.py
```

## Instruções
1. Leia o código legado.
2. Liste os problemas encontrados.
3. Refatore sem mudar o comportamento principal.
4. Documente suas **decisões de design** neste README.

---

## DECISÕES DE DESIGN
Abaixo, as falhas corrigidas e o que foi feito em cada uma, de forma concisa.

### Validação de clientes (`legacy/clientes.py`)
- Corrigido regex de e-mail usando raw string e validação real.
- Passou a exigir `cnpj`; valida 14 dígitos (apenas numéricos).
- Deixa de aceitar e-mail/CNPJ inválidos: retorna `False` em vez de seguir adiante.
- Escrita em arquivo com `with` (context manager) e caminho robusto para `clientes.txt` no raiz do projeto.

Por quê: evitar cadastro incorreto, reduzir riscos de I/O (leaks) e dependência do diretório de execução.

### Cálculo de preços (`legacy/preco_calculadora.py`)
- Proteção contra `qtd` inválida (None ou negativa) devolvendo 0.
- Gasolina: troca desconto fixo de `-100` por desconto percentual de 3% quando `qtd > 200` (evita preço negativo e torna proporcional).
- Lubrificante: elimina loop O(n); usa multiplicação direta.
- Mantidos prints mínimos para rastreio, sem alterar fluxo principal.

Por quê: corrigir regra de negócio incoerente, melhorar desempenho e robustez.

### Processamento de pedido (`legacy/pedido_service.py`)
- Normaliza `produto` (lower) e `cupom` (upper), trata `qtd<=0` como 0.
- Descontos reorganizados e consistentes: `MEGA10` (10%), `NOVO5` (5%), `LUB2` (-2 apenas para lubrificante, com piso 0).
- Arredondamento consistente: diesel inteiro (0 casas), gasolina 2 casas, demais 2 casas (remove truncamento silencioso).
- Evita `KeyError` ao imprimir cliente (`p.get("cliente", "desconhecido")`).

Por quê: robustez contra entradas faltantes/variantes, consistência financeira e legibilidade.

### Execução e dados de exemplo (`src/main.py`)
- Adicionado guarda `if __name__ == "__main__":` para evitar efeitos colaterais em import.
- Ajustados e-mails e CNPJs de exemplo para valores válidos.

Por quê: boas práticas de execução e exemplos que não mascaram erros de validação.

---

## Como rodar

```bash
python -m src.main
```
