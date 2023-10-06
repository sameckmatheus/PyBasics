"""
8. Faça um código que receba 4
números e realize a soma deles e a
média entre eles. e mostre os
resultados.
"""
soma = 0
m = 0
for numero in range(1, 5):
    n = int(input(f'Digite o {numero}º número: '))
    soma += n
    m = soma / 4
print(f'Sua média, é: {m:.1f}')
