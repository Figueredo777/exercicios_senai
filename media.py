from colorama import init,Fore
init(autoreset=True)
print("|",30*"_","|")
print("| SISTEMA DE PROVAS")
print("|",30*"_","|")
nome = input("| Qual o nome do aluno? ")

nota1 = float(input("| Nota da primeria prova: "))
nota2 = float(input("| Nota da segunda prova: "))
nota3 = float(input("| Nota da terceira prova: "))
print("|",30*"_","|")
media = round((nota1 + nota2 + nota3)/3, 2)
print("| Aluno:", nome)
print("| Media:", media)
if media >=5:
    print("| ",Fore.GREEN+"Aluno Aprovado")
else:
    print("| ",Fore.RED+"Aluno Reprovado")

print("|",30*"_","|")