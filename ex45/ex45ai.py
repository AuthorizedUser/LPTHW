
import random
# choice(sequence) random element. Can find a key then call sequence[key]
# randint(a, b): choose random int from a to b with endpoints. can use with a
# list of keys to select one. or a list of actions that meet a criteria
# from .values(). can use randint(0,len(list))

class Commander(object):
    """Default Commander class. Contains a name and description.
    Subclasses can be made with varied ai methods.
    """

    def __init__(self):
        self.name = "Default"
        self.description = "Default Description"

    def ai(self, actions_dict, unittype, enemy_unitlist):
        """Bound to army object and used to communicate with ai.
        actions_dict paramter takes the actions dictionary
        unittype parameter takes the unit.type"""

        unittype = unittype
        if unittype == "infantry":
            return self.Infantry(actions_dict, enemy_unitlist)
        elif unittype == "spearmen":
            return self.Spearmen(actions_dict, enemy_unitlist)
        elif unittype == "archers":
            return self.Archers(actions_dict, enemy_unitlist)
        elif unittype == "cavalry":
            return self.Cavalry(actions_dict, enemy_unitlist)
        else:
            print "DEBUG: CANNOT FIND UNIT TYPE METHOD"

    def make_ailist(self, actions_dict, enemy_unitlist):
        """Make a list of format
        [("action_string", "enemy_type_string", "dict_key"),]
        that will be parsed by the ai"""

        ailist = [(x, x, x) for x in range(0, len(actions_dict))]
        i = 0

        for k in actions_dict:
            ailist[i][0] = k.split[0] #takes action word from key
            tarname = " ".join(k.split[1:]) #Gets enemy name from key
            ailist[i][1] = enemy_unitlist[tarname].type
            #need to use enemy list to get unit type
            ailist[i][2] = k
            i += 1

        return ailist

    def make_choice(self, ailist, preferred_list):
        """Takes the ailist and the preferred list of actions
        of a type, and returns a chosen action key"""

        l = ailist
        actkeys = []
        #goes down the preferred action list until it finds
        #a value that matches available actions
        for j in preferred_list:
            for i in l:
                if preferred_list[j] == l[i][:2]: #list match
                    actkeys.append(l[i][2]) #append the matching keys
            if len(actkeys) > 0:
                return random.choice(actkeys)

        # AI COULD NOT FIND A CHOICE
        return random.choice(actions_dict)
        print "DEBUG: NO ACTION FOUND"


    def Infantry(self, actions_dict, enemy_unitlist):
        """Receives actions_dict and enemy_unitlist.
        Returns a key to the actions_dict
        default commander likes steady-state battles
        but infantry will go for archers, then other infantry"""

        ailist = self.make_ailist(actions_dict, enemy_unitlist)

        # ENTER TYPE PREFERRED ACTIONS HERE
        preferred_list = [
                         ('continue_engagement', '')
                         ('continue_fending', '')
                         ('continue_defending', '')
                         ('engage', 'archers')
                         ('engage', 'infantry')
                         ('engage', 'cavalry')
                         ('defend', '')
                         ]

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_unitlist.values():
            if unit.type == "infantry" and unit.status == "idle":
                preferred_list.insert(0, ('engage', 'infantry'))
            if unit.type == "archers" and len(unit.firing_at) > 0:
                preferred_list.insert(1, ('engage', 'archers'))

        return self.make_choice(ailist, preferred_list)

    def Spearmen(self, actions_dict, enemy_unitlist):
        """Receives actions_dict and enemy_unitlist.
        Returns a key to the actions_dict
        default commander likes steady-state battles
        Spearmen will play defense and phalanx during charges"""

        ailist = self.make_ailist(actions_dict, enemy_unitlist)

        # ENTER TYPE PREFERRED ACTIONS HERE
        preferred_list = [
                         ('continue_defending', '')
                         ('defend', '')
                         ('continue_fending', '')
                         ]

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_unitlist.values():
            if unit.charging == True:
                preferred_list.insert(0, ('phalanx', ''))

        return self.make_choice(ailist, preferred_list)


    def Archers(self, actions_dict, enemy_unitlist):
        """Receives actions_dict and enemy_unitlist.
        Returns a key to the actions_dict
        default commander likes steady-state battles
        Archers will defend, and will fire at enemy units"""

        ailist = self.make_ailist(actions_dict, enemy_unitlist)

        # ENTER TYPE PREFERRED ACTIONS HERE
        preferred_list = [
                         ('shoot', 'infantry')
                         ('shoot', 'archers')
                         ('shoot', 'cavalry')
                         ('shoot', 'spearmen')
                         ('defend', '')
                         ('continue_defending', '')
                         ('continue_fending', '')
                         ]

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_unitlist.values():
            if unit.phalanx == True:
                preferred_list.insert(0, ('shoot', 'spearmen'))

        return self.make_choice(ailist, preferred_list)

    def Cavalry(self, actions_dict, enemy_unitlist):
        """Receives actions_dict and enemy_unitlist.
        Returns a key to the actions_dict
        default commander likes steady-state battles
        Cavalry will charge archers and will cancel if phalanx"""

        ailist = self.make_ailist(actions_dict, enemy_unitlist)

        # ENTER TYPE PREFERRED ACTIONS HERE
        preferred_list = [
                         ('finish_charge', 'archers')
                         ('finish_charge', 'cavalry')
                         ('finish_charge', 'infantry')
                         ('finish_charge', 'spearmen')
                         ('begin_charge', '')
                         ('defend', '')
                         ('continue_defending', '')
                         ('continue_fending', '')
                         ]

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_unitlist.values():
            if unit.phalanx == True:
                preferred_list.insert(0, ('cancel_charge', ''))

        return self.make_choice(ailist, preferred_list)

class ArchersCommander(Commander):
    """Commander for an army with many archers who is typically
    very defensive"""

    def __init__(self):
        super(ArchersCommander, self).__init__()
        self.description = ("Commander for an army with many archers"
                           + "who is typically very defensive")

    def Infantry(self, actions_dict, enemy_unitlist):
        raise NotImplemented

    def Spearmen(self, actions_dict, enemy_unitlist):
        raise NotImplemented

    def Archers(self, actions_dict, enemy_unitlist):
        raise NotImplemented

    def Cavalry(self, actions_dict, enemy_unitlist):
        raise NotImplemented #POSSIBLY WOULD INHERIT THIS METHOD

### NEED TO SOMEHOW TRANSFER A TARGET LIST WITH AVAILABLE
### ACTIONS TO THE ENGINE AND ADD IT AS A PARAMETER HERE
### CAN BE AN AI STYLE TARGET LIST. KEY IS ACTION type
### KEY = shoot, engage, defend, etc.
### VALUE = target.

### SOLUTION!! CAN PARSE THE DICT KEYS AND ENEMY ARMY UNITLIST
### TO DETERMINE WHAT EACH KEY MEANS AS FAR AS THE AI needs
### CAN USE split() as long as unit names do not contain spaces

### USE AI IF STATEMENTS TO GO DOWN LIST OF PREFERRED ACTIONS
### BEST ACTION LIST
### PRIORITY 1, ENGAGE PHALANX
###     IF ENGAGE IN KEY AND TARGETS[KEY].PHALANX == TRUE:
###     RETURN ENGAGE TARGET
### PRIORITY 2, SHOOT INFANTRY, etc
### PRIORITY 3, CHARGE DEFENDERS, ETC
