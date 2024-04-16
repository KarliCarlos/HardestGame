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

### --- Main Class --- ###
class Main:

    def __init__(self) -> None:
        self.level = Level(-1, self)
        self.player = Player(self.level)
        self.font = pg.font.SysFont("Cascadia Code Semi Bold", 50)
        self.enemies = []    
        self.deaths = 0

    ## --- Functions --- ###

    def nextLevel(self):
        self.level.currentLevel += 1
        self.level.calcLevel(screen)
        self.enemies = []
        for e in range(len(enemyPath[self.level.currentLevel])):
            self.enemies.append(Enemy(list(enemyPath[self.level.currentLevel][e][0]), e, self.level.currentLevel, enemySpeed[self.level.currentLevel]))
        self.player.PlayerRt.center = PLAYERSPAWN[self.level.currentLevel]

    def checkEnemyCollision(self):
        for e in range(len(self.enemies)):
            if self.player.PlayerRt.colliderect(self.enemies[e].EnemyRt):
                return True
                

    ### --- Game Loop --- ###
    def RUN(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    exit()
                
            self.player.checkPlayerMovement()

            self.level.drawLevel(screen)
            self.player.drawPlayer(screen)
            screen.blit(self.font.render(f"Deaths: {self.deaths}", True, "#000000"), (100, 50))
            
            for n in range(len(self.enemies)):           
                self.enemies[n].movement()
                self.enemies[n].drawEnemy(screen)
            if self.checkEnemyCollision():
                self.player.PlayerRt.center = PLAYERSPAWN[self.level.currentLevel]
                self.deaths += 1

            pg.display.update()
            clock.tick(60)

GAME = Main()
GAME.nextLevel()
GAME.RUN()