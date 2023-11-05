import pygame
import sys


pygame.init()

largura_tela, altura_tela = 700, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Meu Tamagotchi')

animacao_gif = pygame.image.load('assets/duck.gif')

largura_nova, altura_nova = 400, 400
animacao_gif = pygame.transform.scale(animacao_gif, (largura_nova, altura_nova))

animacao_rect = animacao_gif.get_rect(center=(largura_tela // 1.6, altura_tela // 1.7))

cor_fundo = (61, 235, 158)
fonte = pygame.font.Font(None, 26)
fome = 50
felicidade = 50
energia = 50

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                fome -= 5
            elif evento.key == pygame.K_b:
                felicidade += 5
                fome += 5
                energia -= 5
            elif evento.key == pygame.K_d:
                energia += 5
                felicidade -= 5
            elif evento.key == pygame.K_s:
                quit()

    fome = max(0, min(fome, 100))
    felicidade = max(0, min(felicidade, 100))
    energia = max(0, min(energia, 100))

    if fome >= 100 or felicidade <= 0:
        mensagem = f"Seu Tamagotchi morreu!"
    else:
        boas_vindas = f"Interaja com seu tamagotchi!"

        mensagem = (f"Fome: {fome} / "
                    f"Felicidade: {felicidade} / "
                    f"Energia: {energia}")

        opcao1 = "Digite (a) para alimentar."
        opcao2 = "Digite (b) para brincar."
        opcao3 = "Digite (d) para dormir."
        opcao4 = "Digite (s) para sair."

    tela.fill(cor_fundo)
    tela.blit(animacao_gif, animacao_rect)

    bv = fonte.render(boas_vindas, True, (17, 87, 62))
    tela.blit(bv, (20, 10))

    texto = fonte.render(mensagem, True, (17, 87, 62))
    tela.blit(texto, (20, 40))

    user_op1 = fonte.render(opcao1, True, (17, 87, 62))
    tela.blit(user_op1, (20, 70))
    user_op2 = fonte.render(opcao2, True, (17, 87, 62))
    tela.blit(user_op2, (20, 100))
    user_op3 = fonte.render(opcao3, True, (17, 87, 62))
    tela.blit(user_op3, (20, 130))
    user_op4 = fonte.render(opcao4, True, (17, 87, 62))
    tela.blit(user_op4, (20, 160))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
