caixa = input('me fala uma cor? ')

if caixa == 'preto':
    print('legal!')
    cor = input("Poderia me fala outra cor? ")
    if cor == "azul":
        print("Legal, mas não era a cor que eu queria")
        cor = input("Diga - me outra cor: ")

    elif cor == "rosa":
        print("Agora sim, a cor certa :)")

    else:
        print('Fim')





