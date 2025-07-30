import os

tarefas = {
    'tarefas' : ['Lavar Roupas', 'Lavar Banheiro'],
    'datas' : ['03/07', '04/7']
}

def mostrar_tarefas():
    barra = f'|{40*"-"}|'
    print(barra)
    print('| LISTA DE TAREFAS')
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1}. {tarefas['tarefas'][i]} - Data: {tarefas['datas'][i]}')
    print(barra)

def adicionar_tarefa():
    barra = f'|{40*"-"}|'
    print(barra)
    print('| Adicionar nova tarefa')
    print(barra)
    nova_tarefa = input('| Digite o nome da tarefa: ')
    data = input('| Digite a data: ')
    tarefas['tarefas'].append(nova_tarefa)
    tarefas['datas'].append(data)
    print(f'| Tarefa {nova_tarefa} adicionada com sucesso!')
    print(barra)


def remover_tarefa():
    barra = f'|{40*"-"}|'
    print(barra)
    print('| Remover tarefa')
    mostrar_tarefas()
    indice = int(input('| Digite o número da tarefa que deseja remover: '))
    if 0 < indice <= len(tarefas['tarefas']):
        tarefa_removida = tarefas['tarefas'].pop(indice-1)
        tarefas['datas'].pop(indice-1)
        print(f'| Tarefa: "{tarefa_removida}" foi removida com sucesso!')
    else:
        print('| INDICE INVÁLIDO')

def menu():
    while True:
        os.system('cls')
        barra = f'|{40*"-"}|'
        print(barra)
        print('| Gerenciador de Tarefas')
        print(barra)
        print('| (1) Mostrar lista de tarefas')
        print('| (2) Adicionar tarefa')
        print('| (3) Remover tarefa')
        print('| (4) Sair')
        print(barra)
        try:
            opc = int(input('| Digite o número da opção: '))
            if opc == 1:
                os.system('cls')
                mostrar_tarefas()
                input('| Pressione enter para continuar... ')

            elif opc == 2:
                os.system('cls')
                adicionar_tarefa()
                input('| Pressione enter para continuar... ')
                
            elif opc == 3:
                os.system('cls')
                remover_tarefa()
                input('| Pressione enter para continuar... ')
                
            elif opc == 4:
                print('| Encerrando o programa.')
                break

            else:
                print('| Opção Inválida')
                input('| Pressione enter para continuar... ')
        except:
            print('| ERRO! DIGITE UM NÚMERO VÁLIDO!')
            input('| Pressione enter para continuar... ')

menu()