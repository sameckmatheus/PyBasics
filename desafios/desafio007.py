class Poligono:
    def __init__(self, side, nsides, apothem):
        self.Side = side
        self.NumberOfSide = nsides
        self.Apothem = apothem

    def calcular_perimetro(self):
        perimeter = self.Side * self.NumberOfSide
        return perimeter

    def calcular_area(self):
        area = (self.calcular_perimetro() * self.Apothem) / 2
        return area


poligono_regular = Poligono(side=float(input('Digite a medida dos lados: ')),
                            nsides=float(input('Digite o número de lados do polígono: ')),
                            apothem=float(input('Digite a medida do raio: ')))

print(f'A área do polígono, é: ', poligono_regular.calcular_area())
