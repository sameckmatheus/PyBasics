"""
Exercício 02

altere o exercício anterior e mostre na tela,
ao final, o nome de cada aluno e sua
respectiva posição no array.
"""
sala = int(input('Informe o número de alunos na sala: '))
nomes = [0]*sala

for x in range(sala):
    alunos = input(f'Informe o nome do {x+1}º aluno(a): ')
    nomes[x] = alunos

for i in range(sala):
    print(f'O aluno {nomes[i]}, está na posição {i}.')
