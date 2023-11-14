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
player = Player(playerSpawn[level.currentLevel])
enemies = []
for e in range(len(enemyPath[level.currentLevel])):
    enemies.append(Enemy(list(enemyPath[level.currentLevel][e][0]), e, level.currentLevel, enemySpeed[level.currentLevel]))
font = pg.font.SysFont("Cascadia Code Semi Bold", 50)

level.calcLevel(screen)

### --- Functions --- ###

def checkBorderCollision():
    if player.PlayerRt.collideobjects(level.borders["up"]):
        player.allowUp = False
    else:
        player.allowUp = True

    if player.PlayerRt.collideobjects(level.borders["left"]):
        player.allowLeft = False
    else:
        player.allowLeft = True

    if player.PlayerRt.collideobjects(level.borders["down"]):
        player.allowDown = False
    else:
        player.allowDown = True

    if player.PlayerRt.collideobjects(level.borders["right"]):
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
    
    for n in range(len(enemies)):           
        enemies[n].movement()
        enemies[n].drawEnemy(screen)
    if checkEnemyCollision():
        player.coords = list(playerSpawn[level.currentLevel])
        deaths += 1
        print(deaths)

    pg.display.update()
    clock.tick(60)