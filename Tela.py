import pygame as pg
from Doce import Doce
import random
    
class Tela():
    def __init__(self):
        self.largura = 500
        self.altura = 650
        self.layout = []
        self.tela = pg.display.set_mode((self.largura, self.altura))
        self.index = 'home'
        self.background = pg.image.load("Home.png")
        self.botaoHome = pg.Rect(145,463.5,200,55)

    #Escrever texto na tela
    def setTxt(self,texto):
        font = pg.font.get_default_font()
        fontesys = pg.font.SysFont(font, 20)    
        txt = fontesys.render(texto, 1, (255,255,255))
        self.txt = txt.get_rect(topleft=(235,493.5))
        self.tela.blit(txt,(235,493.5))

    def desenharTela(self):
        if(self.index == 'home'):
            self.tela.blit(self.background,(0,0))
            self.setTxt("PLAY")
            
        elif(self.index == 'game'):
            self.tela.blit(self.background,(0,0))
            for doce in self.layout:
                doce.draw(self.tela)
                

    #Definir doces do layout
    def setDoces(self):
        for i in range(6):
            for j in range(6):
                cor = random.randint(0,4)
                pontuacao = random.randint(2,5) * 10
                doce = Doce(cor,pontuacao, i, j)
                self.layout.append(doce)