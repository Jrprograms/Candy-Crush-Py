import pygame as pg
import os

class Player():
    def __init__(self,nome = "Anonymous"):
        self.nome = nome
        self.historico = {
            "vitorias": [],
            "derrotas": []
        }
        self.pontuacao = 0
        self.selecionado = []

    def selecionarDoce(self,doce):
        # print(self.selecionado)
        self.selecionado.append(doce)

        if len(self.selecionado) == 2:
            if self.selecionado[0] == doce:
                self.selecionado = []
                print('Igual')
                return False

            doces = self.selecionado
            self.selecionado = []
            if doces[0].linha == doces[1].linha:
                if doces[0].coluna == doces[1].coluna + 1 or doces[0].coluna == doces[1].coluna - 1:
                    print('Pode trocar 1')
                    return doces

            elif doces[0].coluna == doces[1].coluna:
                if doces[0].linha == doces[1].linha + 1 or doces[0].linha == doces[1].linha - 1:
                    print('Pode trocar')
                    return doces
                
            self.selecionado = []
            return False
        else:
            return False

                    

        

        
            
            