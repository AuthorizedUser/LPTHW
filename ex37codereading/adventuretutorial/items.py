"""Describes the items in the game."""
__author__ = 'Phillip Johnson'


class Item(object):
    """The base class for all items"""
    def __init__(self, name, description, value): #defines attributes for all items
        self.name = name
        self.description = description
        self.value = value

    def __str__(self): # allows this object to be used as a string when printed
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item): #sub class of Item
    def __init__(self, name, description, value, damage): #defines explicitly, no super()
        self.damage = damage #weapon-instance.damage
        super(Weapon, self).__init__(name, description, value) #passes the arguments up to the class

    def __str__(self): #overrides its base class
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon): #another weapon type
    def __init__(self):
        super(Rock, self).__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Gold(Item): # gold subclass, contains an argument for the amount of gold
    def __init__(self, amt):
        self.amt = amt
        super(Gold, self).__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
