import pygame as pg

class Game():
    def __init__(self):
        self.largura = 500
        self.altura = 650
        self.background = pg.image.load("Home.png")
        pg.display.set_caption('Candy Crush')
