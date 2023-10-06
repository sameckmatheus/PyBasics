"""
2. Crie um código que leia um número
diferente de zero e diga se este número
é positivo ou negativo
"""
n = int(input('Digite um número: '))
if n != 0:
    if n > 0:
        mensagem = f'O número {n} é positivo.'
        print(mensagem)
    else:
        mensagem = f'O número {n} é negativo.'
        print(mensagem)
elif n == 0:
    mensagem = f'O número {n} é inválido para a execução do programa.'
    print(mensagem)
