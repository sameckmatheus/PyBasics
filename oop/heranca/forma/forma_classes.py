class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

    def calcular_perimetro(self, base, altura):
        perimetro = 2 * (base + altura)
        return perimetro

    def calcular_area(self, base, altura):
        area = base * altura
        return area


class Quadrado(Forma):
    def __init__(self, ):
        super().__init__()

    def calcular_perimetro(self, lado, **kwargs):
        perimetro = 4 * lado
        return perimetro

    def calcular_area(self, lado, **kwargs):
        area = lado ** 2
        return area


class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcular_perimetro(self, lado, **kwargs):
        perimetro = lado + lado + lado
        return perimetro

    def calcular_area(self, base, altura):
        area = (base * altura) / 2
        return area
