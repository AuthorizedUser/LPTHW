""" Contains the units that will be used in the enemy army as well
as the player army. Also contains the functons for those units that
define actions on a target.

Unit Hierarchy and abilities

	All units
		All units have the 'defend' ability
			All units can defend, which allows them to withhold two enemy
			engagements simultaneously without routing. If engaged by two
			enemy units, the defenders status will change to 'surrounded'
			and it loses all tactical options until one enemy disengages.
			If the engine detects that all of an armies unit.status
			are 'surrounded', then the army will be captured.
			unit.defending = True during defense
				For this implementation, capture and route have similar
				outcomes, although perhaps some text differences


	Basic Units	- Inherits ALL UNITS abilities
		Infantry can engage any unit (it has no abilities)
			engage only functions when status is 'idle', 'defending',
			or 'fending off'.
			Breaking off an engagement with an enemy is useful in that it
			leaves them exposed to be engaged by an ally if they have not
			yet fallen back.
	Specialists - Inherits PEASANTS abilities (because we all started somewhere)
		Cavalry has the additional "Charge" ability (infantry subclass)
			Charge takes two turns to happen and can be cancelled on
			the turn when it is due to hit, just prior to hitting.
			Charge will immediately route the unit when it completes.
			Cavalry cannot be engaged until the charge lands.
		Spearmen have the additional "Phalanx" ability
			Phalanx() places the Spearmen.status object to phalanx
			Cavalry completing charge will parse the enemy army unit
			dictionary for a phalanx = True argument. The Cavalry will
			be destroyed if it is found. The army with spearmen has one
			opportunity to set up the phalanx before the charge hits.
			Spearmen are sorted to get orders directly before cavalry
			so they are less likely to be engaged, but may have to
			make a difficult decision
			phalanx is similar to engage. It can only be used when
			status is idle, defending, or fending_off
		Archers have a special "engage" action method
			Archer engage: Can engage or route an enemy without engaging
			themselves. On the next turn, the enemy will be hunkered
			down under archer fire if previously idle... with 'engage'
			status. The enemy will be routed if already engaged by a
			friendly unit.
	Not Implemented
		Swordsmen
		Cannons
		Elite Infantry / Hero bodyguard
		Stealth archers (typically unit named 'dark elf' or some shit)
		Fortifications (Castle, tower, fort, motte-and-bailey)
		New 'upgrade' attributes
			Flame arrows (good against wooden forts)


Unit Attributes:
	name: Simply the name of the unit. Completely customizable for various
		races and armies. Is used as the key in the unitlist dictionary
		for the unit object

	status: Similar to recharging hp in normal games. Each unit engage
		method reduces the targets engagement status, and it's own
		METHODOLOGY:
		When engaged by enemy unit and defending == False:
			idle > engaged > routed
		when engaged by enemy unit and defending == True:
			defending > fending_off > surrounded

		Technically, nobody in tactics adventure ever dies

	engaged_with: dictionary of unit.name and unit instance of
		# all enemies that are engaging self

	description: Fully customizable argument on a per unit basis when
	the unit is initialized

	type: infantry, cavalry, spearmen, archer

	loc_conditions: All units have the 'loc_conditions' attribute
		location may alter some unit action methods.
		Rain negates arrows so archers cannot choose who to engage
		(a scenario will have you choose if you	want to await
		 a rainstorm or attack immediately)
		 Mud will inhibit cavalry charges and throw them into disarray
		 prior to the hit sequence

	charging (Cavalry only): True/False Currently in step 2 of charge
	 sequence where a turn has been sacrificed. The cavalry was not
	 engageable in the meantime. Now, the cavalry available_actions
	 includes overrun() and cancel() as an option.

	phalanx (spear only):

"""


