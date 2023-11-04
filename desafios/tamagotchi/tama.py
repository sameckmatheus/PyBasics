import sys
import pygame
from pygame.locals import QUIT
from game_animation import animar_tamagotchi


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


pygame.init()

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tamagotchi')

while True:
    def interagir_com_usuario(tamagotchi):
        while True:
            print(f'Tamagotchi - {tamagotchi.nome}:\n'
                  f'Fome: {tamagotchi.fome}\n'
                  f'Felicidade: {tamagotchi.felicidade}\n'
                  f'Energia: {tamagotchi.energia}\n')
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

    # Eventos do Pygame
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Chama a função de animação
    animar_tamagotchi(tela)
