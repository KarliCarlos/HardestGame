from gc import collect
import pygame as pg
from sys import exit
from level import *
from player import *
from enemyTypes import *
from other import *

### --- Initialize Game --- ###

pg.init()
screen = pg.display.set_mode((1100, 800))
pg.display.set_caption('The Worlds Hardest Game')
clock = pg.time.Clock()
printPos = True;

### --- Main Class --- ###
class Main:

    def __init__(self):
        self.level = Level(3, self)
        self.player = Player(self.level)
        self.font = pg.font.SysFont("Cascadia Code Semi Bold", 50)
        self.enemies = []
        self.coins = []
        self.deaths = 0
        self.loadLevel(self.level.currentLevel)

    ## --- Functions --- ###

    def loadLevel(self, level):
        self.level.currentLevel = level
        self.level.calcLevel(screen)
        self.enemies = []
        self.coins = []
        straight = EnemyDict[self.level.currentLevel]["Straight"]
        for i in range(len(straight["Start"])):
            self.enemies.append(StraightEnemy(screen, straight["xSpeed"][i], straight["ySpeed"][i], straight["Start"][i], straight["Finish"][i]))
        for i in Coins[self.level.currentLevel]:
            self.coins.append(Coin(i, screen))
        self.player.Rt.center = PLAYERSPAWN[self.level.currentLevel]

    def checkEnemyCollision(self):
        for e in self.enemies:
            if self.player.Rt.colliderect(e.Rt):
                return True
            
    def checkCoinCollision(self):
        for c in self.coins:
            if self.player.Rt.colliderect(c.Rt):
                c.collected = True

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
            if printPos == True:
                print(self.player.Rt.center)
            screen.blit(self.font.render(f"Deaths: {self.deaths}", True, "#000000"), (100, 50))

            self.checkCoinCollision()
            for c in self.coins:
                c.draw()
            
            for e in self.enemies:
                e.movement()
                e.checkSpeed()
                e.draw()
            if self.checkEnemyCollision():
                self.player.Rt.center = PLAYERSPAWN[self.level.currentLevel]
                self.deaths += 1
                for c in self.coins:
                    c.collected = False

            pg.display.update()
            clock.tick(60)

GAME = Main()
GAME.RUN()