from PyQt5 import QtWidgets

from scene import Scene
from config import GAME_WIDTH, GAME_HEIGHT

class GUI(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.x = 500
        self.y = 500
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.title = "Snail's Adventure"
        self.init_window()

    def init_window(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()
        self.setMouseTracking(True)
        self.setFixedSize(self.width, self.height)
        self.scene = Scene(self.width, self.height)
        self.set_view()

    def set_view(self):
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()