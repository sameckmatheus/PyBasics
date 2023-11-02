class NPC:
    def __init__(self, nome, grupamento, resistencia, ataque):
        self.nome = nome
        self.grupamento = grupamento
        self.resistencia = resistencia
        self.ataque = ataque
        self.vivo = True
        self.energia = 100

    def informacoes(self):
        print(f'Nome.........: {self.nome}\n'
              f'Grupamento...: {self.grupamento}\n'
              f'Resistência..: {self.resistencia}\n'
              f'Ataque.......: {self.ataque}\n'
              f'Vivo.........: {"Sim" if {self.vivo} else "Não"}\n'
              f'Energia......: {self.energia}\n'
              f'*******************************')


class Soldado(NPC):
    # este "filho" construtor sobrepõe o contronstrutor da superclass "pai"
    def __init__(self, nome, grupamento):  
        self.resistencia = 200
        self.ataque = 200
        super().__init__(nome, grupamento, self.resistencia, self.ataque)


class Guarda(NPC):
    # este "filho" construtor sobrepõe o contronstrutor da superclass "pai"
    def __init__(self, nome, grupamento):
        self.resistencia = 150
        self.ataque = 250
        super().__init__(nome, grupamento, self.resistencia, self.ataque)


class SoldadoElite(NPC):
    # este "filho" construtor sobrepõe o contronstrutor da superclass "pai"
    def __init__(self, nome, grupamento):
        self.resistencia = 400
        self.ataque = 860
        super().__init__(nome, grupamento, self.resistencia, self.ataque)
