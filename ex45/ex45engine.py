from sys import exit

import ex45armies #imports units into itself


class LocationEngine(object):

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

class BattleEngine(object):
	"""Engine() instance will instantiate Battle as an object that
	it manipulates when battles commence."""

	def __init__(self, player_army, enemy_army):
		"""Place two army objects in the init parameters"""
		self.pa = player_army
		self.ea = enemy_army

	def pre_battle(self):
		"""Runs army refresh and sort routines"""

		self.pa.refresh()
		self.ea.refresh()
		self.pa.sort_units()
		self.ea.sort_units()

	def change_conditions(self, newconditions='clear'):
		"""Changes location conditions. Current possibilities
		include "mud" and "rain""""

		self.pa.loc_conditions(newconditions)
		self.ea.loc_conditions(newconditions)

	def battle_commence(self):
		"""Begins the battle sequence for the battle object
		Returns "player routed", "player surrounded",
		"enemy routed", "enemy surrounded""""

		ai = self.ea.ai #ai method to be called

		self.pre_battle()

		statuspa = "ok"
		statusea = "ok"

		while statuspa == "ok" and statusea == "ok":

			nextpa = self.pa.unitorder[self.pa.next_move] #key nextpa
			nextea = self.ea.unitorder[self.ea.next_move]
			paunit = self.pa.unitlist[nextpa] # object next unit
			eaunit = self.ea.unitlist[nextea] # PRIOR to increment

			self.pa.print_engagements()
			self.ea.print_enemy_reserves()

			# PLAYER BLOCK
			paunit.sitrep()
			aactions = paunit.available_actions(ea) #print actions, get dictionary
			if aactions != {}:
				player_choice = raw_input("Enter Choice $")
				while player_choice not in aactions.keys():
					player_choice = raw_input("Re-input $")
				aactions[player_choice] #performs the chosen action
			estatus = self.ea.status_check()
			if estatus == "routed" or estatus == "surrounded":
				print "DEBUG. YOU WIN"
				return ("enemy " + estatus)

			# ENEMY BLOCK
			eaunit.sitrep()
			raw_input("Continue $)
			aactions = self.ea.available_actions(pa)
			if aactions != {}:
				ai_choice = ai(aactions,
							   eaunit.type,
							   pa.unitlist,
							  )
				if ai_choice not in aactions.keys():
					print "DEBUG: AI CHOICE NOT IN KEYS"
				aactions[ai_choice]
			pstatus = self.pa.status_check()
			if pstatus == "routed" or pstatus == "surrounded":
				print "DEBUG. YOU LOSE"
				return ("player " + estatus)


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
# DONE

# a battle(army, army) class will be needed
# This need to include an 'available actions list parse' type method
# that reads the second returned value from action functions
# DONE

# play_player_army = ex45armies.####(###)
# play_map = Map()
# play_map.load("ex45locations.py") #should include location dictionary
#
# engine_object = Engine(play_map, play_player_army)

#BATTLE CLASS
# use list comprehensions for unit order if needed
#DONE

# An battle.sort__turn_order() method will be needed when units
# are added or removed. Will still maintain 'unit.tookturn' for the
# current turn. (0 or 1) The turn_order return string can have a
# sequence with the unitlist dict keys
# Turn order is type: archer, infantry, spearmen, cavalry
#DONE

# START: ARMY REFRESH > SORT UNITS >
# > PLAYERARMY.PRINT_ENGAGEMENTS
# > ENEMYARMY.PRINT_ENEMY_RESERVES

# AFTER BATTLE STARTS:
# PLAYERUNIT SITREP > PLAYERUNIT ACTIONLIST > INPUT ACTION >
#  > ENEMYARMY.STATUS_CHECK
# ENEMYUNIT SITREP > ENEMYUNIT ACTIONLIST > AI ACTION >
# > PLAYERARMY.STATUS_CHECK
# > PLAYERARMY.PRINT_ENGAGEMENTS
# > ENEMYARMY.PRINT_ENEMY_RESERVES
# > PLAYERUNIT SITREP.......... >>>>>
# Call on next unit by unitlist[unitorder[next_move]]
# Call on enemyarmy.ai by using its type argument
# enemyarmy.ai(actiondict, enemyunit.type)

# engine.battle.status is run after every turn. It checks the
# army statuses, and also resets the .tookturn counters to
# 1 if all units have .tookturn == 0. The '0, 1' rather than
# true false is simply for extensibility in case another
# unit type is implemented that gets more than 1 turn.
