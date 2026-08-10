import pygame
import sys
import random

pygame.init()

# ==========================================
# CONFIGURAÇÕES
# ==========================================
LINHAS = 6
COLUNAS = 6
TAMANHO_BLOCO = 140

LARGURA = COLUNAS * TAMANHO_BLOCO
ALTURA = LINHAS * TAMANHO_BLOCO

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Guerra do Contestado")

fonte = pygame.font.SysFont("arial", 32)

# ==========================================
# IMAGENS
# ==========================================
img_fundo = pygame.transform.scale(
    pygame.image.load("Aprendizado.py/Jogo/Exemplo/Images/Fundo.png"),
    (LARGURA, ALTURA)
)

tamanho_p = TAMANHO_BLOCO - 20

img_tropa_rep = pygame.transform.scale(
    pygame.image.load("Aprendizado.py/Jogo/Exemplo/Images/Republica.png"),
    (tamanho_p, tamanho_p)
)

img_cmdt_rep = pygame.transform.scale(
    pygame.image.load("Aprendizado.py/Jogo/Exemplo/Images/Presidente.png"),
    (tamanho_p, tamanho_p)
)

img_tropa_cont = pygame.transform.scale(
    pygame.image.load("Aprendizado.py/Jogo/Exemplo/Images/Contestado.png"),
    (tamanho_p, tamanho_p)
)

img_cmdt_cont = pygame.transform.scale(
    pygame.image.load("Aprendizado.py/Jogo/Exemplo/Images/JoaoMaria.png"),
    (tamanho_p, tamanho_p)
)


# MATRIZ DO JOGO
# 0 = vazio
# 1 = tropa república
# 2 = presidente
# 3 = tropa contestado
# 4 = joão maria

matriz_jogo = [
    [1, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 3]
]


# POSIÇÕES

tropa_rep_lin = 0
tropa_rep_col = 0

tropa_cont_lin = 5
tropa_cont_col = 5

joao_lin = 4
joao_col = 5


# VIDA

vida_jogador = 3
vida_joao = 5


# TABULEIRO

vidro_tabuleiro = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):

        if (linha + coluna) % 2 == 0:
            cor = (240, 217, 181, 100)
        else:
            cor = (181, 136, 99, 100)

        x = coluna * TAMANHO_BLOCO
        y = linha * TAMANHO_BLOCO

        pygame.draw.rect(
            vidro_tabuleiro,
            cor,
            (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)
        )

        pygame.draw.rect(
            vidro_tabuleiro,
            (50, 50, 50, 200),
            (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO),
            1
        )


# FUNÇÕES

def desenhar_texto(texto, x, y, cor=(255,255,255)):
    render = fonte.render(texto, True, cor)
    tela.blit(render, (x, y))


def inimigo_perto():
    global tropa_rep_lin
    global tropa_rep_col
    global joao_lin
    global joao_col

    if abs(tropa_rep_lin - joao_lin) <= 1 and abs(tropa_rep_col - joao_col) <= 1:
        return True

    return False


def mover_inimigo():
    global tropa_cont_lin
    global tropa_cont_col

    matriz_jogo[tropa_cont_lin][tropa_cont_col] = 0

    # IA simples
    direcoes = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    random.shuffle(direcoes)

    for dlin, dcol in direcoes:

        nova_lin = tropa_cont_lin + dlin
        nova_col = tropa_cont_col + dcol

        if 0 <= nova_lin < LINHAS and 0 <= nova_col < COLUNAS:

            if matriz_jogo[nova_lin][nova_col] == 0:

                tropa_cont_lin = nova_lin
                tropa_cont_col = nova_col
                break

    matriz_jogo[tropa_cont_lin][tropa_cont_col] = 3



# LOOP

rodando = True

while rodando:

    tela.blit(img_fundo, (0, 0))
    tela.blit(vidro_tabuleiro, (0, 0))

    
    # EVENTOS
    
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            nova_lin = tropa_rep_lin
            nova_col = tropa_rep_col

            # MOVIMENTO
            if evento.key == pygame.K_RIGHT:
                nova_col += 1

            elif evento.key == pygame.K_LEFT:
                nova_col -= 1

            elif evento.key == pygame.K_DOWN:
                nova_lin += 1

            elif evento.key == pygame.K_UP:
                nova_lin -= 1

            # ATAQUE
            elif evento.key == pygame.K_SPACE:

                if inimigo_perto():
                    vida_joao -= 1
                    print("João Maria levou dano!")

                if vida_joao <= 0:
                    print("Vitória da República!")
                    rodando = False

            # VALIDAÇÃO MOVIMENTO
            if 0 <= nova_lin < LINHAS and 0 <= nova_col < COLUNAS:

                if matriz_jogo[nova_lin][nova_col] == 0:

                    matriz_jogo[tropa_rep_lin][tropa_rep_col] = 0

                    matriz_jogo[nova_lin][nova_col] = 1

                    tropa_rep_lin = nova_lin
                    tropa_rep_col = nova_col

                    # turno do inimigo
                    mover_inimigo()

    
    # ATAQUE INIMIGO
    
    if abs(tropa_rep_lin - tropa_cont_lin) <= 1 and abs(tropa_rep_col - tropa_cont_col) <= 1:

        vida_jogador -= 0.002

    
    # DERROTA
    
    if vida_jogador <= 0:
        print("Você perdeu!")
        rodando = False

    
    # DESENHAR PERSONAGENS
    
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):

            valor = matriz_jogo[linha][coluna]

            if valor != 0:

                pos_x = (coluna * TAMANHO_BLOCO) + 10
                pos_y = (linha * TAMANHO_BLOCO) + 10

                if valor == 1:
                    tela.blit(img_tropa_rep, (pos_x, pos_y))

                elif valor == 2:
                    tela.blit(img_cmdt_rep, (pos_x, pos_y))

                elif valor == 3:
                    tela.blit(img_tropa_cont, (pos_x, pos_y))

                elif valor == 4:
                    tela.blit(img_cmdt_cont, (pos_x, pos_y))

    
    # HUD
    
    desenhar_texto(f"Vida: {int(vida_jogador)}", 20, 20)

    desenhar_texto(
        f"João Maria: {vida_joao}",
        20,
        60
    )

    
    # ATUALIZAÇÃO
    
    pygame.display.flip()

pygame.quit()
sys.exit()