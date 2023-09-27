lista_numeros = []

for _ in range(5):
    elementos = int(input('Digite um número aleatório: '))
    lista_numeros.append(elementos)

for x in range(len(lista_numeros)):
    menor_indice = x
    for z in range(x + 1, len(lista_numeros)):
        if lista_numeros[z] < lista_numeros[menor_indice]:
            menor_indice = z
    lista_numeros[x], lista_numeros[menor_indice] = lista_numeros[menor_indice], lista_numeros[x]

print(lista_numeros)
