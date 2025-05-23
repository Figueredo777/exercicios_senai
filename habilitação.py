from colorama import init,Fore
init(autoreset=True)

nome = input("Qual é o seu nome? ")
idade = int(input("Qual sua idade? "))

if idade >= 18:
    print(Fore.GREEN+"Maior de Idade")
    carteira = int(input("Você tem carteira?   (1- Sim/ 2- Não) "))
    if carteira == 1:
        print("Pode Dirigir")
    else:
        print("Não Pode Dirigir")

else:
    print(Fore.RED+"Menor de Idade")
    print("Não pode dirigir")
    