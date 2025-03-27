nome_filme_usuario = input("Insira o nome do filme: ")

if nome_filme_usuario == 'AnnaBelle':
    idade_Usuario = int(input("Qual a sua idade? "))
    if idade_Usuario > 18:
        print(f'Você pode assistir o filme {nome_filme_usuario}')
    else:
        print(f"Você não pode assistir o filme {nome_filme_usuario}")

elif nome_filme_usuario == 'Vingadores':
    idade_Usuario = int(input("Qual a sua idade? "))
    if idade_Usuario > 16:
        print(f'Você pode assistir o filme {nome_filme_usuario}')
    else:
        print(f"Você não pode assistir o filme {nome_filme_usuario}")
else:
    print('Filme não encontrado. Ou não registrado.')