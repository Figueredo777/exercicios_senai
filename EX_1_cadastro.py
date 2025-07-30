# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

barra = f"{"|"}{30*"_"}{"|"}"
print(barra)
nome = input("| Digite o seu nome: ")
idade = input("| Digite sua Idade: ")
email = input("| Digite seu email: ")
senha = input("| Digite sua senha: ")
print(barra)
print("| -----","USUÁRIO CADASTRADO","---- |")
print("| Seja bem vindo(a)", nome)
print("| Email:", email)

print(barra)