# Desconto Progressivo para Loja 
# Estrutura condicional encadeada (if / elif / else)

# Entrada de dados: solicita o valor da compra e converte para float
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica cada faixa de valor em sequência (igual ao exemplo da nota do material)
if valor_compra < 200:
    percentual_desconto = 0.05  # 5%
elif valor_compra < 300:
    percentual_desconto = 0.10  # 10%
else:
    percentual_desconto = 0.15  # 15%

# Processamento: calcula o valor do desconto e o valor final a pagar
valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto

# Saída: exibe o resultado ao usuário
print("\n--- Compra ---")
print("Valor da compra: R$", round(valor_compra, 2))
print("Desconto:", int(percentual_desconto * 100), "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Valor total a pagar: R$", round(valor_final, 2))

