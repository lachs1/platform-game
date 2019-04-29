from PyQt5 import QtGui, QtWidgets

from menus.menu_button import MenuButton
from menus.menu_text import MenuText

from config import GAME_WIDTH, GAME_HEIGHT, BLACK, FADED_BLACK

class PauseMenu():

    def __init__(self, scene):
        self.scene = scene
        self.open = False

    def remove_pause_menu(self):
        self.scene.removeItem(self.MENU_TITLE)
        self.scene.removeItem(self.RESUME_BUTTON)
        self.scene.removeItem(self.MAIN_MENU_BUTTON)
        self.scene.removeItem(self.BACKGROUND)
    
    def add_pause_menu(self):
        self.MENU_TITLE = MenuText("Game Paused", GAME_WIDTH / 2, GAME_HEIGHT / 2 - 150, BLACK, 7)
        self.RESUME_BUTTON = MenuButton("Resume", 5, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 50, self.scene, BLACK, None)
        self.MAIN_MENU_BUTTON = MenuButton("Main Menu", 4, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 10, self.scene, BLACK, None)
        self.BACKGROUND = QtWidgets.QGraphicsRectItem(0, 0, GAME_WIDTH, GAME_HEIGHT)
        self.BACKGROUND.setBrush(FADED_BLACK)
        self.scene.addItem(self.BACKGROUND)
        self.scene.addItem(self.MENU_TITLE)
        self.scene.addItem(self.RESUME_BUTTON)
        self.scene.addItem(self.MAIN_MENU_BUTTON)