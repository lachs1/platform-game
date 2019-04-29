from PyQt5 import QtWidgets, QtGui

class GameObject(QtWidgets.QGraphicsRectItem):

    def __init__(self, x, y, width, height, start_x, start_y):
        super().__init__(x, y, width, height)
        self.x = start_x
        self.y = start_y
        self.width = width
        self.height = height
        self.start_x = start_x
        self.start_y = start_y
        self.setPos(start_x, start_y)
        self.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0, 0)))