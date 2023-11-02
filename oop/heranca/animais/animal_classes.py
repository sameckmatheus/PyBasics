class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'O(A) {self.nome} está comendo.')

    def emitir_som(self):
        print(f'O {self.nome} está emitindo o som correspondente.')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f'Gato {self.nome} está miando.')


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f'Cachorro {self.nome} está latindo.')


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f'Coelho {self.nome} está ronrronando.')


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f'Vaca {self.nome} está mugindo.')
