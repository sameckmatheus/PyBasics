from biblioteca import *

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite um valor: '))
numero3 = int(input('Digite um valor: '))
somar = adicao(numero1, numero2, numero3)

print(f'O resultado da soma entre os argumentos '
      f'{numero1}, {numero2} e {numero3}, é: {somar}')
