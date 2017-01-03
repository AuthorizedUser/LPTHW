from sys import exit

invstart = []



def topbar(): #used for formatting descriptions
	print "\n---------------------------------------------------------------------"
	
	
	
def lowbar(invbar): #bottom bar formatter
	print "---------------------------------------------------------------------"
	inventory(invbar)
	


def inventory(inventorylist):
	print "\n---------- Inventory ----------"
		
	for i in inventorylist:
		print "%d. %s" % (inventorylist.index(i) + 1, i)
		
	print "\n"



def start(inv):
	emerald_revealed = False
	
	topbar()
	print "You are in a dark hole. There is moss and wet stone all around."
	print "The only direction to go is up. You can climb out if you are careful."
	print "You can 'look' to see your environment"
	lowbar(inv)
	
	command = raw_input("> ")
	gladecomm = ["climb", "up", "out"]
	
	if command in gladecomm:
		#This line did not like ("climb" or "up") in parentheses
		glade(inv)
	elif "look" in command:
		print "\nYou survey the environment. It is too dark to make out anything\n"
		start(inv)
	elif "torch" in command and "emerald" not in inv and "torch" in inv:
		print "\nYou light the torch and look around."
		print "There is a large emerald wedged in a crack in the wall."
		print "You grab the emerald."
		inv.append("emerald")
		start(inv)		
	else:
		print "\nThat doesn't make much sense."
		start(inv)



def glade(inv):
	topbar()
	print "You come into a glade, there are three paths."
	print "Forward leads into a stone temple, lit by braziers."
	print "East leads through an overgrown forest trail."
	print "West leads down a well-worn pathway through the trees."
	print "Down leads back into the dark hole."
	lowbar(inv)
	
	command = raw_input("> ")
	
	if "east" in command:
		print "\nYou carefully tread the overgrown forest trail."
		pond(inv)
	elif "west" in command:
		print "\nYou walk down the hard-packed dirt of the forest path."
		clearing(inv)
	elif "forward" in command:
		print "\nYou enter the stone temple, past the burning braziers."
		temple(inv)
	elif "down" in command:
		print "\nYou climb back down the hole."
		start(inv)
	else:
		print "\nThat makes no sense."
		glade(inv)
	


def pond(inv):
	topbar()
	print "You stumble into a clear forest pond."
	print "You gaze into the clear water."
	
	if "ruby" not in inv: #adds ruby dialog to environment if it isn't
	# already taken
		print "There is a shining ruby at the bottom of the pond."
		print "You can wade in and grab the ruby."
	else:
		print "There is nothing in the pond."

	print "To the west is the trail that returns to the glade."
	lowbar(inv)
	
	commandpond = raw_input("> ")
	trailcomm = ["west", "trail", "return"]
	rubycomm = ["ruby", "pond", "wade", "grab"]
	
	if commandpond in trailcomm:
		print "\nYou walk back down the overgrown forest trail."
		glade(inv)
	elif commandpond in rubycomm and "ruby" not in inv:
	#second boolean statement added to avoid adding a double-ruby
		print "\nYou reach into the crystal clear water and grab the ruby."
		inv.append("ruby")
		pond(inv)
	else:
		print "\nThat makes no sense."
		pond(inv)
		
		
		
def clearing(inv):
	topbar()
	print "A clearing at the end of the path."
	print "Trees cover the clearing, there are some bushes."
	print "To the east is the path leading back to the glade."
	
	if "torch" not in inv:
		print "There is a torch on the ground, and an accompanying striker."
	
	lowbar(inv)
	
	command = raw_input("> ")
	commtorch = ["torch"]
	commpath = ["glade", "east", "path", "back", "return"]
	
	if command in commtorch and "torch" not in inv:
		print "\nYou pick up the torch"
		inv.append("torch")
		clearing(inv)
	elif command in commpath:
		print "\nYou walk back down the path to the glade"
		glade(inv)
	else:
		print "\nThat makes no sense."
		clearing(inv)
		
	
	
def temple(inv):
	topbar()
	print "You walk past the braziers into a stone temple."
	print "There is a pedestal with two slots where gems can fit."
	print "If you have gems, you can place them in the slots."
	print "A hallway leads back out to the glade."
	lowbar(inv)
	
	command = raw_input("> ")
	commandexit = ["exit", "glade", "hall", "hallway", "leave", "return"]
	commandplacegems = ["place", "insert", "gems", "ruby", "emerald", \
	"pedestal", "slot"]
	bothgems = "ruby" in inv and "emerald" in inv
	
	if command in commandexit:
		print "\nYou exit the temple to return to the glade."
		glade(inv)
	elif command in commandplacegems and bothgems == True:
		print "\nYou insert both gems into the slots."
		print "A door opens in the stone wall at the back of the room."
		print "Curious, you proceed through the door into the deeper room."
		inv.remove("emerald")
		inv.remove("ruby")
		finalroom(inv)
	elif command in commandplacegems and bothgems == False:
		print "\nBoth gems are needed for the pedestal."
		temple(inv)
	else:
		print "\nThat makes no sense."
		temple(inv)
		


def finalroom(inv):
	topbar()
	print "The room is very dark. You can hear a metallic clink as you walk."
	lowbar(inv)
	
	command = raw_input("> ")
	
	if "torch" in command:
		topbar()
		print "You light the room with the torch to reveal a vast fortune!"
		print "The ground is covered in gold coins."
		inv.append("3,000,000 gold coins")
		lowbar(inv)
		print "Congratulations! You are rich!"
		exit(0)
	else:
		print "\nThat makes no sense."
		finalroom(inv)
	


start(invstart)

# Use sys.exit to exit
# Use lists and functions

# Idea - use a list to collect inventory items needed to complete game.
# List can use append, count, index, pop, insert, remove.
# Append and Remove will be the most useful. 
# Count can be used to check if an item is contained in inventory.
# Can have a 'inventory' UI function that displays options in each room.
# for-loop cqn be used to enumerate and list the inventory contents.
# len(list) will return number of values in a list

# functions can return a value that will alter a script global variable
# the global variable can also enter the script as an argument
# the global variable can be a list object that can go into functions \
# and return with them.

#list = ["one", "one"]
#list.remove("one")
#print "%r" % list
#The above code shows that list.remove(x) will only remove the first instance
# of x