"""
1. Faça um algoritmo que receba 2
notas e calcule a média aritmética
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
media = (n1 + n2) / 2
mensagem = (f'Você inseriu os números {n1} e {n2}'
            f'A média entre eles, é: {media}')
print(mensagem)
