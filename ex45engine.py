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