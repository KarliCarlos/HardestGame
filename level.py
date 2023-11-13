import pygame as pg

levels = [
   ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X', # Level 1
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','S','S','S','X','X','X','X','X','X','X','X','X','X','O','O','Z','Z','Z','X','X',
    'X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X',
    'X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X',
    'X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X',
    'X','X','S','S','S','X','O','O','O','O','O','O','O','O','O','O','X','Z','Z','Z','X','X',
    'X','X','S','S','S','O','O','X','X','X','X','X','X','X','X','X','X','Z','Z','Z','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
    'X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X' ]
    ]

class Level:
    def __init__(self, currentLevel):
        self.currentLevel = currentLevel
        self.borders = [[],[],[],[]] # 0 = Up | 1 = Left | 2 = Down | 3 = Right
        self.void = []
        self.start = []
        self.finish = []
        self.backgroundSf = pg.image.load('./img/background.png').convert()


    def calcLevel(self,screen):
        x = 1
        y = 1

        screen.blit(self.backgroundSf,(0,0))

        for l in range(len(levels[self.currentLevel])):

            if levels[self.currentLevel][l] == 'S':
                self.start.append(
                    pg.draw.rect(screen, (172,236,174), (x*50-50,y*50-50,50,50))
                )
            
            elif levels[self.currentLevel][l] == 'Z':
                self.finish.append(
                    pg.draw.rect(screen, (172,236,174), (x*50-50,y*50-50,50,50))
                )

            elif levels[self.currentLevel][l] == 'X':
                self.void.append(
                    pg.draw.rect(screen, (176,179,253), (x*50-50,y*50-50,50,50))
                )

                ### --- Borders --- ### //+-1 because of line thickness

                if not levels[self.currentLevel][l-22] == 'X':
                    self.borders[2].append( # Down
                        pg.draw.line(screen, (0,0,0), (x*50-50,y*50-50+1), (x*50,y*50-50+1), 7)
                    )

                if l+22 < len(levels[self.currentLevel]):
                    if not levels[self.currentLevel][l+22] == 'X':
                        self.borders[0].append( # Up
                            pg.draw.line(screen, (0,0,0), (x*50-50,y*50-1), (x*50,y*50-1), 7)
                        )

                if not levels[self.currentLevel][l-1] == 'X':
                    self.borders[3].append( # Right
                        pg.draw.line(screen, (0,0,0), (x*50-50+1,y*50-50), (x*50-50+1,y*50), 7)
                    )

                if l+1 < len(levels[self.currentLevel]):
                    if not levels[self.currentLevel][l+1] == 'X':
                        self.borders[1].append( # Left
                            pg.draw.line(screen, (0,0,0), (x*50-1,y*50-50), (x*50-1,y*50), 7)
                        )

            if x == 22:
                x = 1
                y += 1
            else:
                x += 1

    def drawLevel(self, screen):
        screen.blit(self.backgroundSf,(0,0))

        for i in range(len(self.void)):
            pg.draw.rect(screen, (176,179,253), self.void[i])

        for i in range(len(self.start)):
            pg.draw.rect(screen, (172,236,174), self.start[i])

        for i in range(len(self.finish)):
            pg.draw.rect(screen, (172,236,174), self.finish[i])

        for i in range(len(self.borders)):
            for j in range(len(self.borders[i])):
                pg.draw.rect(screen, (0,0,0), self.borders[i][j])
