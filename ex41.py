# Word Drills

# Class - Tell Python to make a new kind of thing
# Object - Two meanings: the most basic kind of thing, and any instance of some thing.
# Instance - what you get when you tell python to create a class (as an object?)
# def - how you define a function within a class
# self - inside the functions in a class, self is a variable for the instance, object, being accessed
# inheritance - The concept that one class can inherit traits from another class, much like you are your parents
# composition - The concept that a class can be composed of other classes as parts, much like how a car has wheels.
# attribute - A property classes have that are from composition and are usually variables
# is-a - a phrase to say that something inherits from another, as in a Salmon is-a Fish
# has-a - a phrase to say that something is composed of other things or has a trait, as in a salmon has-a mouth

# Phrase Drills

# Will drill the statements

#oop_test.py

import random
from urllib import urlopen #must be some function that opens a url
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = [] # global variable? Shows up in function convert()
PHRASES = {
	"class ###(###):":
	"Make a class named ### that is-a ###.",
	"class ###(object):\n\tdef  __init__(self, ***)" :
	"class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self, @@@)":
	"class ### has-a function named *** that takes self and @@@ parameters.",
	"*** = ###()":
	"Set *** to an instance of class ###.",
	"***.***(@@@)":
	"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english": #remember, argv[0] is script name
	PHRASE_FIRST = True #if there are two arguments to the script and the second one
	# is english, set to true
	
# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #will return a list of each line
	WORDS.append(word.strip()) #begins populating the WORDS list and stripping
	#off whitespace or \n characters (space characters)
	

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("###"))]
# populates class_names[] with random words for each ### in snippet. They are all
# capitalized. Looks like a mad-lib type exercise to me using words (or phrases)
# from the website. basically choosing random lines
# WORDS can be passed as a read-only local variable even though it is global
	other_names = random.sample(WORDS, snippet.count("***"))
	#same as before without capitalizing
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		# for a random amount of parameters, 1 to 3, it will select
		# words and join them in strings that have comma seperations
		# these comma-including strings will be places in the list param_names
		# I am assuming the join characters are not used if random is 1
		
	for sentence in snippet, phrase: #two layer list containing both main lists
		result = sentence[:] # will store snippet in sentence, then store phrase
		#on next loop
		
		#fake class names
		for word in class_names:
			result = result.replace("###", word, 1)
		#good that it kept this logic in the same function. The ###s were meant
		# to store class names and we counted in the snippet
		# We already counted the ###'s to store class names, so we know the
		#class name amount is good. We now replace each ### 1 time
		# with an item from the class_names list. The replace function does
		# 1 at a time for each word in the list as it works through 'result'
		
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			#same as above, incrementally finds the *** and replaces them with words
			# from the list
			
		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			#these list items can have up to two ", "s between words
			
		results.append(result) #results is a different var from result
		# will pass through the snippets and phrases arguments and
		# perform this work until a list is created
		
	return results
	
# Keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet] #retrieves the value
			question, answer = convert(snippet, phrase)
			#enters the key and value into our convert function which essentially
			# are going to do the same thing to both side of the dictionary
			# a new two-level list will be created with question/answer pairs
			if PHRASE_FIRST: #if the script argument is 'english'
				question, answer = answer, question #reverses the list
				
			print question
			raw_input("> ")
			print "ANSWER:  %s\n\n" % answer
except EOFError: #end of file error with no input to raw_input
	print "\nBye"
	
# EXERCISE Read through code and state classes, functions, objects, paramneters
# BELOW is code for exercise 


#"""Describes the tiles in the world space."""
#__author__ = 'Phillip Johnson'

#import items, enemies, actions, world

 # Create class Maptile with an __init__ that takes parameters x and y.
