import pygame as pg


Coins = [   [],
            [],
            [
                (550, 400)
            ],
            [
                (450+25, 250+25)
            ]
        ]


class Coin:
    def __init__(self, coords, screen):
        self.screen = screen
        self.Rt = pg.draw.circle(self.screen, '#ffff00', coords, 15)
        self.collected = False

    def draw(self):
        if self.collected == False:
            self.Rt = pg.draw.circle(self.screen, '#ffff00', self.Rt.center, 15)
            pg.draw.circle(self.screen, '#000000', self.Rt.center, 15, 6)
        