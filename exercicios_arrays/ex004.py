"""
4. Crie um algoritmo que receba 3
números e informe qual o maior entre
eles.
"""
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 > n3:
    mensagem = f'O número {n1} é o maior.'
    print(mensagem)
elif n2 > n3:
    mensagem = f'O número {n2} é o maior.'
    print(mensagem)
else:
    mensagem = f'O número {n3} é o maior.'
    print(mensagem)
