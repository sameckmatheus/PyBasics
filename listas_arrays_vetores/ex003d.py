loop = 'S'


sala = int(input('Informe o número de alunos na sala: '))
nomes = [0]*sala

for x in range(sala):
    alunos = input(f'Informe o nome do {x+1}º aluno(a): ')
    nomes[x] = alunos

while loop == 'S' or loop == 's':
    localize_aluno = input('Digite um nome: ')
    achou = 0

    for i in range(sala):
        if nomes[i] == localize_aluno:
            achou = achou + 1
            print(f'O aluno {nomes[i]}, está na posição {i}.')

    if achou == 0:
        print('Esse nome não consta na lista.')

    loop = input('Deseja realizar uma nova pesquisa? (s/n):')
    if loop == 'N' or loop == 'n':
        print('Obrigado por utilizar nosso programa.')
