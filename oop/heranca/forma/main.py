from forma_classes import *

triangulo = Triangulo(side=float(input('Digite a medida dos lados: ')),
                      nsides=float(input('Digite o número de lados do polígono: ')),
                      apothem=float(input('Digite a medida do raio: ')))

print(f'A área do polígono, é: ', triangulo.calcular_area())
