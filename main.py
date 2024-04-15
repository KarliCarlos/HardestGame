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

# 0 1 2
# 3 4 5     4 = Player
# 6 7 8

def checkBorderCollision():
    for i, j in enumerate(level.loadedVoidTiles):
        if level.loadedVoidTiles[i] != -1:
            if i == 0 or i == 1 or i == 2:
                if player.PlayerRt.colliderect(level.void[j]):
                    player.allowUp = False
                else:
                    player.allowUp = True

            if i == 0 or i == 3 or i == 6:
                if player.PlayerRt.colliderect(level.void[j]):
                    player.allowLeft = False
                else:
                    player.allowLeft = True

            if i == 6 or i == 7 or i == 8:
                if player.PlayerRt.colliderect(level.void[j]):
                    player.allowDown = False
                else:
                    player.allowDown = True

            if i == 2 or i == 5 or i == 8:
                if player.PlayerRt.colliderect(level.void[j]):
                    player.allowRight = False
                else:
                    player.allowRight = True

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
        
    checkBorderCollision()
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