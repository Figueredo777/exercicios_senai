import os
tarefas = {
    "Tarefas": ["Limpar a casa", "Arrumar o quarto", "Lavar a louça"],
    "Datas": ["01/07", "02/07", "03/07"]
}
def mostrar_tarefas():
    for i in range(len(tarefas["Tarefas"])):
        print(f"| {i+1}. {tarefas['Tarefas'][i]} - Datas: {tarefas['Datas'][i]}")
    print("|------------------------------------")
    
# ------------------------------------------------------------------------------------------------------------------
def adicionar_tarefa():
    nova_tarefa = input("| Adicione a tarefa: ")
    tarefas["Tarefas"].append(nova_tarefa)
    nova_data = input("| Adicione a data: ")
    tarefas["Datas"].append(nova_data)
# ------------------------------------------------------------------------------------------------------------------
def remover_tarefa():
    mostrar_tarefas()
    numero_tarefa = int(input("| Digite o número da tarefa: "))
    if 0 < numero_tarefa <= len(tarefas["Tarefas"]):
        tarefa_removida = tarefas["Tarefas"].pop(numero_tarefa - 1)
        tarefas["Datas"].pop(numero_tarefa - 1)
        print(f"| A tarefa {tarefa_removida} foi removida com sucesso! ")
    else:
        print('| INDICE INVÁLIDO')
# ------------------------------------------------------------------------------------------------------------------
def mostrar_menu():
    while True:
        os.system("cls")
        barra = f"| {"_" * 30} |"
        print(barra)
        print("| Gerenciador de Tarefas")
        print(barra)
        print("| (1) Mostrar Tarefas")
        print("| (2) Adicionar Tarefa")
        print("| (3) remover Tarefa")
        print("| (4) Sair")
        print(barra)
        try:
            opcao = int(input("| Escolha uma opção: "))
            if opcao == 1:
                os.system("cls")
                print("| ----- Mostrar Tarefa -----")
                mostrar_tarefas()
                input("| Pressione enter para continuar...")
            elif opcao == 2:
                os.system("cls")
                print("| ----- Adicionar Tarefa -----")
                print(barra)
                adicionar_tarefa()
                input("| Pressione enter para continuar...")
            elif opcao == 3:
                os.system("cls")
                print("| ----- Remover Tarefa -----")
                remover_tarefa()
                input("| Pressione enter para continuar...")
            elif opcao == 4:
                print("| Saindo...")
                break
            else:
                print("| Opção invalida.")
                input("| Pressione enter para continuar...")
                print(barra)
        except:
            print("| ERRO! DIGITE UM NÚMERO VÁLIDO")
            input("| Pressione enter para continuar...")
            
mostrar_menu()