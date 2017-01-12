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
	Basic Units	
		Infantry can engage any unit (it has no abilities)
	Specialists
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
		Archers have a special "engage" action method
			Archer engage: Can engage or route an enemy without engaging
			themselves. On the next turn, the enemy will be hunkered
			down under archer fire if previously idle... with 'engage'
			status. The enemy will be routed if already engaged by a 
			friendly unit.
			
Unit Attributes:
	name: Simply the name of the unit. Completely customizable for various
		races and armies. Is used as the key in the unitlist dictionary
		for the unit object
		
	status: Similar to recharging hp in normal games. Each unit engage
		method reduces the targets engagement status, and it's own
		When
		idle > engaged > routed, charging, phalanx
		
	description: Fully customizable argument on a per unit basis when
	the unit is initialized
	
	type: infantry, cavalry, spearmen, archer
			
"""


class Unit(object):
	"""Base class for all units"""
	
	def __init__(self, name=None, description=None):
		"""	__init__(self[, name][, description])
		If name and description are not passed, they will default to None"""
		self.name = name
		self.status = None
		self.description = description
		self.type = None
		self.engaged_with = [] #can contain two enemy units
		self.defending = False
		
		def defend(self): #The only un-individualized method so far..
		"""Unit does nothing. No defense advantages but can help
		avoid a 'counter' or trap"""
			self.defending = True
			returned = ("{self.name} takes a defensive position"
						+ "and digs in").format(self)
			return


class Infantry(Unit):
	"""Infantry(Unit) subclass. Used for sword/club style infantry.
	.type: 'infantry'
	"""
	def __init__(self):
		super(Infantry, self).__init__(name=None, description=None)
		self.type = "infantry"
		self.status = "idle"
	
	def engage(self, target):
		"""	engage(self, target):
		target: enemy unit instance. e.g. enemyarmy1.unit3
		Engage an enemy unit, altering it's status to 'engaged'
		or 'routed' or potentially is blocked by an enemy ability
		"""
		# Manually change engage text if desired in subclasses
		# I could not come up with an elegant solution for it
		self.engage_text = ("{thisunit.name} attacks {tar.name}"
							+ ".").format(thisunit=self, tar=target)
		# Needs to check for charging cavalry and surrounded units
		# so cannot engage
		if target.type ==
		
		if target.status == "idle":
			target.status = "engaged"
			self.status = "engaged"
			self.defending = False
			self.engaged_with
			
		
		self.return_txt = engage_text + "\n"+("-" * 20)+"\n" + ######
		
		
	def available_actions(self):
		"""Returns a dictionary of available actions for this unit
		instance. These actions are subclass specific and may not
		always be available, based on the unit's status"""
		if self.status == "idle"
		idleactions = {"defend": self.defend(), ###
		
		
	
	
	
# UNITS AACTIONS CAN RETURN ENEMY UNIT STATUS METHOD OBJECT AT THE  END
# TO SOME KIND OF ENEMY_AFFECTS OBJECT IN THE ENGINE
# REMEMBER TO ADD UNITS THAT RAISE NOTIMPLEMETED ERROR