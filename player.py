import pygame as pg

PLAYERSPAWN = [ # Per Level
            (150+25, 300+25), 
            (100+25, 350+25)
        ]

loadedTilesPos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
class Player:
    def __init__(self, level):
        self.level = level
        self.allowUp = True
        self.allowLeft = True
        self.allowDown = True
        self.allowRight = True
        self.PlayerRt = pg.Rect(PLAYERSPAWN[level.currentLevel][0], PLAYERSPAWN[level.currentLevel][1], 40, 40)
        self.TilePos = [0,0]
        self.speed = 4
    
    def drawPlayer(self, screen):
        self.PlayerRt = pg.draw.rect(screen, '#ff0000', (self.PlayerRt.x, self.PlayerRt.y, 40, 40))
        pg.draw.rect(screen, '#000000', (self.PlayerRt.x, self.PlayerRt.y, 40, 40), 7)



    def getTilePos(self):
        self.TilePos[0] = int(self.PlayerRt.centerx/50)
        self.TilePos[1] = int(self.PlayerRt.centery/50)
        
        loadedTilesPos[0] = [self.TilePos[0]-1,self.TilePos[1]-1]   # 0 1 2
        loadedTilesPos[1] = [self.TilePos[0],self.TilePos[1]-1]     # 3 4 5     4 = Player
        loadedTilesPos[2] = [self.TilePos[0]+1,self.TilePos[1]-1]   # 6 7 8
        loadedTilesPos[3] = [self.TilePos[0]-1,self.TilePos[1]]
        loadedTilesPos[4] = [self.TilePos[0],self.TilePos[1]]
        loadedTilesPos[5] = [self.TilePos[0]+1,self.TilePos[1]]
        loadedTilesPos[6] = [self.TilePos[0]-1,self.TilePos[1]+1]
        loadedTilesPos[7] = [self.TilePos[0],self.TilePos[1]+1]
        loadedTilesPos[8] = [self.TilePos[0]+1,self.TilePos[1]+1]
        self.level.getVoidTiles(loadedTilesPos)

    def checkPlayerMovement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            if self.playerMoveUp():
                self.PlayerRt.y -= self.speed
                self.getTilePos()

        if keys[pg.K_a]:
            if self.playerMoveLeft():
                self.PlayerRt.x -= self.speed
                self.getTilePos()

        if keys[pg.K_s]:
            if self.playerMoveDown():
                self.PlayerRt.y += self.speed
                self.getTilePos()

        if keys[pg.K_d]:
            if self.playerMoveRight():
                self.PlayerRt.x += self.speed
                self.getTilePos()

    def playerMoveUp(self) ->bool:
        moveUp = True
        for i in range(3):
            self.PlayerRt.y -= self.speed
            if self.level.loadedVoidTiles[i] != -1:
                if self.PlayerRt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                    moveUp = False
                    self.PlayerRt.y = self.level.void[self.level.loadedVoidTiles[i]].y+50
                    continue
            self.PlayerRt.y += self.speed
        return moveUp

    def playerMoveLeft(self) ->bool:
        moveLeft = True
        for i in range(0, 7, 3):
            self.PlayerRt.x -= self.speed
            if self.level.loadedVoidTiles[i] != -1:
                if self.PlayerRt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                    moveLeft = False
                    self.PlayerRt.x = (self.level.void[self.level.loadedVoidTiles[i]].x+50)
                    continue
            self.PlayerRt.x += self.speed
        return moveLeft

    def playerMoveDown(self) ->bool:
        moveDown = True
        for i in range(6, 9, 1):
            self.PlayerRt.y += self.speed
            if self.level.loadedVoidTiles[i] != -1:
                    if self.PlayerRt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                        moveDown = False
                        self.PlayerRt.y = self.level.void[self.level.loadedVoidTiles[i]].y - self.PlayerRt.h
                        continue
            self.PlayerRt.y -= self.speed
        return moveDown
        
    def playerMoveRight(self) ->bool:
        moveRight = True
        for i in range(2, 9, 3):
            self.PlayerRt.x += self.speed
            if self.level.loadedVoidTiles[i] != -1:
                    if self.PlayerRt.colliderect(self.level.void[self.level.loadedVoidTiles[i]]):
                        moveRight = False
                        self.PlayerRt.x = self.level.void[self.level.loadedVoidTiles[i]].x - self.PlayerRt.w
                        continue
            self.PlayerRt.x -= self.speed
        return moveRight
        