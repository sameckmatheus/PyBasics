"""

"""
sala = int(input('Informe o número de alunos na sala: '))
nomes = [0]*sala
achou = 0

for x in range(sala):
    alunos = input(f'Informe o nome do {x+1}º aluno(a): ')
    nomes[x] = alunos

localize_aluno = input('Digite um nome: ')
for i in range(sala):
    if localize_aluno == nomes[i]:
        achou = achou + 1
        print(f'O aluno {nomes[i]}, está na posição {i}.')
        break

if achou == 0:
    print('Esse nome não consta na lista.')