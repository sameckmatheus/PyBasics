# Crie uma lista com 10 números inteiros aleatórios e ordene-os em ordem crescente.

lista_numeros = []

for x in range(10):
    menor_indice = x
    elementos = int(input(
        'Digite um número aleatório: '
    ))
    lista_numeros.append(elementos)
    for i2 in range(x + 1, len(lista_numeros)):
        if lista_numeros[i2] < lista_numeros[x]:
            menor_indice = i2
    lista_numeros[x], lista_numeros[menor_indice] = lista_numeros[menor_indice], lista_numeros[x]

print(lista_numeros)
