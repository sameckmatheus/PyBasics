# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c...
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes...
# situações:

# a. Se o usuário informar o valor de A igual a zero...
# a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao usuário;
# d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;

while True:
    a = float(input('Entre com o valor de a: '))

    if a == 0:
        print('A equação não é do segundo grau.')
        quit()

    b = float(input('Entre com o valor de b: '))
    c = float(input('Entre com o valor de c: '))

    delta = b ** 2 - 4 * a * c
    print(f'Delta: {delta}')

    if delta < 0:
        print('A equação não possui raízes reais.')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'A equação possui apenas uma raiz real: {x}')
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f'A equação possui duas raízes reais: {x1} e {x2}')

    continuar = input('Deseja sair?\n'
                      'Digite q ou Enter para novo cálculo: ')
    if continuar == 'q':
        break
