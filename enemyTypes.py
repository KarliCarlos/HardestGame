import pygame as pg
from enemy import Enemy


EnemyDict = {
    1: {
        "Straight": {
                "Start":    [(300+25,300+25), (750+25,350+25), (300+25,400+25), (750+25,450+25)],
                "Finish":   [(750+25,300+25), (300+25,350+25), (750+25,400+25), (300+25,450+25)],
                "xSpeed":   [+8, -8, +8, -8],
                "ySpeed":   [0, 0, 0, 0]
        },
        "Square": {

        },
        "Circular": {

        },
    }    
}

class StraightEnemy(Enemy):
    def __init__(self, screen, xSpeed, ySpeed, startCoords, endCoords):
        super().__init__(screen, xSpeed, ySpeed, startCoords)
        self.start = startCoords
        self.finish = endCoords

    def checkSpeed(self):
        if self.xSpeed > 0:
            if self.Rt.centerx > self.finish[0]:
                self.Rt.centerx = self.finish[0]
                self.xSpeed *= -1
                self.start, self.finish = self.finish, self.start
        if self.xSpeed < 0:
            if self.Rt.centerx < self.finish[0]:
                self.Rt.centerx = self.finish[0]
                self.xSpeed *= -1
                self.start, self.finish = self.finish, self.start

        if self.ySpeed > 0:
            if self.Rt.centery > self.finish[1]:
                self.Rt.centerx = self.finish[1]
                self.ySpeed *= -1
                self.start, self.finish = self.finish, self.start
        if self.ySpeed < 0:
            if self.Rt.centery < self.finish[1]:
                self.Rt.centerx = self.finish[1]
                self.ySpeed *= -1
                self.start, self.finish = self.finish, self.start



class SquareEnemy():
    def __init__(self, screen, xSpeed, ySpeed, startCoords):
        super().__init__(screen, xSpeed, ySpeed, startCoords)


class CircularEnemy():
    def __init__(self, screen, xSpeed, ySpeed, startCoords):
        super().__init__(screen, xSpeed, ySpeed, startCoords)
