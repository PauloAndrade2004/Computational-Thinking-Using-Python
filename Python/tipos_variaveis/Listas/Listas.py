line = (40 * '-')



# Criando a minha primeira lista.
minha_Lista = [1, 2, 3, 4, 5, 6, 7]
print(minha_Lista)

# Acessando o elemento da nossa lista.
print('Acessando o elemento do indice ' + str(minha_Lista[5])) # SAIDA: 6


# Removendo elemento na nossa lista.
minha_Lista.remove(1) # O elemento 1 foi removido da nossa Lista.
print(minha_Lista)

print(line)
#Criando a minha lista vazia.
minha_lista_vazia = []

# Adicionando elemento na minha lista.
minha_lista_vazia.append(1) # O elemento 1 foi adicionado na nossa Lista.
print(minha_lista_vazia)

print(line)

# Verificando se a lista está vazia:
teste_minha = [2]

if teste_minha:  # Verifica se a lista não está vazia
    print('Minha lista não está vazia')
else:
    print('Lista vazia')
    print('Adicione um elemento na lista:')
    adicionar = input()  # Solicita um elemento ao usuário
    teste_minha.append(adicionar)  # Adiciona o elemento à lista
    print('Elemento adicionado com sucesso!')
    print('Lista atualizada ', teste_minha)
    #print('ultimo elemento adicionado na Lista ', teste_minha[-1])

print(line)

# Percorrendo a lista com o for
print('Exibindo minha lista percorrendo')
for i in minha_Lista:
    print(i)

print(line)

#Podemos buscar elementos na nossa lista.
print(5, minha_Lista)

print(line)

# Usando o Extend() para adicionar mais de um elemento na nossa lista.
minha_lista_extend = [1, 2, 3]
minha_lista_extend.extend([4, 5, 6])# adicionando mais de um elemento na nossa lista.
print(minha_lista_extend)

print(line)

# Método pop()
elemento_removivel = minha_lista_extend.pop(1) # Removendo o elemento do indice 0
print('Elemento removivel:', elemento_removivel)
print(minha_lista_extend)




















