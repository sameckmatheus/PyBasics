class Forma:
    def __init__(self, lado, numero_lados):
        self.lado = lado
        self.numero_lados = numero_lados
        self.area = 0
        self.perimetro = 0


class Quadrado(Forma):
    def __init__(self, lado, numero_lados):
        super().__init__(lado, numero_lados)

    def calcular_perimetro(self):
        perimetro = self.lado * self.numero_lados
        return perimetro

    def calcular_area(self):
        area = ()
        return area


class Triangulo(Forma):
    def __init__(self, lado, numero_lados):
        super().__init__(lado, numero_lados)

    def calcular_perimetro(self):
        perimetro = self.lado * self.numero_lados
        return perimetro

    def calcular_area(self):
        area =
        return area
