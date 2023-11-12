import pygame as pg

playerSpawn = [
    [150+5, 300+5]
]

class Player:
    def __init__(self, coords):
        self.coords = coords
        self.allowUp = True
        self.allowLeft = True
        self.allowDown = True
        self.allowRight = True
        self.PlayerRt = pg.Rect(0, 0, 40, 40)
    
    def drawPlayer(self, SF):
        self.PlayerRt = pg.draw.rect(SF, '#ff0000', (self.coords[0], self.coords[1], 40, 40))
        pg.draw.rect(SF, '#000000', (self.coords[0], self.coords[1], 40, 40), 6)

    def checkPlayerMovement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            if self.allowUp:
                self.coords[1] -= 2

        if keys[pg.K_a]:
            if self.allowLeft:
                self.coords[0] -= 2

        if keys[pg.K_s]:
            if self.allowDown:
                self.coords[1] += 2

        if keys[pg.K_d]:
            if self.allowRight:
                self.coords[0] += 2

