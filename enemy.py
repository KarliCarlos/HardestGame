import pygame as pg

enemyPath = [
    [ # Level 1
        [(300+25,300+25), (750+25,300+25)],
        [(750+25,350+25), (300+25,350+25)],
        [(300+25,400+25), (750+25,400+25)],
        [(750+25,450+25), (300+25,450+25)]
    ], 
    [
        [(250+25,500+25), (250+25,250+25)],
        [(300+25,250+25), (300+25,500+25)],
        [(350+25,500+25), (350+25,250+25)],
        [(400+25,250+25), (400+25,500+25)],
        [(450+25,500+25), (450+25,250+25)],
        [(500+25,250+25), (500+25,500+25)],
        [(550+25,500+25), (550+25,250+25)],
        [(600+25,250+25), (600+25,500+25)],
        [(650+25,500+25), (650+25,250+25)],
        [(700+25,250+25), (700+25,500+25)],
        [(750+25,500+25), (750+25,250+25)],
        [(800+25,250+25), (800+25,500+25)]
    ]
]

enemySpeed = [9, 6]

class Enemy:
    def __init__(self, coords, n, level, speed):
        self.coords = coords
        self.number = n
        self.level = level
        self.dest = 1
        self.speed = speed

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
            if enemyPath[self.level][self.number][self.dest][0] - self.coords[0] < self.speed:
                self.coords[0] += enemyPath[self.level][self.number][self.dest][0] - self.coords[0]
            else:
                self.coords[0] += self.speed
        elif enemyPath[self.level][self.number][self.dest][0] < self.coords[0]:
            if self.coords[0] - enemyPath[self.level][self.number][self.dest][0] < self.speed:
                self.coords[0] -= self.coords[0] - enemyPath[self.level][self.number][self.dest][0]
            else:
                self.coords[0] -= self.speed
            
        if enemyPath[self.level][self.number][self.dest][1] > self.coords[1]:
            if enemyPath[self.level][self.number][self.dest][1] - self.coords[1] < self.speed:
                self.coords[1] += enemyPath[self.level][self.number][self.dest][1] - self.coords[1]
            else:
                self.coords[1] += self.speed
        elif enemyPath[self.level][self.number][self.dest][1] < self.coords[1]:
            if self.coords[1] - enemyPath[self.level][self.number][self.dest][1] < self.speed:
                self.coords[1] -= self.coords[1] - enemyPath[self.level][self.number][self.dest][1]
            else:
                self.coords[1] -= self.speed