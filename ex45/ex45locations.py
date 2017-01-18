


# Rain scenario
# mud scenario
# endless reinforcement 'kill the king' scenario
# surround all spearmen scenario where you have temporary cavalry reinforcements
# 	but the ai keeps spearmen on constant defense > phalanx (When charging)
# 	forces are balanced but when an enemy unit defends you can free up
#   one cavalry to start routing them.

import sys
import ex45armies as armies
import ex45units as units
import ex45ai as ai
import ex45engine as engine

class Location(object):
    """Object that contains the location name attribute and
    a function to enter the location"""

    def __init__(self, name="location"):
        self.name = name

    def enter(self, player_army):
        """player army enters the location. can instantiate
        enemy armies here"""
        # print "You enter the location"
        # print "This will be different for every location"

        # enemy = armies.Army()

        # outcome = battle() engine info here

        # if outcome == "enemy routed" or outcome == "enemy surrounded":
        #     print 'you win'
        #     return "next location"

class PlainsofGorgoth(Location):

    def __init__(self, name="Plains of Gorgoth"):
        super(PlainsofGorgoth, self).__init__(name)

    def enter(self, player_army):
        """Entry method for plains of gorgoth"""

        print "\n\nEnter plains of Gorgoth\n"
        raw_input(">")

        # INSTANTIATE UNITS
        goblins = units.Infantry(name="Goblins")
        goblins_II = units.Infantry("Goblins II")
        goblin_slingerz = units.Archers(name="Goblin Slingerz")
        troll_pikemen = units.Spearmen(name="Troll Pikemen")
        warg_riders = units.Cavalry(name="Warg Riders")

        # INSTANTIATE ARMY AND POPULATE
        goblins_of_gorgoth = armies.Army()
        goblins_of_gorgoth.name = "Goblins of Gorgoth"
        goblins_of_gorgoth.add_unit(goblins)
        goblins_of_gorgoth.add_unit(goblins_II)
        goblins_of_gorgoth.add_unit(goblin_slingerz)
        goblins_of_gorgoth.add_unit(troll_pikemen)
        goblins_of_gorgoth.add_unit(warg_riders)

        # INSTANTIATE AI COMMANDER
        goblin_commander = ai.Commander()
        goblins_of_gorgoth.register_ai(goblin_commander)

        # INSTANTIATE BATTLE
        battle_for_the_plains_of_gorgoth = engine.BattleEngine(
                                           player_army,
                                           goblins_of_gorgoth
                                           )
        battlegorgoth = battle_for_the_plains_of_gorgoth

        print "about to commence battle of gorgoth"
        raw_input(">")

        # BATTLE METHOD WITH OUTCOME
        outcome = battlegorgoth.battle_commence()

        if outcome == "enemy routed" or outcome == "enemy surrounded":
            print outcome
            raw_input(">")
            return "Mountains of Gorgoth"
        else:
            print "You lost, game over. exit"
            sys.exit()

class MountainsofGorgoth(Location):

    def __init__(self, name="Mountains of Gorgoth"):
        super(MountainsofGorgoth, self).__init__(name)

    def enter(self, player_army):
        """Entry method for mountains of gorgoth"""

        print ("Enter mountains of gorgoth. Not written, should"
              + "crash now")
        raw_input(">")
