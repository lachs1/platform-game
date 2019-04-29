import unittest
from resourceloader import ResourceLoader
from game_objects.player import Player
from game_objects.flag import Flag
from corrupt_file_exception import CorruptedMapFileError

class TestMaps(unittest.TestCase):

    def setUp(self):
        self.resourceloader = ResourceLoader()
        self.game = None
    
    def test_woodland(self):

        self.game = self.resourceloader.load("maps/woodland.txt")

        self.assertEqual(60, self.game.time)
        self.assertEqual("Woodland", self.game.name)
        self.assertEqual(6440, self.game.length)
        self.assertEqual(70, self.game.player.x)
        self.assertEqual(6300, self.game.flag.x)
        self.assertEqual(Player, type(self.game.player))
        self.assertEqual(Flag, type(self.game.flag))
        self.assertEqual(107, len(self.game.grounds))
        self.assertEqual(28, len(self.game.spikes))
        self.assertEqual(31, len(self.game.boxes))

    def test_iceland(self):

        self.game = self.resourceloader.load("maps/iceland.txt")

        self.assertEqual(60, self.game.time)
        self.assertEqual("Iceland", self.game.name)
        self.assertEqual(6230, self.game.length)
        self.assertEqual(70, self.game.player.x)
        self.assertEqual(6090, self.game.flag.x)
        self.assertEqual(Player, type(self.game.player))
        self.assertEqual(Flag, type(self.game.flag))
        self.assertEqual(64, len(self.game.grounds))
        self.assertEqual(34, len(self.game.spikes))
        self.assertEqual(41, len(self.game.boxes))

    def test_with_corrupted_file(self):

        raised = None
        try:
            self.resourceloader.load("maps/corrupted_map.txt")
        except CorruptedMapFileError as e:
            raised = e

        self.assertNotEqual(None, raised, "A CorruptedMapFileError was not thrown.")

if __name__ == '__main__':
    unittest.main()