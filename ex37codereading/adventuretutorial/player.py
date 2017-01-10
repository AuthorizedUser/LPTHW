import random
import items, world

__author__ = 'Phillip Johnson'


class Player(object): # single class, no instances apparent
    def __init__(self): #these attributes are set only on initialization important
    #to keep them here and not in the main class since it will reset every time it's called
        self.inventory = [items.Gold(15), items.Rock()] #some attributes of player # inventory list
        #contains some items from list module. One of them has an argument
        self.hp = 100
        self.location_x, self.location_y = world.starting_position # two locations assigned that are unpacked
        # from starting position tuple
        self.victory = False

    def is_alive(self): #player.is_alive seems to return the hp value, else returns False if 0 or less
        return self.hp > 0

    def do_action(self, action, **kwargs): #player.do_action(action, allows named arguments to be added)
        action_method = getattr(self, action.method.__name__) #__name__ is module being run, player
        # getattr should argue getattr(Player, action.method.player) and return Player.action.method.player
        # is action written as a variable?
        # getattr(module, attribute as a string). So it will search the player module
        # for the Action.method.actions string?
        #NOTE: action has not been imported... so it can't be looking there
        #tested... can include an argument in a module call chain... as long as the
        # argument is another object
        # Summary: getattr wants a string in it's second argument.
        # we are giving it an object that includes one of the arguments
        # below, the argument is tile.adjacentmoves() method
        # so our argument returns a list named moves[] than can contain
        # actions.MoveEast() and any other potential actions (or none). MoveDir() items
        # since actions.py is imported into tiles.py, those methods can run here
        # Player.move_east is the method for actions.MoveEast()
        # Need to determine how Player.move_east.name returns
        # So far: action.method.__name__ > actions.MoveEast.method.__name__ >
        # > Player.move_east.__name__ >> "move_east"
        # so it essentially checks the action list for the name of the action in player module
        # and if it is valid. then returns Player.move_east() as the action_method
        # NOTE: Figure out why the methods have been split across two modules
        if action_method:
            action_method(**kwargs)

    def print_inventory(self): #looks like Player.print_inventory prints the inventory list
        for item in self.inventory:
            print item, '\n' #removing the parentheses around these statements fixed
            # the issue with it printing the literal

    def move(self, dx, dy): # dx can be positive or negative and will increment or decrement the objects
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
        #print the location and intro text if the tile exists

    def move_north(self): #uses the move function
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy): #player.attack(enemy)
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon): # if item i in the inventory is part of items.Weapon
                if i.damage > max_dmg: # if the damage is better than max_dmg
                    max_dmg = i.damage #if it's a better weapon increment max_dmg
                    best_weapon = i #the best weapon is now this weapon

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage #modified hp object on enemty by damage
        if not enemy.is_alive(): #if enemy is dead
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp)) #if enemy is alive

    def flee(self, tile): # if player.flee is invoked, looks at all avail moves
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves() #the move[] list
        r = random.randint(0, len(available_moves) - 1) #random integer from zero to available moves
        self.do_action(available_moves[r]) #choose the randomized move

