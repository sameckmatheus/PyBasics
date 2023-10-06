"""
Exercício 04

Escreva um código que permita a leitura
das notas de uma turma de 5 alunos e
guarde num vetor, Calcular a média da
turma e contar quantos alunos obtiveram
nota acima desta média calculada
Escrever a média da turma e o resultado
da contagem
"""
notas = [''] * 5

for _ in range(5):
    notas[_] = float(input(f'Informe a {_+1}ª nota: '))

soma = 0
for i in range(5):
    soma += notas[i]

media = soma / 5
acima_media = 0
for j in range(5):
    if notas[j] > media:
        acima_media += 1

print(f'A média geral da turma foi: {media}.')
print(f'{acima_media} alunos ficaram acima da média.')
