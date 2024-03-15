# ### Parte 1 - Operações e Variáveis
# Crie um programa que imprima os principais indicadores da loja Drink
# no último ano.
# Obs: faça tudo usando variáveis.

# Valores do último ano:

# Quantidade de Vendas de Coca = 150
# Quantidade de Vendas de Pepsi = 130
# Preço Unitário da Coca = 1,50
# Preço Unitário da Pepsi = 1,50
# Custo da Loja: 2.500,00

# Use o bloco abaixo para criar todas as variáveis que precisar.

qntd_Coca_Vendida = 150
qntd_Pepsi_Vendida = 130
preco_Coca = 1.50
preco_Pepsi = 1.50
custo_Loja = 2500

# Faturamento Pepsi
faturamento_Pepsi = qntd_Pepsi_Vendida * preco_Pepsi
print(f"O faturamento de vendas de Pepsi foi: R${faturamento_Pepsi}")

# Faturamento Coca
faturamento_Coca = qntd_Coca_Vendida * preco_Coca
print(f"O faturamento de vendas de Pepsi foi: R${faturamento_Coca}")

# Qual foi o lucro da Loja
faturamento_Bebidas = (faturamento_Pepsi + faturamento_Coca)
lucro = (faturamento_Bebidas - custo_Loja)
print(f'O lucro foi de {lucro}')


# Calcule quanto foi a margem de lucro líquido
margem_Lucro = (lucro / faturamento_Bebidas) * 100
print(f'A margem de lucro foi de {margem_Lucro:.2f}%')
