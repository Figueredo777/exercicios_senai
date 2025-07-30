from colorama import init,Fore
import emoji

init(autoreset=True)



# print(emoji.emojize('Python is :medical_symbol:'))

barra = f'{'|'}{65*'_'}{"|"}'
print(barra)
print(emoji.emojize("| :medical_symbol:  Monitoramento de Saúde com Cálculo de IMC :)"))
print(barra)

nome = input("| Digite seu nome: ")

peso = float(input("| Qual o seu peso? "))
altura = float(input("| Qual a sua altura? "))
imc = round(peso / (altura ** 2),2)
print(f"| O seu imc é de ",imc )
print(barra)

if imc <= 18.5:
    print("| Clasificação:", Fore.YELLOW+"abaixo do peso.")
    print("| Recomendação: Coma mais pizza :) e procure um médico.")

elif imc >18.5 and imc <=24.9:
    print("| Clasificação:", Fore.GREEN+"Peso Normal")
    print("| Recomendação: Tudo ok, mas sempre tome cuidado! :)")

elif imc >25.0 and imc <=29.9:
    print("| Clasificação:", Fore.RED+"Sobrepeso.")
    print("| Recomendação: adotar um estilo de vida mais saudável. :|")

elif imc >30.0 and imc <= 34.9:
    print("| Clasificação:",Fore.RED+"Obesidade Grau I.")
    print("| Recomendação: seguir uma dieta equilibrada e saudável, combinada com a prática regular de exercícios físicos. :|")

elif imc >35.0 and imc <= 39.9:
    print("| Clasificação:",Fore.LIGHTRED_EX+"Obesidade Grau II.")
    print("| Recomendação: buscar orientação profissional especializada. :(")

else: 
    print("| Clasificação:", Fore.LIGHTRED_EX+"Obesidade Grau III (mórbida)")
    print("| Recomendação: dieta, atividade física e suporte psicológico. :(")
print(barra)