alunos = int(input('Informe a quantidade de alunos na sala: '))
quantidade = 0

if alunos > 0:
    while quantidade <= alunos:
        print('Informe as notas deste Estudante: ')
        MediaEstudante = float(input(f'Este estudante, tem média: '))
else:
    print('ENTRADA INVÁLIDA!!!')
    print('A quantidade de alunos deve ser representada por um número inteiro...')
    quit()

media = MediaEstudante / alunos
