"""
12. Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores.
"""

totalEleitores = int(input('Informe a quantidade de eleitores: '))
votosBrancos = int(input('Informe a quantidade de votos brancos: '))
votosValidos = int(input('Informe a quantidade de votos válidos: '))
votosNulos = int(input('Informe a quantidade de votos nulos: '))

percentualVotosBrancos = (votosBrancos / totalEleitores) * 100
percentualVotosValidos = (votosValidos / totalEleitores) * 100
percentualVotosNulos = (votosNulos / totalEleitores) * 100

print(f'Votos Brancos: {percentualVotosBrancos}%')
print(f'Votos Válidos: {percentualVotosValidos}%')
print(f'Votos Nulos: {percentualVotosNulos}%')
