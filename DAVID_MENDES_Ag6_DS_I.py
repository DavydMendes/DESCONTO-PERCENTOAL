# Sistema de desconto progressivo
# Agenda 6 - Desenvolvimento de Sistemas

# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica qual percentual de desconto deve ser aplicado
if valor_compra < 200:
    desconto_percentual = 5
elif valor_compra < 300:
    desconto_percentual = 10
else:
    desconto_percentual = 15

# Calcula o valor do desconto
valor_desconto = valor_compra * desconto_percentual / 100

# Calcula o valor final da compra
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
