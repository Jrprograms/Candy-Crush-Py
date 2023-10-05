import pygame as pg

class Doce():
    def __init__(self,cor,pts,l,c):
        self.cor = cor  
        self.pontuacao = pts
        self.linha = l
        self.coluna = c
        self.x = (50 * (c + 1)) + 45
        self.y = 35 * (l + 1 )
        self.obj = pg.Rect((self.x,self.y,30,30))

        self.setCor()

    def __repr__(self) -> str:
        return f"<cor:{self.cor}, pont:{self.pontuacao}, linha:{self.linha}, coluna:{self.coluna}>\n"
    
    #Definir cor do doce
    def setCor(self):
        cores = {
            0 : (255,0,0),
            1 : (0,255,0),
            2 : (0,0,255),
            3 : (150,150,0),
            4 : (255,0,255)
        }
        for cor in cores:
            if cor == self.cor:
                self.cor = cores[cor]

    def draw(self,tela):
        pg.draw.rect(tela,self.cor,(self.x,self.y,30,30))