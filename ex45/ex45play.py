"""Script used for instantiating and playing.
Some classes instantiate objects themselves
Most of this will be done when scenarios are made...
the main army will be instantiated in the first location"""


import ex45units as units
import ex45armies as armies
import ex45engine as engine
import ex45ai as ai
import ex45locations as locations

# INSTANTIATE UNITS
human_infantry = units.Infantry(name="Human Infantry")
elven_archers = units.Archers(name="Elven Archers")
honorable_spearmen = units.Spearmen(name="Honorable Spearmen")
horselords = units.Cavalry(name="Horselords")

# INSTANTIATE ARMY AND POPULATE
alliance_forces = armies.Army()
alliance_forces.name = "Alliance Forces"
alliance_forces.add_unit(horselords)
alliance_forces.add_unit(human_infantry)
alliance_forces.add_unit(elven_archers)
alliance_forces.add_unit(honorable_spearmen)

# Create map with location objects. Can enter key as INSTANTIATION
# argument for the locatons
the_map = {"Plains of Gorgoth": locations.PlainsofGorgoth(),
           "Mountains of Gorgoth": locations.MountainsofGorgoth()}

# Instantiate location engine
campaign = engine.LocationEngine(the_map, alliance_forces)

campaign.start("Plains of Gorgoth")
