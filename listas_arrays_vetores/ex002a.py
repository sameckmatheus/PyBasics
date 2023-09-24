# Crie uma lista com 10 números inteiros aleatórios e ordene-os em ordem crescente.

lista_numeros = []

for reps in range(10):
    elementos = int(input(
        'Digite um número aleatório: '
    ))
    lista_numeros.append(elementos)
print(lista_numeros)
