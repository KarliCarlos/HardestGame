import pygame as pg

playerSpawn = [ # Per Level
    (150+5, 300+5)
]

class Player:
    def __init__(self, coords):
        self.coords = list(coords)
        self.allowUp = True
        self.allowLeft = True
        self.allowDown = True
        self.allowRight = True
        self.PlayerRt = pg.Rect(0, 0, 40, 40)
    
    def drawPlayer(self, screen):
        self.PlayerRt = pg.draw.rect(screen, '#ff0000', (self.coords[0], self.coords[1], 40, 40))
        pg.draw.rect(screen, '#000000', (self.coords[0], self.coords[1], 40, 40), 7)

    def checkPlayerMovement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            if self.allowUp:
                self.coords[1] -= 5

        if keys[pg.K_a]:
            if self.allowLeft:
                self.coords[0] -= 5

        if keys[pg.K_s]:
            if self.allowDown:
                self.coords[1] += 5

        if keys[pg.K_d]:
            if self.allowRight:
                self.coords[0] += 5