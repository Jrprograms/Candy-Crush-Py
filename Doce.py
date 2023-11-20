import pygame as pg

TAMANHO_IMG = 50

class Doce():
    def __init__(self,tipo,pts,l,c,index):
        self.tipo = tipo  
        self.pontuacao = pts
        self.linha = l
        self.coluna = c
        self.index = index
        self.x = (60 * (self.coluna + 1)) + 15
        self.y = 55 * (self.linha + 1 ) + 85
        self.obj = pg.Rect((self.x,self.y,TAMANHO_IMG,TAMANHO_IMG))
        self.imagem = tipo
        self.borda = False

        self.setTipo()

    def __repr__(self) -> str:
        return f"[{self.tipo},{self.pontuacao},{self.linha},{self.coluna},{self.index}]"
    
    #Definir cor do doce
    def setTipo(self):
        self.imagem = pg.image.load(f"src/D{self.tipo}.png")
        self.imagem =  pg.transform.scale(self.imagem, (TAMANHO_IMG, TAMANHO_IMG))

    #desenhar o doce na tela
    def draw(self,tela):
        self.drawBorda(tela)
        self.x = (60 * (self.coluna + 1)) + 15
        self.y = 55 * (self.linha + 1 ) + 85
        self.obj = pg.Rect((self.x,self.y,TAMANHO_IMG,TAMANHO_IMG))
        self.imagem = pg.image.load(f"src/D{self.tipo}.png")
        self.imagem =  pg.transform.scale(self.imagem, (TAMANHO_IMG, TAMANHO_IMG))
        # pg.draw.rect(tela,self.cor,(self.x,self.y,30,30))
        return [self.imagem,(self.x,self.y)]
    
    #Borda de quando o doce está selecionado
    def addBorda(self,ativo):
        self.borda = ativo

    #Desenhar Borda no Doce
    def drawBorda(self,tela):
        if(self.borda):
            pg.draw.rect(tela,(0,0,0),(self.x - 5,self.y - 5, 40 ,40))