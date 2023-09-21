"""
    Escreva um código para ler as notas
    da 1a. e 2a. avaliações de um aluno,
    calcule e imprima a média desse
    aluno. Só devem ser aceitos valores
    válidos durante a leitura (0 a 10) para
    cada nota.
"""

n1 = float(input('Informe a primeira nota: '))
while n1 < 0 and n1 > 10:
    n1 = float(input('Informe a primeira nota, com valores válidos entre 0 e 10: '))
n2 = float(input('Informe a segunda nota: '))
while n2 < 0 and n2 > 10:
    n2 = float(input('Informe a segunda nota, com valores válidos entre 0 e 10: '))
media = (n1 + n2) / 2
print(f'A sua média foi calculada.\n'
      f'Resultado: {media}')
