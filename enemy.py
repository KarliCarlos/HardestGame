import pygame as pg
from abc import ABC, abstractmethod

# enemyPath = [
#     [ # Level 1
#         [(300+25,300+25), (750+25,300+25)],
#         [(750+25,350+25), (300+25,350+25)],
#         [(300+25,400+25), (750+25,400+25)],
#         [(750+25,450+25), (300+25,450+25)]
#     ], 
#     [
#         [(250+25,500+25), (250+25,250+25)],
#         [(300+25,250+25), (300+25,500+25)],
#         [(350+25,500+25), (350+25,250+25)],
#         [(400+25,250+25), (400+25,500+25)],
#         [(450+25,500+25), (450+25,250+25)],
#         [(500+25,250+25), (500+25,500+25)],
#         [(550+25,500+25), (550+25,250+25)],
#         [(600+25,250+25), (600+25,500+25)],
#         [(650+25,500+25), (650+25,250+25)],
#         [(700+25,250+25), (700+25,500+25)],
#         [(750+25,500+25), (750+25,250+25)],
#         [(800+25,250+25), (800+25,500+25)]
#     ]
# ]

# enemySpeed = [8, 6]

class Enemy(ABC):
    def __init__(self, screen, xSpeed, ySpeed, startCoords):
        self.screen = screen
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.Rt = pg.draw.circle(self.screen, '#0000ff', startCoords, 15, -1)

    def draw(self):
        self.Rt = pg.draw.circle(self.screen, '#0000ff', self.Rt.center, 15)
        pg.draw.circle(self.screen, '#000000', self.Rt.center, 15, 7)

    def movement(self):
        self.Rt.centerx += self.xSpeed
        self.Rt.centery += self.ySpeed

    @abstractmethod
    def checkSpeed(self):
        pass

# class Enemy:
#     def __init__(self, coords, n, level, speed):
#         self.coords = coords
#         self.number = n
#         self.level = level
#         self.dest = 1
#         self.speed = speed

#     def drawEnemy(self, screen):
#         self.EnemyRt = pg.draw.circle(screen, '#0000ff', self.coords, 18)
#         pg.draw.circle(screen, '#000000', self.coords, 18, 8)               #black border
    
#     def movement(self):
#         if list(enemyPath[self.level][self.number][self.dest]) == self.coords:
#             if self.dest < len(enemyPath[self.level][self.number])-1:
#                 self.dest +=1
#             else:
#                 self.dest = 0

#         if enemyPath[self.level][self.number][self.dest][0] > self.coords[0]:
#             if enemyPath[self.level][self.number][self.dest][0] - self.coords[0] < self.speed:
#                 self.coords[0] += enemyPath[self.level][self.number][self.dest][0] - self.coords[0]
#             else:
#                 self.coords[0] += self.speed
#         elif enemyPath[self.level][self.number][self.dest][0] < self.coords[0]:
#             if self.coords[0] - enemyPath[self.level][self.number][self.dest][0] < self.speed:
#                 self.coords[0] -= self.coords[0] - enemyPath[self.level][self.number][self.dest][0]
#             else:
#                 self.coords[0] -= self.speed
            
#         if enemyPath[self.level][self.number][self.dest][1] > self.coords[1]:
#             if enemyPath[self.level][self.number][self.dest][1] - self.coords[1] < self.speed:
#                 self.coords[1] += enemyPath[self.level][self.number][self.dest][1] - self.coords[1]
#             else:
#                 self.coords[1] += self.speed
#         elif enemyPath[self.level][self.number][self.dest][1] < self.coords[1]:
#             if self.coords[1] - enemyPath[self.level][self.number][self.dest][1] < self.speed:
#                 self.coords[1] -= self.coords[1] - enemyPath[self.level][self.number][self.dest][1]
#             else:
#                 self.coords[1] -= self.speed