class MapTile(object): #Creates the MapTile
    """The base class for a tile within the world space"""
    def __init__(self, x, y): #defines the class creation, and takes two parameters
    #seems that when you enter the class as a parameter in any of the functions below, it initiates the
    #object as a room with the two arguments
    #each room has its own special changes to the base class
        """Creates a new tile.

        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y #puts the arguments into a variable object within the class
# Class MapTile has a function named intro_text
    def intro_text(self): #not used
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()
# Class MapTile has a function named modify_player that takes parameter the_player
    def modify_player(self, the_player): #not used
        """Process actions that change the state of the player."""
        raise NotImplementedError()
# Class MapTile has a function named adjacent_moves
    def adjacent_moves(self): #will be the class instance roomname.adjacent_moves()
        """Returns all move actions for adjacent tiles."""
        moves = [] # list to store moved
        if world.tile_exists(self.x + 1, self.y): #if exists, returns that particular dictionary key value
        # which will be a room object
            moves.append(actions.MoveEast()) #appends the MoveEast() action from the action module and appends to moves
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves # returns the possible adjacent move options from the actions module
# Class MapTile has a function named available_actions
    def available_actions(self): #room available actions
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves() #available actions from adjacent moves
        moves.append(actions.ViewInventory()) #add viewinventory from actions module to the moves list

        return moves #return moves list with adjacent moves and the newly added viewinventory

# Class StartingRoom is-a Maptile
class StartingRoom(MapTile): #an instance of the maptile class
# Class StartingRoom has a function intro_text
    def intro_text(self): #StartingRoom.intro_text() will return some text
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
# Class StartingRoom has a function modify_player that takes parameter the_player
    def modify_player(self, the_player): #startingroom.modifyplayer(player) will do nothing
        #Room has no action on player
        pass

# Make class EmptyCavePath is-a Maptile
class EmptyCavePath(MapTile):
# Class EmptyCavePath has a function intro_text
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
# Class EmptyCavePath has a function modify_player that takes parameter the_player
    def modify_player(self, the_player):
        #Room has no action on player
        pass

# Class LootRoom is-a Maptile that has a __init__ with parameters x, y, and item
class LootRoom(MapTile):
    """A room that adds something to the player's inventory"""
    def __init__(self, x, y, item): #needs some kind of item passed as an argument. A new type of maptile.
    #the init statement will use the init from the parent class using super(). the item is
    #specific for this type of room using the self.item line
        self.item = item
        super(LootRoom, self).__init__(x, y)
# class LootRoom has a function add_loot that takes parameter the_player
    def add_loot(self, the_player): #adds the item this room has to the specified player
        the_player.inventory.append(self.item) #uses the inventory.append method from an object added as argument
# class LootRoom has a function modify_player that takes paramter the_player
    def modify_player(self, the_player):
        self.add_loot(the_player) #calls the add loot function using the lootroominstance.add_loot(player)
        #no idea why add_loot is kept seperate. perhaps to keep consistent with modify_player(player)

# Class FindDaggerRoom is-a LootRoom that takes parameters x, y and passes
# parameter items.Dagger into it's parent, MapTile
class FindDaggerRoom(LootRoom): #part of the lootroom subclass
    def __init__(self, x, y):
        super(FindDaggerRoom, self).__init__(x, y, items.Dagger()) #specifies the item to be a dagger from items module
# DONE WITH EXERCISE, THATS PLENTY
    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super(Find5GoldRoom, self).__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        Someone dropped a 5 gold piece. You pick it up.
        """


class EnemyRoom(MapTile): #new type of room subclass
    def __init__(self, x, y, enemy): #adds an enemy
        self.enemy = enemy #object for enemy in the room
        super(EnemyRoom, self).__init__(x, y) #inherits these arguments from super()

    def modify_player(self, the_player):
        if self.enemy.is_alive(): #checks if enemy is alive from some other module
            the_player.hp = the_player.hp - self.enemy.damage #decreases a player hp value from another class
            # by the enemy.damage value from an enemy class
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
            # new string.format seems to add the values in the {} fields

    def available_actions(self): # must overwrite the same method from parent class. returns the
    # adjacent_moves() object so I'm assuming we can't use inventory
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)] #two from the actions module
        else:
            return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom): #enemy room instance for giant spider. has it's own intro text.
# seems enemy hp and other properties must be in the object for the enemy
    def __init__(self, x, y):
        super(GiantSpiderRoom, self).__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super(OgreRoom, self).__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An ogre is blocking your path!
            """
        else:
            return """
            A dead ogre reminds you of your triumph.
            """


class SnakePitRoom(MapTile): #a particular room that uses maptile. 
    def intro_text(self):
        return """
        You have fallen into a pit of deadly snakes!

        You have died!
        """

    def modify_player(self, player): # modifies the player attribute hp
        player.hp = 0


class LeaveCaveRoom(MapTile): # another instance of MapTile
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modify_player(self, player): # this instance alters the player.victory object
        player.victory = True
