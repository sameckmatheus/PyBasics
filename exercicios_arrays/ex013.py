'''Faça um algoritmo que leia 30 valores do
tipo inteiro e armazene-os em um vetor.
A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no
vetor;
(2) o menor e o maior valor existente no
vetor;
(3) quantos dos valores do vetor são
maiores que a média desses valores:'''

A = [0]*30
Par = [" "]*30
maior = 0

soma = 0

for x in range (30):
    A[x] = int(input(f"Digite o {x+1}º valor: "))
    if x == 0:
        menor = A[x]
    soma += A[x]
    if A[x] > maior:
        maior = A[x]
    if A[x] < menor:
        menor = A[x]

media = soma / 30
cont_maior_que_media = 0
for w in range (30):
    if A[w] > media :
        cont_maior_que_media += 1

for y in range (30):
    if A[y] % 2 == 0 :
        Par[y] = A[y]

print(f"\n(1) Os numeros pares são: ")
for z in range(30):
    if Par[z] != " " :
        print(Par[z], end = " ")

print(f"\n(2) O menor de todos é o {menor}. \n"
      f"(2) O maior de todos é  o {maior}. \n"
      f"(3) No total, existem {cont_maior_que_media}, numeros maiores que a média dos valores ({media}). ")