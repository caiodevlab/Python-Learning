import pygame

pygame.init()
#janela
largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
#cor de fundo
tela.fill((255, 255, 255))
pygame.display.set_caption("Jogo de Física")

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        pygame.display.update()

pygame.quit()