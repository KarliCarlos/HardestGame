import pygame as pg

PLAYERSPAWN = [ # Per Level
            None,
            (150+25, 300+25), 
            (100+25, 350+25),
            (550, 400)
        ]

loadedTilesPos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
class Player:
    def __init__(self, level):
        self.level = level
        self.allowUp = True
        self.allowLeft = True
        self.allowDown = True
        self.allowRight = True
        self.Rt = pg.Rect(PLAYERSPAWN[level.currentLevel][0], PLAYERSPAWN[level.currentLevel][1], 40, 40)
        self.TilePos = [0,0]
        self.speed = 4
        self.coinsCollected = 0
    
    def drawPlayer(self, screen):
        self.Rt = pg.draw.rect(screen, '#ff0000', self.Rt)  
        pg.draw.rect(screen, '#000000', self.Rt, 7)         #black border

    def getTilePos(self):
        self.TilePos[0] = int(self.Rt.centerx/50)
        self.TilePos[1] = int(self.Rt.centery/50)
        
        loadedTilesPos[0] = [self.TilePos[0]-1,self.TilePos[1]-1]   # 0 1 2
        loadedTilesPos[1] = [self.TilePos[0],self.TilePos[1]-1]     # 3 4 5     4 = Player
        loadedTilesPos[2] = [self.TilePos[0]+1,self.TilePos[1]-1]   # 6 7 8
        loadedTilesPos[3] = [self.TilePos[0]-1,self.TilePos[1]]
        loadedTilesPos[4] = [self.TilePos[0],self.TilePos[1]]
        loadedTilesPos[5] = [self.TilePos[0]+1,self.TilePos[1]]
        loadedTilesPos[6] = [self.TilePos[0]-1,self.TilePos[1]+1]
        loadedTilesPos[7] = [self.TilePos[0],self.TilePos[1]+1]
        loadedTilesPos[8] = [self.TilePos[0]+1,self.TilePos[1]+1]
        self.level.checkTiles(loadedTilesPos)

    def checkPlayerMovement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            if self.playerMoveUp():
                self.Rt.y -= self.speed
                self.getTilePos()

        if keys[pg.K_a]:
            if self.playerMoveLeft():
                self.Rt.x -= self.speed
                self.getTilePos()

        if keys[pg.K_s]:
            if self.playerMoveDown():
                self.Rt.y += self.speed
                self.getTilePos()

        if keys[pg.K_d]:
            if self.playerMoveRight():
                self.Rt.x += self.speed
                self.getTilePos()

    def playerMoveUp(self) ->bool:
        moveUp = True
        for i in range(3):
            self.Rt.y -= self.speed
            if self.level.loadedVoidTiles[i] != -1:
                if self.Rt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                    moveUp = False
                    self.Rt.y = self.level.void[self.level.loadedVoidTiles[i]].y+50
                    continue
            self.Rt.y += self.speed
        return moveUp

    def playerMoveLeft(self) ->bool:
        moveLeft = True
        for i in range(0, 7, 3):
            self.Rt.x -= self.speed
            if self.level.loadedVoidTiles[i] != -1:
                if self.Rt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                    moveLeft = False
                    self.Rt.x = (self.level.void[self.level.loadedVoidTiles[i]].x+50)
                    continue
            self.Rt.x += self.speed
        return moveLeft

    def playerMoveDown(self) ->bool:
        moveDown = True
        for i in range(6, 9, 1):
            self.Rt.y += self.speed
            if self.level.loadedVoidTiles[i] != -1:
                    if self.Rt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                        moveDown = False
                        self.Rt.y = self.level.void[self.level.loadedVoidTiles[i]].y - self.Rt.h
                        continue
            self.Rt.y -= self.speed
        return moveDown
        
    def playerMoveRight(self) ->bool:
        moveRight = True
        for i in range(2, 9, 3):
            self.Rt.x += self.speed
            if self.level.loadedVoidTiles[i] != -1:
                    if self.Rt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                        moveRight = False
                        self.Rt.x = self.level.void[self.level.loadedVoidTiles[i]].x - self.Rt.w
                        continue
            self.Rt.x -= self.speed
        return moveRight
        