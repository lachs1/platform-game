from PyQt5 import QtGui, QtWidgets

from menus.menu_button import MenuButton
from menus.menu_text import MenuText

from config import GAME_WIDTH, GAME_HEIGHT, BLACK, DARKRED, FADED_BLACK

class DeadMenu():

    def __init__(self, scene):
        self.scene = scene
        self.open = False

    def remove_dead_menu(self):
        self.scene.removeItem(self.MENU_TITLE)
        self.scene.removeItem(self.RETRY_BUTTON)
        self.scene.removeItem(self.MAIN_MENU_BUTTON)
        self.scene.removeItem(self.BACKGROUND)
    
    def add_dead_menu(self):
        self.MENU_TITLE = MenuText("YOU ARE DEAD!!!", GAME_WIDTH / 2, GAME_HEIGHT / 2 - 150, DARKRED, 7)
        self.RETRY_BUTTON = MenuButton("Play again", 1, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 50, self.scene, BLACK, None)
        self.MAIN_MENU_BUTTON = MenuButton("Main Menu", 4, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 10, self.scene, BLACK, None)
        self.BACKGROUND = QtWidgets.QGraphicsRectItem(0, 0, GAME_WIDTH, GAME_HEIGHT)
        self.BACKGROUND.setBrush(FADED_BLACK)
        self.scene.addItem(self.BACKGROUND)
        self.scene.addItem(self.MENU_TITLE)
        self.scene.addItem(self.RETRY_BUTTON)
        self.scene.addItem(self.MAIN_MENU_BUTTON)