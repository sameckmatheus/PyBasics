'''Escreva um algoritmo que solicite ao
usuário a entrada de 5 nomes, e que exiba
a lista desses nomes na tela.
Após exibir essa lista, o programa deve
mostrar também os nomes na ordem
inversa em que o usuário os digitou, um
por linha.'''

A = [0]*5

for x in range (5):
    A[x] = input(f"Digite seu nome, {x+1}º usuário: ")

print("Os nomes listados são: ")
for y in range (5):
    print(A[y], end = " ")

print("\n"
      "Ou na ordem inversa: \n")
for z in range (4,-1,-1):
    print(A[z])