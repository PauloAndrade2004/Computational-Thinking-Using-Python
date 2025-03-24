from selenium.webdriver.common.print_page_options import PrintOptions

# Listas 
-   Listas em Python são 






# Adicionando elementos na nossa lista.
 - Podemos adicionar um elemento a uma lista, utilizando o método append().
 - O método append() adiciona um elemento ao final da lista.
```python
lista = [1, 2, 3]
lista.append(5)

print(lista)
 ```

# Acessando os elementos da nossa Lista:
- Podemos acessar os elementos de uma lista, utilizando o índice do elemento.
```Python
lista = [1, 2, 3, 4, 5]
print('Acessando o elemento do indice ' + [5] + ' da lista: ' + str(lista[5]))
```

# Acessando os elementos da nossa Lista com índice negativo O ULTIMO ELEMENTO:
```Python
lista = [1, 2, 3, 4, 5]
print('Acessando o elemento do indice' + str(lista[-1]))

# SAIDA: 5
```

# Verificando se a lista está vazia:
- Podemos verificar se uma lista está vazia, utilizando a função len() ou utilizando o if-else.

```Python
lista = []
if len(lista):
    print('Minha lista não está vazia')
else:
    print('Minha lista está cheia')
```
### Exemplo 2:
```Python
teste_minha = []
if teste_minha:
    print('Minha lista não está vazia')
else:
    print('Lista vazia')
    print('Por favor, adicione um elemento em nossa Lista')
    elemento = input('Digite um elemento: ')
    teste_minha.append(elemento)
    print('Elemento adicionado com sucesso!')
    print('Lista atualizada: ', teste_minha)

```
* (1) Utilizamos a condicional if-else, para verificar se a lista está vazia.
* (2) Caso a lista esteja vazia elem pede para que nós adicionemos um elemento a lista.
* (3) Após isso, este elemento é exibindo uma mensagem de sucesso.
* (4) por fim exibimos a lista atualizada.