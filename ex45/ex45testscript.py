import ex45units as units

# *************JANUARY 15, UNIT TESTS

# TEST IMPORT SYNTAX DEBUG
# DONE, DEBUG IS COMPLETE


#create unit objects and test them against eachother
human_infantry = units.Infantry(name="Human Infantry")
elven_archers = units.Archers(name="Elven Archers")
honorable_spearmen = units.Spearmen(name="Honorable Spearmen")
horselords = units.Cavalry(name="Horselords")

goblins = units.Infantry(name="Goblins")
goblins_II = units.Infantry()
goblin_slingerz = units.Archers(name="Goblin Slingerz")
troll_pikemen = units.Spearmen(name="Troll Pikemen")
warg_riders = units.Cavalry(name="Warg Riders")

# TEST INSTANTIATION
# FIXED __INIT__ TO INCLUDE PARAMETERS
# DONE
# TEST attributes
# print "\n\n\n"
# print "-" * 150
# print "TEST INSTANTIATION"
# print "-" * 150
# print "Test .name attribute: " + goblins.name
# print "Test undefined .name attribute: " + goblins_II.name
# PASSED TEST

#TEST status_down()
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.status_down()"
# print "-" * 150
# print "Status Before: {status}".format(status=human_infantry.status)
# human_infantry.status_down()
# print "Status After: {status}".format(status=human_infantry.status)

#TEST status_up()
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.status_up()"
# print "-" * 150
# print "Status Before: {status}".format(status=human_infantry.status)
# human_infantry.status_up()
# print "Status After: {status}".format(status=human_infantry.status)

#TEST engage()
print "\n\n\n"
print "-" * 150
print "TEST unit.engage()"
print "-" * 150
print "Status Before: {status}".format(status=human_infantry.status)
print "Engagement list before: {}".format(human_infantry.engaged_with)
human_infantry.engage(goblins)
print "Status After: {status}".format(status=human_infantry.status)
print "Engagement list after: {}".format(human_infantry.engaged_with)

#TEST break_engagement
print "\n\n\n"
print "-" * 150
print "TEST unit.break_engagement()"
print "-" * 150
print "Status Before: {status}".format(status=human_infantry.status)
human_infantry.break_engagement()
print "Status After: {status}".format(status=human_infantry.status)

#TEST unit.defend()
print "\n\n\n"
print "-" * 150
print "TEST unit.defend()"
print "-" * 150
# Need proper break engagement attributes for it to works
print ("Defense Before: {defending}\nStatus Before: {status}").format(
      status=human_infantry.status, defending=human_infantry.defending)
human_infantry.defend()
print ("Defense After: {defending}\nStatus After: {status}").format(
      status=human_infantry.status, defending=human_infantry.defending)







print "\n\n"
