from PyQt5 import QtWidgets, QtGui

from game_objects.game_object import GameObject
from config import SPRITE_ENEMY

class Enemy(GameObject):

    def __init__(self, x, y, width, height, start_x, start_y):
        super().__init__(x, y, width, height, start_x, start_y)
        self.setBrush(QtGui.QBrush(QtGui.QImage(SPRITE_ENEMY[0])))
        self.fly_clock = 0
        self.fly_sprite = 0
        

    def update_wings(self):
        self.fly_clock += 1
        if self.fly_clock == 10:
            if self.fly_sprite == 1:
                self.fly_sprite = 0
            else:
                self.fly_sprite += 1
            self.setBrush(QtGui.QBrush(QtGui.QImage(SPRITE_ENEMY[self.fly_sprite])))
            self.fly_clock = 0
        
        
            