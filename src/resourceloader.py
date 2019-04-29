from game_objects.ground import Ground
from game_objects.coin import Coin
from game_objects.flag import Flag
from game_objects.spike import Spike
from game_objects.player import Player
from game_objects.box import Box
from game_objects.cloud import Cloud
from game_objects.enemy import Enemy
from game_objects.ice import Ice
from game_objects.rock import Rock
from game import Game
from random import randint
from corrupt_file_exception import CorruptedMapFileError

class ResourceLoader():

    def load(self, path):

        critical_data = {
            "name" : None,
            "time" : None
        }

        #map data holds all of the game objects for example grounds and spikes and also length of the map

        map_data = {
            "G" : [],
            "I" : [],
            "R" : [],
            "S" : [],
            "C" : [],
            "F" : None,
            "P": None,
            "B" : [],
            "E" : [],
            "length" : 0
        }

        # reads critical data: name and time of the map

        def read_critical_data(args):
            args = clean_list(args)
            if len(args) == 2:
                for props in args:
                    prop = props.split(":") 
                    if prop[0] in critical_data:
                        if prop[0] == "name":
                            critical_data[prop[0]] = prop[1].capitalize()
                        elif prop[0] == "time":
                            try:
                                critical_data[prop[0]] = int(prop[1])
                            except ValueError:
                                raise CorruptedMapFileError("Wrong type of time. needs to be int.")
                    else:
                        raise CorruptedMapFileError("Wrong property type in game file (CRRITICAL DATA). Allowed types: are 'name' and 'time'.")
            else:
                raise CorruptedMapFileError("Wrong amount of properties in game file (CRITICAL DATA).")

        def read_map_data(args):
            args = clean_list(args)
            # stage length is determined by the first map row.
            stage_length = 0
            y = 0
            for index, line in enumerate(args):
                x = 0
                line = line.rstrip().split(',')
                for column in line:
                    column = column.capitalize()
                    if column in map_data:
                        if column == 'G': # ground
                            ground = Ground(0, 0, 70, 70, x, y)
                            map_data[column].append(ground)
                        elif column == 'I': # ice
                            ice = Ice(0, 0, 70, 70, x, y)
                            map_data[column].append(ice)
                        elif column == 'R': # rock
                            rock = Rock(0, 0, 70, 70, x, y)
                            map_data[column].append(rock)
                        elif column == 'C': # coin
                            coin = Coin(0, 0, 38, 38, x + 19, y + 19)
                            map_data[column].append(coin)
                        elif column == 'E': # enemy
                            enemy = Enemy(0, 0, 70, 30, x, y)
                            map_data[column].append(enemy)
                        elif column == 'S': # spike
                            spike = Spike(0, 0, 70, 35, x, y + 35)
                            map_data[column].append(spike)
                        elif column == 'F': # flag
                            if map_data[column] is not None: #only one winning flag per game
                                raise CorruptedMapFileError("Only one winning flag per game.")
                            else:
                                flag = Flag(0, 0, 70, 70, x, y)
                                map_data[column] = flag
                        elif column == 'B': # box
                            box = Box(0, 0, 70, 70, x, y)
                            map_data[column].append(box)
                        elif column == 'P': # player
                            if map_data[column] is not None: # if there ia already an Player added
                                raise CorruptedMapFileError("Only one player per game!")
                            else:
                                player = Player(0, 0, 50, 29, x, y, None)
                                map_data[column] = player
                    x += 70
                # set the stage_length when we are at the 0 index
                if index == 0:
                    stage_length = x
                    map_data["length"] = stage_length
                else:
                    if x != stage_length:
                        raise CorruptedMapFileError("Error while reading map data. All of the rows should have equal amount of blocks.")
                y += 70

        # helper method for cleaning up the list for data prosessing

        def clean_list(a):
            a = a[1:]
            a = list(filter(None, a))
            return a

        # random cloud generator method

        def generate_random_clouds(max):
            
            clouds = []
            start_x = 20
            while start_x < max:
             
                random_y = randint(5, 70)
                cloud = Cloud(0, 0, 100, 42, start_x, random_y)
                clouds.append(cloud)
                random_x = randint(450, 480)
                start_x += random_x

            return clouds

        datas = {
            '#critical': [
                read_critical_data,
                []
            ],
            '#map': [
                read_map_data,
                []
            ]
        }

        try:
            file = open(path)
            line = None
            reading = None

            while line != '':
                line = file.readline()
                parts = line.strip().split( ' ' )
                parts = ' '.join(parts)
                parts = parts.lower()
                if parts in datas:
                    reading = parts
                if reading:
                    datas[reading][1].append(parts)

            for chunk in datas:
                datas[chunk][0](datas[chunk][1])
            
        except IOError:

            raise CorruptedMapFileError("File not found.")

        finally:

            file.close()

        time = critical_data["time"]
        name = critical_data["name"]
        player = map_data["P"]
        grounds = map_data["G"] + map_data["I"] # Grounds and ice are the same
        boxes = map_data["B"] + map_data["R"] # Boxes and rocks are the same
        spikes = map_data["S"] 
        coins = map_data["C"] 
        enemies = map_data["E"] 
        flag = map_data["F"]
        length = map_data["length"]
        clouds = generate_random_clouds(length)

        if (player == None or flag == None):
            raise CorruptedMapFileError("No player or winning flag added in map file.")

        game = Game(time, name, player, grounds, spikes, coins, clouds, enemies, boxes, flag, length, None)
        
        return game