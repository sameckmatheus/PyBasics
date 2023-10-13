class Poligono:
    def __init__(self, paramSide, paramNumberOfSide, paramApothem):
        self.Side = paramSide
        self.NumberOfSide = paramNumberOfSide
        self.Apothem = paramApothem

    def calculatePerimeter(self):
        perimeter = self.Side * self.NumberOfSide
        return perimeter

    def CalcularArea(self):
        area = (self.calculatePerimeter() * self.Apothem) / 2
        return area


triangulo = Poligono(5, 3, 5)
print('A área do triângulo, é:', triangulo.CalcularArea())
