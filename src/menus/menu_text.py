from PyQt5 import QtWidgets, QtCore

class MenuText(QtWidgets.QGraphicsTextItem):

    def __init__(self, text, x, y, color, size):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.draw(color, size)
        self.setPos(self.x - self.boundingRect().width() / 2, self.y - self.boundingRect().height() / 2)
    
    def draw(self, color, size):
        self.setHtml("<font color='{}' align='center' size='{}'>{}</font>".format(color, size, self.text))