from PyQt5 import QtGui

from config import GAME_WIDTH, GAME_HEIGHT, BLACK, SPRITE_MENU_BACKGROUND, MAP_DIR
from menus.menu_text import MenuText
from menus.menu_button import MenuButton
from resourceloader import ResourceLoader
from corrupt_file_exception import CorruptedMapFileError
import os

class MainMenu():

    def __init__(self, scene):
        self.scene = scene

    def construct_main_menu(self):
        self.scene.clear()
        self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QImage(SPRITE_MENU_BACKGROUND)))

        self.TITLE = MenuText("Snail's Adventure", GAME_WIDTH / 2, GAME_HEIGHT / 2 - 150, BLACK, 7)
        self.PLAY_BUTTON = MenuButton("Play", 6, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 70, self, BLACK, None)
        self.CONTROLS_BUTTON = MenuButton("Controls", 2, GAME_WIDTH / 2, GAME_HEIGHT / 2 - 30, self.scene, BLACK, None)
        self.EXIT_BUTTON = MenuButton("Exit", 3, GAME_WIDTH / 2, GAME_HEIGHT / 2 + 10, self.scene, BLACK, None)

        self.scene.addItem(self.TITLE)
        self.scene.addItem(self.PLAY_BUTTON)
        self.scene.addItem(self.CONTROLS_BUTTON)
        self.scene.addItem(self.EXIT_BUTTON)

    def construct_field_select(self):
        self.scene.clear()
        self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QImage(SPRITE_MENU_BACKGROUND)))
        self.TITLE = MenuText("Select Stage", GAME_WIDTH / 2, GAME_HEIGHT / 2 - 150, BLACK, 7)
        resourceloader = ResourceLoader()
        y = -70
        for filename in os.listdir(MAP_DIR):
            if filename.endswith(".txt"):
                try:
                    game = resourceloader.load(MAP_DIR + filename)
                    BUTTON = MenuButton(game.name, 0, GAME_WIDTH / 2, GAME_HEIGHT / 2 + y, self.scene, BLACK, game)
                    self.scene.addItem(BUTTON)
                    y += 40
                except CorruptedMapFileError:
                    continue
            else:
                continue
        
        self.BACK_BUTTON = MenuButton("&larr; Back", 4, GAME_WIDTH / 2, GAME_HEIGHT / 2 + y, self.scene, BLACK, None)
        
        self.scene.addItem(self.TITLE)
        self.scene.addItem(self.BACK_BUTTON)

    def construct_controls_menu(self):
        self.scene.clear()
        self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QImage(SPRITE_MENU_BACKGROUND)))
        self.TITLE = MenuText("Game Controls", GAME_WIDTH / 2, GAME_HEIGHT / 2 - 150, BLACK, 7)

        self.LEFT_RIGHT_TEXT_1 = MenuText("Movement", GAME_WIDTH / 2 - 100, GAME_HEIGHT / 2 - 70, BLACK, 5)
        self.LEFT_RIGHT_TEXT_2 = MenuText("Arrow keys (&larr; AND &rarr;)", GAME_WIDTH / 2 + 100, GAME_HEIGHT / 2 - 70, BLACK, 5)

        self.PAUSE_GAME_1 = MenuText("Pause and Resume Game", GAME_WIDTH / 2 - 100, GAME_HEIGHT / 2 - 30, BLACK, 5)
        self.PAUSE_GAME_2 = MenuText("P", GAME_WIDTH / 2 + 100, GAME_HEIGHT / 2 - 30, BLACK, 5)

        self.JUMP_1 = MenuText("Jump", GAME_WIDTH / 2 - 100, GAME_HEIGHT / 2 + 10, BLACK, 5)
        self.JUMP_2 = MenuText("SPACE", GAME_WIDTH / 2 + 100, GAME_HEIGHT / 2 + 10, BLACK, 5)

        self.BACK_BUTTON = MenuButton("&larr; Back", 4, GAME_WIDTH / 2, GAME_HEIGHT / 2 + 40, self.scene, BLACK, None)

        self.scene.addItem(self.TITLE)
        self.scene.addItem(self.LEFT_RIGHT_TEXT_1)
        self.scene.addItem(self.LEFT_RIGHT_TEXT_2)

        self.scene.addItem(self.PAUSE_GAME_1)
        self.scene.addItem(self.PAUSE_GAME_2)

        self.scene.addItem(self.JUMP_1)
        self.scene.addItem(self.JUMP_2)
        self.scene.addItem(self.BACK_BUTTON)