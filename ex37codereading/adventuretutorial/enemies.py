"""Defines the enemies in the game"""
__author__ = 'Phillip Johnson'


class Enemy(object): #base class, initializes with the following variables
    """A base class for all enemies"""
    def __init__(self, name, hp, damage):
        """Creates a new enemy

        :param name: the name of the enemy
        :param hp: the hit points of the enemy
        :param damage: the damage the enemy does with each attack
        """
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy): #giant spider type of enemy
    def __init__(self):
        super(GiantSpider, self).__init__(name="Giant Spider", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super(Ogre, self).__init__(name="Ogre", hp=30, damage=15)
