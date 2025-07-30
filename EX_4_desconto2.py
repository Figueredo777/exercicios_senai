# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

carro = input("Produto: ")
preco = float(input("Preço: "))
porcentagem = float(input("Porcentagem de edesconto: ")) 
desconto = preco * (porcentagem / 100)
valor_novo = preco - desconto
print(f"O {carro} com {porcentagem}% de desconto custará R$ {valor_novo}" )