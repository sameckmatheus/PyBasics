import pygame
from moviepy.editor import VideoFileClip
import sys

pygame.init()

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tamagotchi')

caminho_gif = 'assets/animacao.gif'

clip = VideoFileClip(caminho_gif, audio=False)
relogio = pygame.time.Clock()


def animar_tamagotchi():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        tempo_entre_frames = 1000 / 60

        frame = clip.get_frame(tela.get_time() / 1000)

        frame_surface = pygame.image.fromstring(frame.tobytes(), clip.size, 'RGB')

        tela.fill((255, 255, 255))
        tela.blit(frame_surface, (largura_tela // 2 - clip.size[0] // 2, altura_tela // 2 - clip.size[1] // 2))

        pygame.display.flip()

        relogio.tick_busy_loop(60)

    pygame.quit()
    sys.exit()


animar_tamagotchi()
