import pygame as pg
import os


class Player():
    def __init__(self, nome="Anonymous"):
        self.nome = nome
        self.historico = [] #Antigas Pontuações
        self.pontuacao = 0
        self.bonus = 0 #Bonus de power-up
        self.powerup = 0
        self.estadoLayout = []
        self.selecionado = []

    def __repr__(self) -> str:
        return f"Nome:{self.nome}, Historico:{self.historico}, pont:{self.pontuacao}, estado:{self.estadoLayout}"

    def selecionarDoce(self, doce):
        # print(self.selecionado)
        self.selecionado.append(doce)

        if len(self.selecionado) == 1:
            doce.addBorda(True)
            print(doce)
            pass

        elif len(self.selecionado) == 2:

            self.selecionado[0].addBorda(False)

            if self.selecionado[0] == doce:
                self.selecionado = []
                print('Igual')
                return False

            doces = self.selecionado
            self.selecionado = []
            if doces[0].linha == doces[1].linha:
                if doces[0].coluna == doces[1].coluna + 1 or doces[0].coluna == doces[1].coluna - 1:
                    return doces

            elif doces[0].coluna == doces[1].coluna:
                if doces[0].linha == doces[1].linha + 1 or doces[0].linha == doces[1].linha - 1:
                    return doces

            self.selecionado = []
            return False
        else:
            return False
