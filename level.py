import pygame as pg

levels = [                                   #   #
   [['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'], # Level 1
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','S','S','S','X','X','X','X','X','X','X','X','X','X','O','O','Z','Z','Z','X','X'],
    ['X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X'],
    ['X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X'], #mid
    ['X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X'], #mid
    ['X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X'],
    ['X','X','S','S','S','O','O','X','X','X','X','X','X','X','X','X','X','Z','Z','Z','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']],

                                             #   #
   [['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'], # Level 2
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','O','O','O','O','O','O','O','O','O','O','O','O','X','X','X','X','X'],
    ['X','X','X','X','X','O','O','O','O','O','O','O','O','O','O','O','O','X','X','X','X','X'],
    ['X','X','S','S','S','O','O','O','O','O','O','O','O','O','O','O','O','Z','Z','Z','X','X'], #mid
    ['X','X','S','S','S','O','O','O','O','O','O','O','O','O','O','O','O','Z','Z','Z','X','X'], #mid
    ['X','X','X','X','X','O','O','O','O','O','O','O','O','O','O','O','O','X','X','X','X','X'],
    ['X','X','X','X','X','O','O','O','O','O','O','O','O','O','O','O','O','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]
    ]

class Level:
    def __init__(self, currentLevel):
        self.currentLevel = currentLevel
        self.borders = {"up": [],"left": [],"down": [],"right": []} # 0 = Up | 1 = Left | 2 = Down | 3 = Right
        self.void = []
        self.start = []
        self.finish = []
        self.backgroundSf = pg.image.load('./img/background.png').convert()
        self.lineThickness = 5
        self.loadedVoidTiles = [-1, -1, -1, -1, -1, -1, -1, -1, -1]


    def calcLevel(self,screen):

        screen.blit(self.backgroundSf,(0,0))

        for y in range(len(levels[self.currentLevel])):
            
            for x in range(len(levels[self.currentLevel][y])):
                if levels[self.currentLevel][y][x] == 'X':
                    self.void.append(
                        pg.draw.rect(screen, (176,179,253), (x*50,y*50,50,50))
                    )
                else:
                    if levels[self.currentLevel][y][x] == 'S':
                        self.start.append(
                            pg.draw.rect(screen, (172,236,174), (x*50,y*50,50,50))
                        )
                    
                    if levels[self.currentLevel][y][x] == 'Z':
                        self.finish.append(
                            pg.draw.rect(screen, (172,236,174), (x*50,y*50,50,50))
                        )

                    self.calcBorders(screen, x, y) 

    def calcBorders(self, screen, x, y): #+-3 because of line thickness
        if y+1 <= len(levels[self.currentLevel]):
            if levels[self.currentLevel][y+1][x] == 'X':
                self.borders["down"].append(
                    pg.draw.line(screen, (0,0,0), (x*50,y*50+49+self.lineThickness/2), (x*50+49,y*50+49+self.lineThickness/2), self.lineThickness)
                )

        if y-1 >= 0:
            if levels[self.currentLevel][y-1][x] == 'X':
                self.borders["up"].append(
                    pg.draw.line(screen, (0,0,0), (x*50,y*50-self.lineThickness/2), (x*50+49,y*50-self.lineThickness/2), self.lineThickness)
                )

        if x+1 <= len(levels[self.currentLevel][0]):
            if levels[self.currentLevel][y][x+1] == 'X':
                self.borders["right"].append(
                    pg.draw.line(screen, (0,0,0), (x*50+49+self.lineThickness/2,y*50+50-50), (x*50+49+self.lineThickness/2,y*50+49), self.lineThickness)
                )

        if x-1 >= 0:
            if levels[self.currentLevel][y][x-1] == 'X':
                self.borders["left"].append(
                    pg.draw.line(screen, (0,0,0), (x*50-self.lineThickness/2,y*50), (x*50-self.lineThickness/2,y*50+49), self.lineThickness)
                )
        

    def drawLevel(self, screen):
        screen.blit(self.backgroundSf,(0,0))

        for i in range(len(self.void)):
            pg.draw.rect(screen, (176,179,253), self.void[i])

        for i in range(len(self.start)):
            pg.draw.rect(screen, (172,236,174), self.start[i])

        for i in range(len(self.finish)):
            pg.draw.rect(screen, (172,236,174), self.finish[i])

        for i in self.borders.items():
            for j in i[1]:
                pg.draw.rect(screen, (0,0,0), j)

    def getVoidTiles(self, loadedTilesPos):
        for j, i in enumerate(loadedTilesPos):
            if levels[self.currentLevel][i[1]][i[0]] == 'X':
                self.loadedVoidTiles[j] = self.void.index(pg.Rect(i[0]*50,i[1]*50,50,50))
                continue
            self.loadedVoidTiles[j] = -1