import pygame as pg
from sys import exit
from level import *
from player import *
from enemyTypes import *

### --- Initialize Game --- ###

pg.init()
screen = pg.display.set_mode((1100, 800))
pg.display.set_caption('The Worlds Hardest Game')
clock = pg.time.Clock()

### --- Main Class --- ###
class Main:

    def __init__(self):
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
        straight = EnemyDict[1]["Straight"]
        for i in range(len(straight["Start"])):
            self.enemies.append(StraightEnemy(screen, straight["xSpeed"][i], straight["ySpeed"][i], straight["Start"][i], straight["Finish"][i]))
        self.player.Rt.center = PLAYERSPAWN[self.level.currentLevel]

    def checkEnemyCollision(self):
        for e in range(len(self.enemies)):
            if self.player.Rt.colliderect(self.enemies[e].Rt):
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
                self.enemies[n].checkSpeed()
                self.enemies[n].draw()
            if self.checkEnemyCollision():
                self.player.Rt.center = PLAYERSPAWN[self.level.currentLevel]
                self.deaths += 1

            pg.display.update()
            clock.tick(60)

GAME = Main()
GAME.nextLevel()
GAME.RUN()