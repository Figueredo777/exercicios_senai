from colorama import init,Fore
init(autoreset=True)

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso / (altura * altura)

resultado = round(imc, 2)
print(resultado)
if resultado >=30: 
    print(Fore.RED+"Toma cuidado com a sua Saude")
else:
    print(Fore.GREEN+"Tudo ok com a sua Saude")

