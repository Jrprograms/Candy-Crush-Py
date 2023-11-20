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
                    EstadoSalvo = GAME.carregarEstado(PLAYER)
                    if(EstadoSalvo):
                        # print(PLAYER.estadoLayout)
                        TELA.setDoces(PLAYER.estadoLayout)
                    else:
                        TELA.setDoces()
                        TELA.divdSeq()
            else:
                print(event.pos)
                for doce in TELA.layout:
                    if(doce.obj.collidepoint(event.pos)):
                        print(doce.obj.collidepoint(event.pos))
                        doces = PLAYER.selecionarDoce(doce)

                        #https://gist.github.com/ValmirNogFilho/945ce8f9ace05fe2aebdfef1f13bf45b
                        if doces:
                            doce1 = TELA.layout.index(doces[0])
                            doce2 = TELA.layout.index(doces[1])
                            

                            #Trocando os doces
                            TELA.swap(doce1,doce2)

                            #Trocar os doces no layout
                            TELA.atualizarLayout(doce1,doce2)

                            pontuacaoJogada = 0
                            for el in TELA.divdSeq(preView=True):
                                if doce1 == el or doce2 == el:
                                    #Verificar sequencias na tela
                                    pontuacaoJogada = TELA.divdSeq(first=True) 
                                    PLAYER.pontuacao += pontuacaoJogada
                                    
                            if pontuacaoJogada == 0:
                                #Reverte a troca dos doces
                                TELA.swap(doce1,doce2)

                                #Reverte a troca dos doces no layout
                                TELA.atualizarLayout(doce1,doce2)
                            else:
                                if(PLAYER.pontuacao + 1000 >= PLAYER.bonus):
                                    PLAYER.powerup += 1
                                    PLAYER.bonus += 1000

                            if(TELA.divdSeq(preView=True) == 0):
                                GAME.gameOver(TELA)



                           
                            


    TELA.tela.fill('white')
    TELA.desenharTela(PLAYER.pontuacao)

    #Funcionalidades
    pg.display.flip()


GAME.salvarEstado(PLAYER,TELA)
pg.quit()
