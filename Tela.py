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
                imagem = doce.draw(self.tela)
                self.tela.blit(imagem[0],imagem[1])
                

    #Definir doces do layout
    def setDoces(self):
        contadora = 0
        for i in range(6):
            for j in range(6):
                tipo = random.randint(0,2)
                pontuacao = random.randint(2,5) * 10
                doce = Doce(tipo,pontuacao, i, j,contadora)
                contadora += 1
                self.layout.append(doce)

    def atualizarLayout(self,indexDoce1,indexDoce2):
        self.layout[indexDoce1],self.layout[indexDoce2] = self.layout[indexDoce2],self.layout[indexDoce1]
    
    def divdSeq(self):
        lista_Exclusao = []

        #Dividir as colunas do layout
        linhas = [[],[],[],[],[],[]]
        colunas = [[],[],[],[],[],[]]
        for doce in self.layout:
            linhas[doce.linha].append(doce)
            colunas[doce.coluna].append(doce)

        for i in range(6):
            posicoesLinha = self.verfiqSeq(linhas[i])
            posicoesColuna = self.verfiqSeq(colunas[i])
            if(posicoesLinha != -1):
                for j in range(posicoesLinha[0],posicoesLinha[1] + 1):
                    lista_Exclusao.append(j + (6 * i))
            
            if posicoesColuna != -1:
                for j in range(posicoesColuna[0],posicoesColuna[1] + 1):
                    lista_Exclusao.append((j * 6) + i)

        
        print(lista_Exclusao)

            #Verificar Linha
            #[0,1,1,1,2,3] => [1,3] => 1,2,3 * i 
            #[0,1,2,2,2,4] => [2,4] => 2,3,4 + (6 * i)

            #verificar Coluna
            #[0,1,1,1,2,3] => [1,3] => 1 * 6 + i
            #[0,1,2,2,2,4] => [2,4] => 2 + 

    def verfiqSeq(self,linha):
        anterior = None
        contadora = 1
        pos_inicial = 0
        pos_final = 0

        for index,doce in enumerate(linha):
            print(doce)
            if contadora == 1:
                pos_inicial = index
            if doce.tipo == anterior:
                contadora += 1
            else:
                if contadora >= 3:
                    pos_final = pos_inicial + contadora - 1
                    return [pos_inicial -1,pos_final-1]
                else:
                    contadora = 1

            anterior = doce.tipo
        if contadora >= 3:
            pos_final = pos_inicial + contadora - 1
            return [pos_inicial - 1,pos_final - 1]

        return -1