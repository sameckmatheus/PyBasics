from typing import Self


class Poligono:
    def __init__(self, Side, NumberOfSide, Apothem):
        self.Side = Side
        self.NumberOfSide = NumberOfSide
        self.Apothem = Apothem

    def calcularPerimetro(self):
        perimeter = self.Side * self.NumberOfSide
        return perimeter

    def CalcularArea(self):
        area = (self.calcularPerimetro() * self.Apothem) / 2
        return area


poligono_regular = Poligono(Side=float(input('Digite a medida dos lados: ')), 
                            NumberOfSide=float(input('Digite o número de lados do polígono: ')), 
                            Apothem=float(input('Digite a medida do raio: ')))

print(f'A área do polígono, é:', poligono_regular.CalcularArea())
