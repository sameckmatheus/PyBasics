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
              f'Vivo.........: {'Sim' if self.vivo else "Não"}\n'  # operador ternário
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


npc_1 = Guarda('SnakeEyes', str('Thunderbolt-9'))
npc_1.informacoes()

npc_2 = Soldado('IronHands', str('Thunderbolt-9'))
npc_2.informacoes()

npc_3 = SoldadoElite('Shadow', str('Thunderbolt-9'))
npc_3.informacoes()

npc_4 = Guarda('LowLight', str('Hellcat'))
npc_4.informacoes()

npc_5 = Soldado('OnePunch', str('Hellcat'))
npc_5.informacoes()

npc_6 = SoldadoElite('SilenceMelody', str('Hellcat'))
npc_6.informacoes()
