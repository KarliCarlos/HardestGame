import pygame as pg

levels = [
   ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',
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
    

    def drawLevel(self,screen):
        x = 1
        y = 1
        self.borders = []

        backgroundSf = pg.image.load('./img/background.png').convert()
        screen.blit(backgroundSf,(0,0))

        for l in range(len(levels[self.currentLevel])):

            if levels[self.currentLevel][l] == 'S' or levels[self.currentLevel][l] == 'Z':
                pg.draw.rect(screen, (172,236,174), (x*50-50,y*50-50,50,50))

            elif levels[self.currentLevel][l] == 'X':
                pg.draw.rect(screen, (176,179,253), (x*50-50,y*50-50,50,50))

                if not levels[self.currentLevel][l-22] == 'X':
                    self.borders.append(pg.draw.line(screen, (0,0,0), (x*50-50,y*50-50+3), (x*50,y*50-50+3), 7))

                if l+22 < len(levels[self.currentLevel]):
                    if not levels[self.currentLevel][l+22] == 'X':
                        self.borders.append(pg.draw.line(screen, (0,0,0), (x*50-50,y*50-3), (x*50,y*50-3), 7))

                if not levels[self.currentLevel][l-1] == 'X':
                    self.borders.append(pg.draw.line(screen, (0,0,0), (x*50-50+3,y*50-50), (x*50-50+3,y*50), 7))

                if l+1 < len(levels[self.currentLevel]):
                    if not levels[self.currentLevel][l+1] == 'X':
                        self.borders.append(pg.draw.line(screen, (0,0,0), (x*50-3,y*50-50), (x*50-3,y*50), 7))

            if x == 22:
                x = 1
                y += 1
            else:
                x += 1

        
    
            
        