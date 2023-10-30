import pygame as pg

class Doce():
    def __init__(self,tipo,pts,l,c,index):
        self.tipo = tipo  
        self.pontuacao = pts
        self.linha = l
        self.coluna = c
        self.index = index
        self.x = (50 * (self.coluna + 1)) + 45
        self.y = 35 * (self.linha + 1 )
        self.obj = pg.Rect((self.x,self.y,30,30))
        self.imagem = tipo
        self.borda = False

        self.setTipo()

    def __repr__(self) -> str:
        return f"<tipo:{self.tipo}, pont:{self.pontuacao}, linha:{self.linha}, coluna:{self.coluna}>\n"
    
    #Definir cor do doce
    def setTipo(self):
        imagens = {
            0 : "src/1.png",
            1 : "src/2.png",
            2 : "src/3.png",
            3 : (150,150,0),
            4 : (255,0,255)
        }
        for imagem in imagens:
            if imagem == self.imagem:
                self.imagem = pg.image.load(imagens[imagem])

    #desenhar o doce na tela
    def draw(self,tela):
        self.drawBorda(tela)
        self.x = (50 * (self.coluna + 1)) + 45
        self.y = 35 * (self.linha + 1 )
        self.obj = pg.Rect((self.x,self.y,30,30))
        # pg.draw.rect(tela,self.cor,(self.x,self.y,30,30))
        return [self.imagem,(self.x,self.y)]
    
    #Borda de quando o doce está selecionado
    def addBorda(self,ativo):
        self.borda = ativo

    #Desenhar Borda no Doce
    def drawBorda(self,tela):
        if(self.borda):
            pg.draw.rect(tela,(0,0,0),(self.x - 5,self.y - 5, 40 ,40))