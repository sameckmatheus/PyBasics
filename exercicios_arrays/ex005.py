'''Ler um vetor A de 10 números. logo em
seguida, ler mais um número e guardar em
uma variável X.
Armazenar em um vetor M o resultado de
cada elemento de A multiplicado pelo
valor X. Logo após, imprimir o vetor M.'''

fator = int(input("Qual fator multiplicador? "))
A = [" "]*10

for y in range (10):
    A[y] = int(input(f"Digite o {y+1}º valor: "))


M = [" "]*10
for x in range (10):
    M[x] = A[x] * fator
    print(f"o numero {A[x]} x pelo fator {fator} = {M[x]}")
