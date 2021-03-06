from PyQt5 import QtGui

from game_objects.game_object import GameObject
from config import SPRITE_FLAG

class Flag(GameObject):

    def __init__(self, x, y, width, height, start_x, start_y):
        super().__init__(x, y, width, height, start_x, start_y)
        self.setBrush(QtGui.QBrush(QtGui.QImage(SPRITE_FLAG)))