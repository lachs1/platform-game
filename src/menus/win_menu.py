from PyQt5 import QtGui, QtWidgets

from menus.menu_button import MenuButton
from menus.menu_text import MenuText

from config import GAME_WIDTH, GAME_HEIGHT, BLACK, LIME, FADED_BLACK, GOLD

class WinMenu():

    def __init__(self, scene):
        self.scene = scene
        self.open = False

    def remove_win_menu(self):
        self.scene.removeItem(self.MENU_TITLE)
        self.scene.removeItem(self.RETRY_BUTTON)
        self.scene.removeItem(self.MAIN_MENU_BUTTON)
        self.scene.removeItem(self.POINT_TEXT)
        self.scene.removeItem(self.TIME_TEXT)
        self.scene.removeItem(self.BACKGROUND)
    
    def add_win_menu(self, points, time):
        self.MENU_TITLE = MenuText("You have won!", GAME_WIDTH / 2, GAME_HEIGHT / 2 - 150, LIME, 7)
        self.RETRY_BUTTON = MenuButton("Play again", 1, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 50, self.scene, BLACK, self.scene.game)
        self.MAIN_MENU_BUTTON = MenuButton("Main Menu", 4, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 10, self.scene, BLACK, None)
        self.POINT_TEXT = MenuText("Points: {}".format(points), GAME_WIDTH / 2 - 70, GAME_HEIGHT / 2  - 100, GOLD, 6)
        self.TIME_TEXT = MenuText("Time: {}".format(time), GAME_WIDTH / 2 + 70, GAME_HEIGHT / 2  - 100, GOLD, 6)
        self.BACKGROUND = QtWidgets.QGraphicsRectItem(0, 0, GAME_WIDTH, GAME_HEIGHT)
        self.BACKGROUND.setBrush(FADED_BLACK)
        self.scene.addItem(self.BACKGROUND)
        self.scene.addItem(self.MENU_TITLE)
        self.scene.addItem(self.RETRY_BUTTON)
        self.scene.addItem(self.MAIN_MENU_BUTTON)
        self.scene.addItem(self.POINT_TEXT)
        self.scene.addItem(self.TIME_TEXT)