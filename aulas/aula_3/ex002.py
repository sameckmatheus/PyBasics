numero = float(input('Digite um  número para verificar se ele é par, ou, ímpar: '))

mod = numero % 2

if mod != 0:
    print(f'O número que você digitou ({numero:.0f}), é par.')
else:
    print(f'O número que você digitou ({numero:.0f}), é ímpar.')