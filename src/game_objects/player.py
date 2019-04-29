from PyQt5 import QtWidgets, QtGui

from game_objects.game_object import GameObject
from config import GAME_HEIGHT, SPRITE_PLAYER
from game_objects.spike import Spike
from game_objects.coin import Coin
from game_objects.cloud import Cloud
from controls import RIGHT, LEFT

class Player(GameObject):
    def __init__(self, x, y, width, height, start_x, start_y, scene):
        super().__init__(x, y, width, height, start_x, start_y)
        self.setBrush(QtGui.QBrush(QtGui.QImage(SPRITE_PLAYER[1])))
        self.on_ground = False
        self.x_vel = 0
        self.y_vel = 0
        self.y_acc = 0.5
        self.points = 0
        self.y = start_y
        self.scene = scene
        self.start_x = start_x
        self.start_y = start_y
        self.is_dead = False
        self.has_won = False

    def set_direction(self, direction):
        if direction == LEFT:
            self.setBrush(QtGui.QBrush(QtGui.QImage(SPRITE_PLAYER[0])))
        elif direction == RIGHT:
            self.setBrush(QtGui.QBrush(QtGui.QImage(SPRITE_PLAYER[1])))
   
    def jump(self):
        if self.on_ground:
            self.on_ground = False
            self.y_vel = -15

    def die(self):
        self.is_dead = True
        self.points = 0
        self.scene.display_dead_menu()
        self.scene.timer.stop()