


# Rain scenario
# mud scenario
# endless reinforcement 'kill the king' scenario
# surround all spearmen scenario where you have temporary cavalry reinforcements
# 	but the ai keeps spearmen on constant defense > phalanx (When charging)
# 	forces are balanced but when an enemy unit defends you can free up
#   one cavalry to start routing them.

import ex45armies as armies
import ex45units as units

class Location(object):

    def __init__(self, player_army):
        self.pa = player_army
