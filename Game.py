import pygame as pg
import pickle

from Player import Player
from Tela import Tela
from Doce import Doce

class Game():
    def __init__(self):
        self.largura = 500
        self.altura = 650
        self.background = pg.image.load("Home.png")
        pg.display.set_caption('Candy Crush')

    def salvarEstado(self, player:Player = None, tela: Tela = None):
        with open("./src/data.txt","w") as file:
            file.writelines([f"historico :{player.historico}\n",
                             f"pontosAtual :{player.pontuacao}\n"
                            ])
        
        with open("./src/dataLayout.javaebom","wb") as file:
            lista = []
            for el in tela.layout:
                lista.append([el.tipo,el.linha,el.coluna])
            pickle.dump(lista,file)

    def carregarEstado(self, player : Player = None):
        with open("./src/data.txt","r") as file:
            lines = file.readlines()
            for index,line in enumerate(lines):
                print(line)
                line = line.split(":")
                line[1] = (line[1])[:len(line[1])-1]
                lines[index] = line[1]

            if(lines[1] == "0"):
                return False
            else:
                player.historico = eval(lines[0])
                player.pontuacao = eval(lines[1])
                
            
        with open("./src/dataLayout.javaebom","rb") as file:

            data = pickle.load(file)
            player.estadoLayout = data
            return True
        
    def gameOver(tela:Tela):
        print('Game Over')
        tela.setDoces()
        tela.divdSeq()

# PlayerTeste = Player()
# teste = Game()
# PlayerTeste.estadoLayout = [[1,2,3,4],[4,3,2,1]]
# PlayerTeste.pontuacao = 1234
# teste.salvarEstado(PlayerTeste)
# teste.carregarEstado(PlayerTeste)
# print(PlayerTeste)
# print((PlayerTeste.estadoLayout))