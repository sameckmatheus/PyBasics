from moviepy.editor import VideoFileClip
import pygame
import sys

pygame.init()

# Configurações da tela
largura_tela, altura_tela = 800, 600
tela_pygame = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Tamagotchi')

# Caminho para o arquivo GIF
caminho_gif = 'assets/animacao.gif'

# Carregando o GIF usando o MoviePy
clip = VideoFileClip(caminho_gif, audio=False)
clip.preview(fps=30)  # Pré-visualiza o GIF para determinar as dimensões

# Configurações da animação
relogio = pygame.time.Clock()


def animar_tamagotchi(tela):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Obtém um frame do GIF
        frame = clip.get_frame(tela.get_time() / 10000)

        # Converte o frame para o formato Pygame Surface
        frame_surface = pygame.image.fromstring(frame.tobytes(), clip.size, clip.size, 'RGB')

        # Desenha o frame na tela
        tela.fill((255, 255, 255))  # Fundo branco
        tela.blit(frame_surface, (largura_tela // 2 - clip.size[0] // 2, altura_tela // 2 - clip.size[1] // 2))

        # Atualiza a tela
        pygame.display.flip()

        # Limita a taxa de quadros por segundo (FPS)
        relogio.tick(30)


# Chama a função de animação
animar_tamagotchi(tela_pygame)
