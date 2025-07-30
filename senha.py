from colorama import init,Fore
init(autoreset=True)

email = input("Insire o email: ")
senha = "San220108"

senha = input("Insire a senha: ")

if senha == "San220108":
    print(Fore.GREEN+"Senha Correta")


else:
    print(Fore.RED+"Email ou Senha Incorreta")    

