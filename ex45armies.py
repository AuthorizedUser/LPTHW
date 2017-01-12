

# unitlist attribute... uses unit.name as keys, and unit() objects as 
# value

# player and enemy armies defined here. Enemy armies will have the "AI"
# method that returns an action after taking an enemy type, and player
# army object (so it can count units existing and their status)
# for instance, to set phalanx up if player cav is charging

# Need a army.remove(unit) method and army.add(unit) method
# for add/remove, be sure to mention which unit is being added or
# removed prior to displaying the verbose unitlist

# Need an army.return_verbose_unitlist that returns a long string
# with list of units and their descriptions. to be used at beginning
# of battles and when a unit is removed or added

# need to add a 'surrounded' attribute for army that is part of the
# engine's routine army.status checks