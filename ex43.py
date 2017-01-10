# Zed Shaw's Version of exercise 43
from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		## Mini opening scene that isn't built into the scene structure
		print "You awaken to find a Gothon in your room, you grab your blaster"
		gotho = Gothon()
		playr = Player()
		fight1 = Combat(playr, gotho)
		fightoutcome = fight1.begin_fight()
		
		if fightoutcome == "lose":
			self.scene_map.next_scene("death")
		if fightoutcome == "win":
			print "Your trusty blaster begins to smoke and pop. It appears it"
			print "has broken! You cast it aside and leave the barracks for"
			print "the central corridor to assess the situation."
		## End mini opening scene. VERSION 2 - Add this to an oop scene structure
		current_scene = self.scene_map.opening_scene()
		
		while True: #was told never to do this....
			print "\n-----------"
			#print "DEBUG: current_scene: %r" % current_scene
			# debug was due to 'central_corridor' runtime argument missing underscore
			next_scene_name = current_scene.enter() #same thing I did
			#passes back a string to be used in next_scene
			current_scene = self.scene_map.next_scene(next_scene_name)
			#pre-planned to write the functions for opening and next scene later

class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	] #odd... no final comma... maybe only matters for dictionaries

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)] #-1 since randint includes end value
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get to the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death' #no idea why Zed chooses single quotes for the returns
			
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip, and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
			
		elif action == "tell a joke" or action == "cheat":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through ther Weapon Armory door."
			return 'laser_weapon_armory'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
		
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "nuetron bomb in its container. There's a keypad lock on the box"
		print "and you need the code to get the bomb out. If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		#testing, randint includes both numbers on front and end arguments
		guess = raw_input("[keypad]> ")
		guesses = 1 #Drill 1. Changed to 1 from 0
		
		while guess != code and guesses < 10 and guess != "cheat": # the less than sign is because
		#the first guess was already blown... so proceed for 9 more
		# MISTAKE: forgot to include cheat condition here as well as below
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
		
		if guess == code or guess == "cheat": #redundant guess == code condition
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else: #could have done an elif guesses = 10.....
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
			
class TheBridge(Scene):

	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door. Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically trying to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'
			
		elif action == "slowly place the bomb" or action == "cheat":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return "escape_pod"
		else:
			print "DOES NOT COMPUTE!"
			return 'the_bridge'
			
		
class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes. It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference. You get to the chamber with the escape pods, and"
		print "now need to pick one to take. Some of them could be damaged"
		print "but you don't have time to look. There's 5 pods, which one"
		print "do you take?"
		
		good_pod = str(randint(1,5))
		guess = str(raw_input("[pod #]> "))
		
		if guess != good_pod and guess != "cheat":
		#mistake: needed to make them all strings for cheat to work
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the voice of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below. As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright start, taking out the Gothon ship at the same"
			print "time. You won!"
			exit(0)
			
			return 'finished' #this doesn't work... used the exit function
		

class Map(object):
	# very similar dictionary to the one I set up. Uses strings to send
	# commands to the engine to pull more scenes
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death':Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name) #returns Map class variable dictionary item
		# which is an object of the scene subclass
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		#simply runs next_scene using the start_scene parameter
		
#Play() method run was moved to the end of the document to make room for exercise 4



# STUDY DRILLS

# 1 Guesses 10 times in loop due to the 'Less than 10" statement. And the
# first guess was a freebie since the guesses variable wasn't declared

# 2 next_scene_name in the play() method is the variable that holds the return
# value from scene.enter()
# Every scene is passed to next_scene(), which returns a string scene name.
# next_scene ALSO returns that scene string name, which gets stored in
# next_scene name
# this string is used as the argument for next_scene, when it is run again
# essentially, next_scene inputs the current scene and outputs the next one
# all as strings

# 3 Added a line 'cheat' that will pass every scene

# 4 Added this and moved the play() method to the end of the document

class Gothon(object): # in true OOP with multiple enemy types  this would
# be a parent class
	def __init__(self):
		self.hp = 10
		self.alive = True
		self.charging = False
		self.attackdmg = 2
		self.chargedmg = 3
		
class Player(object):
	def __init__(self): #MISTAKE: for some reason I put self.__init__. No idea why.
		self.hp = 10
		self.alive = True
		self.attackdmg = 1
		self.chargedefdmg = 4
		
class Combat(object): #MISTAKE: Capitalized 'object'
	"""Creates a combat class between objects player and enemy"""
	def __init__(self, player, enemy):
		self.enemy = enemy
		self.player = player
	
	def begin_fight(self): #MISTAKE: forgot the self argument!
		"""Begins a fight sequence between player and enemy, returning
		win or lose strings based on outcome"""
		while True: # I know... cheap... had to use it here to keep it simple
			print "-" * 10
			print "Gothon HP: %d\tPlayer HP: %d" % (self.enemy.hp, self.player.hp)
			print "Gothon Charging: %r" % self.enemy.charging
			print "-" * 10
			print "Choose an action:\n1. Attack\n2. Defense Shield"
			choice = int(raw_input("> "))
			
			#player moves first
			if choice == 1:
				print "You attack the Gothon! Doing %d damage." % self.player.attackdmg
				self.enemy.hp -= self.player.attackdmg
			elif choice == 2 and self.enemy.charging == True:
				print "The Gothon bashes into the defensive barrier!"
				print "The Gothon takes %d damage!" % self.player.chargedefdmg
				self.enemy.hp -= self.player.chargedefdmg
				self.enemy.charging = False

			
			if self.enemy.hp <= 0:
				print "The Gothon is defeated!"
				self.enemy.alive = False
				return "win"
			
			#gothon moves
			gothonchoice = randint(1,2)
			# MISTAKES: all booleans in the if structure had only one equals sign
			if self.enemy.charging == True:
				print "The Gothon charges into the player!"
				print "The player is hit hard, doing %d damage!" % self.enemy.chargedmg
				self.enemy.charging == False
			elif gothonchoice == 1:
				print "The Gothon attacks, doing %d damage!" % self.enemy.attackdmg
				self.player.hp -= self.enemy.attackdmg
			elif gothonchoice == 2:
				print "The Gothon begins to charge towards you!"
				self.enemy.charging = True
				
			if self.player.hp <= 0: #MISTAKE: Forgot the colon after if statement
				print "You have been defeated!"
				return "lose"
			
			
#probably overly nested... I need to practice my OOP

# STUDY DRILL 5 
# Finite State Machine - A machine that has a finite number of states. I'm assuming
# Zed means that each 'scene' is a state for the Map class to be in.
# The 'finite' means there are only so many and they are preprogrammed
# Finite state machines take external output. In this case, we use a string
# to tell the game engine to run one of those states (Scene subclasses) in the
# map object. The entry action is performed when entering the state with .enter()
# and the exit action is the string return

a_map = Map('central_corridor') # parameter is the start scene variable
# a_map is an instance of Map with the central corridor parameter
#MISTAKE: forgot the underscore
a_game = Engine(a_map) #engine receives a map object as the argument
#Engine instance argument is the game map object
a_game.play() #runs the play function with no parameters
# play is a function of a_game that now has a_map as an attribute