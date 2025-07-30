print("Seja Bem Vindo Auto Mais")
valor = 0
carro = input("Qual carro que o senhor ou a senhora deseja alugar? ")
if carro == "gol":
    print("Esse carro custara R$60 reais por dia ")
    valor = 60

elif carro == "Toro":
    print("Esse carro custara R$80 reais por dia ")
    valor = 80

elif carro == "fiesta":
    print("Esse carro custara R$59.90 reais por dia")
    valor = 59.90

else:
    print("Esse carro custara R%50 reais por dia")

    
dias = float(input("Por Quantos dias o carro foi alugado: "))

km = float(input("Quantos km o carro rodou: "))

valor_dias = (dias * valor)
valor_km = (km * 0.15)

valor_total = (valor_dias + valor_km)

print(f"Você percorreu {km}km por {dias} dias, então o preço a pagar é R${valor_total} ")
