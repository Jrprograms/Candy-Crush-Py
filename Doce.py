import pygame as pg

class Doce():
    def __init__(self,cor,pts,l,c):
        self.cor = cor  
        self.pontuacao = pts
        self.linha = l
        self.coluna = c
        self.x = (50 * (self.coluna + 1)) + 45
        self.y = 35 * (self.linha + 1 )
        self.obj = pg.Rect((self.x,self.y,30,30))
        self.imagem = cor

        self.setTipo()

    def __repr__(self) -> str:
        return f"<cor:{self.cor}, pont:{self.pontuacao}, linha:{self.linha}, coluna:{self.coluna}>\n"
    
    #Definir cor do doce
    def setTipo(self):
        imagens = {
            0 : "src/teste.png",
            1 : "src/teste2.png",
            2 : (0,0,255),
            3 : (150,150,0),
            4 : (255,0,255)
        }
        for imagem in imagens:
            if imagem == self.imagem:
                self.imagem = pg.image.load(imagens[imagem])

    def draw(self,tela):
        self.x = (50 * (self.coluna + 1)) + 45
        self.y = 35 * (self.linha + 1 )
        self.obj = pg.Rect((self.x,self.y,30,30))
        # pg.draw.rect(tela,self.cor,(self.x,self.y,30,30))
        return [self.imagem,(self.x,self.y)]