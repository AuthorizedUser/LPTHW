# 
from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		pass
		
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_m = scene_map
		#self.next_s_string = "None" MISTAKE: The function kept calling this
		# variable instead of the function variable
		# VESRSION 1 self.next_s_string = "debugtest"
		
	def play(self):
		"""Plays through the scenes, they return the next scene"""
		current_scene = self.scene_m.opening_scene()
		#returns what scene is returned from function as a text string
		count_scenes = len(self.scene_m.scene_list)
		#Mistake: forgot len function
		#print "DEBUG: COUNT SCENES: %r. next_s_string: %r." % (count_scenes, self.next_s_string)
		for scene_number in range(1, count_scenes):
		#notice the '1' in range which causes it to be one scene shorter
		#due to opening scene
			next_scene_string = current_scene.enter()
			current_scene = self.scene_m.next_scene(next_scene_string)
			# VERSION 1 next_scene = self.scene_m.next_scene(self.next_s_string)
			#NEXT VERSION - Should just return the scene object from scene map
			#then run scene.enter() from here
			#returns next scene... which could be 'death' This is per the 
			#exercise description that each room tells the engine
			#what room to run next
			# VERSION 1 self.next_s_string = returned #next scene passed back into the variable
		raise RuntimeError("DEBUG: This should not print unless scenes run out" \
		" before the for loop terminates or program ends")
		

class Death(Scene): 
	def enter(self):
		print "You are dead"
		exit()
		
class CentralCorridor(Scene):

	def enter(self):
		print "You enter a central corridor. A furry 'Gothon' appears and begins"
		print "to ask the player logical questions. Due to an evolutionary flaw,"
		print "Gothons cannot process jokes and irony without their brain short-"
		print "circuiting and killing them."
		pointless = raw_input("> CONTINUE >")
		print '-' * 20
		print "GOTHON >>> This ship is ours. Prepare to get blasted."
		pointless = raw_input("> CONTINUE >")		
		print "-" * 20
		print "\n1. Prepare to be an idiot\n2. Okay, I accept my fate"
		print "3. Why did the chicken cross the road?"
		print "4. Your mom hears that same statement all the time."
		response = raw_input("> RESPONSE NUMBER >")
		if "4" in str(response):
			print "The Gothon begins laughing uncontrollably..."
			pointless = raw_input("> CONTINUE >")
			print "The Gothon then explodes into a cloud of confetti"
			print "You proceed down the hallway towards the Armory"
			return "laser_weapon_armory"
		else:
			#print "DEBUG: Else loop triggered"
			return "death"
		
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You enter a Laser Weapon Armory. There is a neutron bomb in"
		print "a large cage with a keypad on a gate."
		print "The keypad has numbers all over, but you note the \'8\' number"
		print "is very worn."
		print "-" * 20
		for i in range(1, 4):
			number = raw_input("> GUESS A NUMBER. ATTEMPT %d >" % i)
			if int(number) == 8:
				print "You acquire a neutron bomb. You arm it, setting the timer"
				print "to 10 minutes... just in case you don't make it. You "
				print "continue to the bridge."
				print "-" * 20
				return "the_bridge"
			else:
				print "INCORRECT RESPONSE. PLEASE TRY AGAIN"
		print "YOU ARE INCORRECT, ELECTRIC ZAPPER INITIATED"
		print "The electric gate zaps you and fries you to a crisp"
		return "death"
				
class TheBridge(Scene):

	def enter(self):
		print "You enter the bridge. There are tons of knobs, vacuum tubes, and"
		# MISTAKE: FORGOT END QUOTE
		print "CRT television screens. Along with many dials you don't understand."
		print "How on earth do the pilots fly this thing? It's so complex"
		print "-" * 20
		pointless = raw_input("> CONTINUE >")
		print "A Gothon appears and makes a threat:"
		print "\"I will now destroy you with my blaster unless you take me to the"
		print "nuetron bomb we seek! I will let you live if you help me get it!\""
		treasure = raw_input("> GIVE SOMETHING TO THE GOTHON >")
		treaslist = treasure.split(" ")
		if "nuetron" in treaslist or "bomb" in treaslist:
			print "You hand the armed nuetron bomb to the Gothon."
			print "The Gothon responds:"
			print "\"You are wise and may live another day. Now leave!\""
			pointless = raw_input("> CONTINUE >")
			print "You run on to the escape pod deck"
			return "escape_pod"
		else:
			print "The Gothon vaporizes you with its blaster"
			return "death"
		
class EscapePod(Scene):

	def enter(self):
		print "You enter the room with escape pods. There are three pods"
		print "Pod 1 has smoke coming from its console."
		print "Pod 2 has water all over."
		print "Pod 3 has a broken stereo system that cannot be turned off and"
		print "continually loops Neil Diamond concert recordings"
		pod = int(raw_input("> CHOOSE A POD NUMBER >"))
		if pod == 3:
			print "You get in Pod 3, the sounds of Neil Diamond live surround"
			print "you, with the bass stuck on full volume."
			pointless = raw_input("> START POD >")
			print "The pod fires into space, you see the space ship from a far"
			print "distance. It explodes with a blinding flash. The Gothons"
			print "got the bomb they were searching for after all."
			print "-" * 20
			pointless = raw_input("> CONTINUE >")
			print "As the pod continues it's three-month journey to the nearest"
			print "space station, you are continually blasted with the Neil"
			print "Diamond live album."
			pointless = raw_input("> CONTINUE >")
			print "You begin to wonder if you should have just let the Gothon"
			print "blast you."
			print '-' * 20
			print "Game Over! Victory!"
			exit()
		else:
			print "You get into pod %r" % pod
			pointless = raw_input("> START POD >")
			print "The pod malfunctions and explodes!"
			return "death"
		

class Map(object):

	def __init__(self, start_scene):
		self.start_s = start_scene
		self.scene_list = {
							"central_corridor": CentralCorridor(),
							"laser_weapon_armory": LaserWeaponArmory(),
							"the_bridge": TheBridge(),
							"escape_pod": EscapePod(),
							"death": Death(), #mistake, needed a final comma!
							}
		self.scene = "debugtest"				
		pass
		
	def next_scene(self, scene_name):
		"""Uses the text scene_name parameter to commence the
		 given scene function. Calls the enter() method from 
		 the scene in question. returns string name of next scene"""
		# VERSION 1 self.scene = self.scene_list[scene_name]
		#creates instance of object
		# VERSION 1return self.scene.enter() #mistake, forgot to return from here
		#Version 2, just return the scene object. Need to spread this code
		#out into a few variables for clarity
		return self.scene_list[scene_name]
		
	def opening_scene(self):
		"""Opens the starting scene specified when the Map()
		object instance was created. Returns string name of next scene"""
		return self.scene_list[self.start_s]
		#MISTAKE: Forgot a return here. It runs both corridor scene and also
		#the opening_scene functions, both need to return.
		#VERSION 2: Should just return the scene object...	
	
a_map = Map('central_corridor') # parameter is the start scene variable
# a_map is an instance of Map with the central corridor parameter
a_game = Engine(a_map) #engine receives a map object as the argument
#Engine instance argument is the game map object
a_game.play() #runs the play function with no parameters
# play is a function of a_game that now has a_map as an attribute