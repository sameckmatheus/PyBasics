"""
5. Crie um algoritmo que leia um
número e diga se ele é par ou ímpar
"""
n = int(input('Digite um número: '))
if n % 2 == 0:
    mensagem = f'O número {n} é par.'
    print(mensagem)
else:
    mensagem = f'O número {n} é ímpar.'
    print(mensagem)
