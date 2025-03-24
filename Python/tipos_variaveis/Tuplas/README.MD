# Tuplas

 - Tuplas são conhecidas por serém imutaveis, ou seja, não podem ser alteradas.
 - Possuem métodos que que permitem ser realizados algumas operações uteis.

## Criando uma tupla
```python
tupla = (1, 2, 3, 4, 5)
```

# Métodos utilizados com tuplas

* Método COUNT - Retorna a quantidade de vezes que um elemento aparece na tupla.
```Python
tupla_exemplos = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
tupla_exemplos.count(3)
print(tupla_exemplos)
```

* Método INDEX - Retorna o indice do elemento passado como parametro.
```Python
tupla_exemplos = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
tupla_exemplos.index(3)
print(tupla_exemplos)
```

# Imutabilidade das tuplas 
 - Não podemos alterar a caracteristica de uma tuplas, pois sabemos que elas são imutaveis. Com isso podemos afirmar que ela são seguras, pois não pode ser mudado seu valor otiginal.

Exemplo 1
```Python
tuplas_exemplo = (0, 0, 0, 1, 1, 0, 3, 0, 2, 3, 1)
tuplas_exemplo[0] = 1
print(tuplas_exemplo)
```

* Neste exemplo ocorrera um ERROR. Conhecido como TypeError: 'tuple' object does not support item assignment
 - Não podemos alterar o valor de uma tupla, pois ela é imutavel.

