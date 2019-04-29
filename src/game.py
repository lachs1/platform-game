from PyQt5 import QtWidgets, QtGui, QtCore

from controls import RIGHT, LEFT

from game_objects.ground import Ground
from game_objects.coin import Coin
from game_objects.flag import Flag
from game_objects.spike import Spike
from game_objects.box import Box
from game_objects.cloud import Cloud
from game_objects.enemy import Enemy
from game_objects.ice import Ice
from game_objects.rock import Rock

from config import GAME_WIDTH, GAME_HEIGHT

class Game():

    def __init__(self, time, name, player, grounds, spikes, coins, clouds, enemies, boxes, flag, length, scene):
        self.score = 0
        self.time = time
        self.name = name
        self.grounds = grounds
        self.spikes = spikes
        self.coins = coins
        self.clouds = clouds
        self.enemies = enemies
        self.boxes = boxes
        self.player = player
        self.flag = flag
        self.direction = None
        self.length = length
        self.scene = scene
        self.paused = False
        self.offset = player.x
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(1000) # Milliseconds

    def update_time(self):
        self.time -= 1
        self.scene.update_time_text()
        if self.time <= 0:
            self.timer.stop()
            self.player.die()

    def update(self):

        direction = self.direction
        player = self.player
        grounds = self.grounds
        spikes = self.spikes
        coins = self.coins
        clouds = self.clouds
        enemies = self.enemies
        boxes = self.boxes
        flag = self.flag

        # set the sprite according to the direction

        player.set_direction(direction)

        # update sprites for enemies

        for enemy in enemies:
            enemy.update_wings()

        if player.has_won or player.is_dead:
            self.scene.timer.stop()
            self.timer.stop()
        else:
            if player.y_vel is not 0:
                player.on_ground = False

            player.y_vel += player.y_acc
            player.y += player.y_vel

            if player.y >= GAME_HEIGHT:
                player.die()

            else:

                # VERTICAL COLLISION DETECTION

                player.setY(player.y)
                dy = player.y_vel
                next_y = 0

                for obstacle in player.collidingItems():

                    if type(obstacle) in (Coin, Cloud, Enemy, Flag):

                        self.detect_hit(obstacle)

                    elif type(obstacle) in (Ground, Box, Ice, Rock, Spike):

                        if not (player.x + player.width == obstacle.x or player.x == obstacle.x + obstacle.width):

                            if dy > 0:
                                if type(obstacle) == Spike:
                                    player.die()
                                else:
                                    player.y_vel = 0
                                    player.on_ground = True
                                    next_y = obstacle.y - player.height
                            
                            elif dy < 0:
                                player.y_vel = 0.5
                                next_y = obstacle.y + obstacle.height

                if next_y is not 0:
                    
                    player.y = next_y
                    player.setY(player.y)

            if not player.is_dead:

                # HORIZONTAL COLLISION DETECTION
                
                if direction is not None:

                    if direction == LEFT:
                        dx = 5

                    elif direction == RIGHT:
                        dx = -5
                    
                    # first set the player new coordinates according to the direction

                    player.x -= dx
                    player.setX(player.x)

                    if player.x < 0:

                        player.x = 0
                        player.setX(player.x)

                    elif player.x > GAME_WIDTH - player.width:

                        player.x = GAME_WIDTH - player.width
                        player.setX(player.x)

                    else:
                    
                        next_x = dx
                
                        for obstacle in player.collidingItems():

                            if type(obstacle) in (Coin, Cloud, Enemy, Flag):
                                
                                self.detect_hit(obstacle)

                            elif type(obstacle) in (Ground, Box, Spike, Ice, Rock):
                                
                                if not (player.y + player.height == obstacle.y or player.y == obstacle.y + obstacle.height):
                            
                                    if dx > 0:
                                        next_x = -(obstacle.x + obstacle.width - player.x - dx)

                                    elif dx < 0:
                                        next_x = player.x + player.width - obstacle.x + dx
                                        
                                    break

                        self.offset -= next_x

                        # if the offset is less than half of the screen
                        # we move the player and keep the scene still
                        
                        if self.offset < 300 or self.offset > self.length - 600:
                            
                            # move player back after checking for collisions

                            if next_x is 0:
                                player.x += dx
                                player.setX(player.x)
                        else:

                            # if offset is more than half of the screen
                            # stop player from moving and start moving scene

                            player.x += dx
                            player.setX(player.x)

                            # move everything and keep player still
                            
                            if next_x is not 0:
                                for ground in grounds:
                                    ground.x += next_x
                                    ground.setX(ground.x)

                                for enemy in enemies:
                                    enemy.x += next_x
                                    enemy.setX(enemy.x)

                                for box in boxes:
                                    box.x += next_x
                                    box.setX(box.x)

                                for coin in coins:
                                    coin.x += next_x
                                    coin.setX(coin.x)

                                # move clouds a little bit slower

                                for cloud in clouds:
                                    cloud.x += (next_x / 2)
                                    cloud.setX(cloud.x)

                                for spike in spikes:
                                    spike.x += next_x
                                    spike.setX(spike.x)

                                flag.x += next_x
                                flag.setX(flag.x)
                
            else:
                self.timer.stop()

    def detect_hit(self, obj):

        if type(obj) == Coin and obj.isVisible():
            self.player.points += 1
            obj.setVisible(False)
            self.scene.update_point_text()

        elif type(obj) == Flag:
            self.scene.display_win_menu(self.player.points, self.time)
            self.player.has_won = True

        elif type(obj) == Enemy:
            self.player.die()
            self.timer.stop()