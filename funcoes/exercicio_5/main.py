from biblioteca import *

nome_aluno = input('Digite seu nome: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = calcular_media(n1, n2)
x = imprimir_media(nome_aluno, m)

print(f'O aluno(a) {x[1]}, foi {x[0]}')
