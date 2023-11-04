class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.felicidade = 50
        self.energia = 50

    def comer(self):
        self.fome -= 10

    def brincar(self):
        self.felicidade += 10

    def dormir(self):
        self.energia += 25


def interagir_com_usuario(tamagotchi):
    while True:
        print(f'\n{tamagotchi.nome} - Fome: {tamagotchi.fome}, '
              f'Felicidade: {tamagotchi.felicidade}, '
              f'Energia: {tamagotchi.energia}')
        print("O que você quer fazer?")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Dormir")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tamagotchi.comer()
        elif escolha == "2":
            tamagotchi.brincar()
        elif escolha == "3":
            tamagotchi.dormir()
        elif escolha == "4":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
