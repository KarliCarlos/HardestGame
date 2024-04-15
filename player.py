import pygame as pg

PLAYERSPAWN = [ # Per Level
            (150+5, 300+5), 
            (100+25+5, 350+25+5)
        ]

loadedTilesPos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
class Player:
    def __init__(self, level):
        self.level = level
        self.coords = list(PLAYERSPAWN[level.currentLevel])
        self.allowUp = True
        self.allowLeft = True
        self.allowDown = True
        self.allowRight = True
        self.PlayerRt = pg.Rect(0, 0, 40, 40)
        self.TilePos = [0,0]
    
    def drawPlayer(self, screen):
        self.PlayerRt = pg.draw.rect(screen, '#ff0000', (self.coords[0], self.coords[1], 40, 40))
        pg.draw.rect(screen, '#000000', (self.coords[0], self.coords[1], 40, 40), 7)

    def checkPlayerMovement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            if self.allowUp:
                self.coords[1] -= 4
                self.getTilePos()

        if keys[pg.K_a]:
            if self.allowLeft:
                self.coords[0] -= 4
                self.getTilePos()

        if keys[pg.K_s]:
            if self.allowDown:
                self.coords[1] += 4
                self.getTilePos()

        if keys[pg.K_d]:
            if self.allowRight:
                self.coords[0] += 4
                self.getTilePos()

    def getTilePos(self):
        self.TilePos[0] = int(self.PlayerRt.centerx/50)
        self.TilePos[1] = int(self.PlayerRt.centery/50)
        
        loadedTilesPos[0] = [self.TilePos[0]-1,self.TilePos[1]-1]
        loadedTilesPos[1] = [self.TilePos[0],self.TilePos[1]-1]
        loadedTilesPos[2] = [self.TilePos[0]+1,self.TilePos[1]-1]
        loadedTilesPos[3] = [self.TilePos[0]-1,self.TilePos[1]]
        loadedTilesPos[4] = [self.TilePos[0],self.TilePos[1]]
        loadedTilesPos[5] = [self.TilePos[0]+1,self.TilePos[1]]
        loadedTilesPos[6] = [self.TilePos[0]-1,self.TilePos[1]+1]
        loadedTilesPos[7] = [self.TilePos[0],self.TilePos[1]+1]
        loadedTilesPos[8] = [self.TilePos[0]+1,self.TilePos[1]+1]
        self.level.getVoidTiles(loadedTilesPos)
        