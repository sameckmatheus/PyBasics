alunos = int(input('Informe a quantidade de alunos na sala: '))
notas = []
contador = 0
soma = 0

"""
if alunos > 5:
    print('Limite de 5 alunos por turma...')
    quit()
else:
"""

while alunos > 0:
    print('\nInforme as notas deste Estudante: ')
    nota = float(input(f'Este estudante, tem média: '))
    notas[contador:contador+1] = [nota]
    soma = soma + nota
    contador = contador + 1
    alunos = alunos - 1

media = soma / contador

print('\n============================================')
print(f'A média aritmética da turma, é: {media:.2f}')
print('============================================')
