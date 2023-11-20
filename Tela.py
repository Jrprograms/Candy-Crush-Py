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
        self.pontAcumulada = 0  #Guardar a pontuação gerada pela quebra da sequencia dos doces

    #Escrever texto na tela
    def setTxt(self,texto, pos):
        font = pg.font.get_default_font()
        fontesys = pg.font.SysFont(font, 20)    
        txt = fontesys.render(texto, 1, (255,255,255))
        self.txt = txt.get_rect(topleft=pos)
        self.tela.blit(txt,pos)

    #Desenhar cabeçalho na tela
    def header(self,pontos):
        pg.draw.rect(self.tela,(255,0,152),(0,0,500,60))
        self.setTxt(f"Pontos {pontos}", (205,25))

    def desenharTela(self,pontos = 0):
        if(self.index == 'home'):
            self.tela.blit(self.background,(0,0))
            self.setTxt("PLAY",(235,493.5))
            
        elif(self.index == 'game'):
            self.tela.blit(self.background,(0,0))
            self.header(pontos)
            for doce in self.layout:
                imagem = doce.draw(self.tela)
                self.tela.blit(imagem[0],imagem[1])
                
    def novoDoce(self,i,j,index,tipo = "novo"):
        if tipo == "novo": tipo = random.randint(1,5) 
        pontuacao = tipo * 10
        return Doce(tipo,pontuacao, i, j,index)

    #Definir doces do layout
    def setDoces(self,ESTADO = None):
        contadora = 0
        if ESTADO == None:
            for i in range(6):
                for j in range(6):
                    tipo = random.randint(1,5)
                    pontuacao = tipo * 10
                    doce = Doce(tipo,pontuacao, i, j,contadora)
                    contadora += 1
                    self.layout.append(doce)
        else:
            for index,doce in enumerate(ESTADO):
                t,l,c = doce
                self.layout.append(Doce(t,t * 10,l,c,index))


    def atualizarLayout(self,indexDoce1,indexDoce2):
        self.layout[indexDoce1],self.layout[indexDoce2] = self.layout[indexDoce2],self.layout[indexDoce1]
    
    #Funcao para trocar dois doces
    def swap(self,doce1,doce2):
        self.layout[doce1].coluna,self.layout[doce2].coluna = self.layout[doce2].coluna,self.layout[doce1].coluna
        self.layout[doce1].linha,self.layout[doce2].linha = self.layout[doce2].linha,self.layout[doce1].linha
        self.layout[doce1].index ,self.layout[doce2].index = self.layout[doce2].index,self.layout[doce1].index

    #Dividir minha lista como uma matriz e verifica as sequencias
    def divdSeq(self, preView = False, first= False):
        lista_Exclusao = []

        if first:
            self.pontAcumulada = 0

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


        if preView == True:
            print(self.pontAcumulada)
            return lista_Exclusao

        if len(lista_Exclusao) > 0:
            print("Passou aqui")
            self.excluirDoces(lista_Exclusao)
            self.verificarLista()
            

        return self.pontAcumulada    
        


    def excluirDoces(self,lista):
        for el in lista:
            self.layout[el].tipo = "fantasma"
            self.pontAcumulada += self.layout[el].pontuacao

    #Organiza os doces na tela novamente
    def verificarLista(self):
        for i in range(6):
            lista = []
            for j in range(6):
                doce = self.layout[j * 6 + i]
                lista.append(doce)

            self.bubbleSort(lista)  

            #Aqui o x,y está calculado erradamente
            for j in range(6):
                if lista[j].tipo == "fantasma":
                    lista[j] = self.novoDoce(j,i,lista[j].index)
                else:
                    lista[j] = self.novoDoce(j,i,lista[j].index,lista[j].tipo)

            for j in range(6):
                self.layout[j * 6 + i] = lista[j]

        self.divdSeq()


    def bubbleSort(self,alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i+1].tipo == "fantasma":
                    alist[i],alist[i+1] = alist[i+1],alist[i]
                    #alist[i].y,alist[i+1].y = alist[i+1].y,alist[i].y

    #Verificar as sequencias do layout
    def verfiqSeq(self,linha):
        anterior = None
        contadora = 1
        pos_inicial = 0
        pos_final = 0

        for index,doce in enumerate(linha):
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

    def retornarPontuacao(self,pontuacao):
        print(pontuacao)

# teste = Tela()
# teste.setDoces()
# pontos = teste.divdSeq(first=True)
# print(pontos)
# print("*" * 15)
# pontos2 = teste.divdSeq(first=True)
# print(pontos2)