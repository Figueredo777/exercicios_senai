# Aluguel de carros:


# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado


# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

dias = float(input("Por Quantos dias o carro foi alugado: "))

km = float(input("Quantos km o carro rodou: "))

valor_dias = (dias * 60)
valor_km = (km * 0.15)

valor_total = (valor_dias + valor_km)

print(f"Você percorreu {km}km por {dias} dias, então o preço a pagar é R${valor_total} ")
