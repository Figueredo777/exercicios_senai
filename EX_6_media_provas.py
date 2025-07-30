# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

barra = f"{"|"}{30*"_"}{"|"}"
print(barra)
nome = input("| Nome do aluno: ")

nota_1 = float(input("| Nota da primeira prova: "))
nota_2 = float(input("| Nota da segunda prova: "))
nota_3 = float(input("| Nota da terceira prova: "))
print(barra)
media = round((nota_1 + nota_2 + nota_3)/3, 2)
print("| Aluno: ", nome)
print("| Media: ", media)
if media >=5:
    print("| Aluno Aprovado")
else:
    print("| Aluno Reprovado")
print(barra)