from biblioteca import *

quantidade_perguntas = int(input('Quantos valores você tem para calcular? '))
numero = [0]*quantidade_perguntas

for i in range(quantidade_perguntas):
    numero[i] = int(input(f'Digite o {i+1} valor: '))

somar = adicao(numero)

print(f'O resultado da soma entre os argumentos {numero}, é: {somar}')
