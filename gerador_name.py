print("Gerador de Username")
nome = input("Digite seu nome: ").strip().lower().split()

primeiro_nome = (nome[0])
ultimo_nome = nome[-1]
print(f"{primeiro_nome}.{ultimo_nome}")