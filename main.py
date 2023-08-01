import pygame as pg
import funcoes


pg.init()
pg.font.init()

#Cria uma instância do jogo e tela
GAME = funcoes.Game()
TELA = funcoes.Telas()

#Tela selecionada
telaAtual = 'home'

running = True

while running:
    #Leitor de Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    GAME.fill('white')

    GAME.setTela(telaAtual)

    #Funcionalidades
    pg.display.flip()
    GAME.clock.tick(60)

pg.quit()


