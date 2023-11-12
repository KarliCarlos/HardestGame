import pygame as pg
from sys import exit
from level import *

### --- Initialize Game --- ###

pg.init()
screen = pg.display.set_mode((1100,800))
pg.display.set_caption('The Worlds Hardest Game')
clock = pg.time.Clock()

level = Level(0)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()
        
    level.drawLevel(screen)

    pg.display.update()
    clock.tick(60)