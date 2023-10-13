"""
    Faça um código para ler 2 valores e
    realize a divisão do primeiro pelo
    segundo valor recebido, caso o
    segundo valor digitado, seja 0, solicite
    novamente o valor, informando que só
    aceitaremos valores diferentes de
    zero.
"""

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
divisao = 0

while valor2 == 0:
    valor2 = int(input('Só aceitaremos valores diferentes de zero, digite outro valor: '))
else:
    divisao = valor1 / valor2

print(f'A divisão de {valor1} por {valor2}, é igual a: {divisao}')
