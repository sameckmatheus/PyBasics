import pygame
import sys

pygame.init()

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Meu Tamagotchi')

animacao_gif = pygame.image.load('assets/animacao.gif')
animacao_rect = animacao_gif.get_rect(center=(largura_tela // 2, altura_tela // 2))

cor_fundo = (255, 255, 255)
fonte = pygame.font.Font(None, 26)
fome = 50
felicidade = 50
energia = 50
opcoes = (f'Interaja com seu tamagotchi!\n'
          f'Digite (a) para alimentar.\n'
          f'Digite (b) para brincar.\n'
          f'Digite (d) para dormir.\n'
          f'Digite (s) para sair.')

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                fome -= 10
            elif evento.key == pygame.K_b:
                felicidade += 10
                fome += 10
            elif evento.key == pygame.K_d:
                energia += 10
                felicidade -= 5

    fome = max(0, min(fome, 100))
    felicidade = max(0, min(felicidade, 100))
    energia = max(0, min(energia, 100))

    if fome >= 100 or felicidade <= 0:
        mensagem = f"Seu Tamagotchi morreu!"
    else:
        mensagem = (f"Fome: {fome} / "
                    f"Felicidade: {felicidade} / "
                    f"Energia: {energia}"
                    f"{opcoes}")

    tela.fill(cor_fundo)
    tela.blit(animacao_gif, animacao_rect)

    texto = fonte.render(mensagem, True, (0, 0, 0))

    tela.blit(texto, (20, 20))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
