'''Faça um código para ler um valor N qualquer (que
será o tamanho dos vetores). Após, ler dois
vetores A e B (de tamanho N cada um) e depois
armazenar em um terceiro vetor Soma, a soma dos
elementos do vetor A com os do vetor B
(respeitando as mesmas posições) e escrever o
vetor Soma.'''

lista = int(input("Qual o tamanho das suas listas? "))

A = [0]*lista
B = [0]*lista
C = [0]*lista

for x in range (lista):
    A[x] = int(input(f"Digite o {x+1}º valor da 1ª lista: "))
    C[x] = A[x]

for y in range(lista):
    B[y] = int(input(f"Digite o {y+1}º valor da 2ª lista: "))
    C[y] += B[y]

for z in range(lista):
    print(f"A soma do {z+1}º é = {C[z]}")
