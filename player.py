import pygame as pg

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def drawPlayer(self, SF):
        self.PlayerRT = pg.draw.rect(SF, '#ff0000', (self.x, self.y, 40, 40))
        pg.draw.rect(SF, '#000000', (self.x, self.y, 40, 40), 6)
