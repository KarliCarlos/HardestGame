import pygame as pg
from sys import exit
from level import *
from player import *
from enemy import *

### --- Initialize Game --- ###

pg.init()
screen = pg.display.set_mode((1100, 800))
pg.display.set_caption('The Worlds Hardest Game')
clock = pg.time.Clock()

level = Level(0)
player = Player(playerSpawn[level.currentLevel])
enemies = []
for e in range(len(enemyPath[level.currentLevel])):
    enemies.append(Enemy(list(enemyPath[level.currentLevel][e][0]), e, level.currentLevel))

level.calcLevel(screen)

### --- Functions --- ###

def checkBorderCollision():
    if player.PlayerRt.collideobjects(level.borders[0]):
        player.allowUp = False
    else:
        player.allowUp = True

    if player.PlayerRt.collideobjects(level.borders[1]):
        player.allowLeft = False
    else:
        player.allowLeft = True

    if player.PlayerRt.collideobjects(level.borders[2]):
        player.allowDown = False
    else:
        player.allowDown = True

    if player.PlayerRt.collideobjects(level.borders[3]):
        player.allowRight = False
    else:
        player.allowRight = True

def checkEnemyCollision():
    for e in range(len(enemies)):
        if player.PlayerRt.colliderect(enemies[e].EnemyRt):
            player.coords = list(playerSpawn[level.currentLevel])

### --- Game Loop --- ###

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()
        
    checkBorderCollision()
    player.checkPlayerMovement()

    level.drawLevel(screen)
    player.drawPlayer(screen)
    
    for n in range(len(enemies)):           
        enemies[n].movement()
        enemies[n].drawEnemy(screen)
    checkEnemyCollision()

    pg.display.update()
    clock.tick(60)