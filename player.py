import pygame as pg

playerSpawn = [
    (150+5, 300+5)
]

class Player:
    def __init__(self, coords):
        self.coords = coords
    
    def drawPlayer(self, SF):
        self.PlayerRT = pg.draw.rect(SF, '#ff0000', (self.coords[0], self.coords[1], 40, 40))
        pg.draw.rect(SF, '#000000', (self.coords[0], self.coords[1], 40, 40), 6)
