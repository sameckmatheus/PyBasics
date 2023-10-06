"""
Exercício 03

altere o exercício anterior para permitir
achar o nome de um aluno na lista
"""

sala = int(input('Informe o número de alunos na sala: '))
nomes = [0]*sala

for x in range(sala):
    alunos = input(f'Informe o nome do {x+1}º aluno(a): ')
    nomes[x] = alunos

for i in range(sala):
    print(f'O aluno {nomes[i]}, está na posição {i}.')
