import pygame as pg
import random
from pygame.locals import *

# essa função cria um ponto coordenado entre 0 e 59. 
# Usaremos o truque do //10*10 para o arredondamento.
# como a tela terá 600 pixels, vamos até o tile 59 porque cada tile tem 10 pixels.
def lugarRandom():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

# detecta colisões meramente comparando as tuplas.
def detectaColisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#TODO: fazer uma consequência de colisão melhor.
def reInicializa():
    pg.quit()

# essas serão as direções que a "cobrinha" pode se mover.
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# inicializando a tela vazia.
pg.init()
tela = pg.display.set_mode((600,600))
pg.display.set_caption("Snake Game no Python")

# inicializa o relógio do jogo.
relogio = pg.time.Clock()

# cria a cobrinha, com três pedaços no corpo, cada um em uma tupla coordenada adjacente 
# snake skin, o tile que compõe a cobrinha, será um quadrado (surface, do pygame), 
# de 10 por 10 e preenchido com branco. Em cada tupla coordenada esse quadrado será desenhado.
cobra = [(200, 200), (210, 200), (220, 200)]
cobra_skin = pg.Surface((10, 10))
cobra_skin.fill((255,255,255))

# cria a maçã, no mesmo esquema
maca_pos = lugarRandom()
maca = pg.Surface((10,10))
maca.fill((255,0,0))

# define uma direção inicial
direcao = RIGHT

while True:
    # o tick modera a velocidade.
    velocidade = 20 
    relogio.tick(velocidade)
    
    # classificador de eventos.
    for event in pg.event.get():

        # quit do gerenciador.
        if event.type == QUIT:
            pg.quit()
        
        # detecta os eventos de pressionar de teclas.
        if event.type == KEYDOWN:

            # controle direcional
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_LEFT:
                direcao = LEFT
            if event.key == K_RIGHT:
                direcao = RIGHT
            
            # dá quit pelo teclado
            if event.key == K_ESCAPE: 
                pg.quit()
            
    # esse evento coloca um segmento no final da cobra, quando ela pega a maçã.        
    if detectaColisao(cobra[0], maca_pos):
        maca_pos = lugarRandom()
        cobra.append((0,0))

    #detecta colisão com o fim da tela
    if cobra[0][0]<0 or cobra[0][0]>590 or cobra[0][1]<0 or cobra[0][1]>590:
        reInicializa()                

    # muda a direção de movimento da cobra baseado no evento de input.
    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] -10, cobra[0][1])
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

    # isso faz a cobra "andar": dá, a cada i da cobra, a posição do i anterior.
    for i in range(len(cobra) -1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    # renderiza tudo de novo, menos a cobra.
    tela.fill((0,0,0))
    tela.blit(maca, maca_pos)

    # renderiza a cobra, segmento por segmento.
    for pos in cobra:
        tela.blit(cobra_skin, pos)
        tela

    pg.display.update()