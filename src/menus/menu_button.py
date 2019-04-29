from PyQt5 import QtWidgets, QtCore

from config import BLACK, CORAL

class MenuButton(QtWidgets.QGraphicsTextItem):

    def __init__(self, text, action, x, y, scene, color, game):
        super().__init__()
        self.text = text
        self.action = action
        self.x = x
        self.y = y
        self.game = game
        self.draw(color)
        self.scene = scene
        self.setPos(self.x - self.boundingRect().width() / 2, self.y - self.boundingRect().height() / 2)
    
    def draw(self, color):
        self.setHtml("<font color='{}' align='center' size='6'>{}</font>".format(color, self.text))

    def hoverEnterEvent(self, e):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.PointingHandCursor)
        self.draw(CORAL)

    def hoverLeaveEvent(self, e):
        QtWidgets.QApplication.restoreOverrideCursor()
        self.draw(BLACK)

    def mousePressEvent(self, e):
        action = self.action
        if action == 0:
            self.scene.display_game_view(self.game)
        elif action == 1:
            self.scene.main_menu.construct_field_select()
        elif action == 2:
            self.scene.main_menu.construct_controls_menu()
        elif action == 3:
            QtWidgets.QApplication.exit()
        elif action == 4:
            self.scene.display_main_menu()
        elif action == 5:
            self.scene.resume_game()
        elif action == 6:
            # in action 6 scene isn't really a scene
            # it is accutally the MainMenu object
            self.scene.construct_field_select()