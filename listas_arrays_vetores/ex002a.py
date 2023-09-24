# Crie uma lista com 10 números inteiros aleatórios e ordene-os em ordem crescente.

lista_numeros = []

for i1 in range(10):
    menor_indice = i1
    elementos = int(input(
        'Digite um número aleatório: '
    ))
    lista_numeros.append(elementos)
    for i2 in range(i1 + 1, len(lista_numeros)):
        if lista_numeros[i2] < lista_numeros[i1]:
            menor_indice = i2
    lista_numeros[i1], lista_numeros[menor_indice] = lista_numeros[menor_indice], lista_numeros[i1]

print(lista_numeros)
