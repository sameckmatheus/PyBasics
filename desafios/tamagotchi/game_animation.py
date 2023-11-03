import pygame
import sys

pygame.init()

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tamagotchi')

frames = []
for i in range(1, 9):
    frame = pygame.image.load(f'assets/frames/frame{i}.png')
    frames.append(frame)

indice_frame = 0
FPS = 20
relogio = pygame.time.Clock()

def animar_tamagotchi(tela):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        indice_frame = (indice_frame + 1) % len(frames)

        tela.fill((255, 255, 255))
        tela.blit(frames[indice_frame], (largura_tela // 2 - frames[indice_frame].get_width() // 2,
                                         altura_tela // 2 - frames[indice_frame].get_height() // 2))

        pygame.display.flip()

        relogio.tick(FPS)
