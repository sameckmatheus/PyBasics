class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'O {self.nome} está comendo.')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f'O {self.nome} está miando.')


gato = Gato('Jonas', 'Rosa')
gato.miar()
gato.comer()
