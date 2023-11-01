from forma_classes import *

quadrado = Quadrado()
side = 5
perimetro_q = quadrado.calcular_perimetro(side)
area_q = quadrado.calcular_area(side)
print(perimetro_q)
print(area_q)


triangulo = Triangulo()
side1 = 5
side2 = 5
side3 = 5
perimetro_t = triangulo.calcular_perimetro(side1)
area_t = triangulo.calcular_area(side1, side2)
print(perimetro_t)
print(area_t)
