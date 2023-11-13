import pygame as pg

enemyPath = [
    [ # Level 1
        [(300+25,300+25), (750+25,300+25)],
        [(750+25,350+25), (300+25,350+25)],
        [(300+25,400+25), (750+25,400+25)],
        [(750+25,450+25), (300+25,450+25)]
    ]
]

class Enemy:
    def __init__(self, coords, n, level):
        self.coords = coords
        self.number = n
        self.level = level
        self.dest = 1

    def drawEnemy(self, screen):
        self.EnemyRt = pg.draw.circle(screen, '#0000ff', self.coords, 18)
        pg.draw.circle(screen, '#000000', self.coords, 18, 8)
    
    def movement(self):
        if list(enemyPath[self.level][self.number][self.dest]) == self.coords:
            if self.dest < len(enemyPath[self.level][self.number])-1:
                self.dest +=1
            else:
                self.dest = 0

        if enemyPath[self.level][self.number][self.dest][0] > self.coords[0]:
            self.coords[0] += 10
        elif enemyPath[self.level][self.number][self.dest][0] < self.coords[0]:
            self.coords[0] -= 10
            
        if enemyPath[self.level][self.number][self.dest][1] > self.coords[1]:
            self.coords[1] += 10
        elif enemyPath[self.level][self.number][self.dest][1] < self.coords[1]:
            self.coords[1] -= 10