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
deaths = 0

level = Level(0)
player = Player(level)
enemies = []
for e in range(len(enemyPath[level.currentLevel])):
    enemies.append(Enemy(list(enemyPath[level.currentLevel][e][0]), e, level.currentLevel, enemySpeed[level.currentLevel]))
font = pg.font.SysFont("Cascadia Code Semi Bold", 50)

level.calcLevel(screen)

## --- Functions --- ###

def checkEnemyCollision():
    for e in range(len(enemies)):
        if player.PlayerRt.colliderect(enemies[e].EnemyRt):
            return True
            

### --- Game Loop --- ###

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()
        
    #checkBorderCollision()
    player.checkPlayerMovement()

    level.drawLevel(screen)
    player.drawPlayer(screen)
    screen.blit(font.render(f"Deaths: {deaths}", True, "#000000"), (100, 50))
    
    # for n in range(len(enemies)):           
    #     enemies[n].movement()
    #     enemies[n].drawEnemy(screen)
    # if checkEnemyCollision():
    #     player.coords = list(PLAYERSPAWN[level.currentLevel])
    #     deaths += 1

    pg.display.update()
    clock.tick(60)