import unittest
from ex47.game import Room

class TestStringMethods(unittest.TestCase):

    def test_room(self):
        gold = Room("GoldRoom",
                    """ This room has gold"""
                   )
        self.assertEqual(gold.name, "GoldRoom")
