# Crie uma lista com 10 números inteiros aleatórios e ordene-os em ordem crescente.

lista_numeros = []

for x in range(len(lista_numeros)):
    menor_indice = x
    for z in range(x + 1, len(lista_numeros)):
        if lista_numeros[z] < lista_numeros[x]:
            menor_indice = z
    lista_numeros[x], lista_numeros[menor_indice] = lista_numeros[menor_indice], lista_numeros[x]

print(lista_numeros)
