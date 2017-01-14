

# unitlist attribute... uses unit.name as keys, and unit() objects as
# value

# Every enemy army will have an ai.description that describes the
# commanders and their personality during the 'location' phase
# this will give hints about the ai's choices as well as the
# enemy army composition

# player and enemy armies defined here. Enemy armies will have the "AI"
# method that returns an action after taking an enemy type, and player
# army object (so it can count units existing and their status)
# for instance, to set phalanx up if player cav is charging

# Need a army.remove(unit) method and army.add(unit) method
# for add/remove, be sure to mention which unit is being added or
# removed prior to displaying the verbose unitlist. Will need to use a
# list.INSERT(i, x) command that places the unit in the right spot
# in the turn order

# Need an army.return_verbose_unitlist that returns a long string
# with list of units and their descriptions. to be used at beginning
# of battles and when a unit is removed or added

# Need an army.printengagements that prints all engaged enemies and
# friendly units in a formated list, similar to
# ENEMY CHARGING
# ENEMY DEFENSE	Enemy7, Enemy8
# ENEMY PHALANX
# ENEMY IDLE	Enemy5, Enemy 6
# 		Enemy1			Enemy2 Enemy3			Enemy4
#		Unit1			Unit2					Unit3
# IDLE	Unit4, Unit5
# PHALANX
# DEFENSE Unit6, Unit7
# CHARGING

# can cycle through
# enemy_line = [" ".join(unit.engaged_with) for unit in \
# 	playerarmy.unitlist if len(unit.engaged_with) > 0]
# player_line = [unit for unit in playerarmy.unitlist \
# 	if len(unit.engaged_with) > 0]
# Find ideal field width and number of fields (probably 4)
# Create function to print multi-line engagements IF NEEDED Can
# 	use slices to handle lists to print lists that may have partial
# 	# of fields per line. for item in enemy_line[4:8]
#	slices will not return an error if the list only goes to item 7

# army.statuscheck runs after EVERY move
# need to add a 'surrounded' attribute for army that is part of the
# engine's routine army.status checks
# army.status also needs a special trigger for certain scenarios where
# "it starts raining when unitlist length is at 3..." and you are told
# to anticipate a rainstorm at the start of the battle and should
# not focus on routing enemy archers
# CLEANS OUT ANY ARROW TYPE UNITS THAT ARE "IDLE"
# army.loc_conditions(conditions) argument that allows 'rain' and
# 'mud' and 'clear' to be passed to it by the status checks

#army.refresh that will set all units to defending status, not charging,
# and no phalanx. clear conditions, etc. Cleans any arrow units out

# army.statuscheck will route units that are surrounded, and similar actions

class Army(object):
    """Army base class. Stores units in the army and has commands to
    manipulate the data and print information about army status.
    Dictionary unitlist contains the string name and object of
    each unit in the army"""

    def __init__(self):
        self.name = "Default Army"
        self.description = "default army description"
        self.unitlist = {}

    def add_unit(self, unit):
        """Adds a unit to the army. The unit.army attribute will
        be set to the army object name. Remember, units must be
        instantiated prior to adding them."""

        self.unitlist[unit.name] = unit
        self.unitlist[unit.name].army = self

    def remove_unit(self, unit):
        """Removes a unit from the army. The unit.army attribute
        will be set to None. Remember, units remain instantiated
        after removing them."""

        del self.unitlist[unit.name]
        unit.army = None
