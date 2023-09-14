# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c...
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes...
# situações:

# a. Se o usuário informar o valor de A igual a zero...
# a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao usuário;
# d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;

import math

while True:
    a = float(input('Entre com o valor de a: '))

    def calcular_raizes():
        if a == 0:
            print('A equação não é do segundo grau.')
            quit()
        
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print('A equação não possui raízes reais.')
        elif delta == 0:
            x = -b / (2 * a)
            print(f'A equação possui apenas uma raiz real: {x}')
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f'A equação possui duas raízes reais: {x1} e {x2}')


    calcular_raizes()
    continuar = input('Deseja sair, digite [q]?\n'
                      'Ou, digite [Enter] para novo cálculo: ')
    if continuar == 'q':
        break
