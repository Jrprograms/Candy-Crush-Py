import pygame as pg
import math, random

templates = {
    "home" : [
        [(255,0,0),(20,20,100,100)] , [(255,125,100),(50,50,300,300)]
    ]
}

class Game:
    def __init__(self) -> None:
        self.largura = 600
        self.altura = 400
        self.tela = pg.display.set_mode((self.largura, self.altura))
        self.clock = pg.time.Clock()
        self.backgroundColor = (0,0,200)
        self.lvl = 0
        pg.display.set_caption('Candy Crush')

    #Pintar a tela
    def fill(self,cor):
        return self.tela.fill(cor)

    #Desenhar retangulo na tela
    def rect(self,template):
        for i in range(len(templates[template])):
            pg.draw.rect(self.tela,templates['home'][i][0],templates['home'][i][1])
    
    #Escrever texto na tela
    def txt(self,texto):
        font = pg.font.get_default_font()
        fontesys = pg.font.SysFont(font, 20)    
        txt = fontesys.render(texto, 1, (255,255,255))
        self.tela.blit(txt,(50,100))

    def setTela(self,index) -> None:
        if(index == 'home'):
            self.tela.fill('blue')
            self.rect('home')
            self.txt("teste")


class Telas:
    def __init__(self) -> None:
        self.index = ''
        self.cenario = []

    def gerarDoces(self) -> None:
        for i in range(3):
            linha = []
            for i in range(3):
                num = random.randint(0,1 * 100)
                linha.append(num)
            self.cenario.append(linha)
        



class Player():
    def __init__(self,nome = "Anonymous") -> None:
        self.nome = nome
        self.historico = []
        self.pontos = []