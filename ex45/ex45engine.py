from sys import exit

import ex45armies #imports units into itself


class Engine(object):
	
	def __init__(self, map, player_army):
		self.map = map
		self.player_army = player_army
		# Engine needs to recognize re-input in command returns from
		# actionlist. It will re-run the input method. can use a
		# while "re-input" not in command: or something similar
		# to contain this block of code which will likely be in a for
		# loop
		
		#engine needs a for loop to loop through player and enemy 
		# units alternately
		
class Battle(object):
	"""Engine() instance will instantiate Battle as an object that
	it manipulates when battles commence. Battle can return 'routed'/
	'captured'/'won'"""

	def __init__(self, player_army, enemy_army):
		
		# use list comprehensions for unit order if needed

		# An battle.sort__turn_order() method will be needed when units
		# are added or removed. Will still maintain 'unit.tookturn' for the
		# current turn. (0 or 1) The turn_order return string can have a
		# sequence with the unitlist dict keys
		# Turn order is type: archer, infantry, spearmen, cavalry
		
		# engine.battle.status is run after every turn. It checks the
		# army statuses, and also resets the .tookturn counters to
		# 1 if all units have .tookturn == 0. The '0, 1' rather than
		# true false is simply for extensibility in case another
		# unit type is implemented that gets more than 1 turn.
		
class Map(object):
	"""Contains the dictionary list of location objects
	load(loc_file):
		imports location file into a dictionary attribute
		loc_file: locations file to be imported
	travel_to(loc_string):
		Looks up the next location and returns
		loc_string is returned from previous location to point our 
		journey towards the next location"""
		

#don't forget 'captured' condition if all units in army are captured.
# the condition can pass to the location instance for the scenario

# a battle(army, army) class will be needed
# This need to include an 'available actions list parse' type method
# that reads the second returned value from action functions

play_player_army = ex45armies.####(###)
play_map = Map()
play_map.load("ex45locations.py") #should include location dictionary

engine_object = Engine(play_map, play_player_army)