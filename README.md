# Sistema de Desconto Progressivo — Loja Online

Programa em Python que calcula o desconto aplicável a uma compra com base no valor total informado pelo usuário, seguindo uma tabela de descontos progressivos.

## 📋 Descrição

O sistema solicita o valor total da compra e aplica automaticamente o percentual de desconto correspondente, exibindo o valor do desconto e o valor final a ser pago.

### Regras de desconto

| Valor da compra              | Desconto |
|-------------------------------|----------|
| Menor que R$ 200,00            | 5%       |
| De R$ 200,00 até R$ 299,99     | 10%      |
| A partir de R$ 300,00          | 15%      |

## 🎯 Objetivo

Este projeto foi desenvolvido como atividade da disciplina **Desenvolvimento de Sistemas I**, com o objetivo de praticar o uso de **estruturas condicionais encadeadas** (`if` / `elif` / `else`) em Python.

## 🛠️ Tecnologias

- Python 3

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado. Verifique com:
   ```bash
   python3 --version
   ```
2. Clone este repositório ou baixe o arquivo `desconto.py`.
3. Execute o programa pelo terminal:
   ```bash
   python3 desconto.py
   ```
4. Digite o valor total da compra quando solicitado.

## 💻 Exemplo de uso

```
Digite o valor total da compra: R$ 350

--- Compra ---
Valor da compra: R$ 350.0
Desconto: 15 %
Valor do desconto: R$ 52.5
Valor total a pagar: R$ 297.5
```

## 🧠 Estrutura do código

O programa segue o modelo **Entrada → Processamento → Saída**:

1. **Entrada**: solicita o valor da compra e converte para número decimal (`float`).
2. **Processamento**: 
   - Uma estrutura condicional encadeada (`if` / `elif` / `else`) define o percentual de desconto conforme a faixa de valor.
   - O valor do desconto e o valor final são calculados com base nesse percentual.
3. **Saída**: exibe um resumo da compra com valor original, desconto aplicado, valor do desconto e valor final a pagar.

## 📁 Estrutura de arquivos

```
.
├── desconto.py
└── README.md
```

## ✍️ Autor

Nicoly
