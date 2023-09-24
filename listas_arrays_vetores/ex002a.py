# Crie uma lista com 10 números inteiros aleatórios e ordene-os em ordem crescente.
import random

lista_numeros = [random.randint(1, 100) for _ in range(10)]
for x in range(len(lista_numeros)):
    menor_indice = x
    elementos = int(input(
        'Digite um número aleatório: '
    ))
    lista_numeros.append(elementos)
    for z in range(x + 1, len(lista_numeros)):
        if lista_numeros[z] < lista_numeros[x]:
            menor_indice = z
    lista_numeros[x], lista_numeros[menor_indice] = lista_numeros[menor_indice], lista_numeros[x]

print(lista_numeros)
