import math

while True:
    a = float(input('Entre com o valor de a: '))
    b = float(input('Entre com o valor de b: '))
    c = float(input('Entre com o valor de c: '))

    def calcular_raizes():
        if a == 0:
            print('A equação não é do segundo grau.')
            return

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
    continuar = input('Deseja sair?\n'
                      'Digite q ou Enter para novo cálculo: ')
    if continuar == 'q':
        break
