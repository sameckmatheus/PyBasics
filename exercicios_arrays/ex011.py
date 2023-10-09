'''Faça um código para ler um vetor de 30
números. Após isto, ler mais um número
qualquer, calcular e escrever quantas
vezes esse número aparece no vetor'''

A = [0]*30
cont = 0

for x in range (30):
    A[x] = int(input(f"Qual valor da {x+1}º casa? "))

similar = int(input("Qual valor você quer que chequemos sua frequência, na lista? \n"))

for y in range (30):
    if A[y] == similar:
        cont += 1

if cont == 0:
    print("Não existiram numeros iguais")
else:
    print(f"O numero {similar} apareceu {cont} vezes na lista.")