class Unit(object):
	"""Base class for all units"""
	# Class constants to be used for status_up(), status_down()
	defensive_statii = ["surrounded", "fending_off", "defending"]
	non_defensive_statii = ["routed", "engaged", "idle"]

	def __init__(self, name=None, description=None):
		"""	__init__(self[, name][, description])
		If name and description are not passed, they will default to None"""
		self.name = name # Plural name
		self.status = "idle"
		self.description = description
		self.army = None
		self.type = None
		self.engaged_with = {} #can contain two enemy units. name and obj
		self.defending = True
		self.loc_conditions = 'clear'
		self.charging = False #status will be idle
		self.phalanx = False #status will be idle
		self.under_fire = False
		self.firing_at = {}

	def defend(self):
		"""Unit falls to a defensive position. Defenders will not
		route when engaged by two enemies, but will be surrounded"""
		self.defending = True
		self.status = "defending"
		print ("{thisunit.name} fall back take a defensive position"
			  + ".").format(thisunit=self)
		raw_input(">")
		self.break_engagement()

	def break_engagement(self):
		"""Increments engagement status for the target party, and self.
		Should only be run when charging = False and when
		len(self.engaged_with) < 2. Prints a string describing
		that the engagement is broken """
		#Will be used for defend, engage, charge (initial), phalanx

		#Gather info on target engaged with
		only_engager_name = self.engaged_with.keys()[0]
		only_engager_obj = self.engaged_with[only_engager_name]

		#Break engagement for target
		del only_engager_obj.engaged_with[self.name]
		only_engager_obj.status_up()

		#Break engagement for self
		del self.engaged_with[only_engager_name]
		self.status_up()

		#Return string describing the break off with the enemy
		if self.status == "engaged":
			print ("{thisunit.name} break off the engagement with"
				  + " {enemy.name}.").format(thisunit=self,
				  enemy=only_engager_obj)
			raw_input(">")
		elif self.status == "fending_off":
			self.defending = False
			print ("{thisunit.name} move out of defensive position."
				  + " {thisunit.name} are no longer fending off"
				  + " {enemy.name}.").format(thisunit=self,
				  enemy=only_engager_obj)
			raw_input(">")

	def continue_engagement(self):
		"""Available action during engagement. Unit continues fighting.
		Prints a string describing the situation available action for
 		engaged, fending_off"""

		if self.status == "engaged":
			print ("{thisunit.name} remain engaged with"
				  + " {enemy.name}.").format(thisunit=self,
				  enemy=only_engager_obj)
			raw_input(">")
		elif self.status == "fending_off":
			print ("{thisunit.name} have taken a defensive position."
				  + " {thisunit.name} are fending off"
				  + " {enemy.name}.").format(thisunit=self,
				  enemy=only_engager_obj)
			raw_input(">")

	def continue_defending(self):
		"""When defending with no engagers, this action continues"""

		print ("{thisunit.name} stay in their defensive position."
			  ).format(thisunit=self)

	def sitrep(self):
		"""Prints the status and engagement situation for the unit"""

		currentstatus = self.status
		if self.charging:
			currentstatus = "charging"
		elif self.phalanx:
			currentstatus = "phalanx"

		print ("{thisunit.name}\t Status: {current}\t"
			   + " Engaged to: {thisunit.engaged_with.keys()}"
			   ).format(thisunit=self, current=currentstatus)
		raw_input(">")

	def status_up(self):
		"""Brings unit's status up one level regardless if defending or
		attacking. Should not be used if status is idle' or 'defending'"""
		if (self.status == defensive_statii[0]
		or self.status == non_defensive_statii[0]:
			print "DEBUG: This function was called in error"

		if self.status in defensive_statii:
			stat_index = defensive_statii.index[self.status]
			self.status = defensive_statii[stat_index - 1]
		elif self.status in non_defensive_statii:
			stat_index = non_defensive_statii.index[self.status]
			self.status = non_defensive_statii[stat_index - 1]
		else:
			print "DEBUG: Error in status_up class"

	def status_down(self):
		"""Brings unit's status down one level regardless if defending or
		attacking. Should not be used if status is 'routed' or
		'surrounded'"""
		if (self.status == defensive_statii[2]
		or self.status == non_defensive_statii[2]:
			print "DEBUG: This function was called in error"

		if self.status in defensive_statii:
			stat_index = defensive_statii.index[self.status]
			self.status = defensive_statii[stat_index + 1]
		elif self.status in non_defensive_statii:
			stat_index = non_defensive_statii.index[self.status]
			self.status = non_defensive_statii[stat_index + 1]
		else:
			print "DEBUG: Error in status_up class"

	def engage(self, target):
		"""	engage(self, target):
		target: enemy unit instance. e.g. enemyarmy1.unit3
		Engage an enemy unit, altering it's status to 'engaged'
		or 'routed' or potentially is blocked by an enemy ability
		returns 'continue' if method works, 're-input' if it doesn't.
		T: Would be nice to come up with a way to manually alter
		the engage text for subclasses when instantiating. However,
		the escape sequences make it difficult to come up with
		an easy solution...
		"""

		if self.status == "fending_off":
			self.break_engagement()

		self.defending = False

		if target.under_fire == True:
			print ("{targ.name} breaks under arrow fire and melee."
				  ).format(targ=target)
			target.break_engagement()
			target.status = "routed"
			print ("{targ.name} routes.").format(targ=target)
			self.status = "idle"
			raw_input(">")

		if target.charging == True:
			print "Target is charging, re-input"
			raw_input(">")
			return "re-input"
		elif target.status == "routed" or target.status == "surrounded":
			print "Target cannot be engaged. re-input"
			raw_input(">")
			return "re-input"
		elif target.status == "idle" or target.status == "defending":
			target.status_down()
			self.status_down()
			self.engaged_with[target.name] = target
			target.engaged_with[self.name] = self
			print ("{thisunit.name} engages {tar.name}"
					+ ".").format(thisunit=self, tar=target)
			raw_input(">")
			return "continue"
		elif target.status == "engaged":
			target.status_down()
			self.status = "idle"
			allyflank = target.engaged_with.items[0][1]
			target.engaged_with.clear()
			del allyflank.engaged_with[target.name]
			print ("{thisunit.name} engages {tar.name}.\n {tar.name}"
					+ " are already engaged by {ally.name}. Attacked"
					+ " in both flanks, {tar.name} breaks.").format(
					thisunit=self, tar=target, ally=allyflank)
			raw_input(">")
		elif target.status == "fending_off":
			target.status_down()
			self.status_down()
			allyflank = target.engaged_with.items[0][1]
			self.engaged_with[target.name] = target
			target.engaged_with[self.name] = self
			print ("{thisunit.name} engages {tar.name}.\n {tar.name}"
					+ " are already engaged by {ally.name}. Attacked"
					+ " from both sides in their defensive position"
					+ ", {tar.name} is surrounded and digs in.").format(
					thisunit=self, tar=target, ally=allyflank)
			raw_input(">")

	def available_actions(self, enemyarmy):
		"""Returns a dictionary of available actions for this unit
		instance. These actions are subclass specific and may not
		always be available, based on the unit's status. Prints
		the dictionary keys for the actions."""

		# For archers - clears the firing list at turn start
		self.firing_at.items()[0][1].under_fire = False
		self.firing_at.clear()

		# Create an engageable units dictionary
		engageablestatus = ["idle", "engaged", "defending",
						    "fending_off"]
		engageable = [unit for unit in enemyarmy.unitlist.values() if \
					  unit.status in engageablestatus]
		engactions = {}

		for unit in engageable:
			engactions["engage " + unit.name] = self.engage(unit)

		if self.status == "idle":
			idleactions = {"defend": self.defend()}
			idleactions.update(engactions)
			print idleactions.keys()
			return idleactions
		elif self.status == "engaged":
			engagedactions = {"defend": self.defend(),
							  "continue_engagement":
							  self.continue_engagement(),
							 }
		elif self.status == "routed":
			print "{thisunit.name} has routed and cannot act".format(
				  thisunit=self)
			return = {}
		elif self.status == "defending":
			defendingactions = {"continue_defending":
								self.continue_defending()}
			defendingactions.update(engactons)
			print defendingactions.keys()
			return defendingactions
		elif self.status == "fending_off":
			fending_offactions = {"continue_engagement":
								  self.continue_engagement()
								 }
			fending_offactions.update(engactions)
			print fending_offactions.keys()
			return fending_offactions
		elif self.status == "surrounded":
			print "{thisunit.name} is surrounded and cannot act".format(
				  thisunit=self)
			return = {}


class Infantry(Unit):
	"""Infantry(Unit) subclass. Used for sword/club style infantry.
	.type: 'infantry'
	"""
	def __init__(self):
		super(Infantry, self).__init__(name=None, description=None)
		self.type = "infantry"


class Archer(Unit):
	"""Archer(Unit) subclass. Used for ranged units.
	.type: 'archer'
	"""

	def __init__(self):
		super(Archer, self).__init__(name=None, description=None)
		self.type = "archer"
		self.firing_at = {}

	def shoot(self, target):
		"""Places target unit "under fire" which will make it
		route if attacked. The archer does not need to engage it.
		On the next turn for the archer, the unit will no longer
		be under fire."""

		self.firing_at[target.name] = target
		target.under_fire = True
		#These will be cleared at start of archer's next turn

		if (target.status == "engaged" or
			target.status == "fending_off")
			print ("{targ.name} breaks due to fighting and taking"
				  + " arrow fire.").format(targ=target)
			target.break_engagement()
			target.status = "routed"
			print "{targ.name} is routed.".format(targ=target)
			self.firing_at.clear()
			target.under_fire = False
			raw_input(">")


	def available_actions(self, enemyarmy):
		"""Returns a dictionary of available actions for this unit
		instance. These actions are subclass specific and may not
		always be available, based on the unit's status. Prints
		the dictionary keys for the actions."""

		# For archers - clears the firing list at turn start
		self.firing_at.items()[0][1].under_fire = False
		self.firing_at.clear()

		# Create an engageable units dictionary
		engageablestatus = ["idle", "engaged", "defending",
						    "fending_off"]
		engageable = [unit for unit in enemyarmy.unitlist.values() if \
					  unit.status in engageablestatus]
		engactions = {}
		archactions = {}

		for unit in engageable:
			engactions["engage " + unit.name] = self.engage(unit)

		for unit in engageable:
			archactions["shoot " + unit.name] = self.shoot(unit)

		if self.status == "idle":
			idleactions = {"defend": self.defend()}
			idleactions.update(engactions)
			idleactions.update(archactions)
			print idleactions.keys()
			return idleactions
		elif self.status == "engaged":
			engagedactions = {"defend": self.defend(),
							  "continue_engagement":
							  self.continue_engagement(),
							 }
		elif self.status == "routed":
			print "{thisunit.name} has routed and cannot act".format(
				  thisunit=self)
			return = {}
		elif self.status == "defending":
			defendingactions = {"continue_defending":
								self.continue_defending()}
			defendingactions.update(engactions)
			defendingactions.update(archactions)
			print defendingactions.keys()
			return defendingactions
		elif self.status == "fending_off":
			fending_offactions = {"continue_engagement":
								  self.continue_engagement()
								 }
			fending_offactions.update(engactions)
			fending_offactions.update(archactions)
			print fending_offactions.keys()
			return fending_offactions
		elif self.status == "surrounded":
			print "{thisunit.name} is surrounded and cannot act".format(
				  thisunit=self)
			return = {}


class Cavalry(Unit):

	def __init__(self):
		super(Cavalry, self).__init__(name=None, description=None)
		self.type = "cavalry"

	def begin_charge(self):
		"""Cavalry ends its turn and begins the charge sequence. No
		target is necessary"""

		### MUD IF STATEMENT HERE


		print "{thisunit.name} begins its charge, building speed"
			  + " towards the enemy line").format(thisunit=self)
		self.charging = True

	def finish_charge(self, target):
		"""Cavalry ends its charge sequence by landing on an enemy
		unit, routing it. If a phalanx is deployed by the enemy
		army, then finishing the charge will destroy the cavalry"""

		# Checks the target's army to see if any units are in phalanx
		targets_army = target.army
		contains_phalanx = False
		enemy_phalanx_name = None
		for unit in targets_army.unitlist.values():
			if unit.phalanx == True:
				contains_phalanx = True
				enemy_phalanx_name = unit.name

		# If a phalanx was found in the previous block, routes cav
		if contains_phalanx == True:
			print ("{thisunit.name} charge into a wall of spears, set"
				  + " by the {phalanxunit} into a phalanx formation."
				  + " Chaos erupts among the cavalry. {thisunit.name}"
				  + " break and route before even reaching the"
				  + " {tar.name}.").format(
				  thisunit=self, tar=target,
				  phalanxunit=enemy_phalanx_name)
			self.status = "routed"
			self.charging = False

		# If no phalanx detected, cavalry routes the enemy unit
		print ("{thisunit.name} lands its charge, crashing into"
			  + " {tar.name} and routing it.").format(
			  thisunit=self, tar=target)
		self.charging = False
		self.status = "idle"

		if len(target.engaged_with) > 0:
			target.break_engagement()
		else
			target.status = "routed"
			target.defending = False
			target.charging = False
			target.under_fire = False
			target.
		### THIS NEEDS TO BE LISTED ON AVAILABLE ACTIONS

	def cancel_charge(self)
		"""The charge is cancelled and the cavalry adopts a defensive
		stance"""

		print ("{thisunit.name} slows down its charge and returns to"
			  + " a defensive position").format(thisunit=self)
		self.charging = False
		self.status = "defending"


#### WRITE A ROUTED FUNCTION UNDER UNIT CLASS THAT CLEARS ALL UNIT
#### STATUS

#### ADD CHARGING FUNCTIONS TO CAVALRY AVAILABLE ACTIONS.
#### BEGIN_CHARGE WHEN CHARGING IS FALSE. FINISH_CHARGE WITH TARGET
###  WHEN TRUE
#### 	ENSURE THAT YOU CANT CHARGE A SURROUNDED, ROUTED, CHARGING UNIT
####	ADD PHALANX BRANCH TO FINISH_CHARGE. KILLS CAVALARY.


# REMEMBER TO ADD UNITS THAT RAISE NOTIMPLEMETED ERROR

## ADVANCED: Try having cavalry available actions method with cavalry-
# specific actions, then a super(cavalry, self).__init__(self) that
# uses the original unit engagement definitions IF cavalry is not charging
# and appends the charge option to the dictionary if cavalry is not charging
