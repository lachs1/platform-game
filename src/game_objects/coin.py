from PyQt5 import QtWidgets, QtGui

from config import SPRITE_COIN

class Coin(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, x, y, width, height, start_x, start_y):
        super().__init__(x, y, width, height)
        self.x = start_x
        self.y = start_y
        self.setBrush(QtGui.QBrush(QtGui.QImage(SPRITE_COIN)))
        self.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0, 0)))
        self.start_x = start_x
        self.start_y = start_y
        self.setPos(self.x, self.y)