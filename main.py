import pygame as pg
import Doce, Tela, Player, Game


pg.init()
pg.font.init()

#Cria uma instância de cada classe
PLAYER = Player.Player()
TELA = Tela.Tela()
GAME = Game.Game()

running = True

while running:
    #Leitor de Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    
        elif event.type == pg.MOUSEBUTTONDOWN:
            if TELA.botaoHome:
                if TELA.botaoHome.collidepoint(event.pos):
                    TELA.botaoHome = None
                    TELA.background = pg.image.load("Game.png")
                    TELA.index = 'game'
                    TELA.setDoces()
            else:
                for doce in TELA.layout:
                    if(doce.obj.collidepoint(event.pos)):
                        #print(doce)
                        doces = PLAYER.selecionarDoce(doce)
                        
                        if doces:
                            doce1 = TELA.layout.index(doces[0])
                            doce2 = TELA.layout.index(doces[1])
                            #Trocando os doces
                            TELA.layout[doce1].x,TELA.layout[doce2].x = TELA.layout[doce2].x,TELA.layout[doce1].x
                            TELA.layout[doce1].y,TELA.layout[doce2].y = TELA.layout[doce2].y,TELA.layout[doce1].y
                            TELA.layout[doce1].coluna,TELA.layout[doce2].coluna = TELA.layout[doce2].coluna,TELA.layout[doce1].coluna
                            TELA.layout[doce1].linha,TELA.layout[doce2].linha = TELA.layout[doce2].linha,TELA.layout[doce1].linha
                            TELA.layout[doce1].obj = TELA.layout[doce2].obj

                            TELA.layout[doce1] = doces[1]
                            TELA.layout[doce2] = doces[0]



    TELA.tela.fill('white')
    TELA.desenharTela()

    #Funcionalidades
    pg.display.flip()

pg.quit()

