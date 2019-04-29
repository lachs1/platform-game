from PyQt5 import QtWidgets, QtCore, QtGui

from game import Game
from resourceloader import ResourceLoader
from controls import LEFT, RIGHT, SPACE, PAUSE, RETRY
from config import CLOCK_SPEED, SPRITE_MAIN_BACKGROUND

from menus.pause_menu import PauseMenu
from menus.dead_menu import DeadMenu
from menus.win_menu import WinMenu
from menus.main_menu import MainMenu

class Scene(QtWidgets.QGraphicsScene):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.setSceneRect(0, 0, width, height)
        self.timer = QtCore.QBasicTimer()
        self.playing = False
        self.pause_menu = PauseMenu(self)
        self.dead_menu = DeadMenu(self)
        self.win_menu = WinMenu(self)
        self.main_menu = MainMenu(self)
        self.main_menu.construct_main_menu()
        self.game = None

    def display_main_menu(self):
        self.playing = False
        self.close_all_game_menus()
        self.main_menu.construct_main_menu()

    def display_game_view(self, game):
        self.clear()
        self.close_all_game_menus()
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QImage(SPRITE_MAIN_BACKGROUND)))
        self.game = game
        grounds = self.game.grounds
        coins = self.game.coins
        spikes = self.game.spikes
        clouds = self.game.clouds
        enemies = self.game.enemies
        boxes = self.game.boxes
        flag = self.game.flag
        player = self.game.player
        player.scene = self
        self.game.scene = self

        self.addItem(player)
        self.addItem(flag)

        for cloud in clouds:
            self.addItem(cloud)

        for ground in grounds:
            self.addItem(ground)

        for box in boxes:
            self.addItem(box)

        for enemy in enemies:
            self.addItem(enemy)

        for spike in spikes:
            self.addItem(spike)

        for coin in coins:
            self.addItem(coin)

        self.add_point_text()
        self.add_time_text()
        self.timer.start(CLOCK_SPEED, self)
        self.game.start()
        self.playing = True

    def add_point_text(self):
        self.point_text = QtWidgets.QGraphicsTextItem()
        self.point_text.setPos(797, 11)
        self.addItem(self.point_text)
        self.update_point_text()

    def update_point_text(self):
        self.point_text.setHtml("<font color='black' align='center' size='5'>Points: {}</font>".format(self.game.player.points))

    def add_time_text(self):
        self.time_text = QtWidgets.QGraphicsTextItem()
        self.time_text.setPos(700, 11)
        self.addItem(self.time_text)
        self.update_time_text()

    def update_time_text(self):
        self.time_text.setHtml("<font color='black' align='center' size='5'>Time: {}</font>".format(self.game.time))

    def timerEvent(self, e):
        self.game.update()

    def keyPressEvent(self, e):
        pressed = e.key()
        if self.playing:

            if pressed in (LEFT, RIGHT):
                self.game.direction = pressed

            if pressed == SPACE:
                self.game.player.jump()

            if pressed == RETRY:
                if self.game.player.is_dead:
                    self.main_menu.construct_field_select()

            if pressed == PAUSE and not self.game.player.is_dead:
                if self.game.paused:
                    self.resume_game()
                else:
                    self.pause_game()

    def keyReleaseEvent(self, e):
        released = e.key()
        if self.playing:
            if released in (LEFT, RIGHT):
                self.game.direction = None

    def pause_game(self):
        self.game.paused = True
        self.game.timer.stop()
        self.display_pause_menu()
        self.timer.stop()

    def resume_game(self):
        self.game.paused = False
        self.game.timer.start(1000)
        self.hide_pause_menu()
        self.timer.start(CLOCK_SPEED, self)

    def display_pause_menu(self):
        if not self.pause_menu.open:
            self.pause_menu.add_pause_menu()
            self.pause_menu.open = True
       
    def hide_pause_menu(self):
        if self.pause_menu.open:
            self.pause_menu.remove_pause_menu()
            self.pause_menu.open = False
    
    def display_dead_menu(self):
        if not self.dead_menu.open:
            self.dead_menu.add_dead_menu()
            self.dead_menu.open = True

    def hide_dead_menu(self):
        if self.dead_menu.open:
            self.dead_menu.remove_dead_menu()
            self.dead_menu.open = False

    def display_win_menu(self, points, time):
        if not self.win_menu.open:
            self.win_menu.add_win_menu(points, time)
            self.win_menu.open = True

    def hide_win_menu(self):
        if self.win_menu.open:
            self.win_menu.remove_win_menu()
            self.win_menu.open = False
    
    def close_all_game_menus(self):
        self.pause_menu.open = False
        self.dead_menu.open = False
        self.win_menu.open = False