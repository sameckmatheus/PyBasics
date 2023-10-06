"""
Exercício 01

Perguntar ao usuário quantos alunos tem
na sala e criar um array, unidimensional
(Ve0tor) com o nome de todos os alunos da
sala
"""
sala = int(input('Informe o número de alunos na sala: '))
nomes = []

for x in range(sala):
    alunos = nomes.append(input(f'Informe o nome do {x}º aluno(a): '))
print(nomes)
